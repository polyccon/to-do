import pytest
import requests
from src.views import *

def test_login_works_and_set_a_todo_to_complete_subsequently():
    """Test if '/login' and subsequent call to '/complete' endpoint returns 200
        when auth details are correct
    """
    body1 = {
        'username': 'Tom Cruise',
        'password': 'Top Gun'
    }
    body2 = {
        'task': 'wash the dishes'
    }
    s = requests.session()

    s.post('http://localhost:8000/login',
                             json=body1)
    s.post('http://localhost:8000/add',
                             json=body2)
    response = s.put('http://localhost:8000/complete/1',
                             json=body2)

    actual = response.json()['tasks']
    actual_status_code = response.status_code
    assert actual_status_code == 200
    assert actual == [{'complete': True, 'description': 'wash the dishes', 'id': '1'}]
