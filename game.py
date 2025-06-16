from dealer import Dealer
from player import Player
from table import Table

class Game:
    def __init__(self):
        self.table = Table()
        self.dealer = Dealer(self.table)
        self.player = Player(init_cash=10000)

        while True:
            print('-----------------------------------------------------------')
            self.dealer.deal_hand()
            self.table.show_table()
            self.dealer.determine_scores(player_object=self.dealer)
            self.dealer.determine_scores(player_object=self.player)

            while not self.player.stand and not self.player.has_busted: # players turn
                self.player.player_choice(dealer = self.dealer)
                self.table.show_table()
                self.dealer.determine_scores(player_object=self.player)
            
            if not self.player.has_busted:
                dealer_loop = True
                loop_breaker = 0
                while dealer_loop:
                    dealer_loop = self.dealer.dealer_logic(self.player)
                    self.table.show_table(dealer_hidden=False)
                    loop_breaker += 1
                    if loop_breaker > 10:
                        dealer_loop = False

            self.dealer.determine_winner(self.player)

            self.game_reset()

    def game_reset(self):
        self.table.reset()
        self.player.reset()
        self.dealer.reset()
                
        
if __name__ == "__main__":
    game = Game()