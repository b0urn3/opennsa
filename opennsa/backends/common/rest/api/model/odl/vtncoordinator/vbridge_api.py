__author__ = 'Robert Zahradnicek'


def _create_vbridge_uri(base_url, vtn_name):
    """
    Create vbridge uri
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :return:
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges"


def _create_vbridge_body(vbr_name, controller_id, domain_id, description=None):
    """
    Create vbridge body
    :param vbr_name: vbridge name
    :param controller_id: controller id
    :param domain_id: domain id
    :param description: description
    :return: dictionary for the json body
    """
    if description is None:
        request_body = {
            "vbridge": {
                "vbr_name": str(vbr_name),
                "controller_id": str(controller_id),
                "description": "TEST vBridge",
                "domain_id": str(domain_id)
            }
        }
        return request_body
    else:
        request_body = {
            "vbridge": {
                "vbr_name": str(vbr_name),
                "controller_id": str(controller_id),
                "description": str(description),
                "domain_id": str(domain_id)
            }
        }
        return request_body


def create_vbridge(base_url, vtn_name, vbr_name, controller_id, domain_id, description=None):
    """
    Create vbridge uri and body
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param controller_id: controller id
    :param domain_id: domain id
    :param description: description of the vbridge
    :return: tuple (uri,body)
    """
    return _create_vbridge_uri(base_url=base_url, vtn_name=vtn_name), _create_vbridge_body(vbr_name=vbr_name,
                                                                                           controller_id=controller_id,
                                                                                           domain_id=domain_id,
                                                                                           description=description)


def list_vbridge(base_url, vtn_name, vbr_name=None, max_repetition=None):
    """
    Create list vbridges uri
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param max_repetition: max results
    :return: uri with params
    """
    result = base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges"
    query = ""
    if vbr_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vbr_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vbridge_detail(base_url, vtn_name, vbr_name=None, max_repetition=None):
    """
    Create list detail vbridges uri
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param max_repetition: max results
    :return: uri with params
    """
    result = base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/detail"
    query = ""
    if vbr_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vbr_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vbridge_count(base_url, vtn_name, vbr_name=None, max_repetition=None):
    """
    Create list count vbridges uri
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param max_repetition: max results
    :return: uri with params
    """
    result = base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/count"
    query = ""
    if vbr_name is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vbr_name)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def show_vbridge(base_url, vtn_name, vbr_name):
    """
    Create show vbridge uri
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :return: uri with params
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name)


def _update_vbridge_uri(base_url, vtn_name, vbr_name):
    """
    Create update vbridges uri
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :return: uri with params
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name)


def _update_vbridge_body(description=None):
    """
    Create update vbridges body
    :param description: description of the vbridge
    :return: dictionary for json body
    """
    if description is None:
        request_body = {
            "vbridge": {
                "description": "TEST vBridge"
            }
        }
        return request_body
    else:
        request_body = {
            "vbridge": {
                "description": str(description)
            }
        }
        return request_body


def update_vbridge(base_url, vtn_name, vbr_name, description=None):
    """
    Create update vbridges uri and body
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :return: tuple (uri,body)
    """
    return _update_vbridge_uri(base_url=base_url, vtn_name=vtn_name, vbr_name=vbr_name), _update_vbridge_body(
        description=description)


def delete_vbridge(base_url, vtn_name, vbr_name):
    """
    Create delete vbridges uri
    :param base_url: base of the request
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :return: uri with params
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + "/vbridges/" + str(vbr_name)
