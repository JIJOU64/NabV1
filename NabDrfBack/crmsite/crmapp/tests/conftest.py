import os
import django
import pytest

# Définir l'environnement Django pour utiliser les paramètres de 'crmsite.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'crmsite.crmsite.settings'

# Configurer Django
django.setup()

@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    """
    Cette fixture permet d'éviter de spécifier db = True dans chaque test.
    Elle s'assure que l'accès à la base de données est activé pour tous les tests.
    """
    pass