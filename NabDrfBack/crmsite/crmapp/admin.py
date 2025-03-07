from django.contrib import admin
from .models import UserProfile, ClientProgress, TrainingOutline, TrainingStatus

# Register your models here.


admin.site.register(ClientProgress)
admin.site.register(TrainingOutline)

# admin.site.register(TrainingStatus)
# autre façon si on veut par la suite personnaliser l'affichage des modèles :
@admin.register(TrainingStatus)
class TrainingStatusAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('id_status', 'status_name')


"""
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('id_user', 'last_name', 'first_name', 'phone_number', 'email')
    # Champs de recherche
    search_fields = ('last_name', 'first_name', 'email')
    # Filtres sur la barre latérale
    list_filter = ('id_client_clients_data',)
    # Tri par défaut
    ordering = ('last_name', 'first_name')
    # Champs non modifiables dans le formulaire d'édition
    readonly_fields = ('id_user',)
    # Organise le formulaire d’édition en sections claires.
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('last_name', 'first_name', 'phone_number', 'email', 'address')
        }),
        ('Données client', {
            'fields': ('id_client_clients_data',)
        }),
        ('Sécurité', {
            'fields': ('password',)
        }),
    )
"""