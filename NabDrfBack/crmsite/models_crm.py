# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClientProgress(models.Model):
    id_progress = models.SmallAutoField(primary_key=True)
    name_progress = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_progress'


class ClientsData(models.Model):
    id_client = models.SmallAutoField(primary_key=True)
    file_creation_date = models.DateField(blank=True, null=True)
    file_closing_date = models.DateField(blank=True, null=True)
    id_progress_client_progress = models.ForeignKey(ClientProgress, models.DO_NOTHING, db_column='id_progress_client_progress', blank=True, null=True)
    id_training_training_data = models.OneToOneField('TrainingData', models.DO_NOTHING, db_column='id_training_training_data', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients_data'


class FollowUpAfter(models.Model):
    id_followup = models.SmallAutoField(primary_key=True)
    evaluation_sheet = models.CharField(max_length=100, blank=True, null=True)
    planned_date = models.DateField(blank=True, null=True)
    actual_date = models.DateField(blank=True, null=True)
    followup_interval = models.SmallIntegerField(blank=True, null=True)
    id_training_training_data = models.ForeignKey('TrainingData', models.DO_NOTHING, db_column='id_training_training_data', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'follow_up_after'


class TrainingData(models.Model):
    id_training = models.SmallAutoField(primary_key=True)
    follow_edof = models.CharField(max_length=100, blank=True, null=True)
    start_session = models.DateField(blank=True, null=True)
    end_session = models.DateField(blank=True, null=True)
    number_hours = models.SmallIntegerField(blank=True, null=True)
    cost_assessment = models.SmallIntegerField(blank=True, null=True)
    number_trainees = models.SmallIntegerField(blank=True, null=True)
    id_status_training_status = models.ForeignKey('TrainingStatus', models.DO_NOTHING, db_column='id_status_training_status', blank=True, null=True)
    id_title_training_title = models.ForeignKey('TrainingTitle', models.DO_NOTHING, db_column='id_title_training_title', blank=True, null=True)
    id_outline_training_outline = models.ForeignKey('TrainingOutline', models.DO_NOTHING, db_column='id_outline_training_outline', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_data'


class TrainingOutline(models.Model):
    id_outline = models.SmallAutoField(primary_key=True)
    outline_name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_outline'


class TrainingStatus(models.Model):
    id_status = models.SmallAutoField(primary_key=True)
    status_name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_status'


class TrainingTitle(models.Model):
    id_title = models.SmallAutoField(primary_key=True)
    title_name = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training_title'


class UserProfile(models.Model):
    id_user = models.SmallAutoField(primary_key=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=30, blank=True, null=True)
    id_client_clients_data = models.OneToOneField(ClientsData, models.DO_NOTHING, db_column='id_client_clients_data', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile'
