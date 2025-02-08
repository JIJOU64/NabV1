from document.Abstract_document_connection import AbstractDocumentConnection
from presentation.Abstract_crm_display import AbstractCrmDisplay

from utils.document_constants import MAIN_FOLDER_ID, BILAN_FILE_ID, BILAN_SPREADSHEET_SCOPES, RANGE_NAME_BILAN


class DocumentManager:
    """Gère les opérations liées aux documents dans le CRM."""
    def __init__(self,choose_display: AbstractCrmDisplay, connection: AbstractDocumentConnection):
        """Initialise le gestionnaire de documents avec l'interface d'affichage et la connexion aux documents.

        Args :
            choose_display (AbstractCrmDisplay) : Interface d'affichage choisie.
            connection (AbstractDocumentConnection) : Connexion aux documents choisie.
        """
        self.connection = connection
        self.display = choose_display

    # CREATE
    # READ
    def get_folder_contents(self, folder_id=MAIN_FOLDER_ID):
        """Récupère et affiche le contenu du dossier spécifié.

        Args :
            folder_id (str) : ID du dossier à récupérer. Par défaut, le dossier principal est utilisé.
        """
        connection_folder_by_id = self.connection.get_folder_contents_by_folder_id
        items = connection_folder_by_id(folder_id)
        self.display.print_contents_folder(connection_folder_by_id, items)

    def update_bilan_spreadsheet(self, result_bilan):
        """Met à jour la feuille de calcul de bilan avec les données fournies.

        Args :
            result_bilan : Données du bilan à écrire dans la feuille de calcul.
        """
        spreadsheet_id = BILAN_FILE_ID
        range_name = RANGE_NAME_BILAN
        self.connection.write_sheet_data(spreadsheet_id, range_name, result_bilan)

    def open_bilan_spreadsheets_by_id(self):
        """Ouvre la feuille de calcul de bilan dans un navigateur en affichant son URL."""
        url = f"{BILAN_SPREADSHEET_SCOPES}{BILAN_FILE_ID}"
        self.display.show_file_link(url)

    # UPDATE
    # DELETE







"""from document.document_accessor import DocumentAccessor


class DocumentManager:
    def __init__(self,  choose_data_document):
        self.document_accessor = DocumentAccessor(choose_data_document)

    @property
    def document_accessor(self):
        return self._document_accessor

    @document_accessor.setter
    def document_accessor(self, value):
        self._document_accessor = value

    def view_folder_contents(self):
        folder_id = '1AgLZTitaX-SlWmTVnklxwVnwAKBdBqjE'
        self.document_accessor.get_folder_contents(folder_id)"""


