from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_interfaces_api

__author__ = 'Robert Zahradnicek'


class TestODLvBridgeInterfacesCreateApiModel:
    """
    Test basic ODL vBridge Interfaces Create POST request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_create_vbridge_interface_request_uri(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface Shows endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api._create_vbridge_interface_uri(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces"

    def test_create_vbridge_interface_request_body_description(self):
        """
        Test ODL VTN Coordinator request body generation for accessing
        vBridge Interfaces GET Interface Shows endpoint
        """
        result = vbridge_interfaces_api._create_vbridge_interface_body(if_name="test_if_1",
                                                                   description="test")
        assert result["interface"]["if_name"] == "test_if_1"
        assert result["interface"]["description"] == "test"

    def test_create_vbridge_interface_request_body_adminstatus(self):
        """
        Test ODL VTN Coordinator request body generation for accessing
        vBridge Interfaces GET Interface Shows endpoint
        """
        result = vbridge_interfaces_api._create_vbridge_interface_body(if_name="test_if_1",
                                                                   adminstatus="enable")
        assert result["interface"]["if_name"] == "test_if_1"
        assert result["interface"]["adminstatus"] == "enable"

    def test_create_vbridge_interface_request_body_full(self):
        """
        Test ODL VTN Coordinator request body generation for accessing
        vBridge Interfaces GET Interface Shows endpoint
        """
        result = vbridge_interfaces_api._create_vbridge_interface_body(if_name="test_if_1",
                                                                   description="test",
                                                                   adminstatus="enable")
        assert result["interface"]["if_name"] == "test_if_1"
        assert result["interface"]["description"] == "test"
        assert result["interface"]["adminstatus"] == "enable"

    def test_create_vbridge_interface_request(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface Shows endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api.create_vbridge_interface(base_url=base_url,
                                                             vtn_name=vtn_name,
                                                             vbr_name=vbr_name,
                                                             if_name="test_if_1")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces"
        assert result[1]["interface"]["if_name"] == "test_if_1"


class TestODLvBridgeInterfacesListApiModel:
    """
    Test basic ODL vBridge Interfaces List GET request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_list_vbridge_interfaces(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces(base_url=base_url,
                                                          vtn_name=vtn_name,
                                                          vbr_name=vbr_name, ) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces"

    def test_list_vbridge_interfaces_if_name(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                if_name="test_if_1") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces?index=test_if_1"

    def test_list_vbridge_interfaces_max_repetition(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces?max_repetition=500"

    def test_list_vbridge_interfaces_full(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                if_name="test_if_1",
                                                                max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces?index=test_if_1&max_repetition=500"


    def test_list_vbridge_interfaces_detail(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_detail(base_url=base_url,
                                                                 vtn_name=vtn_name,
                                                                 vbr_name=vbr_name) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/detail"

    def test_list_vbridge_interfaces_detail_if_name(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_detail(base_url=base_url,
                                                                 vtn_name=vtn_name,
                                                                 vbr_name=vbr_name,
                                                                 if_name="test_if_1") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/detail?index=test_if_1"

    def test_list_vbridge_interfaces_detail_max_repetition(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_detail(base_url=base_url,
                                                                 vtn_name=vtn_name,
                                                                 vbr_name=vbr_name,
                                                                 max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/detail?max_repetition=500"

    def test_list_vbridge_interfaces_detail_full(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_detail(base_url=base_url,
                                                                 vtn_name=vtn_name,
                                                                 vbr_name=vbr_name,
                                                                 if_name="test_if_1",
                                                                 max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/detail?index=test_if_1&max_repetition=500"

    def test_list_vbridge_interfaces_count(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_count(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/count"

    def test_list_vbridge_interfaces_count_if_name(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_count(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                if_name="test_if_1") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/count?index=test_if_1"

    def test_list_vbridge_interfaces_count_max_repetition(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_count(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/count?max_repetition=500"

    def test_list_vbridge_interfaces_count_full(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.list_vbridge_interfaces_count(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                if_name="test_if_1",
                                                                max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/count?index=test_if_1&max_repetition=500"


class TestODLvBridgeInterfacesShowApiModel:
    """
    Test basic ODL vBridge Interfaces Show GET request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_show_vbridge_interface_request(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface Shows endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.show_vbridge_interface(base_url=base_url,
                                                         vtn_name=vtn_name,
                                                         vbr_name=vbr_name,
                                                         if_name="test_if_1") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"


class TestODLvBridgeInterfacesPutApiModel:
    """
    Test basic ODL vBridge Interfaces Update Put request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_update_vbridge_interface_request_uri(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api._update_vbridge_interface_uri(base_url=base_url,
                                                                vtn_name=vtn_name,
                                                                vbr_name=vbr_name,
                                                                if_name="test_if_1") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"

    def test_update_vbridge_interface_request_body(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """

        result = vbridge_interfaces_api._update_vbridge_interface_body()
        assert result["interface"] == {}

    def test_update_vbridge_interface_request_body_description(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api._update_vbridge_interface_body(description="test")
        assert result["interface"]["description"] == "test"

    def test_update_vbridge_interface_request_body_adminstatus(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api._update_vbridge_interface_body(adminstatus="enable")
        assert result["interface"]["adminstatus"] == "enable"

    def test_update_vbridge_interface_request_body_full(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api._update_vbridge_interface_body(description="test",
                                                                   adminstatus="enable")
        assert result["interface"]["description"] == "test"
        assert result["interface"]["adminstatus"] == "enable"

    def test_update_vbridge_interface_request(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api.update_vbridge_interface(base_url=base_url,
                                                             vtn_name=vtn_name,
                                                             vbr_name=vbr_name,
                                                             if_name="test_if_1")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"
        assert result[1]["interface"] == {}

    def test_update_vbridge_interface_request_description(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api.update_vbridge_interface(base_url=base_url,
                                                             vtn_name=vtn_name,
                                                             vbr_name=vbr_name,
                                                             if_name="test_if_1",
                                                             description="test")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"
        assert result[1]["interface"]["description"] == "test"

    def test_update_vbridge_interface_request_adminstatus(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api.update_vbridge_interface(base_url=base_url,
                                                             vtn_name=vtn_name,
                                                             vbr_name=vbr_name,
                                                             if_name="test_if_1",
                                                             adminstatus="enable")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"
        assert result[1]["interface"]["adminstatus"] == "enable"

    def test_update_vbridge_interface_request_full(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        result = vbridge_interfaces_api.update_vbridge_interface(base_url=base_url,
                                                             vtn_name=vtn_name,
                                                             vbr_name=vbr_name,
                                                             if_name="test_if_1",
                                                             description="test",
                                                             adminstatus="enable")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"
        assert result[1]["interface"]["description"] == "test"
        assert result[1]["interface"]["adminstatus"] == "enable"


class TestODLvBridgeInterfacesDeleteApiModel:
    """
    Test basic ODL vBridge Interfaces DELETE request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_delete_vbridge_interface_request_uri(self, base_url, vtn_name, vbr_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces PUT Interface Update endpoint
        :param base_url: base of the url for the request
        :param vtn_name: Virtual Tenant Network name
        :param vbr_name: vBridge name
        """
        assert vbridge_interfaces_api.delete_vbridge_interface(base_url=base_url,
                                                           vtn_name=vtn_name,
                                                           vbr_name=vbr_name,
                                                           if_name="test_if_1") == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn/vbridges/test_vbr/interfaces/test_if_1"
