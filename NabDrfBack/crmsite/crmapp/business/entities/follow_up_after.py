"""
Ce module définit la classe FollowUpAfter pour gérer les données du suivi après la formation du client.
Il inclut des méthodes pour obtenir et mettre à jour les valeurs des clients.
"""
from business.entities.utils_entities import UtilsEntities


class FollowUpAfter:
    """
    Classe pour gérer le suivi après formation des clients liée par composition avec la classe TrainingData.
    Pour plus d'explication sur les méthodes se référer à la classe UserProfile
    """
    def __init__(self):
        self.id_followup = -1
        self.evaluation_sheet = None
        self.planned_date = None
        self.actual_date = None
        self.followup_interval = None
        self.id_training_training_data = None

        self.utils_entities = UtilsEntities()

    @property
    def id_followup(self):
        return self._id_followup

    @id_followup.setter
    def id_followup(self, value):
        self._id_followup = value

    @property
    def evaluation_sheet(self):
        return self._evaluation_sheet

    @evaluation_sheet.setter
    def evaluation_sheet(self, value):
        self._evaluation_sheet = value

    @property
    def planned_date(self):
        return self._planned_date

    @planned_date.setter
    def planned_date(self, value):
        self._planned_date = value

    @property
    def actual_date(self):
        return self._actual_date

    @actual_date.setter
    def actual_date(self, value):
        self._actual_date = value

    @property
    def followup_interval(self):
        return self._followup_interval

    @followup_interval.setter
    def followup_interval(self, value):
        self._followup_interval = value

    @property
    def id_training_training_data(self):
        return self._id_training_training_data

    @id_training_training_data.setter
    def id_training_training_data(self, value):
        self._id_training_training_data = value

    def get_update_values(self):
        format_value = self.utils_entities.format_value
        update_values = [
            f"evaluation_sheet = {format_value(self.evaluation_sheet)}",
            f"planned_date = {format_value(self.planned_date)}",
            f"actual_date = {format_value(self.actual_date)}",
            f"followup_interval = {format_value(self.followup_interval)}",
            f"id_training_training_data = {format_value(self.id_training_training_data)}"
        ]
        return ", ".join(update_values)

    def update_values(self, all_fields_of_chosen_client):
        formatted_date = self.utils_entities.formatted_date
        self.id_followup = all_fields_of_chosen_client[0][22]
        self.evaluation_sheet = all_fields_of_chosen_client[0][23]
        self.planned_date = formatted_date(all_fields_of_chosen_client[0][24])
        self.actual_date = formatted_date(all_fields_of_chosen_client[0][25])
        self.followup_interval = all_fields_of_chosen_client[0][26]
        self.id_training_training_data = all_fields_of_chosen_client[0][12]


