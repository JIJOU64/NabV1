from crmsite.crmapp.utils.configuration import Configuration


class LayoutHelper:

    @staticmethod
    def get_head_tags() -> str:
        #items = []
        #items.append(f"<link rel=\"stylesheet\" href=\"{Configuration().get_instance().web_url_images_directory}/styles.images\">")
        #items.append(f"<link rel=\"stylesheet\" href=\"{Configuration().get_instance().web_url_css_directory}/styles.css\">")
        #items.append("<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css\">")
        #items.append("<script defer src=\"https://use.fontawesome.com/releases/v6.1.1/js/all.js\"></script>")
        #return "".join(items)

        header_tags = f"<link rel=\"stylesheet\" href=\"{Configuration().get_instance().web_url_css_directory}/styles.css\">"
        header_tags += f"<link rel=\"stylesheet\" href=\"{Configuration().get_instance().web_url_images_directory}/images.css\">"
        header_tags += "<link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bulma@1.0.2/css/bulma.min.css\">"
        header_tags += '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">'

        return header_tags

    @staticmethod
    def get_header() -> str:
        items = []
        items.append("<header>")
        items.append("<nav class=\"navbar is-light\" role=\"navigation\" aria-label=\"main navigation\">")
        items.append("<div class=\"navbar-brand\">")
        items.append('<a class="navbar-item" href="#">')
        items.append('<img src="/images/LogoNabiha.png" alt="Logo" width="26" height="45">')
        items.append('</a>')
        items.append('<a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" '
                     'data-target="navbarBasic">')
        items.append('<span aria-hidden="true"></span><span aria-hidden="true"></span><span aria-hidden="true"></span>')
        items.append('</a>')
        items.append('</div>')

        items.append('<div id="navbarBasic" class="navbar-menu">')
        items.append('<div class="navbar-end">')
        items.append('<a class="navbar-item" href="home_tag.html">')

        items.append('<span class="icon"><i class="fas fa-home"></i></span><span>Accueil</span>')
        items.append('</a>')

        items.append('<a class="navbar-item" href="http://127.0.0.1:8000/MenuClient">')
        items.append('<span class="icon"><i class="fas fa-user"></i></span><span>Clients</span>')
        items.append('</a>')

        items.append('<a class="navbar-item" href="#bilans">')
        items.append('<span class="icon"><i class="fas fa-chart-line"></i></span>')
        items.append('<span>Bilans</span>')
        items.append('</a>')
        items.append('<a class="navbar-item" href="#documents">')
        items.append('<span class="icon"><i class="fas fa-folder"></i></span><span>Documents</span>')
        items.append('</a>')
        items.append('</div></div></nav></header>')

        return "".join(items)

    @staticmethod
    def get_footer() -> str:
        items = []
        items.append('<footer class="footer">')
        items.append('<div class="content has-text-centered">')
        items.append('<p><strong>Contactez-nous</strong> : '
                     '<a href="mailto:contact@votre-site.com">contact@votre-site.com</a></p>')
        items.append('<p><a href="#">Mentions légales</a> | <a href="#">Politique de confidentialité</a></p>')
        items.append('</div></footer>')

        return "".join(items)

    @staticmethod
    def get_home_section() -> str:
        items = []
        items.append('<section class="hero is-primary is-fullheight-with-navbar">')
        items.append('<div class="hero-body">')
        items.append('<div class="container has-text-centered">')
        items.append('<h1 class="title">Votre Univers Pro, Votre gestion Intuitive</h1>')
        items.append('<h2 class="subtitle has-text-light" >Application de Bureau et Mobile Personnalisée</h2>')
        items.append('</div></div></section>')

        return "".join(items)

    @staticmethod
    def get_customer_tab_section() -> str:
        items = []
        items.append('<section class="section">')
        items.append('<h1 class="title has-text-centered">Menu Client</h1>')
        items.append('<h2 class="subtitle has-text-centered">Que souhaitez-vous faire ?</h2>')
        items.append('<form action="http://127.0.0.1:8000/MenuClient/ListeClient" method="post">')
        items.append('<div class="field">')
        items.append('<label class="label">Choisissez une action :</label>')
        items.append('<div class="control">')
        items.append('<div class="select is-fullwidth">')
        items.append('<select name="user_choice_client">')
        items.append('<option value="2">Accéder à la liste de tous les clients</option>')
        items.append('<option value="3">Accéder à la liste des clients prospects</option>')
        items.append('</select></div></div></div>')
        items.append('<div class="field is-grouped is-grouped-centered">')
        items.append('<div class="control">')
        items.append('<button type="submit" class="button is-link">Accéder</button>')
        items.append('</div></div></form></div></section>')

        return "".join(items)

    @staticmethod
    def get_customer_choice_section(list_clients_choose) -> str:
        items = []
        items.append('<section class="section">')
        items.append('<div class="container">')
        items.append('<form action="http://127.0.0.1:8000/MenuClient/ListeClient/DonnéesClient" method="post">')
        items.append('<div class="field">')
        items.append('<label class="label">Veuillez choisir un client :</label>')
        items.append('<div class="control">')
        items.append('<div class="select is-fullwidth">')
        items.append('<select name="user_choice_data">')
        i = 1
        for client in list_clients_choose:
            items.append(f'<option value="{i}">{i} {client[0]} {client[1]} '
                         f'(pour info son id_user = {client[2]})</option>')
            i += 1
        items.append('</select>')
        items.append('</div></div></div>')
        items.append('<div class="field is-grouped is-grouped-centered">')
        items.append('<div class="control">')
        items.append('<button type="submit" class="button is-link">Accéder</button>')
        items.append('</div></div></form></div></section>')
        return "".join(items)

    @staticmethod
    def get_customer_data_section(selected_client) -> str:
        items = []
        items.append('<section class="section">')
        items.append('<div class="container">')
        items.append('<h1 class="title has-text-centered">Informations sur le client</h1>')
        items.append('<h2 class="subtitle has-text-centered">Détails du client sélectionné</h2>')
        items.append('<div class="columns is-multiline">')

        items.append('<div class="column is-half">')
        items.append('<div class="card">')
        items.append('<header class="card-header">')
        items.append('<p class="card-header-title">Informations Utilisateur</p>')
        items.append('</header>')
        items.append('<div class="card-content">')
        items.append('<div class="content">')
        user_profile = {
            "ID Utilisateur : ": selected_client.id_user,
            "Nom : ": selected_client.last_name,
            "Prénom : ": selected_client.first_name,
            "Numéro de téléphone : ": selected_client.phone_number,
            "Adresse : ": selected_client.address,
            "Email : ": selected_client.email,
            "Mot de passe :": selected_client.password,
            "ID Client Data : ": selected_client.id_client_clients_data
        }
        for cle, valeur in user_profile.items():
            items.append(f'<p><strong>{str(cle)}</strong>{str(valeur)}</p>')
        items.append('</div></div></div></div>')

        items.append('<div class="column is-half">')
        items.append('<div class="card">')
        items.append('<header class="card-header">')
        items.append('<p class="card-header-title">Informations Client</p>')
        items.append('</header>')
        items.append('<div class="card-content">')
        items.append('<div class="content">')
        client_field = selected_client.clients_data
        client_data = {
            "ID Client : ": client_field.id_client,
            "Date de creation du dossier : ": client_field.file_creation_date,
            "Date de fermeture du dossier : ": client_field.file_closing_date,
            "Pour info id_training_training_data : ": client_field.id_training_training_data,
            "Pour info id_progress_client_progress: ": client_field.id_progress_client_progress,
            "Avancement client : ": client_field.progress.name_progress
        }
        for cle, valeur in client_data.items():
            items.append(f'<p><strong>{str(cle)}</strong>{str(valeur)}</p>')
        items.append('</div></div></div></div>')

        items.append('<div class="column is-half">')
        items.append('<div class="card">')
        items.append('<header class="card-header">')
        items.append('<p class="card-header-title">Informations sur la formation</p>')
        items.append('</header>')
        items.append('<div class="card-content">')
        items.append('<div class="content">')
        training_field = selected_client.clients_data.training_data
        status_field = training_field.training_status
        title_field = training_field.training_title
        outline_field = training_field.training_outline
        training_data = {
            "Financement par CPF? : ": training_field.follow_edof,
            "Début du bilan :": training_field.start_session,
            "Fin du bilan : ": training_field.end_session,
            "Nombre d'heures :": training_field.number_hours,
            "Coût de la formation :": training_field.cost_assessment,
            "Nombre de stagiaires :": training_field.number_trainees,
            "Pour info id_status ": training_field.id_status_training_status,
            "Nom du status: ": status_field.status_name,
            "Pour info id_title: ": training_field.id_title_training_title,
            "Nom de la formation: ": title_field.title_name,
            "Pour info id_outline: ": training_field.id_outline_training_outline,
            "Mode de suivi ": outline_field.outline_name
        }
        for cle, valeur in training_data.items():
            items.append(f'<p><strong>{str(cle)}</strong>{str(valeur)}</p>')
        items.append('</div></div></div></div>')

        items.append('<div class="column is-half">')
        items.append('<div class="card">')
        items.append('<header class="card-header">')
        items.append('<p class="card-header-title">Données de suivi après formation</p>')
        items.append('</header>')
        items.append('<div class="card-content">')
        items.append('<div class="content">')
        follow_up_field = selected_client.clients_data.training_data.follow_up_after
        training_data = {
            "Fiche d'évaluation?:": follow_up_field.evaluation_sheet,
            "Date de prévu pour l'évaluation?:": follow_up_field.planned_date,
            "Date réelle pour l'évaluation?:": follow_up_field.actual_date,
            "Intervalle :": follow_up_field.followup_interval
        }
        for cle, valeur in training_data.items():
            items.append(f'<p><strong>{str(cle)}</strong>{str(valeur)}</p>')
        items.append('</div></div></div></div>')

        items.append('</div></section>')

        return "".join(items)





