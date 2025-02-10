from django import forms
from .models import UserProfile
from django.forms import ModelChoiceField

class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.last_name + ' ' + obj.first_name

class CustomerChoiceForm(forms.Form):
    #all_clients = UserProfile.objects.values('last_name', 'first_name').order_by('last_name')
    user = UserModelChoiceField(label='Veuillez choisir un client :',
                             required=True,
                             queryset=UserProfile.objects.all(),
                             empty_label="(Choisir un client )",
                             )