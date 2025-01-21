class GeneralView:

    @staticmethod
    def display_header(title):
        """Formate l'affichage de l'entête en fonction d'un titre donné"""

        print("====================================")
        print(title)
        print("====================================")

    @staticmethod
    def display_success_message(entity_name):
        """Affiche un message"""
        print(f"[Nouveau {entity_name} ajouté avec succès !]")
        input("Appuyez sur Entrée pour continuer...")

    @staticmethod
    def choice_enter_menu(max_option):
        """Affiche le texte de choix et vérifie qu'il soit correct"""
        choice = int(input(f"Veuillez selectionner une option (1-{max_option}) :"))

        while choice is None or not (1 <= choice <= int(max_option)):
            choice = int(input(f"Erreur ! Veuillez selectionner une options entre (1-{max_option}) : "))

        return choice
