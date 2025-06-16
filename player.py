import inspect
import sys

class Player:
    def __init__(self, init_cash = 10000):
        self.init_cash = init_cash
        self.player_score = [0,0]
        self.has_busted = False
        self.stand = False

    def player_choice(self, dealer):
        acceptable_choices = []
        methods_raw = {name: func 
                       for name, func in inspect.getmembers(self, predicate=inspect.ismethod)
                       if name.startswith("_") and not name.startswith("__")}
        
        if dealer.table.player_hand[0][:-1] != dealer.table.player_hand[1][:-1]: # drops _split if player hands are not matching
            methods_raw.pop("_split", None)

        methods = {i: func for i, (name, func) in enumerate(methods_raw.items(), start=1)}

        for i, method_name in enumerate(methods_raw, 1):
            print(f"{i}: {method_name}")
            acceptable_choices.append(i)
            
        choice = int(input("\nChoose a number: "))
        while choice not in acceptable_choices:
            choice = int(input("\nChoose between the numbers provided: "))

        methods[choice](dealer)

    def _hit(self, dealer):
        dealer.player_hit()

    def _stand(self, dealer):
        self.stand = True

    def _split(self, dealer):
        print('split')

    def _double_down(self, dealer):
        dealer.player_hit()
        self.stand = True

    def _surrender(self, dealer):
        self.stand = True

    def _exit_game(self, dealer):
        sys.exit()

    def reset(self):
        self.has_busted = False
        self.stand = False

if __name__ == "__main__":
    player = Player()