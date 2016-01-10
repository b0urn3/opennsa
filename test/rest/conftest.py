import pytest

from opennsa import config


__author__ = 'Robert Zahradnicek'


@pytest.fixture(scope="session")
def header_json():
    return {
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="session")
def configuration():
    cfg = {
        config.SDNCREST_URL: "http://10.10.10.96:8083",
        config.SDNCREST_VTN: "test_vtn",
        config.SDNCREST_USER: "admin",
        config.SDNCREST_PASS: "adminpass",
        config.SDNCREST_CNTRL_ID: "controllerxxx",
        config.SDNCREST_CNTRL_IP: "10.10.10.10",
        config.SDNCREST_CNTRL_TYPE: "odc",
        config.SDNCREST_CNTRL_VERSION: "1.0",
        config.SDNCREST_API_TYPE: "odl"
    }
    return cfg


@pytest.fixture(scope="session")
def base_url():
    return "http://10.10.10.96:8083"


@pytest.fixture(scope="session")
def username():
    return "admin"


@pytest.fixture(scope="session")
def password():
    return "adminpass"


@pytest.fixture(scope="session")
def vtn_name():
    return "test_vtn"


@pytest.fixture(scope="session")
def vbr_name():
    return "test_vbr"


@pytest.fixture(scope="session")
def header_json():
    return {
        "Content-Type": "application/json"
    }