from dealer import Dealer
from player import Player
from table import Table

class Game:
    def __init__(self):
        self.table = Table()
        self.dealer = Dealer(self.table)
        self.player = Player(init_cash=10000)

        while True:
            self.dealer.deal_hand()
            self.table.show_table()
            self.dealer.determine_scores(player_object=self.dealer)
            self.dealer.determine_scores(player_object=self.player)

            while not self.player.stand and not self.player.has_busted: # players turn
                self.player.player_choice(dealer = self.dealer)
                self.table.show_table()
                self.dealer.determine_scores(player_object=self.player)
            
            if not self.player.has_busted:
                while self.dealer.dealer_score[0] < 17 and self.dealer.dealer_score[1] < 17:
                    self.dealer.dealer_hit()
                    self.dealer.determine_scores(player_object=self.dealer)

            self.table.show_dealer_cards()
            self.dealer.determine_winner()

            self.game_reset()

    def game_reset(self):
        self.table.reset()
        self.player.reset()
        self.dealer.reset()
                
        
if __name__ == "__main__":
    game = Game()