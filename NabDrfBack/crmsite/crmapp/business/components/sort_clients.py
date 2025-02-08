class SortClients:
    def __init__(self, choose_display, data_accessor):
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

    def sort_clients(self, list_clients_choose):
        """Trie et affiche la liste des clients choisis.

        Affiche la liste des clients avec leurs noms et IDs associés, permet à
        l'utilisateur de choisir un client par son numéro, et retourne l'ID de
        l'utilisateur choisi.

        Args :
            list_clients_choose (list) : Liste des clients à trier et afficher.

        Returns :
            int : ID de l'utilisateur choisi.
        """
        # Affiche la liste des clients triés
        self.display.print_message("Voici la liste des clients triés : ")
        i = 1
        for client in list_clients_choose:
            self.display.print_colored_message(f"{i}.",
                                               f" {client[0]} {client[1]} (pour info son id_user = {client[2]})")
            i += 1

        # Demande à l'utilisateur de choisir un client par numéro
        while True:
            try:
                user_input = int(self.display.prompt("Veuillez entrer le numéro du client choisi : "))
                if 1 <= user_input <= len(list_clients_choose):
                    self.display.print_message(f"Le client choisi est : {list_clients_choose[user_input-1][0]}"
                                               f" {list_clients_choose[user_input-1][1]} ")
                    return list_clients_choose[user_input - 1][2]  # return id_user choose
                else:
                    self.display.print_message(f"Veuillez entrer un nombre valide entre 1 et {len(list_clients_choose)}.")
            except ValueError:
                self.display.print_message("Veuillez entrer un nombre valide.")
