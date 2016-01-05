import pytest
import requests

from opennsa import config


__author__ = 'Robert Zahradnicek'


@pytest.fixture(scope="session")
def header_json():
    return {
        "Content-Type": "application/json"
    }


@pytest.fixture(scope="module")
def configuration():
    cfg = {
        config.SDNCREST_URL: "http://10.10.10.96",
        config.SDNCREST_VTN: "test_vtn",
        config.SDNCREST_USER: "admin",
        config.SDNCREST_PASS: "adminpass"
    }
    return cfg
