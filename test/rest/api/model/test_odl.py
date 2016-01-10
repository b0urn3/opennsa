from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vtn_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vbridge_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import vlanmap_api
from opennsa.backends.common.rest.api.model.odl.vtncoordinator import controller_api
from opennsa.backends.common.rest import restclient

import json

__author__ = 'Robert Zahradnicek'


class TestODLApi:
    """
    Test ODL provision and teardown units
    """

    def test_odlapi_vtncoordinator(self, base_url, username, password):
        """
        Test if vtn coordinator is present

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        url = base_url + "/vtn-webapi/api_version.json"
        response = browser.get(url=url)
        assert response.status_code == 200
        assert response.content == '{"api_version":{"version":"V1.2"}}'

    def test_odlapi_vtncoordinator_post_controller(self, base_url, username, password):
        """
        Test controller addition to VTN coordinator

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        post_request = controller_api.create_controller(base_url=base_url,
                                                        controller_id="controllerone",
                                                        ipaddr="10.0.0.1",
                                                        controller_type="odc",
                                                        version="1.0",
                                                        auditstatus="enable")
        post_result = browser.post(url=post_request[0], data=json.dumps(post_request[1]))
        assert post_result.status_code == 201

    def test_odlapi_vtncoordinator_post_vtn(self, base_url, username, password, vtn_name):
        """
        Test VTN addition to VTN coordinator

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vtn_name: VTN name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        post_request = vtn_api.create_vtn(base_url=base_url,
                                          vtn_name=vtn_name,
                                          description="testing")
        post_result = browser.post(url=post_request[0], data=json.dumps(post_request[1]))
        assert post_result.status_code == 201

    def test_odlapi_vtncoordinator_post_vbridge(self, base_url, username, password, vtn_name, vbr_name):
        """
        Test vBridge addition

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vtn_name: VTN name
        :param vbr_name: vBridge name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        post_request = vbridge_api.create_vbridge(base_url=base_url,
                                                  controller_id="controllerone",
                                                  domain_id="DEFAULT",
                                                  vtn_name=vtn_name,
                                                  vbr_name=vbr_name,
                                                  description="testing")
        post_result = browser.post(url=post_request[0], data=json.dumps(post_request[1]))
        assert post_result.status_code == 202

    def test_odlapi_vtncoordinator_post_vlanmap(self, base_url, username, password, vtn_name, vbr_name):
        """
        Test VLAN map addition

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vtn_name: VTN name
        :param vbr_name: vBridge name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        post_request = vlanmap_api.create_vlanmap(base_url=base_url,
                                                  vtn_name=vtn_name,
                                                  vbr_name=vbr_name,
                                                  vlan_id=100)
        post_result = browser.post(url=post_request[0], data=json.dumps(post_request[1]))
        assert post_result.status_code == 202

    def test_odlapi_vtncoordinator_get_controller(self, base_url, username, password):
        """
        Test controllers listing

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()

        check_request = controller_api.list_controllers(base_url=base_url)
        check_result = browser.get(url=check_request)
        assert check_result.status_code == 200

    def test_odlapi_vtncoordinator_get_vtn(self, base_url, vtn_name, username, password):
        """
        Test VTN listing

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vtn_name: VTN name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        url = vtn_api.list_vtn(base_url=base_url, vtn_name=vtn_name)
        response = browser.get(url=url)
        assert response.status_code == 200
        url = vtn_api.list_vtn(base_url=base_url, vtn_name=vtn_name)
        response = browser.get(url=url)
        assert response.status_code == 200

    def test_odlapi_vtncoordinator_get_vbridge(self, base_url, vtn_name, vbr_name, username, password):
        """
        Test vBridge listing

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vbr_name: vBridge name
        :param vtn_name: VTN name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        url = vbridge_api.list_vbridge(base_url=base_url, vtn_name=vtn_name, vbr_name=vbr_name)
        response = browser.get(url=url)
        assert response.status_code == 200
        url = vtn_api.list_vtn(base_url=base_url, vtn_name=vtn_name)
        response = browser.get(url=url)
        assert response.status_code == 200

    def test_odlapi_vtncoordinator_delete_vbridge(self, base_url, username, password, vtn_name, vbr_name):
        """
        Test vBridge deletion

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vtn_name: VTN name
        :param vbr_name: vBridge name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        delete_request = vbridge_api.delete_vbridge(base_url=base_url, vtn_name=vtn_name, vbr_name=vbr_name)
        delete_result = browser.delete(url=delete_request)
        print(delete_result.content)
        assert delete_result.status_code == 202

    def test_odlapi_vtncoordinator_delete_vtn(self, base_url, username, password, vtn_name):
        """
        Test VTN deletion

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param vtn_name: VTN name
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        delete_request = vtn_api.delete_vtn(base_url=base_url, vtn_name=vtn_name)
        delete_result = browser.delete(url=delete_request)
        assert delete_result.status_code == 204

    def test_odlapi_vtncoordinator_delete_controller(self, base_url, username, password):
        """
        Test controller deletion

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        browser = client._browser().next()
        delete_request = controller_api.delete_controller(base_url=base_url, controller_id="controllerone")
        delete_result = browser.delete(url=delete_request)
        assert delete_result.status_code == 204

    def test_odlapi_provision(self, base_url, username, password, configuration):
        """
        Test ODLApi provision

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param configuration: parsed configuration
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")
        result = client.provision(cfg=configuration,
                                  source_target="source",
                                  dest_target="dest",
                                  bandwidth=20,
                                  connection_id=1)
        assert result

    def test_odlapi_teardown(self, base_url, username, password, configuration):
        """
        Test ODLApi teardown

        :param base_url: base url for requests
        :param username: username to log in with
        :param password: password to log in with
        :param configuration: parsed configuration
        """
        client = restclient.RESTApiClient(api_type=restclient.ODL_API,
                                          base_url=base_url,
                                          username=username,
                                          password=password,
                                          log_system="testing")

        result = client.teardown(cfg=configuration,
                                 connection_id=1,
                                 source_target="source",
                                 dest_target="dest")
        assert result
