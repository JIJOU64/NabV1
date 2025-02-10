from data.data_accessor import DataAccessor


from business.components.update_fields import UpdateFields


class ClientManagerAPI:
    """
    Gère l'ensemble des fonctionnalités pour la gestion des clients dans le système.
    """
    def __init__(self, choose_database):
        """Initialise le gestionnaire de clients avec les dépendances nécessaires.

        Args :
            choose_database : Base de données sélectionnée pour l'accès aux données.
        """
        self.data_accessor = DataAccessor(choose_database)
        self.update_fields = UpdateFields(self.data_accessor)

    @property
    def data_accessor(self):
        return self._data_accessor

    @data_accessor.setter
    def data_accessor(self, value):
        self._data_accessor = value

    @property
    def update_fields(self):
        return self._update_fields

    @update_fields.setter
    def update_fields(self, value):
        self._update_fields = value

    def manage_list_active_clients(self):
        """Gère la liste des clients actifs.

        Récupère la liste des clients actifs depuis la base de données et les gère
        en utilisant la méthode _manage_list.

        Args :
            selected_client : Client sélectionné pour gérer la liste active.
        """
        list_clients = self.data_accessor.fetch_active_clients()
        list_clients = list_clients
        return list_clients

    def manage_list_prospective_clients(self):
        list_clients = self.data_accessor.fetch_prospective_clients()
        list_clients = list_clients
        return list_clients

    def update_field(self, id_user, selected_client):
        """
        Met à jour tous les champs du client sélectionné en fonction
        des données récupérées par l'identifiant utilisateur.

        :param id_user: l'identifiant de l'utilisateur
        :param selected_client: objet du client sélectionné
        """
        self.update_fields.update_all_fields_by_id_user(id_user, selected_client)


