import re
from datetime import datetime, timedelta


def is_valid_date(date_string):
    """Vérifie si une chaîne de caractères est bien formatée sous le format JJ/MM/AAAA et n'contient pas de lettres."""

    try:
        # Vérifier que la chaîne ne contient que des chiffres et des barres obliques
        if not re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$", date_string):
            print(f"Erreur dans le format de la date : {date_string}, veuillez saisir une date au format JJ/MM/AAAA")

            return False

        return True
    except ValueError:
        # Si une exception ValueError est levée, la date n'est pas valide
        return False


def is_date_within_130_years(date):
    """Vérifie qu'une date n'a pas plus de 130 ans par rapport à la date du jour"""
    input_date = datetime.strptime(date, "%d/%m/%Y")

    current_date = datetime.now()
    max_age_date = current_date - timedelta(days=130 * 365)

    if input_date > max_age_date:
        return True
    else:
        print("Erreur : un joueur ne peut avoir plus de 130 ans !")
        return False


def is_date_not_before_today(date):
    """Vérifie si la date n'est pas inférieure à celle du jour"""

    input_date = datetime.strptime(date, "%d/%m/%Y")
    current_date = datetime.now()

    if input_date.date() >= current_date.date():
        return True
    else:
        print(f"Erreur : la date : {date} est inférieur à celle du jour")
        return False


def is_date_not_before(start_date, end_date):
    """Vérifie que start_date ne soit pas inférieur à end_date"""

    start_date = datetime.strptime(start_date, "%d/%m/%Y")
    end_date = datetime.strptime(end_date, "%d/%m/%Y")

    if end_date.date() >= start_date.date():
        return True
    else:
        print("Erreur : La date de fin est inférieure à celle du début !")
        return False
