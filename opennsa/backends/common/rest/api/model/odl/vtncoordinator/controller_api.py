__author__ = 'Robert Zahradnicek'


def _create_controller_uri(base_url):
    """
    VTN Coordinator Create controller URI
    :param base_url: base of request url
    :return: URI with all parameters
    """
    return base_url + "/vtn-webapi/controllers"


def _create_controller_body(controller_id,
                            version,
                            controller_type,
                            description=None,
                            ipaddr=None,
                            auditstatus=None,
                            username=None,
                            password=None):
    """
    VTN Coordinator create controller body for POST request
    :param controller_id: id of the controller to update
    :param version: version of the controller
    :param description: controller description
    :param ipaddr: IP address of the controller
    :param auditstatus: status of the controller
    :param username: username for login
    :param password: password for login
    :return: dictionary body for JSON
    """
    request_body = {
        "controller": {
            "controller_id": str(controller_id),
            "version": str(version),
            "type": str(controller_type),
        }
    }
    if description is not None:
        request_body["controller"]["description"] = description
    if ipaddr is not None:
        request_body["controller"]["ipaddr"] = ipaddr
    if auditstatus is not None:
        request_body["controller"]["auditstatus"] = auditstatus
    if username is not None:
        request_body["controller"]["username"] = username
    if password is not None:
        request_body["controller"]["password"] = password

    return request_body


def create_controller(base_url,
                      controller_id,
                      version,
                      controller_type,
                      description=None,
                      ipaddr=None,
                      auditstatus=None,
                      username=None,
                      password=None):
    """
    VTN Coordinator Create controller body for POST request
    :param base_url: base of the uri request
    :param controller_id: id of the controller to update
    :param version: version of the controller
    :param description: controller description
    :param ipaddr: IP address of the controller
    :param auditstatus: status of the controller
    :param username: username for login
    :param password: password for login
    :return: tuple (URL,body)
    """
    return _create_controller_uri(base_url=base_url), \
           _create_controller_body(controller_id=controller_id,
                                   version=version,
                                   controller_type=controller_type,
                                   description=description,
                                   ipaddr=ipaddr,
                                   auditstatus=auditstatus,
                                   username=username,
                                   password=password)


def list_controllers(base_url, controller_id=None, max_repetition=None):
    """
    VTN Coordinator List controllers URI for GET request
    :param base_url: base of the request uri
    :param controller_id: id of the controller to update
    :param max_repetition: max results option
    :return: URI with parameters
    """
    result = base_url + "/vtn-webapi/controllers"
    query = ""
    if controller_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(controller_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_controllers_detail(base_url, controller_id=None, max_repetition=None):
    """
    VTN Coordinator List controllers detail URI for GET request
    :param base_url: base of the request uri
    :param controller_id: id of the controller to update
    :param max_repetition: max results option
    :return: URI with parameters
    """
    result = base_url + "/vtn-webapi/controllers/detail"
    query = ""
    if controller_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(controller_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_controllers_count(base_url, controller_id=None, max_repetition=None):
    """
    VTN Coordinator List controllers count URI for GET request
    :param base_url: base of the request uri
    :param controller_id: id of the controller to update
    :param max_repetition: max results option
    :return: URI with parameters
    """
    result = base_url + "/vtn-webapi/controllers/count"
    query = ""
    if controller_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(controller_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def show_controller(base_url, controller_id):
    """
    VTN Coordinator Show controller info URI for GET request
    :param base_url: base of the request uri
    :param controller_id: id of the controller to update
    :return: URI with parameters
    """
    return base_url + "/vtn-webapi/controllers/" + str(controller_id)


def _update_controller_uri(base_url, controller_id):
    """
    VTN Coordinator Update controller URI for PUT request
    :param base_url: base of the request uri
    :param controller_id: id of the controller to update
    :return: URI with parameters
    """
    return base_url + "/vtn-webapi/controllers/" + str(controller_id)


def _update_controller_body(controller_id,
                            version,
                            description=None,
                            ipaddr=None,
                            auditstatus=None,
                            username=None,
                            password=None):
    """
    VTN Coordinator Update controller body for PUT request
    :param controller_id: id of the controller to update
    :param version: version of the controller
    :param description: controller description
    :param ipaddr: IP address of the controller
    :param auditstatus: status of the controller
    :param username: username for login
    :param password: password for login
    :return: dictionary body for JSON
    """
    request_body = {
        "controller": {
            "controller_id": str(controller_id),
            "version": str(version),
        }
    }
    if description is not None:
        request_body["controller"]["description"] = description
    if ipaddr is not None:
        request_body["controller"]["ipaddr"] = ipaddr
    if auditstatus is not None:
        request_body["controller"]["auditstatus"] = auditstatus
    if username is not None:
        request_body["controller"]["username"] = username
    if password is not None:
        request_body["controller"]["password"] = password

    return request_body


def update_controller(base_url,
                      controller_id,
                      version,
                      description=None,
                      ipaddr=None,
                      auditstatus=None,
                      username=None,
                      password=None):
    """
    VTN Coordinator Update controller URL + body for PUT request
    :param base_url: base of the request url
    :param controller_id: id of the controller to update
    :param version: version of the controller
    :param description: controller description
    :param ipaddr: IP address of the controller
    :param auditstatus: status of the controller
    :param username: username for login
    :param password: password for login
    :return: tuple (URL,body)
    """
    return _update_controller_uri(base_url=base_url, controller_id=controller_id), \
           _update_controller_body(controller_id=controller_id,
                                   version=version,
                                   description=description,
                                   ipaddr=ipaddr,
                                   auditstatus=auditstatus,
                                   username=username,
                                   password=password)


def delete_controller(base_url, controller_id):
    """
    VTN Coordinator DELETE Controller URL
    :param base_url: base of URL request
    :param controller_id: id of the controller to delete
    :return: URL with all the parameters
    """
    return base_url + "/vtn-webapi/controllers/" + str(controller_id)
