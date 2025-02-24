class RoundView:

    @staticmethod
    def display_round(round):
        print(f"Round : {round.numero_round} : ")

        for index, match in enumerate(round.matches):
            print(f"Match {index + 1} : {match}")
        pass
