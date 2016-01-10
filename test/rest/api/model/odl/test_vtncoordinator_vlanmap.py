from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vlanmap_api

__author__ = 'Robert Zahradnicek'


class TestODLVlanMapPostApiModel:
    """
    Test basic ODL VLAN Map POST request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_post_vlanmap_request_uri(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing VLAN Map POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api._create_vlanmap_uri(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps.json"

    def test_post_vlanmap_logical_port_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map POST endpoint
        """
        result = vlanmap_api._create_vlanmap_body(logical_port_id="logical_port_1")
        body = result
        assert body["vlanmap"]["logical_port_id"] == "logical_port_1"

    def test_post_vlanmap_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map POST endpoint
        """
        result = vlanmap_api._create_vlanmap_body(vlan_id=1)
        body = result
        assert body["vlanmap"]["vlan_id"] == "1"

    def test_post_vlanmap_no_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map POST endpoint
        """
        result = vlanmap_api._create_vlanmap_body(no_vlan_id=True)
        body = result
        assert body["vlanmap"]["no_vlan_id"] == "true"

    def test_post_vlanmap_logical_port_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map POST endpoint
        """
        result = vlanmap_api._create_vlanmap_body(logical_port_id="logical_port_1",
                                                  vlan_id=1)
        body = result
        assert body["vlanmap"]["logical_port_id"] == "logical_port_1"
        assert body["vlanmap"]["vlan_id"] == "1"

    def test_post_vlanmap_logical_port_no_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map POST endpoint
        """
        result = vlanmap_api._create_vlanmap_body(logical_port_id="logical_port_1",
                                                  no_vlan_id=True)
        body = result
        assert body["vlanmap"]["logical_port_id"] == "logical_port_1"
        assert body["vlanmap"]["no_vlan_id"] == "true"

    def test_post_vlanmap_incorrect_params_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map POST endpoint
        """
        result = vlanmap_api._create_vlanmap_body(logical_port_id="logical_port_1",
                                                  vlan_id=1,
                                                  no_vlan_id=True)
        body = result
        assert body["vlanmap"] == {}

    def test_post_vlanmap_logical_port_vlan_id_full_request(self):
        """
        Test ODL VTN Coordinator full request generation for accessing Vlan Map POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vlanmap_api.create_vlanmap(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                            vbr_name="test_vbridge",
                                            logical_port_id="logical_port_1",
                                            vlan_id=1)
        assert result[0] == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps.json"
        body = result[1]
        assert body["vlanmap"]["logical_port_id"] == "logical_port_1"
        assert body["vlanmap"]["vlan_id"] == "1"


class TestODLVlanMapGetApiModel:
    """
    Test basic ODL GET request generation functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_list_vlanmap_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap(base_url="http://10.10.10.96",
                                        vtn_name="test_vtn",
                                        vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps.json"

    def test_list_vlanmap_vlanmap_id_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap(base_url="http://10.10.10.96",
                                        vtn_name="test_vtn",
                                        vbr_name="test_vbridge",
                                        vlanmap_id="no_lpid") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps.json?index=no_lpid"

    def test_list_vlanmap_max_repetition_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap(base_url="http://10.10.10.96",
                                        vtn_name="test_vtn",
                                        vbr_name="test_vbridge",
                                        max_repetition=500) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps.json?max_repetition=500"

    def test_list_vlanmap_full_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap(base_url="http://10.10.10.96",
                                        vtn_name="test_vtn",
                                        vbr_name="test_vbridge",
                                        vlanmap_id="no_lpid",
                                        max_repetition=500) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps.json?index=no_lpid&max_repetition=500"

    def test_list_vlanmap_detail_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/detail.json"

    def test_list_vlanmap_name_detail_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge", vlanmap_id="no_lpid") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/detail.json?index=no_lpid"

    def test_list_vlanmap_max_repetition_detail_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge", max_repetition=500) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/detail.json?max_repetition=500"

    def test_list_vlanmap_detail_full_max_repetition_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.list_vlanmap_detail(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge",
                                               vlanmap_id="no_lpid",
                                               max_repetition=600) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/detail.json?index=no_lpid&max_repetition=600"

    def test_list_vlanmap_count_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vlanmap_api.list_vlanmap_count(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                              vbr_name="test_vbridge") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/count.json"

    def test_list_vlanmap_count_name_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vlanmap_api.list_vlanmap_count(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                              vbr_name="test_vbridge", vlanmap_id="no_lpid") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/count.json?index=no_lpid"

    def test_list_vlanmap_count_max_repetition_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vlanmap_api.list_vlanmap_count(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                              vbr_name="test_vbridge", max_repetition=600) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/count.json?max_repetition=600"

    def test_list_vlanmap_count_full_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert vlanmap_api.list_vlanmap_count(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                              vbr_name="test_vbridge",
                                              vlanmap_id="no_lpid",
                                              max_repetition=600) == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/count.json?index=no_lpid&max_repetition=600"

    def test_show_vlanmap_request(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map GET show endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.show_vlanmap(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge",
                                        vlanmap_id="no_lpid") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/no_lpid.json"


class TestODLVlanMapPutApiModel:
    """
    Test basic ODL PUT request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_update_vlanmap_request_uri(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api._update_vlanmap_uri(base_url="http://10.10.10.96", vtn_name="test_vtn",
                                               vbr_name="test_vbridge", vlanmap_id="no_lpid") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/no_lpid.json"

    def test_update_vlanmap_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map PUT endpoint
        """
        result = vlanmap_api._update_vlanmap_body(vlan_id=1)
        body = result
        assert body["vlanmap"]["vlan_id"] == "1"

    def test_update_vlanmap_no_vlan_id_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map PUT endpoint
        """
        result = vlanmap_api._update_vlanmap_body(no_vlan_id=True)
        body = result
        assert body["vlanmap"]["no_vlan_id"] == "true"

    def test_update_vlanmap_no_params_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map PUT endpoint
        """
        result = vlanmap_api._update_vlanmap_body()
        body = result
        assert body["vlanmap"] == {}

    def test_update_vlanmap_incorrect_params_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Vlan Map PUT endpoint
        """
        result = vlanmap_api._update_vlanmap_body(vlan_id=1,
                                                  no_vlan_id=True)
        body = result
        assert body["vlanmap"] == {}

    def test_update_vlanmap_vlan_id_full_request(self):
        """
        Test ODL VTN Coordinator full request generation for accessing Vlan Map PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vlanmap_api.update_vlanmap(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge",
                                            vlanmap_id="no_lpid", vlan_id=1)
        assert result[0] == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/no_lpid.json"

        body = result[1]
        assert body["vlanmap"]["vlan_id"] == "1"

    def test_update_vlanmap_no_vlan_id_full_request(self):
        """
        Test ODL VTN Coordinator full request generation for accessing Vlan Map PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = vlanmap_api.update_vlanmap(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge",
                                            vlanmap_id="no_lpid", no_vlan_id=True)
        assert result[0] == "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/no_lpid.json"

        body = result[1]
        assert body["vlanmap"]["no_vlan_id"] == "true"


class TestODLVlanMapDeleteApiModel:
    """
    Test basic ODL Vlan Map DELETE request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_delete_vlanmap_request_uri(self):
        """
        Test ODL VTN Coordinator request uri generation for accessing Vlan Map DELETE endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert vlanmap_api.delete_vlanmap(base_url="http://10.10.10.96", vtn_name="test_vtn", vbr_name="test_vbridge",
                                          vlanmap_id="no_lpid") == \
               "http://10.10.10.96/vtn-webapi/vtns/test_vtn/vbridges/test_vbridge/vlanmaps/no_lpid.json"
