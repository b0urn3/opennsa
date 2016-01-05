import json

from opennsa import config

__author__ = 'Robert Zahradnicek'


def _create_vtn_uri(cfg):
    return cfg[config.SDNCREST_URL] + "/vtns"


def _create_vtn_body(cfg, description=None):
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


def create_vtn(cfg, description=None):
    return _create_vtn_uri(cfg=cfg), _create_vtn_body(cfg=cfg, description=description)
