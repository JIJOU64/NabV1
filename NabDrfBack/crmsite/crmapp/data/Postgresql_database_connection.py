import psycopg2
from data.Abstract_database_connection import AbstractDataBaseConnection
from utils.postgresql_constants import HOST, PORT, DATABASE, USER, PASSWORD


class PostgresqlDataBaseConnection(AbstractDataBaseConnection):
    """Implémente une connexion à une base de données PostgreSQL en héritant de AbstractDataBaseConnection."""
    def __init__(self):
        """Initialise une nouvelle instance de la connexion à la base de données PostgreSQL."""

        self._host = HOST
        self._database = DATABASE
        self._user = USER
        self._password = PASSWORD
        self._port = PORT
        self.connection = None

    def open(self):
        """Ouvre une nouvelle connexion à la base de données PostgreSQL."""
        if self.connection is None:
            self.connection = psycopg2.connect(
                host=self._host,
                database=self._database,
                user=self._user,
                password=self._password,
                port=self._port
            )
            print("Connection opened.")
        return self.connection

    def close(self):
        """Ferme la connexion à la base de données PostgreSQL."""
        if self.connection:
            self.connection.close()
            print("Connection closed.")

    def get_connection(self):
        """Retourne l'objet de connexion actuel à la base de données."""
        return self.connection

    def get_database_error(self):
        """Retourne l'erreur de base de données spécifique à psycopg2."""
        error = psycopg2.DatabaseError
        return error





