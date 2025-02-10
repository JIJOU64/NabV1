from .Abstract_database_connection import AbstractDataBaseConnection


class DataAccessor:
    def __init__(self, connection: AbstractDataBaseConnection):
        """
        Initialise une instance de DataAccessor avec une connexion à la base de données.

        Args:
            connection (AbstractDataBaseConnection): Connexion à la base de données.
        """
        self.connection = connection

    # ESSAI CONNECTION
    def connect(self):
        """
        Tente d'établir une connexion à la base de données et affiche la version du serveur PostgreSQL.
        """
        conn = None
        try:
            # obtention de la connexion à la base de données
            conn = self.connection.open()
            cursor = self.connection.get_connection().cursor()
            print('Version du serveur PostgreSQL:')
            cursor.execute('SELECT version()')
            db_version = cursor.fetchone()
            print(db_version)
        except (Exception, self.connection.get_database_error()) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('connection à la base de données fermée')

    # CREATE
    def create_new_id(self, table_name, id_column):
        """
        Crée un nouvel ID unique pour une table spécifiée.

        Args:
            table_name (str): Nom de la table où insérer l'ID.
            id_column (str): Nom de la colonne ID à retourner.

        Returns:
            int: Nouvel ID créé.
        """
        sql = f"INSERT INTO {table_name} DEFAULT VALUES RETURNING {id_column};"
        try:
            result = self._fetch_data_by_sql_query(sql)
            # Convertir le résultat en une valeur unique
            if result and isinstance(result[0], tuple):
                return result[0][0]
            return result[0] if result else None
        except IndexError:
            print(f"Erreur lors de la récupération de l'ID depuis {table_name}.")
            return

    # READ
    def _fetch_data_by_sql_query(self, sql):
        """
        Exécute une requête SQL et récupère les résultats.

        Args:
            sql (str): Requête SQL à exécuter.

        Returns:
            list: Résultats de la requête SQL.
        """
        try:
            with self.connection.open() as conn:
                cursor = conn.cursor()
                cursor.execute(sql)
                rows = cursor.fetchall()
                conn.commit()
                return rows
        except (Exception, self.connection.get_database_error()) as error:
            print("Error in _fetch_data_by_sql_query:")
            print(error)
            raise

    def _fetch_id_and_name_from_table(self, table, id_column, name_column):
        """
        Récupère les ID et noms à partir d'une table spécifiée.

        Args:
            table (str): Nom de la table à interroger.
            id_column (str): Nom de la colonne ID.
            name_column (str): Nom de la colonne nom.

        Returns:
            list: Résultats contenant les ID et noms.
        """
        sql = f"SELECT {id_column}, {name_column} FROM {table};"
        try:
            result = self._fetch_data_by_sql_query(sql)
            return result if result else None
        except IndexError:
            print(f"Erreur lors de la récupération des données depuis la table {table}.")
            return None

    def fetch_data_client_progress(self):
        """
        Récupère les données (ID et noms) depuis la table client_progress.

        Returns:
            list: Résultats contenant les ID et noms depuis la table client_progress.
        """
        return self._fetch_id_and_name_from_table("client_progress",
                                                  "id_progress",
                                                  "name_progress")

    def fetch_data_training_status(self):
        return self._fetch_id_and_name_from_table("training_status",
                                                  "id_status",
                                                  "status_name")

    def fetch_data_training_title(self):
        return self._fetch_id_and_name_from_table("training_title",
                                                  "id_title",
                                                  "title_name")

    def fetch_data_training_outline(self):
        return self._fetch_id_and_name_from_table("training_outline",
                                                  "id_outline",
                                                  "outline_name")

    def _fetch_clients_by_condition_from_id_progress(self, condition):
        """
        Récupère les clients en fonction d'une condition donnée sur l'ID d'avancement du client.

        Args:
            condition (str): Condition SQL pour filtrer les clients.

        Returns:
            list: Résultats contenant les noms, prénoms et ID utilisateur des clients.
        """
        sql = (f"SELECT last_name, first_name, id_user FROM user_profile "
               f"JOIN clients_data "
               f"ON user_profile.id_client_clients_data = clients_data.id_client "
               f"WHERE {condition} ORDER BY last_name, first_name;")
        try:
            result = self._fetch_data_by_sql_query(sql)
            return result if result else None
        except IndexError:
            print(f"Erreur lors de la récupération des données.")
            return None

    def fetch_active_clients(self):  # without archived clients
        """
        Récupère les clients actifs (non archivés).

        Returns:
            list: Résultats contenant les noms, prénoms et ID utilisateur des clients actifs.
        """
        condition = "clients_data.id_progress_client_progress <> '4'"
        return self._fetch_clients_by_condition_from_id_progress(condition)

    def fetch_prospective_clients(self):
        """
        Récupère les clients potentiels (prospects).

        Returns:
            list: Résultats contenant les noms, prénoms et ID utilisateur des clients potentiels.
        """
        condition = "clients_data.id_progress_client_progress = '1'"
        return self._fetch_clients_by_condition_from_id_progress(condition)

    def fetch_training_clients(self):
        condition = "clients_data.id_progress_client_progress = '2'"
        return self._fetch_clients_by_condition_from_id_progress(condition)

    def fetch_followup_clients(self):
        condition = "clients_data.id_progress_client_progress = '3'"
        return self._fetch_clients_by_condition_from_id_progress(condition)

    def fetch_archive_clients(self):
        condition = "clients_data.id_progress_client_progress = '4'"
        return self._fetch_clients_by_condition_from_id_progress(condition)

    def fetch_all_fields_by_id_user(self, id_user):
        """
        Récupère tous les champs associés à un ID utilisateur donné.

        Args:
            id_user (int): ID utilisateur pour lequel récupérer les champs.

        Returns:
            list: Résultats contenant tous les champs associés à l'ID utilisateur spécifié.
        """
        sql = (
            f"SELECT "
            f"    up.id_user, "
            f"    up.last_name, "
            f"    up.first_name, "
            f"    up.phone_number, "
            f"    up.address, "
            f"    up.email, "
            f"    up.password, "
            f"    cd.id_client, "
            f"    cd.file_creation_date, "
            f"    cd.file_closing_date, "
            f"    cd.id_progress_client_progress, "
            f"    cd.id_training_training_data, "
            f"    td.id_training, "
            f"    td.follow_edof, "
            f"    td.start_session, "
            f"    td.end_session, "
            f"    td.number_hours, "
            f"    td.cost_assessment, "
            f"    td.number_trainees, "
            f"    td.id_status_training_status, "
            f"    td.id_title_training_title, "
            f"    td.id_outline_training_outline, "
            f"    fua.id_followup, "
            f"    fua.evaluation_sheet, "
            f"    fua.planned_date, "
            f"    fua.actual_date, "
            f"    fua.followup_interval "
            f"FROM "
            f"    user_profile up "
            f"JOIN "
            f"    clients_data cd ON up.id_client_clients_data = cd.id_client "
            f"LEFT JOIN "
            f"    training_data td ON cd.id_training_training_data = td.id_training "
            f"LEFT JOIN "
            f"    follow_up_after fua ON td.id_training = fua.id_training_training_data "
            f"WHERE "
            f"    up.id_user = {id_user}"
        )

        try:
            result = self._fetch_data_by_sql_query(sql)
            return result if result else None
        except IndexError:
            print("Erreur lors de la récupération des données.")
            return None

    def fetch_data_current_customer_balance(self):
        """Récupère les informations de solde des clients actuels."""
        sql = ("SELECT up.last_name,"
               " up.first_name,"
               " td.number_hours,"
               " td.cost_assessment "
               "FROM public.user_profile up "
               "JOIN public.clients_data cd "
               "ON up.id_client_clients_data = cd.id_client "
               "JOIN public.training_data td "
               "ON cd.id_training_training_data = td.id_training "
               "WHERE cd.id_progress_client_progress = 2;")

        try:
            result = self._fetch_data_by_sql_query(sql)
            # Conversion du résultat au format souhaité
            if result:
                values = [list(row) for row in result]
                return values
            else:
                return None
        except IndexError:
            print("Erreur lors de la récupération des données.")
            return None

    # UPDATE

    def update_data_table_by_id(self, table, values_to_update, name_id_table, id_table):
        """Met à jour les champs d'une table spécifiée en fonction d'un ID spécifié."""
        sql_update = (f"UPDATE {table} "
                      f"SET {values_to_update} "
                      f"WHERE {name_id_table} = %s;")
        try:
            with self.connection.open() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(sql_update, (id_table,))
                    conn.commit()
                    print(f"Les nouveaux champs ont été modifiés selon l'id de la table {table} choisie")
        except (Exception, self.connection.get_database_error()) as error:
            print("Erreur lors de l'enregistrement des nouveaux champs")
            print(error)

    # DELETE






