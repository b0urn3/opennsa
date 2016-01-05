from opennsa import config

__author__ = 'Robert Zahradnicek'


def list_vtn(cfg, max_repetition=None):
    if max_repetition is not None:
        return cfg[config.SDNCREST_URL] + "/vtns?index=" + cfg[config.SDNCREST_VTN] \
                                        + "&max_repetition=" + str(max_repetition)
    else:
        return cfg[config.SDNCREST_URL] + "/vtns?index=" + cfg[config.SDNCREST_VTN]


def list_vtn_detail(cfg, max_repetition=None):
    if max_repetition is not None:
        return cfg[config.SDNCREST_URL] + "/vtns/detail?index=" + cfg[config.SDNCREST_VTN] \
                                        + "&max_repetition=" + str(max_repetition)
    else:
        return cfg[config.SDNCREST_URL] + "/vtns/detail?index=" + cfg[config.SDNCREST_VTN]


def list_vtn_count(cfg, max_repetition=None):
    if max_repetition is not None:
        return cfg[config.SDNCREST_URL] + "/vtns/count?index=" + cfg[config.SDNCREST_VTN] \
                                        + "&max_repetition=" + str(max_repetition)
    else:
        return cfg[config.SDNCREST_URL] + "/vtns/count?index=" + cfg[config.SDNCREST_VTN]


def show_vtn(cfg):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN]
