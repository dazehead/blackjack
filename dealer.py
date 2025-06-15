import random
from deck import Deck

class Dealer:
    def __init__(self, table_object, perc_to_shuffle = 20):
        self.table = table_object
        self.deck = Deck(num_of_decks=1)
        self.perc_to_shuffle = perc_to_shuffle * .01
        self.card_values = {'2': 2,
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
        self.dealer_score = [0,0]
        self.has_busted = False
        self.shuffle()

    def determine_scores(self, player_object):
        class_name = player_object.__class__.__name__.lower()
        setattr(player_object, f"{class_name}_score", [0,0])
        # print(class_name)

        for i in getattr(self.table, f"{class_name}_hand"):
            value = self.card_values[i[:-1]]
            if type(value) == list:
                getattr(player_object, f"{class_name}_score")[0] += value[0]
                getattr(player_object, f"{class_name}_score")[1] += value[1]
            else:
                getattr(player_object, f"{class_name}_score")[0] += value
                getattr(player_object, f"{class_name}_score")[1] += value

        if getattr(player_object, f"{class_name}_score")[0] > 21 and getattr(player_object, f"{class_name}_score")[1] > 21:
            player_object.has_busted = True
            print(f"has_busted : {player_object.has_busted}")
        print(getattr(player_object, f"{class_name}_score"))

    def shuffle(self):
        self.deck.card_deck = self.deck.card_deck_reference.copy()
        random.shuffle(self.deck.card_deck)

    def deal_hand(self):
        self.table.player_hand.append(self.draw_card())
        self.table.dealer_hand.append(self.draw_card())
        self.table.player_hand.append(self.draw_card())
        self.table.dealer_hand.append(self.draw_card())
    
    def player_hit(self):
        self.table.player_hand.append(self.draw_card())
    
    def dealer_hit(self):
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
        #print(f"current_deck_length = {self.deck.size()}")
        if threshold >= self.deck.size():
            return True
        return False
    
    def reset(self):
        self.has_busted = False

    def determine_winner(self, player_object):
        winner = ''
        if self.dealer_score[0] == self.dealer_score[1]:
            if player_object.player_score[0] == player_object.player_score[1]:
                if self.dealer_score[0] > player_object.player_score[0]:
                    print('DEALER IS THE WINNER')
                else:
                    print('PLAYER IS THE WINNER')
            else:
                if player_object.player_score[1] > 21:
                    if self.dealer_score[0] > player_object.player_score[0]:
                        print('DEALER IS THE WINNER')
                    else:
                        print('PLAYER IS THE WINNER')
                else:
                    if self.dealer_score[0] > player_object.player_score[1]:
                        print("DEALER IS THE WINNER")
                    else:
                        print('PLAYER IS THE WINNER')
        else:
            pass

        self.dealer_score
        player_object.player_score
           


if __name__ == "__main__":
    dealer = Dealer()
    print(dealer.deck.card_deck)