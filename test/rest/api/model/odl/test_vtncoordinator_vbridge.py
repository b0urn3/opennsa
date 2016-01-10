from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_api

__author__ = 'Robert Zahradnicek'


class TestODLvBridgePostApiModel:
    """
    Test basic ODL POST request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_post_vtn_request_uri(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api._create_vbridge_uri(base_url="http://10.10.10.96",
                                               vtn_name="test_vtn") == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges"

    def test_post_vtn_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge POST endpoint
        """
        result = vbridge_api._create_vbridge_body(vbr_name="test_vbridge",
                                                  controller_id="test_controller",
                                                  domain_id="test_domain")
        body = result
        assert body["vbridge"]["vbr_name"] == "test_vbridge"
        assert body["vbridge"]["description"] == "TEST vBridge"
        assert body["vbridge"]["controller_id"] == "test_controller"
        assert body["vbridge"]["domain_id"] == "test_domain"

    def test_post_vtn_request(self, configuration):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_api.create_vbridge(base_url="http://10.10.10.96",
                                            vtn_name="test_vtn",
                                            vbr_name="test_vbridge",
                                            controller_id="test_controller",
                                            domain_id="test_domain")
        assert result[0] == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges"
        body = result[1]
        assert body["vbridge"]["vbr_name"] == "test_vbridge"
        assert body["vbridge"]["description"] == "TEST vBridge"
        assert body["vbridge"]["controller_id"] == "test_controller"
        assert body["vbridge"]["domain_id"] == "test_domain"


class TestODLvBridgeGetApiModel:
    """
    Test basic ODL GET request generation functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_list_vbridge_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge(base_url="http://10.10.10.96",
                                        vtn_name="test_vtn") == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges"

    def test_list_vbridge_name_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges?index=test_vbridge"

    def test_list_vbridge_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge(base_url="http://10.10.10.96", vtn_name="test_vtn", max_repetition=500) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges?max_repetition=" + str(500)

    def test_list_vbridge_full_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                        vbr_name="test_vbridge",
                                        max_repetition=500) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges?index=test_vbridge&max_repetition=" + str(500)

    def test_list_vbridge_detail_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge_detail(base_url="http://10.10.10.96",
                                               vtn_name="test_vtn") == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/detail"

    def test_list_vbridge_name_detail_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/detail?index=test_vbridge"

    def test_list_vbridge_max_repetition_detail_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               max_repetition=500) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/detail?max_repetition=500"

    def test_list_vbridge_detail_full_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.list_vbridge_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge",
                                               max_repetition=600) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/detail?index=test_vbridge&max_repetition=600"

    def test_list_vbridge_count_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vbridge_api.list_vbridge_count(base_url="http://10.10.10.96",
                                              vtn_name="test_vtn") == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/count"

    def test_list_vbridge_count_name_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vbridge_api.list_vbridge_count(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                              vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/count?index=test_vbridge"

    def test_list_vbridge_count_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vbridge_api.list_vbridge_count(base_url="http://10.10.10.96", vtn_name="test_vtn", max_repetition=600) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/count?max_repetition=600"

    def test_list_vbridge_count_full_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vbridge_api.list_vbridge_count(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                              vbr_name="test_vbridge",
                                              max_repetition=600) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/count?index=test_vbridge&max_repetition=600"

    def test_show_vbridge_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET show endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.show_vbridge(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge"


class TestODLvBridgePutApiModel:
    """
    Test basic ODL PUT request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_update_vbridge_request_uri(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api._update_vbridge_uri(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge"

    def test_update_vbridge_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge PUT endpoint
        """
        result = vbridge_api._update_vbridge_body("TEST vBridge2")
        body = result
        assert body["vbridge"]["description"] == "TEST vBridge2"

    def test_update_vbridge_request(self, configuration):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vbridge_api.update_vbridge(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge",
                                            description="TEST vBridge3")
        assert result[0] == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge"

        body = result[1]
        assert body["vbridge"]["description"] == "TEST vBridge3"


class TestODLvBridgeDeleteApiModel:
    """
    Test basic ODL vBridge DELETE request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_delete_vbridge_request_uri(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge DELETE endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vbridge_api.delete_vbridge(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge"
