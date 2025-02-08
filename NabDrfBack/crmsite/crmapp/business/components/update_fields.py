"""
Ce module définit la classe UpdateFields pour mettre à jour les champs des utilisateurs
à partir des données récupérées par l'identifiant utilisateur.
"""


class UpdateFields:
    """
    Classe pour mettre à jour les champs des utilisateurs en fonction des données récupérées.
    """
    # def __init__(self, choose_display, data_accessor):
    def __init__(self, data_accessor):
        """
        Initialise une nouvelle instance de UpdateFields avec les valeurs fournies.

        :param choose_display: objet pour gérer l'affichage
        :param data_accessor: objet pour accéder aux données
        """
        # self.display = choose_display
        self.data_accessor = data_accessor

    """@property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value"""

    @property
    def data_accessor(self):
        return self._data_accessor

    @data_accessor.setter
    def data_accessor(self, value):
        self._data_accessor = value

    def update_all_fields_by_id_user(self, id_user, selected_client):
        """
        Met à jour tous les champs du client sélectionné en fonction
        des données récupérées par l'identifiant utilisateur.

        :param id_user: l'identifiant de l'utilisateur
        :param selected_client: objet du client sélectionné
        """
        # Récupère toutes les données du client par id_user dans la base de données
        fetch_all_fields = self.data_accessor.fetch_all_fields_by_id_user(id_user)
        selected_client.update_values(fetch_all_fields)

        # Met à jour les données du client dans l'objet UserProfile
        client_field = selected_client.clients_data
        client_field.update_values(fetch_all_fields)

        # Met à jour l'avancement du client dans l'objet ClientProgress
        fetch_data_client_progress = self.data_accessor.fetch_data_client_progress()
        progress_field = client_field.progress
        progress_field.id_progress = client_field.id_progress_client_progress
        if client_field.id_progress_client_progress is not None:
            progress_field.name_progress = next(
                row[1] for row in fetch_data_client_progress if row[0] == client_field.id_progress_client_progress
            )

        # Met à jour les données formation du client
        training_field = client_field.training_data
        training_field.update_values(fetch_all_fields)

        # Met à jour le statut du client dans la formation
        fetch_data_training_status = self.data_accessor.fetch_data_training_status()
        status_field = training_field.training_status
        status_field.id_status = training_field.id_status_training_status

        if training_field.id_status_training_status is not None:
            status_field.status_name = next(
                row[1] for row in fetch_data_training_status if row[0] == training_field.id_status_training_status
            )

        # Met à jour le nom de la formation
        fetch_data_training_title = self.data_accessor.fetch_data_training_title()
        title_field = training_field.training_title
        title_field.id_title = training_field.id_title_training_title

        if training_field.id_title_training_title is not None:
            title_field.title_name = next(
                row[1] for row in fetch_data_training_title if row[0] == training_field.id_title_training_title
            )

        # Met à jour le déroulement de la formation
        fetch_data_training_outline = self.data_accessor.fetch_data_training_outline()
        outline_field = training_field.training_outline
        outline_field.id_outline = training_field.id_outline_training_outline

        if training_field.id_outline_training_outline is not None:
            outline_field.outline_name = next(
                row[1] for row in fetch_data_training_outline if row[0] == training_field.id_outline_training_outline
            )

        # Met à jour les données du suivi après la formation
        follow_up_field = training_field.follow_up_after
        follow_up_field.update_values(fetch_all_fields)


