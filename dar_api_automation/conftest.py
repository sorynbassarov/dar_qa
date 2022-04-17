import pytest

from dar_api_automation.api.api import Api


@pytest.fixture(scope="function")
def url():
    url = Api("https://reqres.in/api/")
    return url

