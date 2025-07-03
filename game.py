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
            self.table.initial_bets()
            self.dealer.deal_hand()
            
            print(self.table.dealer_hand)
            print(self.table.player_hand)

            self.dealer.determine_scores(player_object=self.dealer)
            self.dealer.determine_scores(player_object=self.player)
            for hand in self.table.player_hand:
                while not hand.consolidated:
                    self.player_turn(hand)

            self.dealer_turn()

            for hand in self.table.player_hand:
                self.dealer.determine_winner(hand)

            print(self.table.dealer_hand)
            print(self.table.player_hand)
            self.table.complete_bets()

            self.game_reset()


    def game_reset(self):
        self.table.reset()
        self.player.reset()
        self.dealer.reset()
    
    def player_turn(self, hand):
        while not hand.stand and not hand.has_busted: # players turn
            print(self.table.player_hand)
            self.player.player_choice(dealer = self.dealer, hand=hand)
            self.dealer.determine_scores(player_object=self.player)
            print('------------------------------------')

                
    def dealer_turn(self):
        for hand in self.table.player_hand:
            if not hand.has_busted:
                dealer_loop = True
                loop_breaker = 0
                while dealer_loop:
                    dealer_loop = self.dealer.dealer_logic(self.player)
                    loop_breaker += 1
                    if loop_breaker > 10:
                        dealer_loop = False  

if __name__ == "__main__":
    game = Game()