from opennsa.backends.common.rest.api.model.odl.vtncoordinator import controller_api

__author__ = 'Robert Zahradnicek'


class TestODLControllerPostApiModel:
    """
    Test basic ODL POST request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_post_controller_request_uri(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api._create_controller_uri(base_url) == "http://10.10.10.96:8083/vtn-webapi/controllers"

    def test_post_controller_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Controller POST endpoint
        """
        result = controller_api._create_controller_body(controller_id="test_controller",
                                                        version="test_version",
                                                        controller_type="test_type")
        body = result
        assert body["controller"]["controller_id"] == "test_controller"
        assert body["controller"]["type"] == "test_type"
        assert body["controller"]["version"] == "test_version"

    def test_post_controller_request(self, base_url):
        """
        Test ODL VTN Coordinator full request generation for accessing Controller POST endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = controller_api.create_controller(base_url=base_url,
                                                  controller_id="test_controller",
                                                  version="test_version",
                                                  controller_type="test_type")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/controllers"
        body = result[1]
        assert body["controller"]["controller_id"] == "test_controller"
        assert body["controller"]["type"] == "test_type"
        assert body["controller"]["version"] == "test_version"


class TestODLcontrollerGetApiModel:
    """
    Test basic ODL GET request generation functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_list_controller_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers(base_url) == "http://10.10.10.96:8083/vtn-webapi/controllers"

    def test_list_controller_name_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers(base_url=base_url, controller_id="test_controller") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers?index=test_controller"

    def test_list_controller_max_repetition_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers(base_url=base_url, max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers?max_repetition=500"

    def test_list_controller_full_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers(base_url=base_url,
                                               controller_id="test_controller",
                                               max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers?index=test_controller&max_repetition=500"

    def test_list_controller_detail_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers_detail(
            base_url=base_url) == "http://10.10.10.96:8083/vtn-webapi/controllers/detail"

    def test_list_controller_name_detail_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers_detail(base_url=base_url, controller_id="test_controller") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/detail?index=test_controller"

    def test_list_controller_max_repetition_detail_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers_detail(base_url=base_url, max_repetition=500) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/detail?max_repetition=500"

    def test_list_controller_detail_full_max_repetition_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.list_controllers_detail(base_url=base_url,
                                                      controller_id="test_controller",
                                                      max_repetition=600) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/detail?index=test_controller&max_repetition=600"

    def test_list_controller_count_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert controller_api.list_controllers_count(
            base_url=base_url) == "http://10.10.10.96:8083/vtn-webapi/controllers/count"

    def test_list_controller_count_name_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET
        count endpoint without max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert controller_api.list_controllers_count(base_url=base_url, controller_id="test_controller") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/count?index=test_controller"

    def test_list_controller_count_max_repetition_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert controller_api.list_controllers_count(base_url=base_url, max_repetition=600) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/count?max_repetition=600"

    def test_list_controller_count_full_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET
        count endpoint with max_repetition set
        :param configuration: configuration object with parsed configuration values
        """

        assert controller_api.list_controllers_count(base_url=base_url,
                                                     controller_id="test_controller",
                                                     max_repetition=600) == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/count?index=test_controller&max_repetition=600"

    def test_show_controller_request(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller GET show endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.show_controller(base_url=base_url, controller_id="test_controller") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/test_controller"


class TestODLcontrollerPutApiModel:
    """
    Test basic ODL PUT request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_update_controller_request_uri(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api._update_controller_uri(base_url=base_url, controller_id="test_controller") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/test_controller"

    def test_update_controller_request_body(self):
        """
        Test ODL VTN Coordinator request body generation for accessing Controller PUT endpoint
        """
        result = controller_api._update_controller_body(controller_id="test_controller", version="test_version")
        body = result
        assert body["controller"]["controller_id"] == "test_controller"
        assert body["controller"]["version"] == "test_version"

    def test_update_controller_request(self, base_url):
        """
        Test ODL VTN Coordinator full request generation for accessing Controller PUT endpoint
        :param configuration: configuration object with parsed configuration values
        """
        result = controller_api.update_controller(base_url=base_url,
                                                  controller_id="test_controller",
                                                  version="test_version")
        assert result[0] == "http://10.10.10.96:8083/vtn-webapi/controllers/test_controller"

        body = result[1]
        assert body["controller"]["controller_id"] == "test_controller"
        assert body["controller"]["version"] == "test_version"


class TestODLcontrollerDeleteApiModel:
    """
    Test basic ODL Controller DELETE request generetion functions
    for creating URI + request body based on the values
    from configuration file
    """

    def test_delete_controller_request_uri(self, base_url):
        """
        Test ODL VTN Coordinator request uri generation for accessing Controller DELETE endpoint
        :param configuration: configuration object with parsed configuration values
        """
        assert controller_api.delete_controller(base_url=base_url, controller_id="test_controller") == \
               "http://10.10.10.96:8083/vtn-webapi/controllers/test_controller"
