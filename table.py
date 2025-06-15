class Table:
    def __init__(self):
        self.dealer_hand = []
        self.player_hand = []

    def reset(self):
        self.dealer_hand = []
        self.player_hand = []
    
    def show_table(self):
        self.dealer_hidden = self.dealer_hand
        self.dealer_hidden = ['Hidden', self.dealer_hand[1]]
        print(self.dealer_hidden)
        print(self.player_hand)
        print('\n')

    def show_dealer_cards(self):
        print(self.dealer_hand)
        print(self.player_hand)
        print('\n')

    