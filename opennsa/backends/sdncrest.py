"""
SDNC REST backend

Notes:


Teardown:


"""

from twisted.python import log
from twisted.internet import defer

from opennsa import constants as cnt, config
from opennsa import error

from opennsa.backends.common import genericbackend
from opennsa.backends.common.rest import rest

import string
import random

import urllib2
import json

LOG_SYSTEM = 'opennsa.rest'


def sdncrest_get_vtn(url, vtn):
    """
        Check if VTN exists using VTN on opennsa.conf
    """

    # TODO: get VTN query
    query, action = 'data.cgi?action=get_workgroups'
    # TODO: make the request through request library from rest moduel!!!!
    response = urllib2.urlopen(url + query)
    response_body = response.read()

    # TODO: Check the response
    json_data = json.loads(response_body)
    search_results = json_data['results']
    for er in search_results:
       if er['vtn_name'] == vtn:
         vtn_id = er['workgroup_id']
         # Debug
         log.msg('SDNCREST: sdncrest_get_vtn_id, vtn_id: %s' % vtn_id, logLevel=logging.DEBUG)
         return vtn_id

    log.msg('SDNCREST: unable to find virtual tenant network named: %s' % vtn_id, logLevel=logging.ERROR)


def sdncrest_authenticate(url, user, pw, log_system):
    """
    Authenticate against controller, create session for reuse!!!
    """
    # TODO: make through the requests library
    # Debug
    log.msg('SDNCREST: SDNCREST_authenticate and url: %s' % (url), logLevel = logging.DEBUG)

    # create a password manager
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

    try:
       # Add the username and password.
       password_mgr.add_password(None, url, user, pw)
       handler = urllib2.HTTPBasicAuthHandler(password_mgr)

       # create "opener" (OpenerDirector instance)
       opener = urllib2.build_opener(handler)

       # use the opener to fetch a URL
       opener.open(url)

       # Install the opener.
       # Now all calls to urllib2.urlopen use our opener.
       urllib2.install_opener(opener)
    except:
       log.msg('ERROR: User or Password Incorrect.', logLevel = logging.ERROR)
       log.err()
       return defer.fail(error.InternalNRMError('SDNCREST\'s User or Password Incorrect'))


def sdncrest_valid_interface(url, interface):
    # TODO: check availability through the REST API from model
    #parse the interface/switch/vlan tag
    (sw,int_vlan) = interface.split(':')
    (int_name,vlan) = int_vlan.split('#')

    #request the data about the interface
    query, action = 'data.cgi?', 'action=get_node_interfaces&node='
    data = urllib2.urlopen(url + query + action + switch)
    jsonData = json.loads(data.read())
    searchResults = jsonData['results']
    if_exist = 0
    for res in searchResults:
        if res['name'] == if1:
            if_exist = 1
    if if_exist == 0:
        return defer.fail(error.InternalNRMError('ERROR: Configured interface %s does not exist' % if1))

    #verify the interface
    query = 'data.cgi?action=is_vlan_tag_available&node=%s&vlan=%s&interface=%s' % (sw,vlan,int_name)
    data = urllib2.urlopen(url + query)
    jsonData = json.loads(data.read())
    searchResults = jsonData['results']
    if searchResults:
        # Debug
        # print searchResults[0]
        if searchResults[0]['available'] == 0:
            return defer.fail(error.InternalNRMError('ERROR: VLAN %s not available on interface %s' % (vlan, iface)))
    else:
        return defer.fail(error.InternalNRMError('ERROR: interface %s does not exist on switch %s' % (iface, s)))

    return sw, int_name, vlan


def sdncrest_validate_input(url, input1, input2):
    """ Validate switches, interfaces and VLANs chosen
        In case of error, return 99 for switch issues, 98 for vlan/interfaces issues and 93 for interfaces issues
        Input should be: sw:interface#vlan
    """

    (sw1, if1, vlan1) = sdncrest_valid_interface(url, input1)
    (sw2, if2, vlan2) = sdncrest_valid_interface(url, input2)


    return sw1, sw2, if1, if2, vlan1, vlan2
    # If we get here, switches, interfaces and vlans are correct. Now, provision the circuit


def find_path(url, sw1, sw2, used_links):
    # TODO check topology via rest api
    # Find primary path

    query = 'data.cgi?action=get_shortest_path&node=%s&node=%s' % (sw1, sw2)

    for link in used_links:
        query += "&link=%s" % (link)

    data = urllib2.urlopen(url + query)
    jsonData = json.loads(tmp.read())
    searchResults = jsonData['results']
    path = []
    if searchResults:
        for link in searchResults:
           path.append(link['link'])
    else:
        return defer.fail(error.InternalNRMError('ERROR: There is no path between %s and %s' % (sw1, sw2)))

    return path


