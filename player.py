import inspect
import sys

class Player:
    def __init__(self, init_cash = 10000):
        self.init_cash = init_cash
        self.player_score = [0,0]

    def player_choice(self, dealer, hand):
        acceptable_choices = []
        methods_raw = {name: func 
                       for name, func in inspect.getmembers(self, predicate=inspect.ismethod)
                       if name.startswith("_") and not name.startswith("__")}
        
        if hand.value[0][:-1] != hand.value[1][:-1] or len(hand) > 2: # drops _split if player hands are not matching
            methods_raw.pop("_split", None)

        methods = {i: func for i, (name, func) in enumerate(methods_raw.items(), start=1)}

        for i, method_name in enumerate(methods_raw, 1):
            print(f"{i}: {method_name}")
            acceptable_choices.append(i)
            
        choice = int(input("\nChoose a number: "))
        while choice not in acceptable_choices:
            choice = int(input("\nChoose between the numbers provided: "))

        methods[choice](dealer, hand)

    def _hit(self, dealer, hand):
        dealer.player_hit(hand)

    def _stand(self, dealer, hand):
        hand.stand = True
        hand.consolidated = True

    def _split(self, dealer, hand):
        dealer.table.split(dealer, hand)
        
    def _double_down(self, dealer, hand):
        dealer.player_hit()
        hand.stand = True
        hand.consolidated = True
        hand.has_doubled = True

    def _surrender(self, dealer, hand):
        hand.stand = True
        hand.consolidated = True
        hand.has_surrendered = True

    def _exit_game(self, dealer, hand):
        sys.exit()

    def reset(self):
        pass

if __name__ == "__main__":
    player = Player()