from opennsa.backends.common.rest import restclient
from opennsa.backends.common.rest.api.model.odl import odl

import requests

__author__ = 'Robert Zahradnicek'


class TestRestClient:

    def test_restclient_browser(self):
        """
        Test correct browser setup for creating sessions and sending actual requests
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url="http://localhost",
                                          username="test",
                                          password="test",
                                          log_system="testing")
        browser = client._browser().next()
        assert isinstance(browser, requests.Session)
        assert browser.headers["username"] == "test"
        assert browser.headers["password"] == "test"
        assert browser.headers["Content-Type"] == "application/json"

    def test_restclient_init(self):
        """
        Test correct model instance based on api_type parameter

        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url="http://localhost",
                                          username="test",
                                          password="test",
                                          log_system="testing")
        assert isinstance(client._model, restclient.RESTApiModel)

    def test_restapimodel_init(self):

        """
        Test correct model instance based on api_type parameter

        """
        model = restclient.RESTApiModel(api_type=restclient.ODL_API,
                                        base_url="http://localhost",
                                        log_system="testing")
        assert isinstance(model._model, odl.ODLApi)
        assert model._model.base_url == "http://localhost"
