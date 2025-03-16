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
    def display_message(message):
        """Affiche un message"""
        print(message)
        input("Appuyez sur Entrée pour continuer...")
