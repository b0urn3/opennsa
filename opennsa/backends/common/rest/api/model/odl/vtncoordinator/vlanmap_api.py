__author__ = 'Robert Zahradnicek'


def _create_vlanmap_uri(base_url, vtn_name, vbr_name):
    """
    Create vlanmap uri
    :param base_url: base of the requests uri
    :param vtn_name: vtn name
    :param vbr_name: vBridge name
    :return: URI with parameters
    """
    return base_url + "/vtn-webapi/vtns/" + str(vtn_name) + \
           "/vbridges/" + str(vbr_name) + "/vlanmaps.json"


def _create_vlanmap_body(logical_port_id=None, vlan_id=None, no_vlan_id=None):
    """
    Create vlan mapping body
    :param logical_port_id: id of the logical port mapped to vBridge
    :param vlan_id: id of the vlan
    :param no_vlan_id: true or false if vlan_id is not specified
    :return: dictionary for JSON body
    """
    if logical_port_id is not None and vlan_id is not None and no_vlan_id is None:
        request_body = {
            "vlanmap": {
                "logical_port_id": str(logical_port_id),
                "vlan_id": str(vlan_id),
            }
        }
    elif logical_port_id is not None and vlan_id is None and no_vlan_id is None:
        request_body = {
            "vlanmap": {
                "logical_port_id": str(logical_port_id),
            }
        }
    elif logical_port_id is not None and vlan_id is None and no_vlan_id is True:
        request_body = {
            "vlanmap": {
                "logical_port_id": str(logical_port_id),
                "no_vlan_id": "true",
            }
        }
    elif logical_port_id is None and vlan_id is not None and no_vlan_id is None:
        request_body = {
            "vlanmap": {
                "vlan_id": str(vlan_id)
            }
        }
    elif logical_port_id is None and vlan_id is None and no_vlan_id is True:
        request_body = {
            "vlanmap": {
                "no_vlan_id": "true"
            }
        }
    else:
        request_body = {
            "vlanmap": {
            }
        }

    return request_body


def create_vlanmap(base_url, vtn_name, vbr_name, logical_port_id=None, vlan_id=None, no_vlan_id=None):
    """
    Create vlan mapping request URI and body
    :param base_url: base of the request uri
    :param vtn_name: vtn name
    :param vbr_name: vBridge name
    :param logical_port_id: id of the logical port mapped to vBridge
    :param vlan_id: id of the vlan
    :param no_vlan_id: true or false if vlan_id is not specified
    :return: tuple (uri,body)
    """
    return _create_vlanmap_uri(base_url=base_url, vtn_name=vtn_name, vbr_name=vbr_name), _create_vlanmap_body(
        logical_port_id=logical_port_id,
        vlan_id=vlan_id,
        no_vlan_id=no_vlan_id)


def list_vlanmap(base_url, vbr_name, vtn_name, vlanmap_id=None, max_repetition=None):
    """
    Create vlan mapping listing uri
    :param base_url: base of the uri
    :param vbr_name: vBridge name
    :param vtn_name: vtn name
    :param vlanmap_id: id of the vlan mapping
    :param max_repetition: max results
    :return: URI with parameters
    """
    result = base_url + \
             "/vtn-webapi/vtns/" + str(vtn_name) + \
             "/vbridges/" + str(vbr_name) + "/vlanmaps.json"
    query = ""
    if vlanmap_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vlanmap_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vlanmap_detail(base_url, vtn_name, vbr_name, vlanmap_id=None, max_repetition=None):
    """
    Create vlan mapping detail listing uri
    :param base_url: base of the uri
    :param vbr_name: vBridge name
    :param vtn_name: vtn name
    :param vlanmap_id: id of the vlan mapping
    :param max_repetition: max results
    :return: URI with parameters
    """
    result = base_url + \
             "/vtn-webapi/vtns/" + str(vtn_name) + \
             "/vbridges/" + str(vbr_name) + "/vlanmaps/detail.json"
    query = ""
    if vlanmap_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vlanmap_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_vlanmap_count(base_url, vtn_name, vbr_name, vlanmap_id=None, max_repetition=None):
    """
    Create vlan mapping count listing uri
    :param base_url: base of the uri
    :param vbr_name: vBridge name
    :param vtn_name: vtn name
    :param vlanmap_id: id of the vlan mapping
    :param max_repetition: max results
    :return: URI with parameters
    """
    result = base_url + \
             "/vtn-webapi/vtns/" + str(vtn_name) + \
             "/vbridges/" + str(vbr_name) + "/vlanmaps/count.json"
    query = ""
    if vlanmap_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(vlanmap_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def show_vlanmap(base_url, vtn_name, vbr_name, vlanmap_id):
    """
    Create show vlan mapping uri
    :param base_url: base of the uri
    :param vbr_name: vBridge name
    :param vtn_name: vtn name
    :param vlanmap_id: id of the vlan mapping
    :return: URI with parameters
    """
    return base_url + \
           "/vtn-webapi/vtns/" + str(vtn_name) + \
           "/vbridges/" + str(vbr_name) + "/vlanmaps/" + str(vlanmap_id) + ".json"


def _update_vlanmap_uri(base_url, vtn_name, vbr_name, vlanmap_id):
    """
    Create vlan mapping update uri
    :param base_url: base of the uri
    :param vbr_name: vBridge name
    :param vtn_name: vtn name
    :param vlanmap_id: id of the vlan mapping
    :return: URI with parameters
    """
    return base_url + \
           "/vtn-webapi/vtns/" + str(vtn_name) + \
           "/vbridges/" + str(vbr_name) + \
           "/vlanmaps/" + str(vlanmap_id) + ".json"


def _update_vlanmap_body(vlan_id=None, no_vlan_id=None):
    """
    Create vlan mapping listing body
    :param vlan_id: id of the vlan
    :param no_vlan_id: true if vlan_id not specified
    :return: dictionary for json body
    """
    if vlan_id is None and no_vlan_id is None:
        request_body = {
            "vlanmap": {
            }
        }
        return request_body
    elif vlan_id is not None and no_vlan_id is None:
        request_body = {
            "vlanmap": {
                "vlan_id": str(vlan_id)
            }
        }
        return request_body
    elif vlan_id is None and no_vlan_id is True:
        request_body = {
            "vlanmap": {
                "no_vlan_id": "true"
            }
        }
        return request_body
    else:
        request_body = {
            "vlanmap": {
            }
        }
        return request_body


def update_vlanmap(base_url, vtn_name, vbr_name, vlanmap_id, vlan_id=None, no_vlan_id=None):
    """
    Create update vlan mapping request
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vBridge name
    :param vlanmap_id: id of the vlanmap
    :param vlan_id: if of the vlan
    :param no_vlan_id: true if vlan_id not specified
    :return: tuple (uri,body)
    """
    return _update_vlanmap_uri(base_url=base_url, vtn_name=vtn_name, vbr_name=vbr_name, vlanmap_id=vlanmap_id), \
           _update_vlanmap_body(vlan_id=vlan_id, no_vlan_id=no_vlan_id)


def delete_vlanmap(base_url, vtn_name, vbr_name, vlanmap_id):
    """
    Create delete vlan mapping uri
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vBridge name
    :param vlanmap_id: if of vlanmap
    :return:
    """
    return base_url + \
           "/vtn-webapi/vtns/" + str(vtn_name) + \
           "/vbridges/" + str(vbr_name) + "/vlanmaps/" + str(vlanmap_id) + ".json"
