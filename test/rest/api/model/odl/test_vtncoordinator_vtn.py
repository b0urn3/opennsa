from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vtn_api

__author__ = 'Robert Zahradnicek'


class TestODLVTNPostApiModel:
    """
    Test basic ODL POST request generetion functions
    for creating URI + request body based on the values
    from base_url file
    """

    def test_post_vtn_request_uri(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN POST endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api._create_vtn_uri(base_url) == "http://10.10.10.96:8083/vtn-webapi/vtns"

    def test_post_vtn_request_body(self, vtn_name):
        """
        Test ODL VTN Coordinator request body generation for accessing VTN POST endpoint
        :param base_url: base_url object with parsed base_url values
        """
        result = vtn_api._create_vtn_body(vtn_name)
        body = result
        assert body["vtn"]["vtn_name"] == "test_vtn"
        assert body["vtn"]["description"] == "TEST VTN"

    def test_post_vtn_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator full request generation for accessing VTN POST endpoint
        :param base_url: base_url object with parsed base_url values
        """
        result = vtn_api.create_vtn(base_url, vtn_name)
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns"
        body = result[1]
        assert body["vtn"]["vtn_name"] == "test_vtn"
        assert body["vtn"]["description"] == "TEST VTN"


class TestODLVTNGetApiModel:
    """
    Test basic ODL GET request generation functions
    for creating URI + request body based on the values
    from base_url file
    """

    def test_list_vtn_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.list_vtn(base_url=base_url,
                                vtn_name=vtn_name) == "http://10.10.10.96:8083/vtn-webapi/vtns?index=test_vtn"

    def test_list_vtn_max_repetition_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.list_vtn(base_url=base_url,
                                vtn_name=vtn_name,
                                max_repetition=500) == "http://10.10.10.96:8083/vtn-webapi/vtns?index=test_vtn&max_repetition=500"

    def test_list_vtn_detail_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.list_vtn_detail(base_url, vtn_name) == "http://10.10.10.96:8083/vtn-webapi/vtns/detail?index=test_vtn"

    def test_list_vtn_detail_max_repetition_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.list_vtn_detail(base_url, vtn_name, 600) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/detail?index=test_vtn&max_repetition=600"

    def test_list_vtn_count_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET count endpoint without max_repetition set
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.list_vtn_count(base_url, vtn_name) == "http://10.10.10.96:8083/vtn-webapi/vtns/count?index=test_vtn"

    def test_list_vtn_count_max_repetition_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET count endpoint with max_repetition set
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.list_vtn_count(base_url, vtn_name, 700) == \
               "http://10.10.10.96:8083/vtn-webapi/vtns/count?index=test_vtn&max_repetition=700"

    def test_show_vtn_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN GET show endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.show_vtn(base_url, vtn_name) == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn"


class TestODLVTNPutApiModel:
    """
    Test basic ODL PUT request generetion functions
    for creating URI + request body based on the values
    from base_url file
    """

    def test_update_vtn_request_uri(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN PUT endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api._update_vtn_uri(base_url, vtn_name) == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn"

    def test_update_vtn_request_body(self, vtn_name):
        """
        Test ODL VTN Coordinator request body generation for accessing VTN PUT endpoint
        :param base_url: base_url object with parsed base_url values
        """
        result = vtn_api._update_vtn_body(vtn_name, "TEST VTN2")
        body = result
        assert body["vtn"]["vtn_name"] == "test_vtn"
        assert body["vtn"]["description"] == "TEST VTN2"

    def test_update_vtn_request(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator full request generation for accessing VTN PUT endpoint
        :param base_url: base_url object with parsed base_url values
        """
        result = vtn_api.update_vtn(base_url, vtn_name, "TEST VTN3")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn"
        body = result[1]
        assert body["vtn"]["vtn_name"] == "test_vtn"
        assert body["vtn"]["description"] == "TEST VTN3"


class TestODLVTNDeleteApiModel:
    """
    Test basic ODL DELETE request generetion functions
    for creating URI + request body based on the values
    from base_url file
    """

    def test_delete_vtn_request_uri(self, base_url, vtn_name):
        """
        Test ODL VTN Coordinator request uri generation for accessing VTN DELETE endpoint
        :param base_url: base_url object with parsed base_url values
        """
        assert vtn_api.delete_vtn(base_url, vtn_name) == "http://10.10.10.96:8083/vtn-webapi/vtns/test_vtn"
