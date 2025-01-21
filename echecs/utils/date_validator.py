import re
from datetime import datetime


def is_valid_date(date_string):
    """Vérifie si une chaîne de caractères est bien formatée sous le format JJ/MM/AAAA et n'contient pas de lettres."""
    # Vérifier que la chaîne ne contient que des chiffres et des barres obliques
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", date_string):
        return False

    try:
        # Essayer de parser la date avec le format JJ/MM/AAAA
        print(datetime.strptime(date_string, "%d/%m/%Y"))

        # return True
        return False
    except ValueError:
        # Si une exception ValueError est levée, la date n'est pas valide
        return False
