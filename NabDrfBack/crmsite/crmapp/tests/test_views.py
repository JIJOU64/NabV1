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

@pytest.fixture
def create_client_filter(db):
    #Fixture to create a client filter object.
    return ClientProgress.objects.create(name_progress="Client Progress")

def test_get_client_progress_list(api_client, create_client_progress):
    #test : retrieve client progress list.
    response = api_client.get("/crmapp/api/client-progress/")
    assert response.status_code == 200
    assert len(response.json()) > 0

@pytest.mark.django_db
def test_client_filter_valid(api_client):
    # test check the response with a valid 'user_choice_client' parameter
    response = api_client.get("/crmapp/api/client-filter/filter/?user_choice_client=1")
    print("voici reponse.json() : ")
    print(response.json())
    assert response.status_code == 200

