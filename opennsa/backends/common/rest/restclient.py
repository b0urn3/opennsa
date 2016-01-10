import requests

from twisted.python import log
from twisted.internet import defer

from opennsa import error
from opennsa.backends.common.rest.api.model.odl import odl

import logging

__author__ = 'Robert Zahradnicek'

LOG_SYSTEM = 'opennsa.SDNCREST'

# Define API types for instantiation
ODL_API = 'odl'


class RESTApiModel(object):
    """
    REST API model abstraction. Selects correct API model based on the configuration parameter api_type
    """

    def __init__(self, api_type, base_url, log_system):
        # Instantiate correct model based on api_type config parameter
        if api_type == ODL_API:
            self._model = odl.ODLApi(base_url)
        self._log_system = log_system

    def provision(self, cfg, client, connection_id, source_target, dest_target, bandwidth):
        """
        Provision VLAN through the REST API of the controller
        :param cfg: parsed configuration file
        :param client: requests library Session with headers set
        :param connection_id: ID of the connection
        :param source_target: source of the connection
        :param dest_target: destination of the connection
        :param bandwidth: bandwith of the connection
        :return: 
        """
        result = self._model.provision(cfg=cfg,
                                       client=client,
                                       connection_id=connection_id,
                                       source_target=source_target,
                                       dest_target=dest_target,
                                       bandwidth=bandwidth)
        if result:
            log.msg('SDNCREST: RESTApiModel VLAN %s provisioned between %s -> %s' % (connection_id,
                                                                                     source_target,
                                                                                     dest_target),
                    logLevel=logging.INFO)
            return result
        else:
            return defer.fail(
                error.InternalNRMError('ERROR: It was not possible to provision the circuit. Check SDNCREST logs!'))

    def teardown(self, cfg, client, connection_id, source_target, dest_target):
        """
        Teardown VLAN through the REST API of the controller
        :param cfg: parsed configuration file
        :param client: requests library Session with headers set
        :param connection_id: ID of the connection
        :return: 
        """
        result = self._model.teardown(cfg=cfg,
                                      client=client,
                                      connection_id=connection_id,
                                      source_target=source_target,
                                      dest_target=dest_target)
        if result:
            log.msg('SDNCREST: RESTApiModel teardown successful', logLevel=logging.INFO)
            return result
        else:
            return defer.fail(error.InternalNRMError('ERROR: RESTApiModel it was not possible to remove the VLAN'))


class RESTApiClient(object):
    """
    Generic rest api client that uses requests library
    for handling sessions and setting up authentication
    headers of the requests.
    """

    def __init__(self, api_type, base_url, username, password, log_system):
        self._model = RESTApiModel(api_type=api_type,
                                   base_url=base_url,
                                   log_system=log_system)
        self._username = username
        self._password = password

    def _browser(self):
        """
        Create requests session with added headers and return it
        """
        session = requests.Session()
        session.headers["username"] = self._username
        session.headers["password"] = self._password
        session.headers["Content-Type"] = "application/json"
        yield session
        session.close()

    def provision(self, cfg, connection_id, source_target, dest_target, bandwidth):
        """
        Provision the VLAN using parameters received

        :param connection_id: ID of the connection in NSA
        :param source_target: source of the connection
        :param dest_target: destination of the connection
        :param bandwidth: bandwith to reserve
        """
        # Debug
        log.msg('SDNCREST: RESTApiClient provision()', logLevel=logging.DEBUG)

        # Get the new session from the generator object
        client = self._browser().next()

        # provision vlan through the model implementation
        return self._model.provision(cfg=cfg,
                                     client=client,
                                     connection_id=connection_id,
                                     source_target=source_target,
                                     dest_target=dest_target,
                                     bandwidth=bandwidth)

    def teardown(self, cfg, connection_id, source_target, dest_target):
        """
        Remove exiting VLAN

        :param circuit_id: ID of the circuit to deallocate
        """

        # Debug
        log.msg('SDNCREST: RESTApiClient teardown()')

        # Get the new session from the generator object
        client = self._browser().next()

        # teardown through model implementation
        return self._model.teardown(cfg=cfg,
                                    client=client,
                                    connection_id=connection_id,
                                    source_target=source_target,
                                    dest_target=dest_target)
