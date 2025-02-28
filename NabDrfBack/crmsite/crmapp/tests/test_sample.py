# content of test_sample.py
import pytest
from crmapp.models import UserProfile  # Exemple d'import pour vérifier que tout fonctionne
import django
django.setup()
def func(x):
    return x + 1


def test_answer():
    assert func(4) == 5
