import re


def is_valid_player_identifiant(player_identifiant):
    """Vérifie si l'indentifiant du joueur qui a été renseigné respecte le format :
    deux lettres suivi de cinq chiffres"""

    if not re.match(r"^[a-zA-Z]{2}\d{5}$", player_identifiant):
        return False

    return True
