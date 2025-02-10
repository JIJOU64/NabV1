"""
Class to create all new ids in a database in order to create a new contact by implementing them as objects
 in the classes contained in the business/entities folder.
"""


class InsertAllNewId:
    """
    La classe sert à insérer de nouveaux IDs pour les entités associées à un contact donné
    """
    def __init__(self, data_accessor):
        """Initialise l'objet InsertAllNewId avec un data_accessor.

        Args :
            data_accessor (object): Accesseur aux données pour la base de données.
        """
        self.data_accessor = data_accessor

    @property
    def data_accessor(self):
        return self._data_accessor

    @data_accessor.setter
    def data_accessor(self, value):
        self._data_accessor = value

    def insert_all_new_id(self, new_contact):
        """Insère de nouveaux IDs pour les entités associées à new_contact.

        Met à jour les IDs des entités associées à new_contact en utilisant
        les méthodes de data_accessor pour créer de nouveaux IDs.

        Args :
            new_contact (object) : L'objet contact contenant les entités à mettre à jour.
        """
        new_contact.id_user = self.data_accessor.create_new_id("user_profile", "id_user")

        client_field = new_contact.clients_data
        client_field.id_client = self.data_accessor.create_new_id("clients_data", "id_client")

        new_contact.id_client_clients_data = client_field.id_client

        training_field = client_field.training_data
        training_field.id_training = self.data_accessor.create_new_id("training_data", "id_training")

        follow_up_field = training_field.follow_up_after
        follow_up_field.id_followup = self.data_accessor.create_new_id("follow_up_after", "id_followup")
        follow_up_field.id_training_training_data = training_field.id_training

        client_field.id_training_training_data = training_field.id_training







