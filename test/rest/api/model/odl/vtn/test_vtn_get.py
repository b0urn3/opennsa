from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vtn import get
from opennsa import config

__author__ = 'Robert Zahradnicek'


class TestODLVTNGetApiModel:

    """
    Test basic ODL GET request generation functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_list_vtn_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vtn(configuration) == "http://10.10.10.96/vtns?index=" + configuration[config.SDNCREST_VTN]

    def test_list_vtn_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vtn(configuration, 500) == "http://10.10.10.96/vtns?index=" + \
                                                   configuration[config.SDNCREST_VTN] + "&max_repetition=500"

    def test_list_vtn_detail_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vtn_detail(configuration) == "http://10.10.10.96/vtns/detail?index=" + \
                                                     configuration[config.SDNCREST_VTN]

    def test_list_vtn_detail_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vtn_detail(configuration, 600) == "http://10.10.10.96/vtns/detail?index=" + \
                                                          configuration[config.SDNCREST_VTN] + "&max_repetition=600"

    def test_list_vtn_count_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vtn_count(configuration) == "http://10.10.10.96/vtns/count?index=" + \
                                                    configuration[config.SDNCREST_VTN]

    def test_list_vtn_count_max_repetition_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """
        assert get.list_vtn_count(configuration, 700) == "http://10.10.10.96/vtns/count?index=" + \
                                                         configuration[config.SDNCREST_VTN] + "&max_repetition=700"

    def test_show_vtn_request(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET show endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert get.show_vtn(configuration) == "http://10.10.10.96/vtns/" + configuration[config.SDNCREST_VTN]

