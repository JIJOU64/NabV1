
class ViewFields:
    """
    Classe pour afficher les champs des objets dans l'interface utilisateur.
    """
    def __init__(self, display):
        """
        Initialise une instance de ViewFields.

        :param display: Objet gérant l'affichage dans l'interface utilisateur.
        """
        self.display = display

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value

    def view_fields(self, selected_client):
        """
        Affiche les champs spécifiés d'un objet client dans l'interface utilisateur.

        :param selected_client: Le client sélectionné dont les champs doivent être affichés.
        """
        self.display.display_view_fields_header()
        fields_to_view = {
            "les données utilisateur": self.view_fields_data_user,
            "les données client": self.view_fields_data_client,
            "les données de formation": self.view_fields_data_training,
            "les données de suivi après la formation": self.view_fields_data_followup
        }
        self.display.display_view_fields_body(fields_to_view, selected_client)

    def view_fields_data_user(self,selected_client):
        """
        Affiche les champs des données utilisateur d'un client.

        :param selected_client: Le client sélectionné.
        """
        self.display.print_message("\n Données utilisateurs")
        user_profile = {
            "pour info id_user : ": selected_client.id_user,
            "Nom de l'utilisateur : ": selected_client.last_name,
            "Prénom de l'utilisateur : ": selected_client.first_name,
            "Numéro de téléphone : ": selected_client.phone_number,
            "Adresse : ": selected_client.address,
            "Votre email : ": selected_client.email,
            "<Mot de passe> :": selected_client.password,
            "id_client_clients_data : ": selected_client.id_client_clients_data
        }
        for cle, valeur in user_profile.items():
            self.display.print_message(cle, valeur)

    def view_fields_data_client(self,selected_client):
        client_field = selected_client.clients_data
        self.display.print_message("\n Données clients")
        client_data = {
            "pour info id_client : ": client_field.id_client,
            "date de creation du dossier : ": client_field.file_creation_date,
            "date de fermeture du dossier : ": client_field.file_closing_date,
            "pour info id_training_training_data : ": client_field.id_training_training_data,
            "pour info id_progress_client_progress: ": client_field.id_progress_client_progress,
            "avancement client : ": client_field.progress.name_progress
        }
        for cle, valeur in client_data.items():
            self.display.print_message(cle, valeur)

    def view_fields_data_training(self, selected_client):
        training_field = selected_client.clients_data.training_data
        status_field = training_field.training_status
        title_field = training_field.training_title
        outline_field = training_field.training_outline

        self.display.print_message("\n Données formations")
        training_data = {
            "Financement par CPF? : ": training_field.follow_edof,
            "Début du bilan :": training_field.start_session,
            "Fin du bilan : ": training_field.end_session,
            "Nombre d'heures :": training_field.number_hours,
            "Coût de la formation :": training_field.cost_assessment,
            "Nombre de stagiaires :": training_field.number_trainees,
            "Pour info id_status ": training_field.id_status_training_status,
            "Nom du status: ": status_field.status_name,
            "Pour info id_title: ": training_field.id_title_training_title,
            "Nom de la formation: ": title_field.title_name,
            "Pour info id_outline: ": training_field.id_outline_training_outline,
            "Mode de suivi ": outline_field.outline_name
        }
        for cle, valeur in training_data.items():
            self.display.print_message(cle, valeur)

    def view_fields_data_followup(self, selected_client):
        follow_up_field = selected_client.clients_data.training_data.follow_up_after
        self.display.print_message("\n Suivi après le bilan de compétence")
        training_data = {
            "Fiche d'évaluation?:": follow_up_field.evaluation_sheet,
            "Date de prévu pour l'évaluation?:": follow_up_field.planned_date,
            "Date réelle pour l'évaluation?:": follow_up_field.actual_date,
            "Intervalle :": follow_up_field.followup_interval
        }
        for cle, valeur in training_data.items():
            self.display.print_message(cle, valeur)
