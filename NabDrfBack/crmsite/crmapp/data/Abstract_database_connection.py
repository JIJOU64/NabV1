from abc import ABC, abstractmethod


class AbstractDataBaseConnection(ABC):
    @abstractmethod
    def open(self):
        """Ouvre une connexion à la base de données."""
        pass

    @abstractmethod
    def close(self):
        """Ferme la connexion à la base de données."""
        pass

    @abstractmethod
    def get_connection(self):
        """Retourne l'objet de connexion."""
        pass

    @abstractmethod
    def get_database_error(self):
        """Retourne l'exception spécifique à la base de données."""
        pass

