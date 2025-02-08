import os
import pickle
import logging
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError

from document.Abstract_document_connection import AbstractDocumentConnection
from utils.document_constants import CREDENTIALS_FILE, TOKEN_FILE, DRIVE_SCOPES, PAGE_SIZE

# Configuration du journal (logging)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GoogleDriveConnection(AbstractDocumentConnection):
    def __init__(self):
        """Initialise la connexion à Google Drive et Google Sheets."""
        self._credentials_file = os.path.abspath(CREDENTIALS_FILE)
        self._token_file = TOKEN_FILE
        self._scopes = DRIVE_SCOPES  # Scopes d'accès autorisés
        self._service = None
        self._sheets_service = None

    def _get_credentials(self):
        """Obtient les identifiants d'authentification pour accéder aux APIs."""
        creds = None
        if os.path.exists(self._token_file):
            try:
                with open(self._token_file, 'rb') as token:
                    creds = pickle.load(token)
            except Exception as e:
                logger.error(f"Erreur lors du chargement du token : {e}")

        if not creds or not creds.valid:
            try:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                    logger.info("Jeton actualisé avec succès.")
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(self._credentials_file, self._scopes)
                    creds = flow.run_local_server(port=0)
                    logger.info("Authentification réussie et nouveau jeton obtenu.")
                with open(self._token_file, 'wb') as token:
                    pickle.dump(creds, token)
            except RefreshError as e:
                logger.error(f"Erreur de rafraîchissement du jeton : {e}")
                raise e
            except Exception as e:
                logger.error(f"Erreur lors de l'obtention des identifiants : {e}")
                raise e
        return creds

    def _get_service(self):
        """Initialise et retourne le service Google Drive."""
        if not self._service:
            creds = self._get_credentials()
            self._service = build('drive', 'v3', credentials=creds)
        return self._service

    def get_folder_contents_by_folder_id(self, folder_id):
        """Récupère le contenu d'un dossier spécifié par son ID.

        Args :
            folder_id (str) : ID du dossier à récupérer.

        Returns:
            list : Liste des fichiers et dossiers contenus dans le dossier spécifié.
        """
        try:
            service = self._get_service()
            query = f"'{folder_id}' in parents"
            results = service.files().list(
                q=query,
                pageSize=PAGE_SIZE,
                fields="files(id, name, mimeType)"
            ).execute()
            items = results.get('files', [])
            return items
        except Exception as e:
            logger.error(f"Erreur lors de la récupération du contenu du dossier : {e}")
            raise e

    def _get_sheets_service(self):
        """Initialise et retourne le service Google Sheets."""
        if not self._sheets_service:
            creds = self._get_credentials()
            self._sheets_service = build('sheets', 'v4', credentials=creds)
        return self._sheets_service

    def read_sheet_data(self, spreadsheet_id, range_name):
        """Lit les données à partir d'une feuille de calcul spécifiée.

        Args :
            spreadsheet_id (str) : ID de la feuille de calcul.
            range_name (str) : Nom de la plage de cellules à lire.

        Returns:
            lis t: Liste des lignes de données lues depuis la feuille de calcul.
        """
        try:
            service = self._get_sheets_service()
            result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
            rows = result.get('values', [])
            return rows
        except Exception as e:
            logger.error(f"Erreur lors de la lecture des données de la feuille : {e}")
            raise e

    def write_sheet_data(self, spreadsheet_id, range_name, values):
        """Écrit des données dans une feuille de calcul spécifiée.

        Args:
            spreadsheet_id (str): ID de la feuille de calcul.
            range_name (str): Nom de la plage de cellules où écrire les données.
            values (list): Liste des valeurs à écrire dans la feuille de calcul.

        Returns:
            dict: Résultat de l'opération d'écriture.
        """
        try:
            service = self._get_sheets_service()
            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption="RAW", body=body).execute()
            return result
        except Exception as e:
            logger.error(f"Erreur lors de l'écriture des données dans la feuille : {e}")
            raise e
