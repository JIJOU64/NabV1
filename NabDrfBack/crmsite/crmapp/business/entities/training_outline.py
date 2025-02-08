"""
Ce module définit la classe TrainingOutline pour gérer le déroulement de la formation (présentiel Etc...)
"""


class TrainingOutline:
    def __init__(self):
        self.id_outline = -1
        self.outline_name = ""

    @property
    def id_outline(self):
        return self._id_outline

    @id_outline.setter
    def id_outline(self, value):
        self._id_outline = value

    @property
    def outline_name(self):
        return self._outline_name

    @outline_name.setter
    def outline_name(self, value):
        self._outline_name = value
