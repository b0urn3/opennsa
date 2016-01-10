__author__ = 'Robert Zahradnicek'


def _create_vbridge_interface_uri(base_url, vtn_name, vbr_name):
    """
    Create vbridge interface uri
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :return: return uri with parameters
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name) + "/interfaces"


def _create_vbridge_interface_body(if_name, description=None, adminstatus=None):
    """
    Create vbridge interface body
    :param if_name: interface name
    :param description: description of the interface
    :param adminstatus: status of the interface
    :return: dictionary for json body
    """
    request_body = {
        "interface": {
            "if_name": str(if_name)
        }
    }
    if description is not None:
        request_body["interface"]["description"] = str(description)
    if adminstatus is not None:
        request_body["interface"]["adminstatus"] = str(adminstatus)
    return request_body


def create_vbridge_interface(base_url, vtn_name, vbr_name, if_name, description=None, adminstatus=None):
    """
    Create vbridge interface request uri + body
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :param description: description of the interface
    :param adminstatus: status of the interface
    :return: tuple (uri,body)
    """
    return _create_vbridge_interface_uri(base_url=base_url,
                                         vtn_name=vtn_name,
                                         vbr_name=vbr_name), \
           _create_vbridge_interface_body(if_name=if_name,
                                          description=description,
                                          adminstatus=adminstatus)


def list_vbridge_interfaces(base_url, vtn_name, vbr_name, if_name=None, max_repetition=None):
    """
    Create list uri for interfaces
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :param max_repetition: max results
    :return: uri with parameters
    """
    result = base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name) + "/interfaces"
    query = ""
    if if_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(if_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vbridge_interfaces_detail(base_url, vtn_name, vbr_name, if_name=None, max_repetition=None):
    """
    Create list detail uri for interfaces
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :param max_repetition: max results
    :return: uri with parameters
    """
    result = base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name) + "/interfaces/detail"
    query = ""
    if if_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(if_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vbridge_interfaces_count(base_url, vtn_name, vbr_name, if_name=None, max_repetition=None):
    """
    Create list detail uri for interfaces
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :param max_repetition: max results
    :return: uri with parameters
    """
    result = base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/"  + str(vbr_name) + "/interfaces/count"
    query = ""
    if if_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(if_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def show_vbridge_interface(base_url, vtn_name, vbr_name, if_name):
    """
    Show info about vBridge interface of name {if_name}
    :param base_url: base of the request url (generally http://(IP or hostname):PORT
    :param vtn_name: vBridge name
    :param vbr_name: Virtual Tenant Network name where vBridge belogns
    :param if_name: interface name
    :return: uri with parameters
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name) + "/interfaces/" + str(if_name)


def _update_vbridge_interface_uri(base_url, vtn_name, vbr_name, if_name):
    """
    Create update interface uri
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :return: return uri with parameters
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name) + "/interfaces/" + str(if_name)


def _update_vbridge_interface_body(description=None, adminstatus=None):
    """
    Create update interface body
    :param description: description of the interface
    :param adminstatus: status of the interface
    :return: dictionary for json body
    """
    request_body = {
        "interface": {

        }
    }
    if description is not None:
        request_body["interface"]["description"] = str(description)
    if adminstatus is not None:
        request_body["interface"]["adminstatus"] = str(adminstatus)

    return request_body


def update_vbridge_interface(base_url, vtn_name, vbr_name, if_name, description=None, adminstatus=None):
    """
    Create update uri and body for interfaces
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :param description: description of the interface
    :param adminstatus: status of the interface
    :return: tuple (uri,body)
    """
    return _update_vbridge_interface_uri(base_url=base_url, vtn_name=vtn_name, vbr_name=vbr_name, if_name=if_name), \
           _update_vbridge_interface_body(description=description, adminstatus=adminstatus)


def delete_vbridge_interface(base_url, vtn_name, vbr_name, if_name):
    """
    Create delete uri for the interface
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :return: uri with parameters
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name) + "/interfaces/" + str(if_name)
