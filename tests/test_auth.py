import pytest
import requests
from src.views import *


def test_when_not_logged_in_then_call_to_add_should_be_rejected():
    """ Test if call to '/add' endpoint is authenticated """

    response = requests.session().post(url='http://localhost:8000/add',
                    json={'task': 'clean my cds'})
    assert response.status_code == 401