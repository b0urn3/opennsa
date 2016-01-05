from opennsa import config

__author__ = 'Robert Zahradnicek'


def _delete_vbridge(cfg, vbr_name):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges/" + str(vbr_name)
