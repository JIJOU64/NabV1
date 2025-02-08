from rest_framework.views import APIView # Class-based Views
from rest_framework.generics import ListAPIView, RetrieveAPIView # Django's generic views as a shorcut for commun usage patterns
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import authentication, permissions
from .models import UserProfile, ClientProgress
from .serializers import ClientFilterSerializer, UserProfileSerializer, ClientProgressSerializer


class ClientProgressListView(ListAPIView):
    queryset = ClientProgress.objects.all()
    serializer_class = ClientProgressSerializer

class ClientFilterViewSet(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        user_choice_client = request.query_params.get('user_choice_client')

        if not user_choice_client:
            raise ValidationError({"detail": "Le paramètre 'user_choice_client' est requis."})

        if user_choice_client == '1': # active clients
            users = UserProfile.objects.filter(
                id_client_clients_data__id_progress_client_progress__id_progress__in=[1, 2, 3]
            )
        elif user_choice_client == '2': # prospective clients
            users = UserProfile.objects.filter(
                id_client_clients_data__id_progress_client_progress__id_progress__in=[1]
            )
        elif user_choice_client == '3': # training clients
            users = UserProfile.objects.filter(
                id_client_clients_data__id_progress_client_progress__id_progress__in=[2]
            )
        elif user_choice_client == '4': # followup clients
            users = UserProfile.objects.filter(
                id_client_clients_data__id_progress_client_progress__id_progress__in=[3]
            )
        elif user_choice_client == '5': # archive clients
            users = UserProfile.objects.filter(
                id_client_clients_data__id_progress_client_progress__id_progress__in=[4]
            )
        else:
            raise ValidationError({"detail": "Valeur invalide pour 'user_choice_client'."})

        serializer = ClientFilterSerializer(users, many=True)

        return Response(serializer.data)

# Vue pour lister tous les profils utilisateurs
class UserProfileListView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

# Vue pour afficher un profil utilisateur spécifique
class UserProfileDetailView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



"""
A SUPPRIMER

import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import CustomerChoiceForm

from .models import UserProfile
from .models import ClientsData

logger = logging.getLogger("django")

def hello_world(request):
    return HttpResponse("Hello World")
# Create your views here.
#@login_required(login_url='/crmapp/login/')
def home(request):
    logger.info("Page d'acceuil consultée")
    return render(request, 'crmapp/home.html', {})

@login_required(login_url='/crmapp/login/')
def customer_choice(request):
    if request.method == 'POST':
        form = CustomerChoiceForm(request.POST)
        if form.is_valid():
            selected_user = form.cleaned_data['user']
            # Utilise le champ id_user, qui est la clé primaire de UserProfile
            user_id = selected_user.id_user
            logger.info(f"Utilisateur sélectionné : {user_id}")

            # Modifie explicitement la session pour signaler une mise à jour
            request.session.modified = True
            return redirect('crmapp:customer_data', user_id=user_id)
        else:
            logger.warning("Formulaire non valide")
    else:
        form = CustomerChoiceForm()
        logger.info("Formulaire de choix de client affiché")

    # Récupérer l'historique des clients depuis la session
    recent_clients_ids = request.session.get('recent_clients', [])
    recent_clients = UserProfile.objects.filter(id_user__in=recent_clients_ids)
    logger.debug(f"Historique des clients récents : {recent_clients_ids}")

    return render(request, 'crmapp/customer_choice.html', {
        'form': form,
        'recent_clients': recent_clients
    })

#@login_required(login_url='/crmapp/login/')
def customer_data(request, user_id):

    save_error = False
    is_create = True

    try:
        # Récupère l'utilisateur depuis la base de données avec l'ID fourni
        user = get_object_or_404(UserProfile, id_user=user_id)
        client_data = ClientsData.objects.get(pk=user.id_client_clients_data.id_client)
        logger.info(f"Données récupérées pour l'utilisateur : {user_id}")
        if not user:
            save_error = True  # Indique une erreur si les données sont manquantes
    except UserProfile.DoesNotExist:
        save_error = True
        user = None  # Définit `user` sur None pour éviter les erreurs d'affichage
        logger.error(f"Utilisateur introuvable avec ID : {user_id}")
    except ClientsData.DoesNotExist:
        save_error = True
        logger.error(f"Données client introuvables pour l'utilisateur : {user_id}")

    # Gérer l'historique des clients consultés
    # Récupère l'historique des clients depuis la session ou initialise-le
    history = request.session.get('recent_clients', [])

    # Ajoute l'utilisateur actuel à l'historique s'il n'est pas déjà présent
    if user_id not in history:
        history.insert(0, user_id)  # Ajoute au début de la liste
        history = history[:2]  # Garde seulement les 2 derniers clients
        logger.debug(f"Historique mis à jour : {history}")

    # Sauvegarde l'historique dans la session
    request.session['recent_clients'] = history
    request.session.modified = True  # Marque la session comme modifiée

    # Rend la page avec les informations de l'utilisateur et les indicateurs d'état
    return render(request, 'crmapp/customer_data.html', {
        'user': user,
        'client_data': client_data,
        'save_error': save_error,
        'is_create': is_create,
    })
"""
