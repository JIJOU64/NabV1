"""
Ce module définit la classe ClientsData pour gérer les données des clients.
Il inclut des méthodes pour obtenir et mettre à jour les valeurs des clients.
"""
from business.entities.utils_entities import UtilsEntities
from business.entities.client_progress import ClientProgress
from business.entities.training_data import TrainingData


class ClientsData:
    """
    Classe pour gérer les données des clients liée par composition avec la classe ClientsData.
    Pour plus d'explication sur les méthodes se référer à la classe UserProfile
    """
    def __init__(self):
        self.id_client = -1
        self.file_creation_date = None
        self.file_closing_date = None
        self.id_progress_client_progress = None
        self.id_training_training_data = None

        self.progress = ClientProgress()
        self.training_data = TrainingData()
        self.utils_entities = UtilsEntities()

        # ------------------------------
        # property
        # ------------------------------

    @property
    def id_client(self):
        return self._id_client

    @id_client.setter
    def id_client(self, value):
        self._id_client = value

    @property
    def file_creation_date(self):
        return self._file_creation_date

    @file_creation_date.setter
    def file_creation_date(self, value):
        self._file_creation_date = value

    @property
    def file_closing_date(self):
        return self._file_closing_date

    @file_closing_date.setter
    def file_closing_date(self, value):
        self._file_closing_date = value

    @property
    def id_progress_client_progress(self):
        return self._id_progress_client_progress

    @id_progress_client_progress.setter
    def id_progress_client_progress(self, value):
        self._id_progress_client_progress = value

    @property
    def id_training_training_data(self):
        return self._id_training_training_data

    @id_training_training_data.setter
    def id_training_training_data(self, value):
        self._id_training_training_data = value

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value

    @property
    def training_data(self):
        return self._training_data

    @training_data.setter
    def training_data(self, value):
        self._training_data = value

    def get_update_values(self):
        format_value = self.utils_entities.format_value
        update_values = [
            f"file_creation_date = {format_value(self.file_creation_date)}",
            f"file_closing_date = {format_value(self.file_closing_date)}",
            f"id_progress_client_progress = {format_value(self.id_progress_client_progress)}",
            f"id_training_training_data = {format_value(self.id_training_training_data)}"
        ]
        return ", ".join(update_values)

    def update_values(self, all_fields_of_chosen_client):
        formatted_date = self.utils_entities.formatted_date
        self.id_client = all_fields_of_chosen_client[0][7]
        self.file_creation_date = formatted_date(all_fields_of_chosen_client[0][8])
        self.file_closing_date = formatted_date(all_fields_of_chosen_client[0][9])
        self.id_progress_client_progress = int(all_fields_of_chosen_client[0][10])
        self.id_training_training_data = all_fields_of_chosen_client[0][11]


