"""
Ce module définit la classe UserProfile pour gérer les informations de profil utilisateur.
Il inclut des méthodes pour obtenir et mettre à jour les valeurs de profil.
"""
from business.entities.utils_entities import UtilsEntities
from business.entities.clients_data import ClientsData


class UserProfile:
    """
    Classe pour gérer les informations de profil utilisateur.
    """
    def __init__(self):
        """
        Initialise une nouvelle instance de UserProfile avec des valeurs par défaut.
        """
        self.id_user = -1
        self.last_name = None
        self.first_name = None
        self.phone_number = None
        self.address = None
        self.email = None
        self.password = None
        self.id_client_clients_data = None

        self.clients_data = ClientsData()
        self.utils_entities = UtilsEntities()

    # ------------------------------
    # property
    # ------------------------------

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        self._id_user = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def id_client_clients_data(self):
        """
        Retourne l'identifiant du client dans clients_data.
        """
        return self._id_client_clients_data

    @id_client_clients_data.setter
    def id_client_clients_data(self, value):
        """
        Définit l'identifiant du client dans clients_data.
        """
        self._id_client_clients_data = value

    @property
    def clients_data(self):
        """
        Retourne l'instance de ClientsData associée.
        """
        return self._clients_data

    @clients_data.setter
    def clients_data(self, value):
        """
        Définit l'instance de ClientsData associée.
        """
        self._clients_data = value

    def get_update_values(self):
        """
        Retourne une chaîne de caractères avec les valeurs du profil utilisateur formatées
        pour une mise à jour dans la base de donnée.
        Utilise la méthode format_value de UtilsEntities.

        :return: Chaîne de caractères des valeurs du profil utilisateur formatées
        """
        format_value = self.utils_entities.format_value
        update_values = [
            f"last_name = {format_value(self.last_name)}",
            f"first_name = {format_value(self.first_name)}",
            f"phone_number = {format_value(self.phone_number)}",
            f"address = {format_value(self.address)}",
            f"email = {format_value(self.email)}",
            f"password = {format_value(self.password)}",
            f"id_client_clients_data = {format_value(self.id_client_clients_data)}"
        ]
        return ", ".join(update_values)

    def update_values(self, all_fields_of_chosen_client):
        """
        Met à jour les valeurs du profil utilisateur en utilisant les données fournies.

        :param all_fields_of_chosen_client: liste contenant les nouvelles valeurs de profil
        """
        self.id_user = all_fields_of_chosen_client[0][0]
        self.last_name = all_fields_of_chosen_client[0][1]
        self.first_name = all_fields_of_chosen_client[0][2]
        self.phone_number = all_fields_of_chosen_client[0][3]
        self.address = all_fields_of_chosen_client[0][4]
        self.email = all_fields_of_chosen_client[0][5]
        self.password = all_fields_of_chosen_client[0][6]
        self.id_client_clients_data = all_fields_of_chosen_client[0][7]