def sdncrest_provision_circuit(url, wg_id ,sw1, sw2, if1, if2, vlan1, vlan2):
    """ Provision the circuit using parameters received
        Support Backup and Primary path
    """
    # Debug
    log.msg('SDNCREST: SDNCREST_provision_circuit', logLevel = logging.DEBUG)

    provision_string = 'action=provision_circuit&workgroup_id=%s&node=%s&interface=%s&tag=%s&node=%s&interface=%s&tag=%s' % (sw1, if1, vlan1, sw2, if2, vlan2)

    primary_path = find_path(url, sw1, sw2, [])
    backup_path = find_path(url, sw1, sw2, primary_path)

    for link in primary_path:
        provision_string += "&link=" + link

    for link in backup_path:
        provision_string += "&backup_link=" + link

    #start/end times
    provision_string += 'provision_time=-1&remove_time=-1&description=NSI-VLAN %s' % (vlan1)

    # start and remove time are handled by OpenNSA, so we set as -1
    query = 'provisioning.cgi?' + provisioning_string
    request = urllib2.urlopen(url + query)
    jsonData = json.loads(request.read())

    searchResults = jsonData['results']
    if searchResults['success']:
        return searchResults['circuit_id']
    else:
        return defer.fail(error.InternalNRMError('ERROR: It was not possible to provision the circuit. Check SDNCREST logs'))


def sdncrest_remove_circuit(url, circuit_id, wg_id):
    """ Remove circuit using circuit_id and workgroup_id
    """
    # Debug
    log.msg('SDNCREST: SDNCREST_remove_circuit')

    action = 'provisioning.cgi?action=remove_circuit&circuit_id=' + circuit_id + '&remove_time=-1&workgroup_id=' + wg_id
    request = urllib2.urlopen(url + action)
    jsonData = json.loads(request.read())
    searchResults = jsonData['results']
    if jsonData:
        pass
        log.msg('SDNCREST: SDNCREST_remove_circuit: circuit %s removed' % circuit_id, logLevel = logging.INFO)
    else:
        return defer.fail(error.InternalNRMError('ERROR: it was not possible to remove the circuit'))


def SDNCRESTBackend(network_name, nrm_ports, parent_requester, configuration):
    """
    SDNC REST Api backend generic class for setup it extends GenericBackend

    :param network_name:
    :param nrm_ports:
    :param parent_requester:
    :return:

    """
    log.msg('SDNCREST: SDNCRESTBackend')
    name = 'SDNCREST NRM %s' % network_name
    # for the generic backend
    nrm_map = dict([(p.name, p) for p in nrm_ports])
    # for the nrm backend
    port_map = dict([(p.name, p.interface) for p in nrm_ports])

    cm = SDNCRESTConnectionManager(name, port_map, configuration)
    return genericbackend.GenericBackend(network_name, nrm_map, cm, parent_requester, name, minimum_duration=1)


class SDNCRESTConnectionManager(object):

    def __init__(self, log_system, port_map, cfg):
        self.log_system = log_system
        self.port_map = port_map

        self.url = cfg[config.SDNCREST_URL]
        self.username = cfg[config.SDNCREST_USER]
        self.password = cfg[config.SDNCREST_PASSWORD]
        self.vtn = cfg[config.SDNCREST_VTN]
  
        self.wg_id = sdncrest_authenticate(self.url, self.username, self.password, log_system)

    def getResource(self, port, label_type, label_value):
        # Debug
        log.msg('SDNCREST: getResource',system=self.log_system)
        return self.port_map[port] + ':' + str(label_value)

    def getTarget(self, port, label_type, label_value):
        # Debug
        log.msg('SDNCREST: getTarget, port_map[port] = %s and str(label_value) = %s' % (self.port_map[port], str(label_value)),system=self.log_system)        
        return self.port_map[port] + '#' + str(label_value)

    def createConnectionId(self, source_target, dest_target):
        # Debug
        log.msg('SDNCREST: createConnectionId',system=self.log_system)
        return 'SDNCREST-' + ''.join( [ random.choice(string.hexdigits[:16]) for _ in range(8) ] )

    def canSwapLabel(self, label_type):
        # Debug
        log.msg('SDNCREST: canSwapLabel',system=self.log_system)
        #return True
        return False

    def setupLink(self, connection_id, source_target, dest_target, bandwidth):    
        # Debug
        log.msg('SDNCREST: setupLink',system=self.log_system)
        sw1, sw2, if1, if2, vlan1, vlan2 = sdncrest_validate_input(self.url, source_target, dest_target)
        wg_id = SDNCREST_get_wg_id(self.url, self.workgroup) 
        self.circuit_id = sdncrest_provision_circuit(self.url, wg_id, sw1, sw2, if1, if2, vlan1, vlan2)
        log.msg('Link %s -> %s up, circuit_id = %s' % (source_target, dest_target, self.circuit_id), system=self.log_system)
        return defer.succeed(None)

    def teardownLink(self, connection_id, source_target, dest_target, bandwidth):
        # Debug
        log.msg('SDNCREST: teardownLink and self.circuit_id = %s' % self.circuit_id, system=self.log_system)
        wg_id = SDNCREST_get_wg_id(self.url, self.workgroup)
        SDNCREST_remove_circuit(self.url, self.circuit_id, wg_id)
        log.msg('Link %s -> %s down' % (source_target, dest_target), system=self.log_system)
        return defer.succeed(None)