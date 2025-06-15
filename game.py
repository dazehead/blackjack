from dealer import Dealer
from player import Player
from table import Table

class Game:
    def __init__(self):
        self.table = Table()
        self.dealer = Dealer(self.table)
        self.player = Player(init_cash=10000)
        self.dealer.deal_hand()
    
    def hit(self):
        self.dealer.draw_card()

    def stand(self):
        pass

    def split(self):
        pass

    def double_down(self):
        pass

    def surrender(self):
        pass
                    
    
if __name__ == "__main__":
    game = Game()