import json

from opennsa import config

__author__ = 'Robert Zahradnicek'


def _create_vbridge_uri(cfg):
    return cfg[config.SDNCREST_URL] + "/vtns/" + cfg[config.SDNCREST_VTN] + "/vbridges"


def _create_vbridge_body(cfg, vbr_name, controller_id, domain_id, description=None):
    if description is None:
        request_body = {
            "vbridge": {
                "vbr_name": str(vbr_name),
                "controller_id": str(controller_id),
                "description": "TEST vBridge",
                "domain_id": str(domain_id)
            }
        }
        return json.dumps(request_body)
    else:
        request_body = {
            "vbridge": {
                "vbr_name": str(vbr_name),
                "controller_id": str(controller_id),
                "description": str(description),
                "domain_id": str(domain_id)
            }
        }
        return json.dumps(request_body)


def create_vbridge(cfg, vbr_name, controller_id, domain_id, description=None):
    return _create_vbridge_uri(cfg=cfg), _create_vbridge_body(cfg=cfg,
                                                      vbr_name=vbr_name,
                                                      controller_id=controller_id,
                                                      domain_id=domain_id,
                                                      description=description)
