from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_interface_portmap_api

__author__ = 'Robert Zahradnicek'


class TestODLvBridgeInterfacePortMapShowApiModel:
    """
    Test basic ODL vBridge Interface Port Map GET request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_show_vbridge_interface_portmap_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge DELETE Interface Port Map endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_interface_portmap_api.show_vbridge_interface_portmap(base_url=base_url,
                                                                            vtn_name=vtn_name,
                                                                            vbr_name="test_vbridge",
                                                                            if_name="test_if") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/interfaces/test_if/portmap"


class TestODLvBridgeInterfacePortMapPutApiModel:
    """
    Test basic ODL vBridge Interface Port Map PUT request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_update_vbridge_interface_portmap_request_uri(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_interface_portmap_api._update_vbridge_interface_portmap_uri(base_url=base_url,
                                                                                   vtn_name=vtn_name,
                                                                                   vbr_name="test_vbridge",
                                                                                   if_name="test_if") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/interfaces/test_if/portmap"

    def test_update_vbridge__interface_portmap_logical_port_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge PUT endpoint
        """
        result = vbridge_interface_portmap_api._update_vbridge_interface_portmap_body(logical_port_id="logical_port_1")
        body = result
        assert body["portmap"]["logical_port_id"] == "logical_port_1"

    def test_update_vbridge__interface_portmap_with_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge PUT endpoint
        """
        result = vbridge_interface_portmap_api._update_vbridge_interface_portmap_body(logical_port_id="logical_port_1",
                                                                                      vlan_id="vlan_1")
        body = result
        assert body["portmap"]["logical_port_id"] == "logical_port_1"
        assert body["portmap"]["vlan_id"] == "vlan_1"

    def test_update_vbridge__interface_portmap_with_tagged_request_body(self, configuration):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_interface_portmap_api._update_vbridge_interface_portmap_body(logical_port_id="logical_port_1",
                                                                                      tagged="tag_1")
        body = result
        assert body["portmap"]["logical_port_id"] == "logical_port_1"
        assert body["portmap"]["tagged"] == "tag_1"

    def test_update_vbridge__interface_portmap_full_request_body(self, configuration):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_interface_portmap_api._update_vbridge_interface_portmap_body(logical_port_id="logical_port_1",
                                                                                      vlan_id="vlan_1",
                                                                                      tagged="tag_1")
        body = result
        assert body["portmap"]["logical_port_id"] == "logical_port_1"
        assert body["portmap"]["vlan_id"] == "vlan_1"
        assert body["portmap"]["tagged"] == "tag_1"

    def test_update_vbridge_interface_portmap_with_vlan_id_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_interface_portmap_api.update_vbridge_interface_portmap(base_url=base_url,
                                                                                vtn_name=vtn_name,
                                                                                vbr_name="test_vbridge",
                                                                                if_name="test_if",
                                                                                logical_port_id="logical_port_1",
                                                                                vlan_id="vlan_1")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/interfaces/test_if/portmap"

        body = result[1]
        assert body["portmap"]["logical_port_id"] == "logical_port_1"
        assert body["portmap"]["vlan_id"] == "vlan_1"

    def test_update_vbridge_interface_portmap_with_tagged_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_interface_portmap_api.update_vbridge_interface_portmap(base_url=base_url,
                                                                                vtn_name=vtn_name,
                                                                                vbr_name="test_vbridge",
                                                                                if_name="test_if",
                                                                                logical_port_id="logical_port_1",
                                                                                tagged="tag_1")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/interfaces/test_if/portmap"

        body = result[1]
        assert body["portmap"]["logical_port_id"] == "logical_port_1"
        assert body["portmap"]["tagged"] == "tag_1"

    def test_update_vbridge_interface_portmap_full_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_interface_portmap_api.update_vbridge_interface_portmap(base_url=base_url,
                                                                                vtn_name=vtn_name,
                                                                                vbr_name="test_vbridge",
                                                                                if_name="test_if",
                                                                                logical_port_id="logical_port_1",
                                                                                vlan_id="vlan_1",
                                                                                tagged="tag_1")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/interfaces/test_if/portmap"

        body = result[1]
        assert body["portmap"]["logical_port_id"] == "logical_port_1"
        assert body["portmap"]["vlan_id"] == "vlan_1"
        assert body["portmap"]["tagged"] == "tag_1"


class TestODLvBridgeInterfacePortMapDeleteApiModel:
    """
    Test basic ODL vBridge Interface Port Map DELETE request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_delete_vbridge_interface_portmap_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge DELETE Interface Port Map endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_interface_portmap_api.delete_vbridge_interface_portmap(base_url=base_url,
                                                                              vtn_name=vtn_name,
                                                                              vbr_name="test_vbridge",
                                                                              if_name="test_if") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/interfaces/test_if/portmap"
