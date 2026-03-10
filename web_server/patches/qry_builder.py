# find id  in json : ie frequency / continent

def find_id_json(json_object, name):
    return [obj for obj in json_object if obj["id"] == name][0]


def query_build_callsign(logger, callsign):

    query_string = ""
    if len(callsign) <= 14:
        query_string = (
            "(SELECT rowid, spotter AS de, freq, "
            "CASE "
            "WHEN ("
            "(freq BETWEEN 1800.0 AND 1839.9) OR "
            "(freq BETWEEN 3500.0 AND 3569.9) OR "
            "(freq BETWEEN 7000.0 AND 7039.9) OR "
            "(freq BETWEEN 10100.0 AND 10129.9) OR "
            "(freq BETWEEN 14000.0 AND 14069.9) OR "
            "(freq BETWEEN 18068.0 AND 18099.9) OR "
            "(freq BETWEEN 21000.0 AND 21069.9) OR "
            "(freq BETWEEN 24890.0 AND 24914.9) OR "
            "(freq BETWEEN 28000.0 AND 28069.9) OR "
            "(freq BETWEEN 50000.0 AND 50312.9) OR "
            "(freq BETWEEN 50313.1 AND 50499.9) OR "
            "(freq BETWEEN 51000.0 AND 52000.0) OR "
            "(freq BETWEEN 70030 AND 70250) OR "
            "(freq BETWEEN 144000 AND 144150) OR "
            "(freq BETWEEN 432000 AND 432150) OR "
            "(freq BETWEEN 1296000 AND 1296150) OR "
            "(freq BETWEEN 2320100 AND 2320150) OR "
            "(freq BETWEEN 3400000 AND 3402000) OR "
            "(freq BETWEEN 5668000 AND 5670000) OR "
            "(freq BETWEEN 5760000 AND 5762000) OR "
            "(freq BETWEEN 10368000 AND 10370000) OR "
            "(freq BETWEEN 10450000 AND 10452000) OR "
            "(freq BETWEEN 24048000 AND 24050000) OR "
            "(freq BETWEEN 47087000 AND 47089000)"
            ") THEN 'CW' "
            "WHEN ("
            "(freq BETWEEN 1840.0 AND 1841.0) OR "
            "(freq BETWEEN 3570.0 AND 3600.0) OR "
            "(freq BETWEEN 7040.0 AND 7080.0) OR "
            "(freq BETWEEN 10130.0 AND 10150.0) OR "
            "(freq BETWEEN 14070.0 AND 14095.0) OR "
            "(freq BETWEEN 18100.0 AND 18105.0) OR "
            "(freq BETWEEN 21070.0 AND 21100.0) OR "
            "(freq BETWEEN 21140.0 AND 21141.0) OR "
            "(freq BETWEEN 24915.0 AND 24930.0) OR "
            "(freq BETWEEN 28070.0 AND 28120.0) OR "
            "(freq BETWEEN 28180.0 AND 28180.0) OR "
            "(freq BETWEEN 50500.0 AND 51000.0)"
            ") THEN 'DIGI' "
            "WHEN ("
            "(freq BETWEEN 1843.0 AND 2000.0) OR "
            "(freq BETWEEN 3600.0 AND 4000.0) OR "
            "(freq BETWEEN 7081.0 AND 7300.0) OR "
            "(freq BETWEEN 14100.0 AND 14350.0) OR "
            "(freq BETWEEN 18105.0 AND 18168.0) OR "
            "(freq BETWEEN 21100.0 AND 21139.0) OR "
            "(freq BETWEEN 21141.0 AND 21450.0) OR "
            "(freq BETWEEN 24930.0 AND 24990.0) OR "
            "(freq BETWEEN 28120.0 AND 29700.0) OR "
            "(freq BETWEEN 50100 AND 50312.9) OR "
            "(freq BETWEEN 50313.1 AND 50500) OR "
            "(freq BETWEEN 70030 AND 70250) OR "
            "(freq BETWEEN 144150 AND 144500) OR "
            "(freq BETWEEN 432150 AND 432500) OR "
            "(freq BETWEEN 1296150 AND 1296800)"
            ") THEN 'PHONE' "
            "ELSE '' END AS mode, "
            "spotcall AS dx, comment AS comm, time, spotdxcc from spot WHERE spotter='"
            + callsign
            + "'"
        )
        query_string += " ORDER BY rowid desc limit 10)"
        query_string += " UNION "
        query_string += (
            "(SELECT rowid, spotter AS de, freq, "
            "CASE "
            "WHEN ("
            "(freq BETWEEN 1800.0 AND 1839.9) OR "
            "(freq BETWEEN 3500.0 AND 3569.9) OR "
            "(freq BETWEEN 7000.0 AND 7039.9) OR "
            "(freq BETWEEN 10100.0 AND 10129.9) OR "
            "(freq BETWEEN 14000.0 AND 14069.9) OR "
            "(freq BETWEEN 18068.0 AND 18099.9) OR "
            "(freq BETWEEN 21000.0 AND 21069.9) OR "
            "(freq BETWEEN 24890.0 AND 24914.9) OR "
            "(freq BETWEEN 28000.0 AND 28069.9) OR "
            "(freq BETWEEN 50000.0 AND 50312.9) OR "
            "(freq BETWEEN 50313.1 AND 50499.9) OR "
            "(freq BETWEEN 51000.0 AND 52000.0) OR "
            "(freq BETWEEN 70030 AND 70250) OR "
            "(freq BETWEEN 144000 AND 144150) OR "
            "(freq BETWEEN 432000 AND 432150) OR "
            "(freq BETWEEN 1296000 AND 1296150) OR "
            "(freq BETWEEN 2320100 AND 2320150) OR "
            "(freq BETWEEN 3400000 AND 3402000) OR "
            "(freq BETWEEN 5668000 AND 5670000) OR "
            "(freq BETWEEN 5760000 AND 5762000) OR "
            "(freq BETWEEN 10368000 AND 10370000) OR "
            "(freq BETWEEN 10450000 AND 10452000) OR "
            "(freq BETWEEN 24048000 AND 24050000) OR "
            "(freq BETWEEN 47087000 AND 47089000)"
            ") THEN 'CW' "
            "WHEN ("
            "(freq BETWEEN 1840.0 AND 1841.0) OR "
            "(freq BETWEEN 3570.0 AND 3600.0) OR "
            "(freq BETWEEN 7040.0 AND 7080.0) OR "
            "(freq BETWEEN 10130.0 AND 10150.0) OR "
            "(freq BETWEEN 14070.0 AND 14095.0) OR "
            "(freq BETWEEN 18100.0 AND 18105.0) OR "
            "(freq BETWEEN 21070.0 AND 21100.0) OR "
            "(freq BETWEEN 21140.0 AND 21141.0) OR "
            "(freq BETWEEN 24915.0 AND 24930.0) OR "
            "(freq BETWEEN 28070.0 AND 28120.0) OR "
            "(freq BETWEEN 28180.0 AND 28180.0) OR "
            "(freq BETWEEN 50500.0 AND 51000.0)"
            ") THEN 'DIGI' "
            "WHEN ("
            "(freq BETWEEN 1843.0 AND 2000.0) OR "
            "(freq BETWEEN 3600.0 AND 4000.0) OR "
            "(freq BETWEEN 7081.0 AND 7300.0) OR "
            "(freq BETWEEN 14100.0 AND 14350.0) OR "
            "(freq BETWEEN 18105.0 AND 18168.0) OR "
            "(freq BETWEEN 21100.0 AND 21139.0) OR "
            "(freq BETWEEN 21141.0 AND 21450.0) OR "
            "(freq BETWEEN 24930.0 AND 24990.0) OR "
            "(freq BETWEEN 28120.0 AND 29700.0) OR "
            "(freq BETWEEN 50100 AND 50312.9) OR "
            "(freq BETWEEN 50313.1 AND 50500) OR "
            "(freq BETWEEN 70030 AND 70250) OR "
            "(freq BETWEEN 144150 AND 144500) OR "
            "(freq BETWEEN 432150 AND 432500) OR "
            "(freq BETWEEN 1296150 AND 1296800)"
            ") THEN 'PHONE' "
            "ELSE '' END AS mode, "
            "spotcall AS dx, comment AS comm, time, spotdxcc from spot WHERE spotcall='"
            + callsign
            + "'"
        )
        query_string += " ORDER BY rowid desc limit 10);"
    else:
        logger.warning("callsign too long")
    return query_string


