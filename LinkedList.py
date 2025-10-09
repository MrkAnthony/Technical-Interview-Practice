
class Card():
    def __init__(self, suit, rank, next = None):
        self.suit = suit
        self.rank = rank
        self.next = next

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def is_valid(self):
        suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
        rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        if self.suit in suit and self.rank in rank:
            return True
        else:
            return False

    def get_value(self):
        rank = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        try:
            return int(self.rank)
        except ValueError:
            if self.rank == "Ace":
                return 1
            elif self.rank == "Jack":
                return 11
            elif self.rank == "Queen":
                return 12
            elif self.rank == "King":
                return 13
            else:
                return None

    def __repr__(self):
        return f"card_{self.rank.lower()}" if self.rank.isdigit() else f"card_{self.rank.lower()}"


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        print(f"added cards to hand: {card.rank} of {card.suit}")

    def remove_card(self, card):
        self.cards.remove(card)
        print(f"Removed card from hand: {card.rank} of {card.suit}")


def sum_hand(hand):
    total = 0
    for card in hand.cards:
        if not card.is_valid():
            return None
        card_value = card.get_value()  # Call the method on the card instance
        total += card_value
    return total


def print_hand(starting_card):
    head = starting_card
    result = []
    while head:
        result.append(head)
        head = head.next

    return result

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked(head):
    current_node = head
    result = []
    while current_node:
        result.append(current_node.value)
        current_node = current_node.next

    return result


'''
Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

It should insert new_node as the new head of the linked_list. The function returns new_node.
'''

def add_first(head, new_node):
    new_node.next = head
    return new_node
'''
Write a function get_tail() that takes in the head of a linked list as a parameter.

It should print out the value of the tail of the list.

If the list is empty (head is None), return None.
'''
def get_tail(head):
    current_node = head
    while current_node:
        if current_node.next is None:
            return current_node.value
        current_node = current_node.next


'''
Using the Node class, write a function ll_replace() that takes a head of a linked list 
and two values, original and replacement as parameters.

The function updates any node with value original to have value replacement

Original
# initial linked list: 5 -> 6 -> 5
Replacement
# updated linked list: "banana" -> 6 -> "banana"
'''
def ll_replace(head, original, replacement):
    current_node = head
    while current_node:
        if current_node.value == original:
            current_node.value = replacement
        current_node = current_node.next


'''
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.
The function returns a list of values of the first n nodes.
- If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.

# linked list: a -> b -> c
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)
'''
#stonycodes

def listify_first_n(head, n):
    lst = []
    current_node = head
    count = 0
    while current_node:
        lst.append(current_node.value)
        count += 1
        current_node = current_node.next
        if count == n:
            break
    return lst

def ll_insert(head, val, i):
    pass


# linked list: a -> b -> c
head = Node("a")
node_2 = Node("b")
node_3 = Node("c")
head.next = node_2
node_2.next = node_3
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l
head2 = Node("J")
another_node1 = Node("K")
another_node2 = Node("L")

head2.next = another_node1
another_node1.next = another_node2
lst2 = listify_first_n(head2,5)
print(lst2)

'''
UNDERSTAND: 
write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0
and print out "<Opponent name> fainted>.

Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".
'''
class Pokemon():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp # hit points
        self.damage = damage # The amount of damage this Pokemon does to its opponent every attack

    def attack(self, opponent):
        self.hp -= self.damage

        if self.hp <= 0:
            self.hp = 0
            print(f"{opponent.name} has bit the dust")
        else:
            print(f"{self.name} dealt {self.damage} to {opponent.name}")


# pikachu = Pokemon("Pikachu", 35, 20)
# bulbasaur = Pokemon("Bulbasaur", 45, 30)

# opponent = bulbasaur
# pikachu.attack(opponent)