import random

class Node:
    """
    A single node in a linked list, holding a value and a reference to the next node.
    """
    def __init__(self, value):
        self.value = [value]
        self.next = None
        self.consolidated = False

class LinkedList:
    """
    A basic singly-linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """Add a node with the given value to the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def __iter__(self):
        """Allow iteration over the list's values."""
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def __repr__(self):
        """String representation: e.g. LinkedList([1, 2, 3])"""
        values = list(self)
        return f"LinkedList({values})"

class Test:
    def __init__(self):
        ll = LinkedList()
        ll.append((3, 3))

        for node in ll:
            while not node.consolidated:
                card1, card2 = node.value
                if card1 == card2:
                    #chocie to split
                    print(f"values are the same {card1}, {card2}")
                    node.value = (card1, random.randint(1,10))
                    ll.append((card2, random.randint(1,10)))
                else:
                    node.consolidated = True
        
        for node in ll:
            print(node.value)

# Example usage:
if __name__ == "__main__":
    test = Test()