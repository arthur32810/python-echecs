class MenuView:

    def __init__(self, choices):
        self.choices = choices
        self.max_option = len(choices)

    def display(self):
        for index, choice in enumerate(self.choices):

            print(f"{index + 1}. {choice["text"]}")

        print("\nq. Quitter le programme")

    def selected_choice(self):
        """Affiche le texte de choix et vérifie qu'il soit correct"""
        choice = int(input(f"Veuillez selectionner une option (1-{self.max_option}) :"))

        while choice is None or not (1 <= choice <= self.max_option) or not "q":
            choice = int(
                input(f"Erreur ! Veuillez selectionner une options entre (1-{self.max_option}) ou q pour quitter: ")
            )

        if choice == "q":
            return "quit"

        return self.choices[choice - 1]["route"]
