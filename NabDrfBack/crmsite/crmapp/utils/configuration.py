# class permet l'acces aux éléments de configuration partagés par toute l'application
# Utilisation ici du pattern singleton

from configparser import ConfigParser

from .singleton import Singleton


class Configuration(metaclass=Singleton):

    def __init__(self):

        self._config_file_path = r"C:\Users\TURON\Desktop\JEROME\VivreDuCode\ProjetMeteoCss\ProjetMeteo\config.ini"
        self._web_port = 80  # changé dynamiquement à l'exécution car paramètres utilisateur, ici valeur par défaut
        self._web_root_url = "http://localhost"
        self._web_local_images_directory = (r"C:\Users\TURON\Desktop\JEROME\CrmProject2"
                                            r"\presentation\crm_display_fastAPI\views\ressources\images")
        self._web_local_css_directory = (r"C:\Users\TURON\Desktop\JEROME\CrmProject2"
                                         r"\presentation\crm_display_fastAPI\views\ressources\css")

    @property
    def web_port(self):
        '''
        NB : voir l'explication écrite dans le setter
        nous allons lire l'information dans un fichier de configuration, car le port tcp-ip pour le serveur web est définit par l'utilisateur
        dans l'application console, donc dans un espace mémoire partagée.

        Si nous voulons pouvoir connaître cette valeur, nous allons donc la cherché dans un fichier de configuration partagée.

        '''

        config_object = ConfigParser()
        config_object.read(self._config_file_path)
        web_port_config_section = config_object["WEB_PORT"]
        return web_port_config_section["port"]

    @web_port.setter
    def web_port(self, value):
        print(f"Configuration : définition du port pour le serveur web à {str(value)}")
        self._web_port = value

        '''
        Cette valeur est définit par l'utilisateur via la ligne de commande et permet l'exécution du serveur web uvicorn sur ce port

        Cependant le serveur web uvicorn va ensuite initialiser son propre espace d'exécution en initialisation FastAPI, ce qui va
        créer deux espaces mémoire :

        1) un espace mémoire Python pour l'application en mode console qui va initialiser le serveur web uvicorn
        2) un espace mémoire Python pour le serveur uvicorn lui-même

        La class Configuration, même si elle utilise la pattern Singleton peut être dans les deux espaces mémoires, lorsqu'elle sera
        utilisé par du code Python (sont dans l'espace mémoire 1 et/ou dans l'espace mémoire 2).

        Ainsi, si on définit des valeurs via la class configuration dans l'espace mémoire 1 (celui de l'application console), elles
        ne seront pas visible dans l'espace mémoire 2 (Python instancié par Uvicorn).

        C'est pourquoi nous allons échanger les informations de configuration nécessaire par un fichier de configuration.

        ainsi, peut importe l'espace mémoire dans lequel se trouver la class Configuration, elle pourra fournir les informations en
        se basant sur ce fichier.

        '''

        config_object = ConfigParser()
        config_object["WEB_PORT"] = {
            "port": str(value)
        }
        with open(self._config_file_path, 'w') as conf:
            config_object.write(conf)

    @property
    def web_url(self):
        return f"{self._web_root_url}:{self.web_port}"

    @property
    def web_local_images_directory(self):
        return self._web_local_images_directory

    @property
    def web_local_css_directory(self):
        return self._web_local_css_directory

    @property
    def web_url_images_directory(self):
        return f"{self.web_url}/images"

    @property
    def web_url_css_directory(self):
        return f"{self.web_url}/css"

    def get_instance(self):
        return self
