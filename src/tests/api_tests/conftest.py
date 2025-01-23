import pytest
from unittest.mock import Mock

# Fixture for base URL
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

# Fixture for headers
@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_auth_token"
    }

# Fixture for post payload
@pytest.fixture
def post_payload():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

# Fixture for mock_response
@pytest.fixture
def mock_response():
    def _mock_response(status_code=200, json_data=None):
        mock_resp = Mock()
        mock_resp.status_code = status_code
        mock_resp.json = Mock(return_value=json_data)
        return mock_resp
    return _mock_response