import random
from deck import Deck

class Dealer:
    def __init__(self, table_object, perc_to_shuffle = 20):
        self.table = table_object
        self.deck = Deck(num_of_decks=1)
        self.perc_to_shuffle = perc_to_shuffle * .01
        self.shuffle()

    def determine_values(self):
        self.card_values = {'1': 1,
                            '2': 2,
                            '3': 3,
                            '4': 4,
                            '5': 5,
                            '6': 6,
                            '7': 7,
                            '8': 8,
                            '9': 9,
                            '10': 10,
                            'J': 10,
                            'Q': 10,
                            'K': 10,
                            'A': [1, 11]}
        
        for i in self.table.dealer_hand: #striping suites
            value = self.card_values[i[:-1]]
            print(value)
        
        for i in self.table.player_hand:
            value = self.card_values[i[:-1]]
            print(value)

    def shuffle(self):
        self.deck.card_deck = self.deck.card_deck_reference
        random.shuffle(self.deck.card_deck)

    def deal_hand(self):
        self.table.player_hand.append(self.draw_card())
        self.table.dealer_hand.append(self.draw_card())
        self.table.player_hand.append(self.draw_card())
        self.table.dealer_hand.append(self.draw_card())
        

    def draw_card(self):
        if self.to_shuffle():
            self.shuffle()
        return self.deck.pop()
    
    def to_shuffle(self):
        threshold = int(round(self.deck.total_length * self.perc_to_shuffle, 0))

        # print(f"total_length = {self.deck.total_length}")
        # print(f'percentage_to_shuffle = {self.perc_to_shuffle}')
        # print(f"threshold = {threshold}")
        # print(f"current_deck_length = {self.deck.size()}")

        if threshold >= self.deck.size():
            return True
        return False
           


if __name__ == "__main__":
    dealer = Dealer()
    print(dealer.deck.card_deck)