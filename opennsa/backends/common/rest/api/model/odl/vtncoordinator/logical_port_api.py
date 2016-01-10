__author__ = 'Robert Zahradnicek'


def list_logical_ports(base_url, controller_id, domain_id, logical_port_id=None, max_repetition=None):
    """
    Create list of logical ports
    :param base_url: base of the uri
    :param controller_id: id of the controller
    :param domain_id: id of the domain
    :param logical_port_id: id of the logical port
    :param max_repetition: max results
    :return: uri with parameters
    """
    result = base_url + "/vtn-webapi/controllers/" + str(controller_id) + "/domains/" + str(domain_id) + "/logical_ports"
    query = ""
    if logical_port_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(logical_port_id) + "&logical_port_id=" + str(logical_port_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_logical_ports_detail(base_url, controller_id, domain_id, logical_port_id=None, max_repetition=None):
    """
    Create list detail of logical ports
    :param base_url: base of the uri
    :param controller_id: id of the controller
    :param domain_id: id of the domain
    :param logical_port_id: id of the logical port
    :param max_repetition: max results
    :return: uri with parameters
    """
    result = base_url + "/vtn-webapi/controllers/" + str(controller_id) + "/domains/" + str(domain_id) + "/logical_ports/detail"
    query = ""
    if logical_port_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(logical_port_id) + "&logical_port_id=" + str(logical_port_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query


def list_logical_ports_count(base_url, controller_id, domain_id, logical_port_id=None, max_repetition=None):
    """
    Create list count of logical ports
    :param base_url: base of the uri
    :param controller_id: id of the controller
    :param domain_id: id of the domain
    :param logical_port_id: id of the logical port
    :param max_repetition: max results
    :return: uri with parameters
    """
    result = base_url + "/vtn-webapi/controllers/" + str(controller_id) + "/domains/" + str(domain_id) + "/logical_ports/count"
    query = ""
    if logical_port_id is not None:
        if query == "":
            query += "?"
        query += "index=" + str(logical_port_id) + "&logical_port_id=" + str(logical_port_id)
    if max_repetition is not None:
        if query == "":
            query += "?"
        else:
            query += "&"
        query += "max_repetition=" + str(max_repetition)

    return result + query
