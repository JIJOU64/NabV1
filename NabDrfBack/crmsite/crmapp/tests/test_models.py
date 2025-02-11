import pytest
from crmsite.crmapp.models import ClientProgress, ClientsData

@pytest.mark.django_db
def test_create_client_progress():
    client_progress = ClientProgress.objects.create(name_progress="Completed")
    assert client_progress.id_progress is not None
    assert client_progress.name_progress == "Completed"


@pytest.mark.django_db
def test_create_clients_data():
    client_progress = ClientProgress.objects.create(name_progress="In Progress")

    clients_data = ClientsData.objects.create(
        file_creation_date="2025-01-01",
        file_closing_date="2025-02-01",
        id_progress_client_progress=client_progress
    )

    assert clients_data.id_client is not None
    assert clients_data.id_progress_client_progress == client_progress