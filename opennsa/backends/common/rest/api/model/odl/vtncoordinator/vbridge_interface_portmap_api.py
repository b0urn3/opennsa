__author__ = 'Robert Zahradnicek'


def show_vbridge_interface_portmap(base_url, vtn_name, vbr_name, if_name):
    """
    Create show port mapping uri
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :return: uri with parameters
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name + \
           "/vbridges/" + str(vbr_name) + \
           "/interfaces/" + str(if_name) + "/portmap"


def _update_vbridge_interface_portmap_uri(base_url, vtn_name, vbr_name, if_name):
    """
    Create update uri for port mapping
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :return: URI with parameters
    """
    return base_url + \
           "/vtn-webapi/vtns/" + vtn_name + \
           "/vbridges/" + str(vbr_name) + \
           "/interfaces/" + str(if_name) + "/portmap"


def _update_vbridge_interface_portmap_body(logical_port_id, vlan_id=None, tagged=None):
    """
    Create update body for port mapping
    :param logical_port_id: id of the logical port
    :param vlan_id: id of the vlan
    :param tagged: true if vlan is tagged false otherwise
    :return: return dictionary for json body
    """
    if vlan_id is not None and tagged is None:
        request_body = {
            "portmap": {
                "logical_port_id": str(logical_port_id),
                "vlan_id": str(vlan_id)
            }
        }
    elif vlan_id is None and tagged is not None:
        request_body = {
            "portmap": {
                "logical_port_id": str(logical_port_id),
                "tagged": str(tagged)
            }
        }
    elif vlan_id is None and tagged is None:
        request_body = {
            "portmap": {
                "logical_port_id": str(logical_port_id),
            }
        }
    else:
        request_body = {
            "portmap": {
                "logical_port_id": str(logical_port_id),
                "vlan_id": str(vlan_id),
                "tagged": str(tagged)
            }
        }

    return request_body


def update_vbridge_interface_portmap(base_url, vtn_name, vbr_name, if_name, logical_port_id, vlan_id=None, tagged=None):
    """
    Create update uri and body for interface portmap update
    :param base_url: base of the url
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :param logical_port_id: id of the logical port
    :param vlan_id: id of the vlan
    :param tagged: true if vlan is tagged flase otherwise
    :return: tuple (uri,body)
    """
    return _update_vbridge_interface_portmap_uri(base_url=base_url,
                                                 vtn_name=vtn_name,
                                                 vbr_name=vbr_name,
                                                 if_name=if_name), \
           _update_vbridge_interface_portmap_body(logical_port_id=logical_port_id,
                                                  vlan_id=vlan_id,
                                                  tagged=tagged)


def delete_vbridge_interface_portmap(base_url, vtn_name, vbr_name, if_name):
    """
    Create delete portmapping uri
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param vbr_name: vbridge name
    :param if_name: interface name
    :return: uri with parameters
    """
    return base_url + \
           "/vtn-webapi/vtns/" + vtn_name + \
           "/vbridges/" + str(vbr_name) + "/interfaces/" + str(if_name) + "/portmap"
