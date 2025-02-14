import os
import pytest
import django

# Définir l'environnement Django pour utiliser les paramètres de 'crmsite.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'crmsite.crmsite.settings'

# Appeler django.setup() pour charger correctement les applications
django.setup()

# Importer les vues et modèles nécessaires
from crmapp.views import ClientFilterViewSet
from crmapp.models import UserProfile
from rest_framework.test import APIRequestFactory

#@pytest.mark.django_db
def test_client_filter_viewset_active_clients(mocker):
    factory = APIRequestFactory()
    request = factory.get('/api/client-filter/', {'user_choice_client': '1'})

    # Mock de "UserProfile.objects.filter" pour simuler une réponse
    mock_filter = mocker.patch('crmapp.models.UserProfile.objects.filter')
    mock_filter.return_value = [
        {"id_user": 1, "first_name": "John", "last_name": "Doe"}  # Réponse simulée avec first_name et last_name
    ]

    view = ClientFilterViewSet.as_view({'get': 'list'})

    response = view(request)

    # Vérifie que la requête a retourné un statut 200
    assert response.status_code == 200

    # Vérifie que "UserProfile.objects.filter" a été appelé une fois avec les bons arguments
    mock_filter.assert_called_once_with(id_client_clients_data__id_progress_client_progress__id_progress__in=[1, 2, 3])

    # Vérifie que la réponse contient les données simulées
    expected_response = [{"id_user": 1, "first_name": "John", "last_name": "Doe"}]
    assert response.data == expected_response

