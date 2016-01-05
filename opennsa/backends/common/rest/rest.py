import string
import random
import requests


from twisted.python import log
from twisted.internet import defer

from opennsa import constants as cnt, config

__author__ = 'Robert Zahradnicek'

LOG_SYSTEM = 'opennsa.SDNCREST'


def request_body_dict(cfg,
                      description=None,
                      operstatus=None,
                      createdtime=None,
                      lastcommittedtime=None,
                      alarmstatus=None
                      ):
    request_body = {
        "vtns": [
            {
                "vtn_name": str(cfg[config.SDNCREST_VTN]),
            }
        ]
    }

    if description:
        request_body["vtns"][0]["description"] = str(description)
    if operstatus:
        request_body["vtns"][0]["operstatus"] = str(operstatus)
    if createdtime:
        request_body["vtns"][0]["createdtime"] = str(createdtime)
    if lastcommittedtime:
        request_body["vtns"][0]["lastcommittedtime"] = str(lastcommittedtime)
    if alarmstatus:
        request_body["vtns"][0]["alarmstatus"] = str(alarmstatus)

    return request_body


class RESTApiModel(object):

    # TODO: pick one model as is done with backends in setup.py/config.py

    def __init__(self, base_url):
        self._base_url = base_url

    def create_vlan(self):
        pass

    def get_vlan(self):
        pass

    def update_vlan(self):
        pass

    def delete_vlan(self):
        pass


class RESTApiClient(object):

    # TODO: generic client use stuff from calistos

    def __init__(self, api_model, configuration):
        self._model = api_model
        self._config = configuration

    def _browser(self):
        session = requests.Session()
        session.headers["username"] = self._config[config.SDNCREST_USER]
        session.headers["password"] = self._config[config.SDNCREST_PASS]
        yield session
        session.close()

    def setupLink(self):
        self._model.create_vlan()

    def tearDown(self):
        self._model.delete_vlan()

    def update(self):
        self._model.update_vlan()

    def get(self):
        self._model.get_vlan()

