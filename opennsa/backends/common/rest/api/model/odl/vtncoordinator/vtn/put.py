import json

from opennsa import config

__author__ = 'Robert Zahradnicek'


def _update_vtn_uri(cfg):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN]


def _update_vtn_body(cfg, description=None):
    if description is None:
        request_body = {
            "vtn": {
                "vtn_name": str(cfg[config.SDNCREST_VTN]),
                "description": "TEST VTN"
            }
        }
        return json.dumps(request_body)
    else:
        request_body = {
            "vtn": {
                "vtn_name": str(cfg[config.SDNCREST_VTN]),
                "description": str(description)
            }
        }
        return json.dumps(request_body)


def update_vtn(cfg, description=None):
    return _update_vtn_uri(cfg=cfg), _update_vtn_body(cfg=cfg, description=description)
