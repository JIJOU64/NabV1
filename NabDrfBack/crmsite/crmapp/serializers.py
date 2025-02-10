from rest_framework import serializers
from .models import (
    UserProfile,
    ClientProgress,
    ClientsData,
    FollowUpAfter,
    TrainingData,
    TrainingOutline,
    TrainingStatus,
    TrainingTitle,
)

# Serializer with last_name, first_name and id_user to filter customers
class ClientFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name', 'id_user']

# Serializers to see all client data
class TrainingOutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingOutline
        fields = ['outline_name']

class TrainingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingStatus
        fields = ['status_name']

class TrainingTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTitle
        fields = ['title_name']

class FollowUpAfterSerializer(serializers.ModelSerializer):
    #id_training_training_data = TrainingDataSerializer()

    class Meta:
        model = FollowUpAfter
        fields = '__all__'

class TrainingDataSerializer(serializers.ModelSerializer):
    id_status_training_status = TrainingStatusSerializer()
    id_title_training_title = TrainingTitleSerializer()
    id_outline_training_outline = TrainingOutlineSerializer()
    followupafter_set = FollowUpAfterSerializer(many=True)

    class Meta:
        model = TrainingData
        fields = '__all__'

class FollowUpAfterSerializer(serializers.ModelSerializer):
    #id_training_training_data = TrainingDataSerializer()

    class Meta:
        model = FollowUpAfter
        fields = '__all__'

class ClientProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProgress
        fields = ['id_progress','name_progress']

class ClientsDataSerializer(serializers.ModelSerializer):
    id_progress_client_progress = ClientProgressSerializer()
    id_training_training_data = TrainingDataSerializer()

    class Meta:
        model = ClientsData
        fields = '__all__'

# Sérializer with all data user
class UserProfileSerializer(serializers.ModelSerializer):
    id_client_clients_data = ClientsDataSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'
        
"""
# Serializer pour le modèle ClientProgress
class ClientProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProgress
        fields = '__all__'


# Serializer pour le modèle ClientsData
class ClientsDataSerializer(serializers.ModelSerializer):
    # Inclure la relation ForeignKey vers ClientProgress
    id_progress_client_progress = ClientProgressSerializer(read_only=True)
    # Inclure la relation OneToOne vers TrainingData
    id_training_training_data = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ClientsData
        fields = '__all__'


# Serializer pour le modèle FollowUpAfter
class FollowUpAfterSerializer(serializers.ModelSerializer):
    # Inclure la relation ForeignKey vers TrainingData
    id_training_training_data = serializers.StringRelatedField()  # Affiche le `__str__` de TrainingData

    class Meta:
        model = FollowUpAfter
        fields = '__all__'


# Serializer pour le modèle TrainingData
class TrainingDataSerializer(serializers.ModelSerializer):
    # Relations ForeignKey vers TrainingStatus, TrainingTitle, et TrainingOutline
    id_status_training_status = serializers.StringRelatedField()
    id_title_training_title = serializers.StringRelatedField()
    id_outline_training_outline = serializers.StringRelatedField()

    class Meta:
        model = TrainingData
        fields = '__all__'


# Serializer pour le modèle TrainingOutline
class TrainingOutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingOutline
        fields = '__all__'


# Serializer pour le modèle TrainingStatus
class TrainingStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingStatus
        fields = '__all__'


# Serializer pour le modèle TrainingTitle
class TrainingTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTitle
        fields = '__all__'




class ClientDetailSerializer(serializers.ModelSerializer):
    # Sérialiser la relation OneToOne de UserProfile vers ClientsData
    user_profile = UserProfileSerializer(read_only=True)  # Sérialiser UserProfile
    clients_data = ClientsDataSerializer(read_only=True)  # Sérialiser ClientsData
    # Sérialiser les relations liées (FollowUpAfter et TrainingData)
    follow_up_after = FollowUpAfterSerializer(many=True, read_only=True)  # Liste de FollowUpAfter
    training_data = TrainingDataSerializer(many=True, read_only=True)  # Liste de TrainingData

    class Meta:
        model = UserProfile  # On sérialise UserProfile
        fields = ['user_profile', 'clients_data', 'follow_up_after', 'training_data']
"""