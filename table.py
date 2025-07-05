class Node:
    def __init__(self, value):
        self.value = [value]
        self.next = None
        self.consolidated = False
        self.has_busted = False
        self.stand = False
        self.score = [0, 0]
        self.has_doubled = False
        self.has_surrendered = False
        self.blackjack = False

    def __len__(self):
        return len(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
    
    def new_hand(self, value, dealer):

        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        cur.next.value = [value, dealer.draw_card()]

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def append(self, value):
        if not self.head:
            new_node = Node(value)
            self.head = new_node
            return
        else:
            self.head.value.append(value)

    def __repr__(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return f"LinkedList({out})"


class Table:
    def __init__(self, player):
        self.player = player
        self.chips = {'1': 5,
                      '2': 25,
                      '3': 100,
                      '4': 500,
                      '5': 0}
        self.bet_size = 10
        self.dealer_hand = LinkedList()
        self.player_hand = LinkedList()
        self.round_results = []


    def reset(self):
        self.dealer_hand = LinkedList()
        self.player_hand = LinkedList()
        self.round_results = []

    def reset_bet_size(self):
        self.bet_size = 10

    def complete_bets(self):
        print(self.round_results)
        for item in self.round_results:
            if item['winner'] == 'Dealer':
                if item['has_doubled']:
                    self.player.cash -= self.bet_size * 2
                else:
                    self.player.cash -= self.bet_size
            elif item['winner'] == 'Player':
                if item['has_blackjack']:
                    self.player.cash += self.bet_size * 1.5
                elif item['has_doubled']:
                    self.player.cash += self.bet_size * 2
                else:
                    self.player.cash += self.bet_size
            elif item['winner'] == 'Surrender':
                self.player.cash -= self.bet_size // 2
            elif item['winner'] == 'Push':
                pass # no money gets taken out tie
    def initial_bets(self, strategy: object = None):
        print(f'Total Cash: {self.player.cash}')

        # This is just taking the original bet as of right now
        if strategy:
            self.bet_size = self.bet_size
            
        else:
            for key, chip in self.chips.items():
                print(f'{key}: {str(chip)}')
            print('6: reset back to minimum')
            bet = input('Please choose: ')
            while bet not in list(self.chips.keys()):
                if bet == '6':
                    break
                bet = input('Please choose correct: ')
            try:
                self.bet_size += self.chips[bet]
            except Exception:
                self.reset_bet_size()

            print(f"Current Bet Size: {self.bet_size}")
            print('-----------------------------------------------')

    def split(self, dealer, hand):
        card1, card2 = hand.value
        hand.value = [card1, dealer.draw_card()]
        self.player_hand.new_hand(card2, dealer)
    