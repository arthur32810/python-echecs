from echecs.utils.date_validator import is_date_within_130_years, is_valid_date
from echecs.utils.player_identifiant_validator import is_valid_player_identifiant


class InputView:

    @staticmethod
    def get_birthday_input():
        """
        Génere un champ date avec le texte donné
        Vérifie si la date est correcte
        Retourne la date
        """

        while True:

            date = input("Date de naissance (JJ/MM/AAAA) : ")

            if is_valid_date(date) and is_date_within_130_years(date):
                return date

        # Un joueur ne peut avoir plus de 130 ans

    @staticmethod
    def get_date_input(text_input):
        """
        Génere un champ date avec le texte donné
        Vérifie si la date est correcte
        Retourne la date
        """
        date = input(text_input)
        while is_valid_date(date) is not True:
            print("Erreur dans le format de la date, veuillez saisir une date au format JJ/MM/AAAA")

            date = input(text_input)

        return date

    @staticmethod
    def get_integer_input(text_input):
        """
        Génére un champ int avec le texte donné
        Vérifie que ce soit bien un int
        Retourne le int
        """

        while True:
            try:
                user_input = int(input(text_input))
                return user_input

            except ValueError:
                print("Erreur : Veuillez entre un nombre entier valide.")

    @staticmethod
    def get_player_id_input():
        while True:
            player_id = input("Identifiant nationnal d'échecs : ")

            if is_valid_player_identifiant(player_id):
                return player_id
            else:
                print(
                    "Erreur dans le format de l'identifiant. Voilà le format attendu :"
                    " deux lettres et cinq chiffres (ex: AB12345)"
                )

    @staticmethod
    def get_required_input(text_input):
        """Génére un input avec le texte donné et vérifie qu'il soit rempli"""

        while True:

            user_input = input(text_input)
            if user_input:
                return user_input
            else:
                print("Erreur : Veuillez remplir ce champ !")

    @staticmethod
    def selected_choice(text_input, max_option):
        """Affiche le texte de choix et vérifie qu'il soit correct"""

        while True:
            try:
                choice = input(text_input)

                if 1 <= int(choice) <= max_option:
                    choice = int(choice)
                    return choice
                else:
                    raise ValueError

            except ValueError:
                print(f"Erreur ! Veuillez selectionner une options entre (1-{max_option}) ")
