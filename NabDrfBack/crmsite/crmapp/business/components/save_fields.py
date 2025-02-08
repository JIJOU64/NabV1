"""
class to save all objects fields in the database implemented by the classes
 contained in the business/entities folder.
"""


class SaveFields:
    """
    Classe pour sauvegarder les champs des objets dans la base de données.
    """
    def __init__(self, choose_display, data_accessor):
        """
        Initialise une instance de SaveFields.

        :param choose_display: Objet gérant l'affichage et les interactions avec l'utilisateur.
        :param data_accessor: Objet permettant d'accéder aux données.
        """
        self.display = choose_display
        self.data_accessor = data_accessor

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value

    @property
    def data_accessor(self):
        return self._data_accessor

    @data_accessor.setter
    def data_accessor(self, value):
        self._data_accessor = value

    def save_fields(self, selected_fields):
        """
        Sauvegarde les champs spécifiés d'un objet sélectionné dans la base de données.

        :param selected_fields: Les champs sélectionnés à sauvegarder.
        """
        self.display.display_save_fields_header()
        fields_to_save = {
            "les données utilisateur": self.save_fields_data_user,
            "les données du client": self.save_fields_data_client,
            "les données de la formation": self.save_fields_data_training,
            "les données de suivi après la formation": self.save_fields_data_followup
        }
        self.display.display_save_fields_body(fields_to_save, selected_fields)

    def save_fields_data_user(self, selected_client):
        """
        Sauvegarde les champs des données utilisateur dans la base de données.

        :param selected_client: Le client sélectionné dont les données utilisateur doivent être sauvegardées.
        """
        table = "user_profile"
        value_to_update = selected_client.get_update_values()
        name_id_table = "id_user"
        id_table = selected_client.id_user
        self.data_accessor.update_data_table_by_id(table, value_to_update,
                                                   name_id_table, id_table)

    def save_fields_data_client(self, selected_client):
        client_field = selected_client.clients_data
        table = "clients_data"
        value_to_update = client_field.get_update_values()
        name_id_table = "id_client"
        id_table = client_field.id_client
        self.data_accessor.update_data_table_by_id(table, value_to_update,
                                                   name_id_table, id_table)

    def save_fields_data_training(self, selected_client):
        client_field = selected_client.clients_data
        training_field = client_field.training_data
        table = "training_data"
        value_to_update = training_field.get_update_values()
        name_id_table = "id_training"
        id_table = training_field.id_training
        self.data_accessor.update_data_table_by_id(table, value_to_update,
                                                   name_id_table, id_table)

    def save_fields_data_followup(self, selected_client):
        client_field = selected_client.clients_data
        training_field = client_field.training_data
        follow_up_field = training_field.follow_up_after
        table = "follow_up_after"
        value_to_update = follow_up_field.get_update_values()
        name_id_table = "id_followup"
        id_table = follow_up_field.id_followup
        self.data_accessor.update_data_table_by_id(table, value_to_update,
                                                   name_id_table, id_table)


