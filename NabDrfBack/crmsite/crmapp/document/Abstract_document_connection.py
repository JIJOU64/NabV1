from abc import ABC, abstractmethod

class AbstractDocumentConnection(ABC):
    @abstractmethod
    def get_folder_contents_by_folder_id(self, folder_id):
        """Méthode abstraite pour récupérer le contenu d'un dossier par son ID.

        Args:
            folder_id (str): ID du dossier à récupérer.

        Returns:
            list: Liste des fichiers et dossiers contenus dans le dossier spécifié.
        """
        pass

    @abstractmethod
    def read_sheet_data(self, spreadsheet_id, range_name):
        """Méthode abstraite pour lire les données depuis une feuille de calcul.

        Args:
            spreadsheet_id (str): ID de la feuille de calcul.
            range_name (str): Plage de cellules à lire.

        Returns:
            list: Liste des lignes de données lues depuis la feuille de calcul.
        """
        pass

    @abstractmethod
    def write_sheet_data(self, spreadsheet_id, range_name, result_bilan):
        """Méthode abstraite pour écrire des données dans une feuille de calcul.

        Args:
            spreadsheet_id (str): ID de la feuille de calcul.
            range_name (str): Plage de cellules où écrire les données.
            result_bilan (list): Données à écrire dans la feuille de calcul.

        Returns:
            dict: Résultat de l'opération d'écriture.
        """
        pass

