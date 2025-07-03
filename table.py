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
    def __init__(self):
        self.dealer_hand = LinkedList()
        self.player_hand = LinkedList()
        self.round_results = []

    def reset(self):
        self.dealer_hand = LinkedList()
        self.player_hand = LinkedList()
        self.round_results = []

    def complete_bets(self):
        print(self.round_results)

    def initial_bets(self):
        print('start initial betting')

    def split(self, dealer, hand):
        card1, card2 = hand.value
        hand.value = [card1, dealer.draw_card()]
        self.player_hand.new_hand(card2, dealer)
        # hand.next.value = [card2, dealer.draw_card()]
        
    