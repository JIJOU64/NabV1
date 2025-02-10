"""
Class to modify fields in a selected contact as objects
 in the classes contained in the business/entities file.
"""

import re


class ModifyFields:
    """
    Classe permettant de modifier les champs des données d'un client.
    """
    def __init__(self, choose_display, data_accessor):
        """
        Initialise une instance de ModifyFields.

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

    def _display_options_and_get_selection(self, current_value, data, prompt_message):
        """
        Affiche les options et récupère la sélection de l'utilisateur.

        :param current_value: Valeur actuelle du champ.
        :param data: Données à afficher comme options.
        :param prompt_message: Message de prompt pour l'utilisateur.
        :return: La sélection de l'utilisateur ou la valeur actuelle si aucune sélection.
        """
        for i, row in enumerate(data, start=1):
            self.display.print_colored_message(f"{i}.", f" {row[1]}")

        while True:
            try:
                user_input = int(self.display.prompt(prompt_message))
                if user_input == 0:
                    return current_value
                elif 1 <= user_input <= len(data):
                    return data[user_input - 1][0]
                else:
                    self.display.print_message(f"Veuillez entrer un nombre valide entre 1 et {len(data)}.")
            except ValueError:
                self.display.print_message("Veuillez entrer un nombre valide.")

    def _prompt_and_update_field(self, current_value, prompt_message, is_date=False):
        """
        Affiche un prompt pour que l'utilisateur entre une nouvelle valeur pour un champ.

        :param current_value: Valeur actuelle du champ.
        :param prompt_message: Message de prompt pour l'utilisateur.
        :param is_date: Booléen indiquant si le champ est une date.
        :return: La nouvelle valeur ou la valeur actuelle si aucune nouvelle entrée.
        """
        display_value = "champs à remplir" if current_value is None else current_value
        while True:
            new_value = self.display.prompt(f"{prompt_message} (actuel : {display_value}) : ")
            new_value = new_value.strip()

            if not new_value:
                return current_value

            if is_date:
                if re.match(r"^\d{2}/\d{2}/\d{4}$", new_value):
                    return new_value
                else:
                    self.display.print_message("Veuillez entrer une date au format jj/mm/aaaa.")
            else:
                return new_value

    def modify_fields(self, selected_client):
        """
        Affiche le menu de modification des champs et appelle les fonctions de modification appropriées.

        :param selected_client: Le client sélectionné dont les champs doivent être modifiés.
        """
        self.display.display_modify_fields_header()
        fields_to_modify = {
            "les données utilisateur": self.modify_fields_data_user,
            "les données client": self.modify_fields_data_client,
            "les données de formation": self.modify_fields_data_training,
            "les données de suivi après la formation": self.modify_fields_data_followup
        }
        self.display.display_modify_fields_body(fields_to_modify, selected_client)

    def modify_fields_data_user(self, selected_client):
        """
        Modifie les champs des données utilisateur.

        :param selected_client: Le client sélectionné.
        """
        self.display.print_message("\n Données utilisateurs")
        selected_client.last_name = self._prompt_and_update_field(selected_client.last_name,
                                                                  "Nom de l'utilisateur")
        selected_client.first_name = self._prompt_and_update_field(selected_client.first_name,
                                                                   "Prénom de l'utilisateur")
        selected_client.phone_number = self._prompt_and_update_field(selected_client.phone_number,
                                                                     "Numéro de téléphone")
        selected_client.address = self._prompt_and_update_field(selected_client.address,
                                                                "Adresse de l'utilisateur")
        selected_client.email = self._prompt_and_update_field(selected_client.email, "Votre email")
        selected_client.password = self._prompt_and_update_field(selected_client.password,
                                                                 "<Mot de passe>")

    def modify_fields_data_client(self, selected_client):
        """
        Modifie les champs des données client.

        :param selected_client: Le client sélectionné.
        """
        self.display.print_message("\n Données clients")
        client_field = selected_client.clients_data
        client_field.file_creation_date = self._prompt_and_update_field(client_field.file_creation_date,
                                                                        "date de creation du dossier",
                                                                        is_date=True)
        client_field.file_closing_date = self._prompt_and_update_field(client_field.file_closing_date,
                                                                       "date de fermeture du dossier",
                                                                       is_date=True)
        self.display.print_message("Pour information pour l'avancement client taper :")
        self.display.print_message("")

        fetch_data_client_progress = self.data_accessor.fetch_data_client_progress()
        client_field.id_progress_client_progress = (self._display_options_and_get_selection
                                                    (client_field.id_progress_client_progress,
                                                     fetch_data_client_progress,
                                                     "Avancement client"
                                                     " (Taper 0 pour garder la valeur actuelle) : "))
        progress_field = client_field.progress
        progress_field.id_progress = client_field.id_progress_client_progress
        progress_field.name_progress = next(
            row[1] for row in fetch_data_client_progress if row[0] == client_field.id_progress_client_progress
        )

    def modify_fields_data_training(self, selected_client):
        """
        Modifie les champs des données de formation.

        :param selected_client: Le client sélectionné.
        """
        self.display.print_message("\n Données formations")
        training_field = selected_client.clients_data.training_data
        training_field.follow_edof = self._prompt_and_update_field(training_field.follow_edof,
                                                                   "Financement par CPF?")
        training_field.start_session = self._prompt_and_update_field(training_field.start_session,
                                                                     "Début du bilan", is_date=True)
        training_field.end_session = self._prompt_and_update_field(training_field.end_session,
                                                                   "Fin du bilan", is_date=True)
        training_field.number_hours = self._prompt_and_update_field(training_field.number_hours,
                                                                    "Nombre d'heures")
        training_field.cost_assessment = self._prompt_and_update_field(training_field.cost_assessment,
                                                                       "Coût de la formation")
        training_field.number_trainees = self._prompt_and_update_field(training_field.number_trainees,
                                                                       "Nombre de stagiaires")

        fetch_data_training_status = self.data_accessor.fetch_data_training_status()
        training_field.id_status_training_status = (self._display_options_and_get_selection
                                                    (training_field.id_status_training_status,
                                                     fetch_data_training_status,
                                                     "Status du client "
                                                     "(Taper 0 pour garder la valeur actuelle) : "))
        status_field = training_field.training_status
        status_field.id_status = training_field.id_status_training_status
        status_field.status_name = next(
            row[1] for row in fetch_data_training_status if row[0] == training_field.id_status_training_status
        )

        fetch_data_training_title = self.data_accessor.fetch_data_training_title()
        training_field.id_title_training_title = (self._display_options_and_get_selection
                                                  (training_field.id_title_training_title,
                                                   fetch_data_training_title,
                                                   "Nom de la formation "
                                                   "(Taper 0 pour garder la valeur actuelle) : "))
        title_field = training_field.training_title
        title_field.id_title = training_field.id_title_training_title
        title_field.title_name = next(
            row[1] for row in fetch_data_training_title if row[0] == training_field.id_title_training_title
        )

        fetch_data_training_outline = self.data_accessor.fetch_data_training_outline()
        training_field.id_outline_training_outline = (self._display_options_and_get_selection
                                                      (training_field.id_outline_training_outline,
                                                       fetch_data_training_outline,
                                                       "Mode du suivi "
                                                       "(Taper 0 pour garder la valeur actuelle) : "))
        outline_field = training_field.training_outline
        outline_field.id_outline = training_field.id_outline_training_outline
        outline_field.outline_name = next(
            row[1] for row in fetch_data_training_outline if row[0] == training_field.id_outline_training_outline
        )

    def modify_fields_data_followup(self, selected_client):
        """
        Modifie les champs des données de suivi après la formation.

        :param selected_client: Le client sélectionné.
        """
        self.display.print_message("\n Suivi après le bilan de compétence")
        follow_up_field = selected_client.clients_data.training_data.follow_up_after
        follow_up_field.evaluation_sheet = self._prompt_and_update_field(follow_up_field.evaluation_sheet,
                                                                         "Fiche d'évaluation?")
        follow_up_field.planned_date = self._prompt_and_update_field(follow_up_field.planned_date,
                                                                     "Date de prévu pour l'évaluation?",
                                                                     is_date=True)
        follow_up_field.actual_date = self._prompt_and_update_field(follow_up_field.actual_date,
                                                                    "Date réelle pour l'évaluation?",
                                                                    is_date=True)
        follow_up_field.follow_interval = self._prompt_and_update_field(follow_up_field.followup_interval,
                                                                        "Intervalle")

