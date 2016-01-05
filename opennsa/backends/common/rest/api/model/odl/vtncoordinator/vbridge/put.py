import json

from opennsa import config

__author__ = 'Robert Zahradnicek'


def _update_vbridge_uri(cfg, vbr_name):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges/" + str(vbr_name)


def _update_vbridge_body(cfg, description=None):
    if description is None:
        request_body = {
            "vbridge": {
                "description": "TEST vBridge"
            }
        }
        return json.dumps(request_body)
    else:
        request_body = {
            "vbridge": {
                "description": str(description)
            }
        }
        return json.dumps(request_body)


def update_vbridge(cfg, vbr_name, description=None):
    return _update_vbridge_uri(cfg=cfg, vbr_name=vbr_name), _update_vbridge_body(cfg=cfg, description=description)
