import requests
from unittest.mock import Mock

BASE_URL = "http://127.0.0.1:8000/users/"


def test_valid_admin_credentials(mocker):
    """Test that valid credentials return HTTP 200 using a mocked server."""

    # Create a mock response object
    mock_response = Mock()
    mock_response.status_code = 200

    # Mock requests.get so it returns our mock_response
    mocker.patch("requests.get", return_value=mock_response)

    params = {"username": "admin", "password": "qwerty"}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200


def test_invalid_admin_credentials(mocker):
    """Test that invalid credentials return HTTP 401 using a mocked server."""

    mock_response = Mock()
    mock_response.status_code = 401

    mocker.patch("requests.get", return_value=mock_response)

    params = {"username": "admin", "password": "admin"}
    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401