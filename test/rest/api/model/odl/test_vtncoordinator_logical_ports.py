from opennsa.backends.common.rest.api.model.odl.vtncoordinator import logical_port_api

__author__ = 'Robert Zahradnicek'


class TestODLvLogicalPortsListApiModel:
    """
    Test basic ODL Logical ports List GET request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_list_logical_ports(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET logical ports List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports(base_url=base_url,
                                                   controller_id="controllerone",
                                                   domain_id="DEFAULT") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports"

    def test_list_logical_ports_logical_port_id(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET logical ports with logical_port_id set List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports(base_url=base_url,
                                                   controller_id="controllerone",
                                                   domain_id="DEFAULT",
                                                   logical_port_id="logical_port") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports?index=logical_port&logical_port_id=logical_port"

    def test_list_logical_ports_max_repetition(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET Logical ports with max_repetition set List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports(base_url=base_url,
                                                   controller_id="controllerone",
                                                   domain_id="DEFAULT",
                                                   max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports?max_repetition=500"

    def test_list_logical_ports_full(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports(base_url=base_url,
                                                   controller_id="controllerone",
                                                   domain_id="DEFAULT",
                                                   logical_port_id="logical_port",
                                                   max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports?index=logical_port&logical_port_id=logical_port&max_repetition=500"

    def test_list_logical_ports_detail(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET logical ports List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_detail(base_url=base_url,
                                                          controller_id="controllerone",
                                                          domain_id="DEFAULT") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/detail"

    def test_list_logical_ports_logical_port_id_detail(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET logical ports with logical_port_id set List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_detail(base_url=base_url,
                                                          controller_id="controllerone",
                                                          domain_id="DEFAULT",
                                                          logical_port_id="logical_port") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/detail?index=logical_port&logical_port_id=logical_port"

    def test_list_logical_ports_max_repetition_detail(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET Logical ports with max_repetition set List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_detail(base_url=base_url,
                                                          controller_id="controllerone",
                                                          domain_id="DEFAULT",
                                                          max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/detail?max_repetition=500"

    def test_list_logical_ports_full_detail(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_detail(base_url=base_url,
                                                          controller_id="controllerone",
                                                          domain_id="DEFAULT",
                                                          logical_port_id="logical_port",
                                                          max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/detail?index=logical_port&logical_port_id=logical_port&max_repetition=500"

    def test_list_logical_ports_count(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET logical ports List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_count(base_url=base_url,
                                                         controller_id="controllerone",
                                                         domain_id="DEFAULT") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/count"

    def test_list_logical_ports_logical_port_id_count(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET logical ports with logical_port_id set List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_count(base_url=base_url,
                                                         controller_id="controllerone",
                                                         domain_id="DEFAULT",
                                                         logical_port_id="logical_port") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/count?index=logical_port&logical_port_id=logical_port"

    def test_list_logical_ports_max_repetition_count(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        GET Logical ports with max_repetition set List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_count(base_url=base_url,
                                                         controller_id="controllerone",
                                                         domain_id="DEFAULT",
                                                         max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/count?max_repetition=500"

    def test_list_logical_ports_full_count(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing
        vBridge Interfaces GET Interface List endpoint
        :param base_url: base of the url for the request
        """
        assert logical_port_api.list_logical_ports_count(base_url=base_url,
                                                         controller_id="controllerone",
                                                         domain_id="DEFAULT",
                                                         logical_port_id="logical_port",
                                                         max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/controllerone/domains/DEFAULT/logical_ports/count?index=logical_port&logical_port_id=logical_port&max_repetition=500"
