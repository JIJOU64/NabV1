from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import UserProfile, ClientProgress
from .serializers import ClientFilterSerializer, UserProfileSerializer, ClientProgressSerializer


class ClientProgressViewSet(ModelViewSet):
    queryset = ClientProgress.objects.all()
    serializer_class = ClientProgressSerializer

    def get_permissions(self):
        # we check the action
        if self.action == 'list': # Allow access without authentication for filtering
            return [AllowAny()]
        # for all other actions (retrieve, create, update), authentification is required
        return [IsAuthenticated()]

class ClientFilterViewSet(ViewSet):
    permission_classes = [AllowAny] # Allow access without authentication

    @action(detail=False, methods=['get'])
    def filter(self, request):
        user_choice_client = request.query_params.get('user_choice_client')

        if not user_choice_client:
            raise ValidationError({"detail": "Le paramètre 'user_choice_client' est requis."})

        filters = {
            '1': [1, 2, 3],  # active clients
            '2': [1],  # prospective clients
            '3': [2],  # training clients
            '4': [3],  # followup clients
            '5': [4],  # archive clients
        }

        if user_choice_client not in filters:
            raise ValidationError({"detail": "Valeur invalide pour 'user_choice_client'."})

        user = UserProfile.objects.filter(
            id_client_clients_data__id_progress_client_progress__id_progress__in=filters[user_choice_client]
        )

        serializer = ClientFilterSerializer(user, many=True)
        return Response(serializer.data)

# to list all user profiles and display a specific user

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_permissions(self):
        # Authentication is required for access to user profiles
        if self.action in ['retrieve', 'update', 'destroy']:
            return [IsAuthenticated()]
        # For the list action (list profiles), you can optionally leave access open if necessary
        return [AllowAny()]
