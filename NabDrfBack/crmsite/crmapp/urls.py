from django.urls import path
from .views import ClientProgressListView, ClientFilterViewSet,  UserProfileListView, UserProfileDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'crmapp'

urlpatterns = [
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/client-progress/', ClientProgressListView.as_view(), name='client-progress'),
    path('api/client-filter/', ClientFilterViewSet.as_view(), name='client-filter'),

    path('api/user-profiles/', UserProfileListView.as_view(), name='user-profile-list'),
    path('api/user-profiles/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile-detail')
]


"""A SUPPRIMER
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

from .views_api import (
    ClientProgressViewSet,
    ClientsDataViewSet,
    FollowUpAfterViewSet,
    TrainingDataViewSet,
    TrainingOutlineViewSet,
    TrainingStatusViewSet,
    TrainingTitleViewSet,
    UserProfileViewSet,
)

app_name = 'crmapp'
# Création d'un router pour les Viewsets
router = DefaultRouter()
router.register('client-progress', ClientProgressViewSet, basename='client-progress')
router.register('clients-data', ClientsDataViewSet, basename='clients-data')
router.register('follow-up', FollowUpAfterViewSet, basename='follow-up')
router.register('training-data', TrainingDataViewSet, basename='training-data')
router.register('training-outline', TrainingOutlineViewSet, basename='training-outline')
router.register('training-status', TrainingStatusViewSet, basename='training-status')
router.register('training-title', TrainingTitleViewSet, basename='training-title')
router.register('user-profile', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    # Routes classiques
    path('home/', views.home, name='home'),
    path('customer_choice/', views.customer_choice, name='customer_choice'),
    path('customer_data/<int:user_id>/', views.customer_data, name='customer_data'),
    path('login/', LoginView.as_view(next_page='/crmapp/home/'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/crmapp/home'), name='logout'),

    # Routes API gérées par le router
    path('api/', include(router.urls)),  # Inclure toutes les routes API générées par le router
]
"""