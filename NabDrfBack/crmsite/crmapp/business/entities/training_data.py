"""
Ce module définit la classe TrainingData pour gérer les informations de formation des utilisateurs.
Il inclut des méthodes pour obtenir et mettre à jour les valeurs de formation.
"""
from business.entities.utils_entities import UtilsEntities
from business.entities.follow_up_after import FollowUpAfter
from business.entities.training_status import TrainingStatus
from business.entities.training_title import TrainingTitle
from business.entities.training_outline import TrainingOutline


class TrainingData:
    """
    Classe pour gérer les informations de formation des utilisateurs liée par composition avec la classe ClientsData
    Pour plus d'explication sur les méthodes se référer à la classe UserProfile
    """
    def __init__(self):
        """
        Initialise une nouvelle instance de TrainingData avec des valeurs par défaut.
        """
        self.id_training = -1
        self.follow_edof = None
        self.start_session = None
        self.end_session = None
        self.number_hours = None
        self.cost_assessment = None
        self.number_trainees = None
        self.id_status_training_status = None
        self.id_title_training_title = None
        self.id_outline_training_outline = None

        self.follow_up_after = FollowUpAfter()
        self.training_status = TrainingStatus()
        self.training_title = TrainingTitle()
        self.training_outline = TrainingOutline()

        self.utils_entities = UtilsEntities()

    @property
    def follow_up_after(self):
        return self._follow_up_after

    @follow_up_after.setter
    def follow_up_after(self, value):
        self._follow_up_after = value

    @property
    def training_status(self):
        return self._training_status

    @training_status.setter
    def training_status(self, value):
        self._training_status = value

    @property
    def training_title(self):
        return self._training_title

    @training_title.setter
    def training_title(self, value):
        self._training_title = value

    @property
    def training_outline(self):
        return self._training_outline

    @training_outline.setter
    def training_outline(self, value):
        self._training_outline = value

    @property
    def id_training(self):
        return self._id_training

    @id_training.setter
    def id_training(self, value):
        self._id_training = value

    @property
    def follow_edof(self):
        return self._follow_edof

    @follow_edof.setter
    def follow_edof(self, value):
        self._follow_edof = value

    @property
    def start_session(self):
        return self._start_session

    @start_session.setter
    def start_session(self, value):
        self._start_session = value

    @property
    def end_session(self):
        return self._end_session

    @end_session.setter
    def end_session(self, value):
        self._end_session = value

    @property
    def number_hours(self):
        return self._number_hours

    @number_hours.setter
    def number_hours(self, value):
        self._number_hours = value

    @property
    def cost_assessment(self):
        return self._cost_assessment

    @cost_assessment.setter
    def cost_assessment(self, value):
        self._cost_assessment = value

    @property
    def number_trainees(self):
        return self._number_trainees

    @number_trainees.setter
    def number_trainees(self, value):
        self._number_trainees = value

    @property
    def id_status_training_status(self):
        return self._id_status_training_status

    @id_status_training_status.setter
    def id_status_training_status(self, value):
        self._id_status_training_status = value

    @property
    def id_title_training_title(self):
        return self._id_title_training_title

    @id_title_training_title.setter
    def id_title_training_title(self, value):
        self._id_title_training_title = value

    @property
    def id_outline_training_outline(self):
        return self._id_outline_training_outline

    @id_outline_training_outline.setter
    def id_outline_training_outline(self, value):
        self._id_outline_training_outline = value

    def get_update_values(self):
        format_value = self.utils_entities.format_value
        update_values = [
            f"follow_edof = {format_value(self.follow_edof)}",
            f"start_session = {format_value(self.start_session)}",
            f"end_session = {format_value(self.end_session)}",
            f"number_hours = {format_value(self.number_hours)}",
            f"cost_assessment = {format_value(self.cost_assessment)}",
            f"number_trainees = {format_value(self.number_trainees)}",
            f"id_status_training_status = {format_value(self.id_status_training_status)}",
            f"id_title_training_title = {format_value(self.id_title_training_title)}",
            f"id_outline_training_outline = {format_value(self.id_outline_training_outline)}"
        ]
        return ", ".join(update_values)

    def update_values(self, all_fields_of_chosen_client):
        formatted_date = self.utils_entities.formatted_date
        self.id_training = all_fields_of_chosen_client[0][12]
        self.follow_edof = all_fields_of_chosen_client[0][13]
        self.start_session = formatted_date(all_fields_of_chosen_client[0][14])
        self.end_session = formatted_date(all_fields_of_chosen_client[0][15])
        self.number_hours = all_fields_of_chosen_client[0][16]
        self.cost_assessment = all_fields_of_chosen_client[0][17]
        self.number_trainees = all_fields_of_chosen_client[0][18]
        self.id_status_training_status = all_fields_of_chosen_client[0][19]
        self.id_title_training_title = all_fields_of_chosen_client[0][20]
        self.id_outline_training_outline = all_fields_of_chosen_client[0][21]


