from dealer import Dealer
from player import Player
from table import Table
from basic_strategy import BasicStrategy

class Game:
    def __init__(self, strategy=None, games_to_play = None):
        self.game_count = 0
        self.games_to_play = games_to_play
        self.player = Player(init_cash=10000, strategy=strategy)
        self.table = Table(self.player)
        self.dealer = Dealer(self.table)


        while True:
            print('-----------------------------------------------------------')
            self.table.initial_bets(strategy=strategy)
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

            self.game_count += 1
            if games_to_play:
                if games_to_play == self.game_count:
                    break
            self.game_reset()


    def game_reset(self):
        self.table.reset()
        self.dealer.reset()
    
    def player_turn(self, hand):
        if hand.score[1] == 21: # has blackjack
            hand.blackjack = True
            hand.stand = True
            hand.consolidated = True
        while not hand.stand and not hand.has_busted and not hand.has_surrendered: # players turn
            print(self.table.player_hand)
            self.player.player_choice(
                dealer = self.dealer, 
                hand=hand, 
                dealer_hand=self.table.dealer_hand.head)
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
    strategy = BasicStrategy()
    game = Game(strategy=strategy, games_to_play=1)