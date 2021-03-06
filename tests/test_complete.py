import pytest
import requests
from src.views import *

def test_set_a_todo_to_complete_endpoint():
    """Test if '/session' and subsequent call to '/complete' endpoint returns 200
        when auth details are correct
    """
    body1 = {
        'username': 'Tom Cruise',
        'password': 'Top Gun'
    }
    body2 = {
        'todo': 'wash the dishes'
    }
    s = requests.session()

    s.post('http://localhost:8000/session',
                             json=body1)
    s.post('http://localhost:8000/todos',
                             json=body2)
    response = s.put('http://localhost:8000/todos/1/complete',
                             json=body2)

    todos = response.json()['todos']
    actual_status_code = response.status_code
    assert actual_status_code == 200
    for item in todos:
        if item['id'] == 1:
            assert actual['complete'] ==  True
            break
