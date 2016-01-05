from opennsa import config

__author__ = 'Robert Zahradnicek'


def list_vbridge(cfg, vbr_name=None, max_repetition=None):
    result = cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges"
    query = ""
    if vbr_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vbr_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vbridge_detail(cfg, vbr_name=None, max_repetition=None):
    result = cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges/detail"
    query = ""
    if vbr_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vbr_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vbridge_count(cfg, vbr_name=None, max_repetition=None):
    result = cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges/count"
    query = ""
    if vbr_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vbr_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def show_vbridge(cfg, vbr_name):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges/" + str(vbr_name)
