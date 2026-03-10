import asyncio
import logging
import re
import struct

import telnetlib3


def parse_who(lines):
    lines = lines.splitlines()
    logging.debug(f"Response to 'who': {lines}")
    row_headers = ("callsign", "type", "state", "started", "name", "average_rtt", "link")
    payload = []

    filler = " " * 50
    for i in range(1, len(lines) - 1):
        line = lines[i].lstrip()
        if line.startswith("Callsign"):
            continue

        logging.debug(f"line ({i}): {line}")
        line_parts = line.split(" ", 1)
        if len(line_parts) < 2:
            continue

        first_part = line_parts[0]
        second_part = line_parts[1]
        ln = len(second_part)

        try:
            if ln > 32:
                fields = [first_part]
                second_part += filler
                fieldstruct = struct.Struct("10s 8s 18s 11s 2x 5s")
                fields += list(fieldstruct.unpack_from(second_part.encode()))
                fields = [f.decode("utf-8").strip() if isinstance(f, bytes) else f.strip() for f in fields]
                payload.append(dict(zip(row_headers, fields)))
        except Exception as e1:
            logging.error(e1)
    return payload


async def _read_buffer(reader, timeout=1.2, max_chunks=20):
    """Read what is currently available without relying on exact prompt strings."""
    chunks = []
    for _ in range(max_chunks):
        try:
            chunk = await asyncio.wait_for(reader.read(4096), timeout=timeout)
        except asyncio.TimeoutError:
            break
        if not chunk:
            break
        if isinstance(chunk, str):
            chunk = chunk.encode("utf-8", errors="ignore")
        chunks.append(chunk)

        # Break early when we likely reached an interactive prompt.
        low = b"".join(chunks).lower()
        if b"dxspider" in low and b">" in low:
            break
    return b"".join(chunks)


async def fetch_who_and_version(host, port, user, password=None):
    logging.debug(f"Connecting to {host}:{port} for WHO and SH/VERSION")

    reader, writer = await telnetlib3.open_connection(host, port, encoding=None)
    who_data = ""
    version_info = "Unknown"

    try:
        initial = await _read_buffer(reader)
        logging.debug(f"Initial banner: {initial!r}")

        writer.write(user.encode("utf-8") + b"\n")
        after_user = await _read_buffer(reader)
        logging.debug(f"After user: {after_user!r}")

        prompt_data = (initial + after_user).lower()
        if b"password" in prompt_data and password:
            writer.write(password.encode("utf-8") + b"\n")
            after_pass = await _read_buffer(reader)
            logging.debug(f"After password: {after_pass!r}")

        logging.debug("Login handshake completed")

        writer.write(b"who\n")
        who_response = await _read_buffer(reader, timeout=1.5, max_chunks=30)
        who_data = who_response.decode("utf-8", errors="ignore")

        writer.write(b"sh/version\n")
        version_response = await _read_buffer(reader, timeout=1.5, max_chunks=20)
        res = version_response.decode("utf-8", errors="ignore").strip().splitlines()
        logging.debug(f"Full SH/VERSION Response:\n{res}")

        for line in res:
            logging.debug(f"Processing Line: {line}")
            match = re.search(r"DXSpider v([\d.]+) \(build\s+(\d+)", line)
            if match:
                version_info = f"DXSpider v{match.group(1)} build {match.group(2)}"
                logging.debug(f"Extracted DXSpider Version: {version_info}")
                break

    except Exception as e:
        logging.error(f"Error retrieving WHO and version info: {e}")
    finally:
        writer.close()
        reader.feed_eof()
        logging.debug("Connection closed")

    return parse_who(who_data), version_info
