from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vbridge import delete
from opennsa import config

__author__ = 'Robert Zahradnicek'


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
        assert delete._delete_vbridge(configuration, "test_vbridge") == "http://10.10.10.96/vtns/" + \
                                                                        str(configuration[config.SDNCREST_VTN]) + \
                                                                        "/vbridges/test_vbridge"
