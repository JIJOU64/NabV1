# ModelViewSet permet de faire les actions CRUD
# ReadOnlyModelViewset ne permet que la lecture
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
import django_filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import (
    ClientProgress,
    ClientsData,
    FollowUpAfter,
    TrainingData,
    TrainingOutline,
    TrainingStatus,
    TrainingTitle,
    UserProfile,
)
from .serializers import (
    ClientProgressSerializer,
    ClientsDataSerializer,
    FollowUpAfterSerializer,
    TrainingDataSerializer,
    TrainingOutlineSerializer,
    TrainingStatusSerializer,
    TrainingTitleSerializer,
    UserProfileSerializer,
)

# ViewSets pour l'API
class ClientProgressViewSet(ReadOnlyModelViewSet):
    queryset = ClientProgress.objects.all()
    serializer_class = ClientProgressSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ClientsDataViewSet(ReadOnlyModelViewSet):
    queryset = ClientsData.objects.all()
    serializer_class = ClientsDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FollowUpAfterViewSet(ReadOnlyModelViewSet):
    queryset = FollowUpAfter.objects.all()
    serializer_class = FollowUpAfterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TrainingDataViewSet(ReadOnlyModelViewSet):
    queryset = TrainingData.objects.all()
    serializer_class = TrainingDataSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TrainingOutlineViewSet(ReadOnlyModelViewSet):
    queryset = TrainingOutline.objects.all()
    serializer_class = TrainingOutlineSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TrainingStatusViewSet(ReadOnlyModelViewSet):
    queryset = TrainingStatus.objects.all()
    serializer_class = TrainingStatusSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TrainingTitleViewSet(ReadOnlyModelViewSet):
    queryset = TrainingTitle.objects.all()
    serializer_class = TrainingTitleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserProfileViewSet(ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

