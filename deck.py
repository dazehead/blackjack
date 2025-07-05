class Deck:
    def __init__(self, num_of_decks = 6, loaded=False):
        self.card_deck = []
        self.card_deck_reference = []
        self.items = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.loaded_items = ['A', 'A', '3', '4', 'A', 'Q', 'K', '8', '9']
        self.suites = {'clubs':'♣',
                       'diamonds':'♦',
                       'spades':'♠',
                       'hearts':'♥'}
        
        self.create_deck(num_of_decks, loaded)
        self.total_length = len(self.card_deck_reference)

    
    def push(self, item):
        """Adds an item to the top of the stack."""
        self.card_deck_reference.append(item)

    def pop(self):
        return self.card_deck.pop()  # Use pop() to remove the last element (top of stack)

    
    def size(self):
        return len(self.card_deck)
    
    def create_deck(self, num_of_decks, loaded):
        for i in range(num_of_decks):
            for value in self.suites.values():
                if loaded:
                    for item in self.loaded_items:
                        self.push(item + value)
                else:
                    for item in self.items:
                        self.push(item + value)

    def __repr__(self):
        deck_string = ' '.join(self.card_deck_reference)
        return deck_string

if __name__ == "__main__":
    deck = Deck(loaded=True)
    print(deck)