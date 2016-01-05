import json

from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vtn import post
from opennsa import config

__author__ = 'Robert Zahradnicek'


class TestODLVTNPostApiModel:
    """
    Test basic ODL POST request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_post_vtn_request_uri(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert post._create_vtn_uri(configuration) == "http://10.10.10.96/vtns"

    def test_post_vtn_request_body(self, configuration):
        """
        Test ODL VTN Coordinator request body generation for accessing VTN POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = post._create_vtn_body(configuration)
        body = json.loads(result)
        assert body["vtn"]["vtn_name"] == configuration[config.SDNCREST_VTN]
        assert body["vtn"]["description"] == "TEST VTN"

    def test_post_vtn_request(self, configuration):
        """
        Test ODL VTN Coordinator full request generation for accessing VTN POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = post.create_vtn(configuration)
        assert result[0] == "http://10.10.10.96/vtns"
        body = json.loads(result[1])
        assert body["vtn"]["vtn_name"] == configuration[config.SDNCREST_VTN]
        assert body["vtn"]["description"] == "TEST VTN"
