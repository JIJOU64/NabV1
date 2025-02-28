"""

import pytest
from rest_framework.test import APIClient
from crmapp.models import ClientProgress


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_client_progress(db):
    #Fixture to create a client progress object.
    return ClientProgress.objects.create(name_progress="Client Progress")

def test_get_client_progress_list(api_client, create_client_progress):
    #test : retrieve client progress list.
    response = api_client.get("/api/client-progress/")
    assert response.status_code == 200
    #sert len(response.json()) > 0

"""