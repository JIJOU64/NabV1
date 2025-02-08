"""
Ce module définit la classe TrainingTitle pour gérer le nom de la formation
"""


class TrainingTitle:
    def __init__(self):
        self.id_title = -1
        self.title_name = ""

    # ------------------------------
    # property
    # ------------------------------

    @property
    def id_title(self):
        return self._id_title

    @id_title.setter
    def id_title(self, value):
        self._id_title = value

    @property
    def title_name(self):
        return self._title_name

    @title_name.setter
    def title_name(self,value):
        self._title_name = value
