from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vbridge import get
from opennsa import config

__author__ = 'Robert Zahradnicek'


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
        assert get.list_vbridge(configuration) == "http://10.10.10.96/vtns/" + \
                                                  configuration[config.SDNCREST_VTN] + "/vbridges"

    def test_list_vbridge_name_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge(configuration, vbr_name="test_vbridge") == "http://10.10.10.96/vtns/" + \
                                                                           configuration[config.SDNCREST_VTN] + \
                                                                           "/vbridges?index=test_vbridge"

    def test_list_vbridge_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge(configuration, max_repetition=500) == "http://10.10.10.96/vtns/" + \
                                                                      configuration[config.SDNCREST_VTN] + \
                                                                      "/vbridges?max_repetition=" + str(500)

    def test_list_vbridge_full_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge(configuration,
                                vbr_name="test_vbridge",
                                max_repetition=500) == "http://10.10.10.96/vtns/" + \
                                                       configuration[config.SDNCREST_VTN] + \
                                                       "/vbridges?index=test_vbridge&max_repetition=" + str(500)

    def test_list_vbridge_detail_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge_detail(configuration) == "http://10.10.10.96/vtns/" + \
                                                         configuration[config.SDNCREST_VTN] + \
                                                         "/vbridges/detail"

    def test_list_vbridge_name_detail_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge_detail(configuration, vbr_name="test_vbridge") == "http://10.10.10.96/vtns/" + \
                                                                                  configuration[config.SDNCREST_VTN] + \
                                                                                  "/vbridges/detail?index=test_vbridge"

    def test_list_vbridge_max_repetition_detail_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge_detail(configuration, max_repetition=500) == "http://10.10.10.96/vtns/" + \
                                                                             configuration[config.SDNCREST_VTN] + \
                                                                             "/vbridges/detail?max_repetition=500"

    def test_list_vbridge_detail_full_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vbridge_detail(configuration,
                                       vbr_name="test_vbridge",
                                       max_repetition=600) == "http://10.10.10.96/vtns/" + \
                                                              configuration[config.SDNCREST_VTN] + \
                                                              "/vbridges/detail?index=test_vbridge&max_repetition=600"

    def test_list_vbridge_count_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert get.list_vbridge_count(configuration) == "http://10.10.10.96/vtns/" + \
                                                        configuration[config.SDNCREST_VTN] + \
                                                        "/vbridges/count"

    def test_list_vbridge_count_name_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert get.list_vbridge_count(configuration, vbr_name="test_vbridge") == "http://10.10.10.96/vtns/" + \
                                                                                 configuration[config.SDNCREST_VTN] + \
                                                                                 "/vbridges/count?index=test_vbridge"

    def test_list_vbridge_count_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert get.list_vbridge_count(configuration, max_repetition=600) == "http://10.10.10.96/vtns/" + \
                                                                            configuration[config.SDNCREST_VTN] + \
                                                                            "/vbridges/count?max_repetition=600"

    def test_list_vbridge_count_full_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert get.list_vbridge_count(configuration,
                                      vbr_name="test_vbridge",
                                      max_repetition=600) == "http://10.10.10.96/vtns/" + \
                                                             configuration[config.SDNCREST_VTN] + \
                                                             "/vbridges/count?index=test_vbridge&max_repetition=600"

    def test_show_vbridge_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing vBridge GET show endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.show_vbridge(configuration, vbr_name="test_vbridge") == "http://10.10.10.96/vtns/" + \
                                                                           configuration[config.SDNCREST_VTN] + \
                                                                           "/vbridges/test_vbridge"
