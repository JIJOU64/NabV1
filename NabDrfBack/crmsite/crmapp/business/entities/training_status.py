"""
Ce module définit la classe TrainingStatus pour gérer le statut du client (Salarié etc...)
"""


class TrainingStatus:
    def __init__(self):
        self.id_status = -1
        self.status_name = "status non défini"

    # ------------------------------
    # property
    # ------------------------------

    @property
    def id_status(self):
        return self._id_status

    @id_status.setter
    def id_status(self, value):
        self._id_status = value

    @property
    def status_name(self):
        return self._status_name

    @status_name.setter
    def status_name(self, value):
        self._status_name = value