def _build_mode_case(modes_frequencies):
    parts = []
    labels = [
        ("cw", "CW"),
        ("digi", "DIGI"),
        ("phone", "PHONE"),
    ]

    for mode_id, label in labels:
        mode_ranges = find_id_json(modes_frequencies["modes"], mode_id)
        clauses = []
        for freq in mode_ranges["freq"]:
            clauses.append(
                "(freq BETWEEN " + str(freq["min"]) + " AND " + str(freq["max"]) + ")"
            )
        if clauses:
            parts.append("WHEN (" + " OR ".join(clauses) + ") THEN '" + label + "'")

    return "CASE " + " ".join(parts) + " ELSE '' END AS mode"


def query_build(logger, parameters, band_frequencies, modes_frequencies, continents_cq, enable_cq_filter):

    try:
        last_rowid = str(parameters["lr"])

        get_param = lambda parameters, parm_name: parameters[parm_name] if (parm_name in parameters) else []
        dxcalls = get_param(parameters, "dxcalls")
        band = get_param(parameters, "band")
        dere = get_param(parameters, "de_re")
        dxre = get_param(parameters, "dx_re")
        mode = get_param(parameters, "mode")
        exclft8 = get_param(parameters, "exclft8")
        exclft4 = get_param(parameters, "exclft4")

        decq = []
        if "cqdeInput" in parameters:
            decq[0] = parameters["cqdeInput"]

        dxcq = []
        if "cqdxInput" in parameters:
            dxcq[0] = parameters["cqdxInput"]

        query_string = ""

        dxcalls_qry_string = " AND spotcall IN (" + ''.join(map(lambda x: "'" + x + "'," if x != dxcalls[-1] else "'" + x + "'", dxcalls)) + ")"

        band_qry_string = " AND (("
        for i, item_band in enumerate(band):
            freq = find_id_json(band_frequencies["bands"], item_band)
            if i > 0:
                band_qry_string += ") OR ("

            band_qry_string += (
                "freq BETWEEN " + str(freq["min"]) + " AND " + str(freq["max"])
            )

        band_qry_string += "))"

        mode_qry_string = " AND  (("
        for i, item_mode in enumerate(mode):
            single_mode = find_id_json(modes_frequencies["modes"], item_mode)
            if i > 0:
                mode_qry_string += ") OR ("
            for j in range(len(single_mode["freq"])):
                if j > 0:
                    mode_qry_string += ") OR ("
                mode_qry_string += (
                    "freq BETWEEN "
                    + str(single_mode["freq"][j]["min"])
                    + " AND "
                    + str(single_mode["freq"][j]["max"])
                )

        mode_qry_string += "))"

        ft8_qry_string = " AND ("
        if exclft8:
            ft8_qry_string += "(comment NOT LIKE '%FT8%')"
            single_mode = find_id_json(modes_frequencies["modes"], "digi-ft8")
            for j in range(len(single_mode["freq"])):
                ft8_qry_string += (
                    " AND (freq NOT BETWEEN "
                    + str(single_mode["freq"][j]["min"])
                    + " AND "
                    + str(single_mode["freq"][j]["max"])
                    + ")"
                )
        ft8_qry_string += ")"

        ft4_qry_string = " AND ("
        if exclft4:
            ft4_qry_string += "(comment NOT LIKE '%FT4%')"
            single_mode = find_id_json(modes_frequencies["modes"], "digi-ft4")
            for j in range(len(single_mode["freq"])):
                ft4_qry_string += (
                    " AND (freq NOT BETWEEN "
                    + str(single_mode["freq"][j]["min"])
                    + " AND "
                    + str(single_mode["freq"][j]["max"])
                    + ")"
                )
        ft4_qry_string += ")"

        dere_qry_string = " AND spottercq IN ("
        for i, item_dere in enumerate(dere):
            continent = find_id_json(continents_cq["continents"], item_dere)
            if i > 0:
                dere_qry_string += ","
            dere_qry_string += str(continent["cq"])
        dere_qry_string += ")"

        dxre_qry_string = " AND spotcq IN ("
        for i, item_dxre in enumerate(dxre):
            continent = find_id_json(continents_cq["continents"], item_dxre)
            if i > 0:
                dxre_qry_string += ","
            dxre_qry_string += str(continent["cq"])
        dxre_qry_string += ")"

        if enable_cq_filter == "Y":
            decq_qry_string = ""
            if len(decq) == 1:
                if decq[0].isnumeric():
                    decq_qry_string = " AND spottercq =" + decq[0]

            dxcq_qry_string = ""
            if len(dxcq) == 1:
                if dxcq[0].isnumeric():
                    dxcq_qry_string = " AND spotcq =" + dxcq[0]

        if last_rowid is None:
            last_rowid = "0"
        if not last_rowid.isnumeric():
            last_rowid = 0

        mode_case = _build_mode_case(modes_frequencies)
        query_string = "SELECT rowid, spotter AS de, freq, " + mode_case + ", spotcall AS dx, comment AS comm, time, spotdxcc from spot WHERE rowid > " + str(last_rowid)

        if dxcalls:
            query_string += dxcalls_qry_string

        if len(band) > 0:
            query_string += band_qry_string

        if len(mode) > 0:
            query_string += mode_qry_string

        if exclft8:
            query_string += ft8_qry_string

        if exclft4:
            query_string += ft4_qry_string

        if len(dere) > 0:
            query_string += dere_qry_string

        if len(dxre) > 0:
            query_string += dxre_qry_string

        if enable_cq_filter == "Y":
            if len(decq_qry_string) > 0:
                query_string += decq_qry_string

            if len(dxcq_qry_string) > 0:
                query_string += dxcq_qry_string

        query_string += " ORDER BY rowid desc limit 50;"

        logger.debug(query_string)

    except Exception as e:
        logger.error(e)
        query_string = ""

    return query_string


query_build_callsing_list = lambda: 'SELECT spotcall AS dx FROM (select spotcall from spot  order by rowid desc limit 50000) s1  GROUP BY spotcall ORDER BY count(spotcall) DESC, spotcall LIMIT 100;'
