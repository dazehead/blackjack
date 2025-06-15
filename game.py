import inspect
from dealer import Dealer
from player import Player
from table import Table

class Game:
    def __init__(self):
        self.table = Table()
        self.dealer = Dealer(self.table)
        self.player = Player(init_cash=10000)
        self.dealer.deal_hand()
        self.table.show_table()
        self.dealer.determine_values()
        #self.player_choice()

    def player_choice(self):
        methods = [name for name, func in inspect.getmembers(self, predicate=inspect.ismethod) if name.startswith("_") and not name.startswith("__")]
        for i, method in enumerate(methods, 1):
            print(f"{i}: {method}")
        choice = int(input("\nChoose a number: "))


    def _hit(self):
        self.dealer.draw_card()

    def _stand(self):
        pass

    def _split(self):
        pass

    def _double_down(self):
        pass

    def _surrender(self):
        pass
                    
    
if __name__ == "__main__":
    game = Game()