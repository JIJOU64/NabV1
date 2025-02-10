from .document_manager import DocumentManager
from .insert_all_new_id import InsertAllNewId
from .modify_fields import ModifyFields
from .save_fields import SaveFields
from .sort_clients import SortClients
from .update_fields import UpdateFields
from .view_fields import ViewFields
from crmsite.crmapp.data.data_accessor import DataAccessor


class ClientManager:
    """
    Gère l'ensemble des fonctionnalités pour la gestion des clients dans le système.
    """
    def __init__(self, choose_display: AbstractCrmDisplay, choose_database, choose_connection_document):
        """Initialise le gestionnaire de clients avec les dépendances nécessaires.

        Args :
            choose_display (AbstractCrmDisplay) : Interface d'affichage choisie.
            choose_database : Base de données sélectionnée pour l'accès aux données.
            choose_connection_document : Connexion aux documents pour la gestion des fichiers.
        """
        self.data_accessor = DataAccessor(choose_database)
        self.display = choose_display
        self.insert_all_new_id = InsertAllNewId(self.data_accessor)
        self.modify_fields = ModifyFields(choose_display, self.data_accessor)
        self.view_fields = ViewFields(choose_display)
        self.save_fields = SaveFields(choose_display, self.data_accessor)
        self.sort = SortClients(choose_display, self.data_accessor)
        self.update_fields = UpdateFields(self.data_accessor)
        # self.update_fields = UpdateFields(choose_display, self.data_accessor)
        self.document_manager = DocumentManager(choose_display, choose_connection_document)

    @property
    def data_accessor(self):
        return self._data_accessor

    @data_accessor.setter
    def data_accessor(self, value):
        self._data_accessor = value

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value

    @property
    def insert_all_new_id(self):
        return self._insert_all_new_id

    @insert_all_new_id.setter
    def insert_all_new_id(self, value):
        self._insert_all_new_id = value

    @property
    def modify_fields(self):
        return self._modify_fields

    @modify_fields.setter
    def modify_fields(self, value):
        self._modify_fields = value

    @property
    def view_fields(self):
        return self._view_fields

    @view_fields.setter
    def view_fields(self, value):
        self._view_fields = value

    @property
    def save_fields(self):
        return self._save_fields

    @save_fields.setter
    def save_fields(self, value):
        self._save_fields = value

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value

    @property
    def update_fields(self):
        return self._update_fields

    @update_fields.setter
    def update_fields(self, value):
        self._update_fields = value

    @property
    def document_manager(self):
        return self._document_manager

    @document_manager.setter
    def document_manager(self, value):
        self._document_manager = value

    def create_new_contact(self, new_contact):
        """Crée un nouveau contact dans le système.

        Initialise les IDs nécessaires pour le nouveau contact, modifie ses champs,
        affiche ses informations, et sauvegarde ses données.

        Args :
            new_contact : Nouveau contact à créer.
        """
        self.insert_all_new_id.insert_all_new_id(new_contact)
        self.modify_fields.modify_fields(new_contact)
        self.view_fields.view_fields(new_contact)
        self.save_fields.save_fields(new_contact)

    def _manage_list(self, selected_client, list_clients):
        """Gère la liste de clients sélectionnée.

        Trie la liste des clients, met à jour tous les champs du client sélectionné,
        affiche ses informations, modifie ses champs et sauvegarde ses données.

        Args :
            selected_client : Client sélectionné à gérer.
            list_clients (list) : Liste de clients à gérer.
        """
        list_clients = list_clients
        id_user = self.sort.sort_clients(list_clients)
        self.update_fields.update_all_fields_by_id_user(id_user, selected_client)
        self.view_fields.view_fields(selected_client)
        self.modify_fields.modify_fields(selected_client)
        self.view_fields.view_fields(selected_client)
        self.save_fields.save_fields(selected_client)

    def manage_list_active_clients(self, selected_client):
        """Gère la liste des clients actifs.

        Récupère la liste des clients actifs depuis la base de données et les gère
        en utilisant la méthode _manage_list.

        Args :
            selected_client : Client sélectionné pour gérer la liste active.
        """
        list_clients = self.data_accessor.fetch_active_clients()
        self._manage_list(selected_client, list_clients)

    def manage_list_prospective_clients(self, selected_client):
        list_clients = self.data_accessor.fetch_prospective_clients()
        self._manage_list(selected_client, list_clients)

    def manage_list_archive_clients(self, selected_client):
        list_clients = self.data_accessor.fetch_archive_clients()
        self._manage_list(selected_client, list_clients)

    def view_folder_contents(self):
        """Affiche le contenu du dossier géré par le gestionnaire de documents."""
        self.document_manager.get_folder_contents()

    def view_spreadsheet_bilan(self):
        """Affiche et gère le bilan de l'entreprise.

        Récupère les données du bilan actuel depuis la base de données, met à jour
        la feuille de calcul du bilan, et permet à l'utilisateur d'ouvrir le bilan.
        """
        result_bilan = self.data_accessor.fetch_data_current_customer_balance()
        self.document_manager.update_bilan_spreadsheet(result_bilan)
        self.display.print_message("\n Le bilan a été mis à jour")
        user_choice = self.display.get_user_choice("Voulez-vous ouvrir le bilan ? (o/n) ")
        if user_choice == 'o':
            self.display.print_message("Veuillez cliquer sur le lien ci-dessous pour accéder au bilan:")
            self.document_manager.open_bilan_spreadsheets_by_id()
        else:
            print("Fin du programme")
