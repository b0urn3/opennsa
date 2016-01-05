from opennsa.backends.common.rest.api.model.odl.vtncoordinator.vtn import delete
from opennsa import config

__author__ = 'Robert Zahradnicek'


class TestODLVTNDeleteApiModel:
    """
    Test basic ODL DELETE request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_delete_vtn_request_uri(self, configuration):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN DELETE endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert delete.delete_vtn(configuration) == "http://10.10.10.96/vtns/" + str(configuration[config.SDNCREST_VTN])
