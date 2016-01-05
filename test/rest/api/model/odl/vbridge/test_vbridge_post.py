import json

from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vbridge import post
from opennsa import config

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
        assert post._create_vbridge_uri(configuration) == "http://10.10.10.96/vtns/" + \
                                                          configuration[config.SDNCREST_VTN] + "/vbridges"

    def test_post_vtn_request_body(self, configuration):
        """
        Test ODL VTN Coordinator request body generation for accessing vBridge POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = post._create_vbridge_body(configuration,
                                           vbr_name="test_vbridge",
                                           controller_id="test_controller",
                                           domain_id="test_domain")
        body = json.loads(result)
        assert body["vbridge"]["vbr_name"] == "test_vbridge"
        assert body["vbridge"]["description"] == "TEST vBridge"
        assert body["vbridge"]["controller_id"] == "test_controller"
        assert body["vbridge"]["domain_id"] == "test_domain"

    def test_post_vtn_request(self, configuration):
        """
        Test ODL VTN Coordinator full request generation for accessing vBridge POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = post.create_vbridge(configuration,
                                     vbr_name="test_vbridge",
                                     controller_id="test_controller",
                                     domain_id="test_domain")
        assert result[0] == "http://10.10.10.96/vtns/" + configuration[config.SDNCREST_VTN] + "/vbridges"
        body = json.loads(result[1])
        assert body["vbridge"]["vbr_name"] == "test_vbridge"
        assert body["vbridge"]["description"] == "TEST vBridge"
        assert body["vbridge"]["controller_id"] == "test_controller"
        assert body["vbridge"]["domain_id"] == "test_domain"
