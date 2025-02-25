from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ClientProgressViewSet,
    ClientFilterViewSet,
    UserProfileViewSet
)

app_name = 'crmapp'

# Creating the router
router = DefaultRouter()
router.register(r'client-progress', ClientProgressViewSet, basename='client-progress')
router.register(r'user-profile', UserProfileViewSet, basename='user-profile')

urlpatterns = [

    path('api/', include(router.urls)),
    path('api/client-filter/filter/', ClientFilterViewSet.as_view({'get': 'filter'}), name='client-filter'),

]

