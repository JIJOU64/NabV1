"""
Ce module définit la classe UtilsEntities avec des méthodes utilitaires pour formater les valeurs et les dates.
"""
import datetime


class UtilsEntities:
    @staticmethod
    def format_value(value):
        """
        Formate une valeur pour l'inclure dans une requête SQL.

        :param value: La valeur à formater
        :return: La valeur formatée en tant que chaîne de caractères ou "NULL" si la valeur est None
        """
        return f"'{value}'" if value is not None else "NULL"

    @staticmethod
    def formatted_date(date):
        """
        Formate un objet de date en une chaîne de caractères 'jj/mm/aaaa'.

        :param date: La date à formater
        :return: La date formatée en tant que chaîne de caractères ou None si l'entrée n'est pas une date
        """
        if isinstance(date, datetime.date):
            return date.strftime('%d/%m/%Y')
        return None
