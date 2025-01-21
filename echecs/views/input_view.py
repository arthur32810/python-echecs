from echecs.utils.date_validator import is_valid_date
from echecs.utils.player_identifiant_validator import is_valid_player_identifiant


class InputView:

    @staticmethod
    def choice_enter_menu(max_option):
        """Affiche le texte de choix et vérifie qu'il soit correct"""
        choice = int(input(f"Veuillez selectionner une option (1-{max_option}) :"))

        while choice is None or not (1 <= choice <= int(max_option)):
            choice = int(input(f"Erreur ! Veuillez selectionner une options entre (1-{max_option}) : "))

        return choice

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
