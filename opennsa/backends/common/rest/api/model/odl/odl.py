from twisted.python import log

from opennsa import config
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import controller_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vtn_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_interfaces_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_interface_portmap_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import logical_port_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vlanmap_api

import json

__author__ = 'Robert Zahradnicek'

LOG_SYSTEM = 'opennsa.SDNCREST'


class ODLApi:
    """
    OpenDaylight API model object for interacting with the API model
    publicly provides only provision and teardown functions. It is
    instantiated from the RESTApiModel class as REST API implementation
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def provision(self, cfg, client, connection_id, source_target, dest_target, bandwidth):
        """
        Provision the virtual link request through OpenDaylight controller
        :param cfg: configuration retrieved from OpenNSA configuration file
        :param client: generic REST client for making requests
        :param connection_id: connection ID from OpenNSA
        :param source_target: source in request
        :param dest_target: destination in request
        :param bandwidth: bandwith in request
        :return: True if successful False otherwise
        """
        # Check and controller through coordinator
        request = controller_api.list_controllers(base_url=self.base_url,
                                                  controller_id=cfg[config.SDNCREST_CNTRL_ID])

        result = client.get(url=request)
        if result.status_code == 200:
            # If controller does not exist add it
            request = controller_api.create_controller(base_url=self.base_url,
                                                       controller_id=cfg[config.SDNCREST_CNTRL_ID],
                                                       version=cfg[config.SDNCREST_CNTRL_VERSION],
                                                       controller_type=cfg[config.SDNCREST_CNTRL_TYPE],
                                                       ipaddr=cfg[config.SDNCREST_CNTRL_IP])
            result = client.post(url=request[0], data=json.dumps(request[1]))
            if result.status_code == 201:
                log.msg('SDNCREST: ODLApi controller %s with IP %s ADDED' %
                        (cfg[config.SDNCREST_CNTRL_ID], cfg[config.SDNCREST_CNTRL_IP]))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi controller %s with IP %s ALREADY EXISTS' %
                        (cfg[config.SDNCREST_CNTRL_ID], cfg[config.SDNCREST_CNTRL_IP]))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi controller %s with IP %s 400 BAD REQUEST' %
                        (cfg[config.SDNCREST_CNTRL_ID], cfg[config.SDNCREST_CNTRL_IP]))
                return False

        # Check VTN
        vtn_name = cfg[config.SDNCREST_VTN]
        request = vtn_api.list_vtn(base_url=self.base_url, vtn_name=vtn_name)
        result = client.get(url=request)
        if result.status_code != 200:
            # If does not exist create it
            request = vtn_api.create_vtn(base_url=self.base_url, vtn_name=vtn_name)
            result = client.post(url=request[0], data=json.dumps(request[1]))
            if result.status_code == 201:
                log.msg('SDNCREST: ODLApi VTN %s ADDED' % vtn_name)
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi VTN %s ALREADY EXISTS' % vtn_name)
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s 400 BAD REQUEST' % vtn_name)
                return False

        # Check vBridge
        vbr_name = "vbridge_" + str(connection_id)
        request = vbridge_api.list_vbridge(base_url=self.base_url,
                                           vtn_name=vtn_name,
                                           vbr_name=vbr_name)
        result = client.get(url=request)
        if result.status_code == 200:
            # If does not exist create it
            request = vbridge_api.create_vbridge(base_url=self.base_url,
                                                 vtn_name=vtn_name,
                                                 vbr_name=vbr_name,
                                                 controller_id=cfg[config.SDNCREST_CNTRL_ID],
                                                 domain_id="DEFAULT")
            result = client.post(url=request[0], data=json.dumps(request[1]))
            if result.status_code == 201:
                log.msg('SDNCREST: ODLApi VTN %s NEW vBridge %s ADDED' % (vtn_name, vbr_name))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi VTN %s with vBridge %s ALREADY EXISTS' % (vtn_name, vbr_name))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s with vBridge %s 400 BAD REQUEST' % (vtn_name, vbr_name))
                return False

        # Check vBridge interfaces
        request = vbridge_interfaces_api.list_vbridge_interfaces(base_url=self.base_url,
                                                                 vtn_name=vtn_name, vbr_name=vbr_name,
                                                                 if_name=source_target)
        result = client.get(url=request)
        if_name_1 = str(vbr_name) + "_logical_" + str(source_target)
        if_name_2 = str(vbr_name) + "_logical_" + str(dest_target)
        if result.status_code == 200:
            # If does not exists create it
            request = vbridge_interfaces_api.create_vbridge_interface(base_url=self.base_url,
                                                                      vtn_name=vtn_name,
                                                                      vbr_name=vbr_name,
                                                                      if_name=if_name_1)
            result = client.post(url=request[0], data=json.dumps(request[1]))
            if result.status_code in (201, 202, 204):
                log.msg(
                    'SDNCREST: ODLApi vBridge %s NEW vInterface %s -> %s ADDED' % (vbr_name, source_target, if_name_1))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi vBridge %s vInterface %s -> %s ALREADY EXISTS' % (vbr_name,
                                                                                            source_target,
                                                                                            if_name_1))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s with vBridge %s vInterface %s -> %s 400 BAD REQUEST' % (vtn_name,
                                                                                                         vbr_name,
                                                                                                         source_target,
                                                                                                         if_name_1))
                return False

            # If does not exists create it
            request = vbridge_interfaces_api.create_vbridge_interface(base_url=self.base_url,
                                                                      vtn_name=vtn_name,
                                                                      vbr_name=vbr_name,
                                                                      if_name=if_name_2)
            result = client.post(url=request[0], data=json.dumps(request[1]))
            if result.status_code in (201, 202, 204):
                log.msg(
                    'SDNCREST: ODLApi vBridge %s NEW vInterface %s -> %s ADDED' % (vbr_name, source_target, if_name_2))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi vBridge %s vInterface %s -> %s ALREADY EXISTS' % (vbr_name,
                                                                                            source_target,
                                                                                            if_name_2))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s with vBridge %s vInterface %s -> %s 400 BAD REQUEST' % (vtn_name,
                                                                                                         vbr_name,
                                                                                                         source_target,
                                                                                                         if_name_2))


        # Check interfaces and create mappings
        request = logical_port_api.list_logical_ports(base_url=self.base_url,
                                                      controller_id=cfg[config.SDNCREST_CNTRL_ID],
                                                      domain_id="DEFAULT")

        result = client.get(url=request)
        logical_port_id_1 = None
        logical_port_id_2 = None
        # Search the source and destination logical ports
        if result.status_code == 200:
            content = json.loads(result.content)
            if content["logical_ports"]:
                for ports in content["logical_ports"]:
                    # Check if such source exists
                    if source_target in ports["logical_port_id"]:
                        logical_port_id_1 = ports["logical_port_id"]
                        request = vbridge_interface_portmap_api.update_vbridge_interface_portmap(base_url=self.base_url,
                                                                                                 vtn_name=vtn_name,
                                                                                                 vbr_name=vbr_name,
                                                                                                 if_name=if_name_1,
                                                                                                 logical_port_id=ports[
                                                                                                     "logical_port_id"])
                        result = client.post(url=request[0], data=request[1])
                        if result.status_code in (201, 202, 204):
                            log.msg('SDNCREST: ODLApi NEW mapping ADDED')
                        elif result.status_code == 409:
                            log.msg('SDNCREST: ODLApi Mapping ALREADY EXISTS')
                        elif result.status_code == 400:
                            log.msg('SDNCREST: ODLApi Mapping 400 BAD REQUEST')
                    # Check if such destination exists
                    if dest_target in ports["logical_port_id"]:
                        logical_port_id_2 = ports["logical_port_id"]
                        request = vbridge_interface_portmap_api.update_vbridge_interface_portmap(base_url=self.base_url,
                                                                                                 vtn_name=vtn_name,
                                                                                                 vbr_name=vbr_name,
                                                                                                 if_name=if_name_2,
                                                                                                 logical_port_id=ports[
                                                                                                     "logical_port_id"])
                        result = client.post(url=request[0], data=request[1])
                        if result.status_code in (201, 202, 204):
                            log.msg('SDNCREST: ODLApi NEW mapping ADDED')
                        elif result.status_code == 409:
                            log.msg('SDNCREST: ODLApi Mapping ALREADY EXISTS')
                        elif result.status_code == 400:
                            log.msg('SDNCREST: ODLApi Mapping 400 BAD REQUEST')

        # Check VLAN mapping
        vlanmap_id = "vlan_" + str(connection_id)
        request = vlanmap_api.list_vlanmap(base_url=self.base_url,
                                           vtn_name=vtn_name,
                                           vbr_name=vbr_name,
                                           vlanmap_id=vlanmap_id)
        result = client.get(url=request)
        if result.status_code == 200:
            # If does not exist create it based on the configuration and unique ID
            request = vtn_api.create_vtn(base_url=self.base_url, vtn_name=vtn_name)
            result = client.post(url=request[0], data=json.dumps(request[1]))
            if result.status_code == 201:
                log.msg('SDNCREST: ODLApi VTN %s vBridge %s VLAN Mapping %s ADDED' %
                        (vtn_name, vbr_name, vlanmap_id))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi VTN %s vBridge %s with VLAN Mapping %s ALREADY EXISTS' %
                        (vtn_name, vbr_name, vlanmap_id))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s vBridge %s with VLAN Mapping %s 400 BAD REQUEST' %
                        (vtn_name, vbr_name, vlanmap_id))
                return False

        return True

    def teardown(self, cfg, client, connection_id, source_target, dest_target):
        """
        Teardown the virtual link request through OpenDaylight controller
        It retains VTN and added controller because they do not change between
        requests and are based on configuration
        :param cfg: parsed configuration file
        :param client: generic REST client for making requests
        :param connection_id: connection ID from OpenNSA
        :return: True if successful False otherwise
        """
        vtn_name = cfg[config.SDNCREST_VTN]
        vbr_name = "vbridge_" + str(connection_id)
        vlanmap_id = "vlan_" + str(connection_id)

        if_name_1 = str(vbr_name) + "_logical_" + str(source_target)
        if_name_2 = str(vbr_name) + "_logical_" + str(dest_target)

        # List vlanmappings
        request = vlanmap_api.list_vlanmap(base_url=self.base_url,
                                           vtn_name=vtn_name,
                                           vbr_name=vbr_name)
        result = client.get(url=request)
        content = json.loads(result.content)
        if content["vlanmaps"]:
            # DELETE VLAN mapping if some exists
            request = vlanmap_api.delete_vlanmap(base_url=self.base_url,
                                                 vtn_name=vtn_name,
                                                 vbr_name=vbr_name,
                                                 vlanmap_id=vlanmap_id)
            result = client.delete(url=request)
            if result.status_code == 204:
                log.msg('SDNCREST: ODLApi VTN %s vBridge %s VLAN Mapping %s DELETED' %
                        (vtn_name, vbr_name, vlanmap_id))
            elif result.status_code == 404:
                log.msg('SDNCREST: ODLApi VTN %s vBridge %s with VLAN Mapping %s DOES NOT EXISTS' %
                        (vtn_name, vbr_name, vlanmap_id))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s vBridge %s with VLAN Mapping %s 400 BAD REQUEST' %
                        (vtn_name, vbr_name, vlanmap_id))
                return False

        # DELETE vBridge interface mapping
        request = vbridge_interface_portmap_api.delete_vbridge_interface_portmap(base_url=self.base_url,
                                                                                 vtn_name=vtn_name,
                                                                                 vbr_name=vbr_name,
                                                                                 if_name=if_name_1)
        result = client.delete(url=request)
        if result.status_code == 204:
            log.msg('SDNCREST: ODLApi Mapping %s DELETED' % if_name_1)
        elif result.status_code == 404:
            log.msg('SDNCREST: ODLApi Mapping %s DOES NOT EXISTS' % if_name_1)
        elif result.status_code == 400:
            log.msg('SDNCREST: ODLApi Mapping %s 400 BAD REQUEST' % if_name_1)
            return False

        request = vbridge_interface_portmap_api.delete_vbridge_interface_portmap(base_url=self.base_url,
                                                                                 vtn_name=vtn_name,
                                                                                 vbr_name=vbr_name,
                                                                                 if_name=if_name_2)
        result = client.delete(url=request)
        if result.status_code == 204:
            log.msg('SDNCREST: ODLApi Mapping %s DELETED' % if_name_2)
        elif result.status_code == 404:
            log.msg('SDNCREST: ODLApi Mapping %s DOES NOT EXISTS' % if_name_2)
        elif result.status_code == 400:
            log.msg('SDNCREST: ODLApi Mapping %s 400 BAD REQUEST' % if_name_2)
            return False

        # List interfaces
        request = vbridge_interfaces_api.list_vbridge_interfaces(base_url=self.base_url,
                                                                 vtn_name=vtn_name,
                                                                 vbr_name=vbr_name)
        result = client.get(url=request)
        content = json.loads(result.content)
        if content["interfaces"]:
            # DELETE vBridge virtual interfaces
            request = vbridge_interfaces_api.delete_vbridge_interface(base_url=self.base_url,
                                                                      vtn_name=vtn_name,
                                                                      vbr_name=vbr_name,
                                                                      if_name=if_name_1)
            result = client.post(url=request)

            if result.status_code in (201, 202, 204):
                log.msg(
                    'SDNCREST: ODLApi vBridge %s NEW vInterface %s -> %s DELETED' % (vbr_name, source_target, if_name_1))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi vBridge %s vInterface %s -> %s DOES NOT EXISTS' % (vbr_name,
                                                                                             source_target,
                                                                                             if_name_1))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s with vBridge %s vInterface %s -> %s 400 BAD REQUEST' % (vtn_name,
                                                                                                         vbr_name,
                                                                                                         source_target,
                                                                                                         if_name_1))
                return False

            request = vbridge_interfaces_api.delete_vbridge_interface(base_url=self.base_url,
                                                                      vtn_name=vtn_name,
                                                                      vbr_name=vbr_name,
                                                                      if_name=if_name_2)
            result = client.post(url=request)
            if result.status_code in (201, 202, 204):
                log.msg(
                    'SDNCREST: ODLApi vBridge %s NEW vInterface %s -> %s DELETED' % (vbr_name, source_target, if_name_2))
            elif result.status_code == 409:
                log.msg('SDNCREST: ODLApi vBridge %s vInterface %s -> %s DOES NOT EXISTS' % (vbr_name,
                                                                                             source_target,
                                                                                             if_name_2))
            elif result.status_code == 400:
                log.msg('SDNCREST: ODLApi VTN %s with vBridge %s vInterface %s -> %s 400 BAD REQUEST' % (vtn_name,
                                                                                                         vbr_name,
                                                                                                         source_target,
                                                                                                         if_name_2))

        # DELETE vBridge
        vbr_name = "vbridge_" + str(connection_id)
        request = vbridge_api.delete_vbridge(base_url=self.base_url,
                                             vtn_name=vtn_name,
                                             vbr_name=vbr_name)
        result = client.delete(url=request)
        if result.status_code == 204:
            log.msg('SDNCREST: ODLApi VTN %s NEW vBridge %s DELETED' % (vtn_name, vbr_name))
        elif result.status_code == 409:
            log.msg('SDNCREST: ODLApi VTN %s with vBridge %s DOES NOT EXISTS' % (vtn_name, vbr_name))
        elif result.status_code == 400:
            log.msg('SDNCREST: ODLApi VTN %s with vBridge %s 400 BAD REQUEST' % (vtn_name, vbr_name))
            return False
        return True
