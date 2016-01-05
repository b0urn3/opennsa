from opennsa import config

__author__ = 'Robert Zahradnicek'


def delete_vtn(cfg):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN]
