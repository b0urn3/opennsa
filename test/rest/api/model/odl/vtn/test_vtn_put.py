import json

from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vtn import put
from opennsa import config

__author__ = 'Robert Zahradnicek'


class TestODLVTNPutApiModel:
    """
    Test basic ODL PUT request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_update_vtn_request_uri(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert put._update_vtn_uri(configuration) == "http://10.10.10.96/vtns/" + configuration[config.SDNCREST_VTN]

    def test_update_vtn_request_body(self, configuration):
        """
        Test ODL VTN Coordinator request body generation for accessing VTN PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = put._update_vtn_body(configuration, "TEST VTN2")
        body = json.loads(result)
        assert body["vtn"]["vtn_name"] == configuration[config.SDNCREST_VTN]
        assert body["vtn"]["description"] == "TEST VTN2"

    def test_update_vtn_request(self, configuration):
        """
        Test ODL VTN Coordinator full request generation for accessing VTN PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = put.update_vtn(configuration, "TEST VTN3")
        assert result[0] == "http://10.10.10.96/vtns/" + configuration[config.SDNCREST_VTN]
        body = json.loads(result[1])
        assert body["vtn"]["vtn_name"] == configuration[config.SDNCREST_VTN]
        assert body["vtn"]["description"] == "TEST VTN3"
