from echecs.views.general_view import GeneralView


class TournamentView:

    @staticmethod
    def display_home_tournament():
        GeneralView.display_header("        GESTION DES TOURNOIS")

        print("1. Créer un nouveau tournoi")
        print("2. Ajouter des tours à un tournoi existant")
        print("3. Afficher les rapports d’un tournoi")
        print("4. Retour au menu principal")

        print("------------------------------------")
        return input("Veuillez sélectionner une option (1-4) : ")
