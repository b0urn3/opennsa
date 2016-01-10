__author__ = 'Robert Zahradnicek'


def _create_vtn_uri(base_url):
    """
    create vtn request uri
    :param base_url: base of the uri
    :return: uri for vtn request
    """
    return base_url + "/vtn-webapi/vtns"


def _create_vtn_body(vtn_name, description=None):
    """
    create body for vtn creation
    :param vtn_name: name of the vtn
    :param description: description
    :return: dictionary for json body
    """
    request_body = {
        "vtn": {
            "vtn_name": str(vtn_name),
        }
    }
    if description is not None:
        request_body["vtn"]["description"] = str(description)
    else:
        request_body["vtn"]["description"] = "TEST VTN"
    return request_body


def create_vtn(base_url, vtn_name, description=None):
    """
    Create vtn uri and body for request
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param description: description of the vtn
    :return: tuple (uri,body)
    """
    return _create_vtn_uri(base_url=base_url), _create_vtn_body(vtn_name=vtn_name, description=description)


def list_vtn(base_url, vtn_name, max_repetition=None):
    """
    Create list uri for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param max_repetition: max results
    :return: uri with params
    """
    if max_repetition is not None:
        return base_url + "/vtn-webapi/vtns?index=" + vtn_name \
                                        + "&max_repetition=" + str(max_repetition)
    else:
        return base_url + "/vtn-webapi/vtns?index=" + vtn_name


def list_vtn_detail(base_url, vtn_name, max_repetition=None):
    """
    Create list detail uri for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param max_repetition: max results
    :return: uri with params
    """
    if max_repetition is not None:
        return base_url + "/vtn-webapi/vtns/detail?index=" + vtn_name \
                                        + "&max_repetition=" + str(max_repetition)
    else:
        return base_url + "/vtn-webapi/vtns/detail?index=" + vtn_name


def list_vtn_count(base_url, vtn_name, max_repetition=None):
    """
    Create list count uri for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param max_repetition: max results
    :return: uri with params
    """
    if max_repetition is not None:
        return base_url + "/vtn-webapi/vtns/count?index=" + vtn_name \
                                        + "&max_repetition=" + str(max_repetition)
    else:
        return base_url + "/vtn-webapi/vtns/count?index=" + vtn_name


def show_vtn(base_url, vtn_name):
    """
    Create show uri for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :return: uri with params
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name


def _update_vtn_uri(base_url, vtn_name):
    """
    Create update uri for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :return: uri with params
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name


def _update_vtn_body(vtn_name, description=None):
    """
    Create update body for vtn
    :param vtn_name: vtn name
    :param description: vtn description
    :return: dictionary for json body
    """
    request_body = {
        "vtn": {
            "vtn_name": str(vtn_name),
        }
    }
    if description is not None:
        request_body["vtn"]["description"] = str(description)
    else:
        request_body["vtn"]["description"] = "TEST VTN"
    return request_body


def update_vtn(base_url, vtn_name, description=None):
    """
    Create update uri and body for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :param description: vtn description
    :return: tuple (uri,body)
    """
    return _update_vtn_uri(base_url=base_url, vtn_name=vtn_name), \
           _update_vtn_body(vtn_name=vtn_name, description=description)


def delete_vtn(base_url, vtn_name):
    """
    Create delete uri for vtn
    :param base_url: base of the uri
    :param vtn_name: vtn name
    :return: uri with params
    """
    return base_url + "/vtn-webapi/vtns/" + vtn_name
