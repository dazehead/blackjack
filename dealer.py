import random
from deck import Deck

class Dealer:
    def __init__(self, table_object=None, perc_to_shuffle = 20):
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
            #print(f"has_busted : {player_object.has_busted}")
        attr_name = f"{class_name}_score"
        print(f"{attr_name}: {getattr(player_object, attr_name)}")

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

        if threshold >= self.deck.size():
            return True
        return False
    
    def reset(self):
        self.has_busted = False

    def determine_winner(self, player_object):
        dealer_hard, dealer_soft = self.dealer_score
        player_hard, player_soft = player_object.player_score

        if self.has_busted:
            print('PLAYER IS THE WINNER - 1')
            return
        if player_object.has_busted:
            print('DEALER IS THE WINNER - 2')
            return
        
        if dealer_hard == dealer_soft:
            if player_hard == player_soft:
                if dealer_hard == player_hard:
                    print('PUSH - 3')
                    return
                elif dealer_hard > player_hard:
                    print('DEALER IS THE WINNER - 4')
                    return
                else:
                    print('PLAYER IS THE WINNER - 5')
                    return
            else:
                if player_soft > 21:
                    if dealer_hard == player_hard:
                        print('PUSH - 6')
                        return
                    elif dealer_hard > player_hard:
                        print('DEALER IS THE WINNER - 7')
                        return
                    else:
                        print('PLAYER IS THE WINNER - 8')
                        return
                else:
                    if dealer_hard == player_soft:
                        print('PUSH - 9')
                        return
                    elif dealer_hard > player_soft:
                        print("DEALER IS THE WINNER - 10")
                        return
                    else:
                        print('PLAYER IS THE WINNER - 11')
                        return
        # Presence of an ACE
        else:
            if player_hard == player_soft:
                # only an ace in the dealers score
                if dealer_soft > 21:
                    if dealer_hard == player_hard:
                        print("PUSH - 12")
                        return
                    elif dealer_hard > player_hard:
                        print('DEALER IS THE WINNER - 13')
                        return
                    else:
                        print('PLAYER IS THE WINNER - 14')
                        return
                else:
                    if dealer_soft == player_hard:
                        print("PUSH - 15")
                        return
                    elif dealer_soft > player_hard:
                        print('DEALER IS THE WINNER - 16')
                        return
                    else:
                        print('PLAYER IS THE WINNER - 17')
                        return
            else:
                if player_soft > 21:
                    if dealer_hard == player_hard:
                        print("PUSH - 18")
                        return
                    elif dealer_hard > player_hard:
                        print('DEALER IS THE WINNER - 19')
                        return
                    else:
                        print('PLAYER IS THE WINNER - 20')
                        return
                else:
                    if dealer_hard == player_soft:
                        print("PUSH - 21")
                        return
                    elif dealer_hard > player_soft:
                        print("DEALER IS THE WINNER - 22")
                        return
                    else:
                        print('PLAYER IS THE WINNER - 23')  
                        return       

    def dealer_logic(self, player_object):
        hard, soft = self.dealer_score               # [0] = Ace as 1 (“hard”), [1] = Ace as 11 (“soft”)
        player_hard, player_soft = player_object.player_score

        # 0) If dealer busts on BOTH counts, stop immediately
        if hard > 21:
            print("Dealer busts!")
            return False

        # 1) Soft-17 rule: if there’s an ace (hard != soft) and soft == 17 → hit
        if hard != soft and soft == 17:
            self.dealer_hit()
            self.determine_scores(self)
            return True

        # 2) If there’s an ace and 18 ≤ soft ≤ 21 → stand
        if hard != soft and 18 <= soft <= 21:
            print("Dealer stands (soft 18–21)")
            return False

        # 3) If soft is busted (>21) but hard < 17 → hit
        if soft > 21 and hard < 17:
            self.dealer_hit()
            self.determine_scores(self)
            return True

        # 4) If hard < 17 → hit
        if hard < 17:
            self.dealer_hit()
            self.determine_scores(self)
            return True

        # 5) If dealer’s hard-score beats player’s hard (and ≤21) → stand
        if hard > player_hard and hard <= 21:
            print("Dealer stands (hard beats player)")
            return False

        # 6) If there’s an ace and dealer’s soft-score beats player’s soft (and ≤21) → stand
        if hard != soft and soft > player_soft and soft <= 21:
            print("Dealer stands (soft beats player)")
            return False

        # 7) Fallback: stand
        print("Dealer stands (default)")
        return False



if __name__ == "__main__":
    dealer = Dealer()
    print(dealer.deck.card_deck)