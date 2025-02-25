from echecs.models.constant import TOURNAMENT_ROUNDS


class RoundView:

    @classmethod
    def display_round(cls, round):
        print(f"Round : {round.numero_round} : ")

        for index, match in enumerate(round.matches):
            print(f"\t Match {index + 1} : {match}")

        print(f"\n Résulat Round {round.numero_round}")

        route = cls.display_choices_round(round)
        return route

    def display_choices_round(round):

        for index, match in enumerate(round.matches):
            if not match.is_finished:
                print(f"\t {index+1}. Entrez le résultat du Match {index+1}")

            else:
                print(f"Résultat du Match {index+1} saisi")

        print(f"\n {TOURNAMENT_ROUNDS+1}. Revenir à la liste des tournois")

        print("\n Q. Quitter le programme")

        print("\n------------------------------------")

        while True:
            try:
                choice = input(f"Veuillez selectionner une option (1-{TOURNAMENT_ROUNDS+1} / Q) :")

                if choice == "q" or choice == "Q":
                    return "quit"

                elif int(choice) == TOURNAMENT_ROUNDS + 1:
                    return "home_tournament"

                elif 1 <= int(choice) <= TOURNAMENT_ROUNDS:
                    choice = int(choice)

                    if not round.matches[choice - 1].is_finished :
                        print("Entrer le résultat")
                        round.matches[choice - 1].score_player1 = int(input("Score Joueur 1 : "))
                    else:
                        print("Résultat déjà saisi")
                else:
                    raise ValueError

            except ValueError:
                print(
                    f"Erreur ! Veuillez selectionner une options entre (1-{TOURNAMENT_ROUNDS+1}) ou Q pour quitter: "
                )
