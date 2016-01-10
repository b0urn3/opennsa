"""
REST backend for connection to SDN Controllers with REST API
Provides function for creating backend connection manager and for handling setup and teardown

SDN Controller is required to provide some REST API for its functionality.
Implementation of each API belongs to backends/common/rest/api/model package and
for every new API suitable constant in backends/common/rest/restclient.py should be created
and added to __init__ function of the clients class. This constant corresponds to api_type
in configuration file and is compared to it. All the functionality is then handed to API Model class
that passes it to the specified REST API model for actual requests.

"""

from twisted.python import log
from twisted.internet import defer

from opennsa import config

from opennsa.backends.common import genericbackend
from opennsa.backends.common.rest import restclient

import string
import random

__author__ = 'Robert Zahradnicek'

LOG_SYSTEM = 'opennsa.SDNCREST'


def SDNCRESTBackend(network_name, nrm_ports, parent_requester, configuration):
    """
    SDNC REST Api backend generic class for setup of circuits it extends GenericBackend class

    :param network_name: name of the network
    :param nrm_ports: ports for the nrm used for provisioning
    :param parent_requester: agent to report the successful provisioning
    :return: initialized backend object for the NSA agent used for provisioning

    """
    # Debug
    log.msg('SDNCREST: SDNCREST Backend starting')
    # Logging system prefix
    name = 'SDNCREST NRM %s' % network_name
    # for the generic backend
    nrm_map = dict([(p.name, p) for p in nrm_ports])
    # for the nrm backend
    port_map = dict([(p.name, p.interface) for p in nrm_ports])

    # Create the connection manager for the provisioned links
    cm = SDNCRESTConnectionManager(log_system=name,
                                   port_map=port_map,
                                   cfg=configuration)
    return genericbackend.GenericBackend(network=network_name,
                                         nrm_ports=nrm_map,
                                         connection_manager=cm,
                                         parent_requester=parent_requester,
                                         log_system=name,
                                         minimum_duration=1)


class SDNCRESTConnectionManager(object):
    """
    Connection Manager for provisioning the circuits with SDN Controller with REST API
    """

    def __init__(self, log_system, port_map, cfg):
        """
        Initialize Connection Manager class based on the configuration file and NRM resources

        :param log_system: logging system of the OpenNSA to use for logging to file o stdout
        :param port_map: NRM portmap for available resources
        :param cfg: parsed configuration file of OpenNSA
        """
        self.log_system = log_system
        self.port_map = port_map

        self.cfg = cfg

        self.url = cfg[config.SDNCREST_URL]
        self.username = cfg[config.SDNCREST_USER]
        self.password = cfg[config.SDNCREST_PASS]
        self.vtn = cfg[config.SDNCREST_VTN]
        self.api_type = cfg[config.SDNCREST_API_TYPE]

        self.circuit_id = None

        self.client = restclient.RESTApiClient(api_type=self.api_type,
                                               base_url=self.url,
                                               username=self.username,
                                               password=self.password,
                                               log_system=log_system)

    def getResource(self, port, label_type, label_value):
        """
        Get NRM port resource with label stored in database and parsed from topology file

        :param port: port to retrieve from port map
        :param label_type: type of the label
        :param label_value: label
        :return: identification of the resource
        """
        # Debug
        log.msg('SDNCREST: getResource', system=self.log_system)
        return self.port_map[port] + ':' + str(label_value)

    def getTarget(self, port, label_type, label_value):
        """
        Get target based on the port and label
        :param port: port of the target
        :param label_type: type of the label
        :param label_value: stored label
        :return: new identification of the target
        """
        # Debug
        log.msg('SDNCREST: getTarget, port_map[port] = %s and str(label_value) = %s' % (
            self.port_map[port], str(label_value)), system=self.log_system)
        return self.port_map[port] + '#' + str(label_value)

    def createConnectionId(self, source_target, dest_target):
        """
        Create new connection ID
        :param source_target: source of the connection
        :param dest_target: destination of the connection
        :return: connection ID
        """
        # Debug
        log.msg('SDNCREST: createConnectionId', system=self.log_system)
        return 'SDNCREST-' + ''.join([random.choice(string.hexdigits[:16]) for _ in range(8)])

    def canSwapLabel(self, label_type):
        # Debug
        log.msg('SDNCREST: canSwapLabel Connection Manager function', system=self.log_system)
        # return True
        return False

    def setupLink(self, connection_id, source_target, dest_target, bandwidth):
        """
        Attempt to setup requested link

        :param connection_id: ID of the connection in NSA
        :param source_target: source of the connection
        :param dest_target: destination of the connection
        :param bandwidth: bandwith to reserve
        :return: deferred notification
        """
        # Debug
        log.msg('SDNCREST: setupLink', system=self.log_system)
        result = self.client.provision(cfg=self.cfg,
                                       connection_id=connection_id,
                                       source_target=source_target,
                                       dest_target=dest_target,
                                       bandwidth=bandwidth)
        if result:
            # Log the provisioning
            log.msg('Link %s -> %s up, connection_id = %s' % (source_target, dest_target, connection_id),
                    system=self.log_system)
            # Return deferred notification
            return defer.succeed(None)
        else:
            # Log the failed provisioning
            log.msg('ERROR: CANNOT Provision Link %s -> %s' % (source_target, dest_target),
                    system=self.log_system)
            # Return deferred notification
            return defer.fail(None)

    def teardownLink(self, connection_id, source_target, dest_target, bandwidth):
        """
        Deallocate provisioned link

        :param connection_id: ID of the connection in NSA
        :param source_target: source of the connection
        :param dest_target: destination of the connection
        :param bandwidth: bandwith to reserve
        :return: deferred notification
        """
        # Debug
        log.msg('SDNCREST: teardownLink and connection_id = %s' % connection_id, system=self.log_system)
        result = self.client.teardown(self.cfg, connection_id, source_target, dest_target)
        if result:
            # Log the deactivation
            log.msg('Link %s -> %s down' % (source_target, dest_target), system=self.log_system)
            # Return deferred notification
            return defer.succeed(None)
        else:
            # Log the failed deactivation
            log.msg('ERROR: CANNOT teardown Link %s -> %s ' % (source_target, dest_target), system=self.log_system)
            # Return deferred notification
            return defer.fail(None)
