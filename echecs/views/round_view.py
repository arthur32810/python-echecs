from echecs.views.choices import Choices
from echecs.models.constant import TOURNAMENT_ROUNDS


class RoundView:

    @staticmethod
    def display_round(round):
        print(f"Round {round.numero_round} : ")

        for index, match in enumerate(round.matches):
            if not match.is_finished:
                print(f"\t Match {index + 1} : {match}")

            else:
                print(f"\t Match {index + 1} : {match} - Gagnant : {match.winner}")

    @staticmethod
    def display_select_result_round(round):
        print(f"\n Résulat Round {round.numero_round}")

        for index, match in enumerate(round.matches):
            if not match.is_finished:
                print(f"\t {index+1}. Entrez le résultat du Match {index+1}")

        print("H. Revenir à la liste des tournois")

        print("Q. Quitter le programme")

        print("\n------------------------------------")

    @staticmethod
    def prompt_for_round_result(round):

        while True:
            try:
                choice = input(f"Veuillez selectionner une option (1-{TOURNAMENT_ROUNDS} / H - Q) :")

                if choice == "q" or choice == "Q":
                    return "quit", None

                elif choice == "h" or choice == "H":
                    return Choices.SELECT_TOURNAMENT["route"] , None

                elif 1 <= int(choice) <= TOURNAMENT_ROUNDS:
                    choice = int(choice)

                    if not round.matches[choice - 1].is_finished :
                        return "select_winner", round.matches[choice - 1]
                        
                    else:
                        print("Résultat déjà saisi\n")
                else:
                    raise ValueError

            except ValueError:
                print(
                    f"Erreur ! Veuillez selectionner une options entre (1-{TOURNAMENT_ROUNDS+1}) ou Q pour quitter: "
                )

    @staticmethod
    def prompt_select_winner(match):
        while True:
            try:
                print("\nVeuillez selectionner le gagnant :")
                print(f"\n1. {match.player1}")
                print(f"2. {match.player2}")
                print("3. Match nul")

                choice = int(input("\nVotre choix : "))

                if int(choice) >= 1 and int(choice) <= 3:
                    return choice
                else:
                    raise ValueError
            
            except ValueError:
                print("Erreur ! Veuillez selectionner une option entre 1 et 3")