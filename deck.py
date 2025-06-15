class Deck:
    def __init__(self, num_of_decks = 6):
        self.card_deck = []
        self.card_deck_reference = []
        self.items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        self.suites = {'clubs':'♣',
                       'diamonds':'♦',
                       'spades':'♠',
                       'hearts':'♥'}
        for i in range(num_of_decks):
            for value in self.suites.values():
                for item in self.items:
                    self.push(item + value)
        self.total_length = len(self.card_deck_reference)


    
    def push(self, item):
        """Adds an item to the top of the stack."""
        self.card_deck_reference.append(item)

    def pop(self):
        """Removes and returns the top item from the stack."""
        if not self.is_empty():
            return self.card_deck.pop()  # Use pop() to remove the last element (top of stack)
        else:
            print("Stack is empty. Cannot pop.")
            return None

    
    def size(self):
        return len(self.card_deck)

    
if __name__ == "__main__":
    deck = Deck()