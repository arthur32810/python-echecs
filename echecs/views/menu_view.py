class MenuView:

    def __init__(self, choices):
        self.choices = choices
        self.max_option = len(choices)

    def display(self):
        """Affiche les choix du menu"""
        for index, choice in enumerate(self.choices):

            print(f"{index + 1}. {choice["text"]}")

        print("\nQ. Quitter le programme")

    def selected_choice(self):
        """Affiche le texte de choix et vérifie qu'il soit correct"""

        while True:
            try:
                choice = input(f"Veuillez selectionner une option (1-{self.max_option}) :")

                if choice == "q" or choice == "Q":
                    return "quit"
                elif 1 <= int(choice) <= self.max_option:
                    choice = int(choice)
                    return self.choices[choice - 1]["route"]
                else:
                    raise ValueError

            except ValueError:
                print(f"Erreur ! Veuillez selectionner une options entre (1-{self.max_option}) ou Q pour quitter: ")
