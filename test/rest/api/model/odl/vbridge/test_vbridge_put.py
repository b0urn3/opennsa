import json

from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vbridge import put
from opennsa import config

__author__ = 'Robert Zahradnicek'


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
        assert put._update_vbridge_uri(configuration, "test_vbridge") == "http://10.10.10.96/vtns/" + \
                                                                         configuration[config.SDNCREST_VTN] + \
                                                                         "/vbridges/test_vbridge"

    def test_update_vbridge_request_body(self, configuration):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = put._update_vbridge_body(configuration, "TEST vBridge2")
        body = json.loads(result)
        assert body["vbridge"]["description"] == "TEST vBridge2"

    def test_update_vbridge_request(self, configuration):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = put.update_vbridge(configuration, "test_vbridge", "TEST vBridge3")
        assert result[0] == "http://10.10.10.96/vtns/" + configuration[config.SDNCREST_VTN] + "/vbridges/test_vbridge"

        body = json.loads(result[1])
        assert body["vbridge"]["description"] == "TEST vBridge3"

