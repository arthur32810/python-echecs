import re
from datetime import datetime, timedelta


def is_valid_date(date_string):
    """Vérifie si une chaîne de caractères est bien formatée sous le format JJ/MM/AAAA et n'contient pas de lettres."""

    try:
        # Vérifier que la chaîne ne contient que des chiffres et des barres obliques
        if not re.match(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$", date_string):
            print("Erreur dans le format de la date, veuillez saisir une date au format JJ/MM/AAAA")

            return False

        return True
    except ValueError:
        # Si une exception ValueError est levée, la date n'est pas valide
        return False


def is_valid_birthday(date):
    """Vérifie qu'une dtae n'a pas plus de 130 ans par rapport à la date du jour"""
    input_date = datetime.strptime(date, "%d/%m/%Y")

    current_date = datetime.now()
    max_age_date = current_date - timedelta(days=130 * 365)

    if input_date > max_age_date:
        return True
    else:
        print("Erreur : un joueur ne peut avoir plus de 130 ans !")
        return False
