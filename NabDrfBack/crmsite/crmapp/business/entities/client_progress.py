"""
Ce module définit la classe ClientProgress pour gérer l'avancement d'un client.
"""


class ClientProgress:
    def __init__(self):
        self.id_progress = -1
        self.name_progress = "Avancement non défini"

    # ------------------------------
    # property
    # ------------------------------

    @property
    def id_progress(self):
        return self._id_progress

    @id_progress.setter
    def id_progress(self, value):
        self._id_progress = value

    @property
    def name_progress(self):
        return self._name_progress

    @name_progress.setter
    def name_progress(self, value):
        self._name_progress = value
