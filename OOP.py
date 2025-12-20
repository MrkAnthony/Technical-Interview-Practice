from typing import List, Any, Type


class Car:
    def __init__(self, name, categories, next_generation=None):
        self.name = name
        self.categories = categories
        self.is_purchased = False
        self.next_generation = next_generation


def get_model_lineage(starter_model):
    res = []

    current_model = starter_model

    while current_model:
        res.append(current_model.name)
        current_model = current_model.next_generation

    return res


'''
mustang_2024 = Car("Mustang 2024", ["sports", "coupe"])
mustang_2022 = Car("Mustang 2022", ["sports", "coupe"], mustang_2024)
mustang_2020 = Car("Mustang 2020", ["sports", "coupe"], mustang_2022)

mustang_2020_lineage = get_model_lineage(mustang_2020)
print(mustang_2020_lineage)

mustang_2022_lineage = get_model_lineage(mustang_2022)
print(mustang_2022_lineage)

mustang_2024_lineage = get_model_lineage(mustang_2024)
print(mustang_2024_lineage)
'''

from collections import defaultdict


class EventBooker:
    def __init__(self):
        self.booking = []
        self.global_bookings = []
        self.user_bookings = defaultdict(list)
        self.user_id = None

    def slot_check(self, slot: str) -> bool:
        if len(self.booking) >= 3:
            return False

        self.booking.append(slot)
        return True

    '''
    UNDERSTAND
    - Attempts to book a time interval [start, end) for the given user_id.
    - Return true if the book succceeds and False if it overlaps with an existing booking for any user
    PLAN
    - Append the users bookings and check if they fall in between the time interval
    - if another user falls in between that same time interval we will return False else we return True
    '''

    def book(self, user_id, start, end) -> bool:

        if start >= end:
            return False

        for s, e, user_id in self.global_bookings:
            if max(s, start) < min(e, end):
                return False

        self.global_bookings.append((start, end, user_id))
        self.user_bookings[user_id].append((start, end))
        return True


from datetime import datetime, date


class Counter:
    def __init__(self):
        self.count = 0
        self.decrement = 1
        self.history_count = {}

    def increment(self):
        self.count += 1
        return self.count

    def set_count(self, value: int):
        self.count = value

    def get_count(self):
        return self.count

    def decrement_count(self):
        self.count -= self.decrement
        return f"This has been decremented {self.count}"

    def reset(self):
        self.count = 0
        return f"{self.count} wiped completely"

    def count_history(self):
        now = date.today()
        self.history_count[now] = self.count
        return f"The history date {self.history_count.keys()} and count {self.history_count.values()}"


class ParkingLotManager:
    def __init__(self, capacity: int):
        self.global_parking = defaultdict(int)
        self.capacity = capacity

    '''
    Update your class so that:

    The same car_id cannot be parked twice at the same time.

    If park(car_id) is called for a car already parked, return False.

    If a car leaves, it should be allowed to park again.
    '''

    def park(self, car_id) -> bool:
        if self.capacity == 0:
            return False

        if len(self.global_parking) < self.capacity and self.global_parking[car_id] != 2:
            self.global_parking[car_id] += 1
            return True
        else:
            return False

    def leave(self, car_id) -> bool:
        if car_id in self.global_parking:
            self.global_parking[car_id] -= 1  # Indicating that the vehicle has left
            return True
        else:
            return False  # that vehicle wasn't found

    def get_parked(self):
        return tuple(self.global_parking.keys())


class Pokemon:
    def __init__(self, name, types, evolution=None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def __str__(self):
        return self.name

    def print_pokemon(self):
        print({
            "name": self.name,
            "types": self.types,
            "is_caught": self.is_caught
        })

    def caught_pokemon(self):
        self.is_caught = True

    def choose_pokemon(self):
        if self.is_caught is True:
            print(f"{self.name} I choose you")
        else:
            print(f"{self.name} is wild! Catch them if you can!")

    def add_type(self, types):
        self.types.append(types)


def get_by_type(collected_pokemon, pokemon_type):
    res = []
    for poke in collected_pokemon:
        if pokemon_type in poke.types:
            res.append(poke)
    return res


class Card:
    def __init__(self, suit, rank, next=None):
        self.suit = suit
        self.rank = rank
        self.next = next

    def print_card(self):
        print(f"{self.rank} of {self.suit}")

    def update_suit(self, string):
        self.suit = string

    def is_valid(self) -> bool:
        valid_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        if self.suit in valid_suits and self.rank in valid_ranks:
            return True
        else:
            return False

    def get_value(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

        if self.rank in ranks:
            return int(self.rank)
        elif self.rank == "Ace":
            return 1
        elif self.rank == "Jack":
            return 11
        elif self.rank == "Queen":
            return 12
        elif self.rank == "King":
            return 13
        else:
            return None


def print_hand(starting_card) -> list[str]:
    current_hand = starting_card
    res = []

    while current_hand:
        res.append(current_hand)
        current_hand = current_hand.next
    return res


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        if card not in self.cards:
            return False
        else:
            self.cards.remove(card)
            return True


def sum_hand(hand):
    total = 0
    for card in hand.cards:
        total += card.get_value()
    return total


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def add_first(head, new_node):
    current = head
    while current.head:
        current = new_node
        current = current.next
    return


node_1 = Node("Jigglypuff")
node_2 = Node("Wigglytuff")
node_1.next = node_2

from collections import defaultdict


class Player:
    def __init__(self, character, kart, outcomes):
        self.character = character
        self.kart = kart
        self.items = []
        self.outcomes = outcomes

    def get_tournament_place(self, opponents):
        if not opponents:
            return None

        avg_scores = defaultdict(float)
        user_avg = sum(self.outcomes) / len(self.outcomes)
        avg_scores[self.character] = user_avg

        for opponent in opponents:
            avg_opp = sum(self.outcomes) / len(self.outcomes)
            avg_scores[opponent.character] = avg_opp

        place = 1
        for character, score in avg_scores.items():
            if character == self.character:
                continue

            if score < avg_scores[self.character]:
                place += 1

        return place


player1 = Player("Mario", "Standard", [1, 2, 1, 1, 3])
player2 = Player("Luigi", "Standard", [2, 1, 3, 2, 2])
player3 = Player("Peach", "Standard", [3, 3, 2, 3, 1])

opponents = [player2, player3]
print(f"{player1.character} was number {player1.get_tournament_place(opponents)}")


class API:
    def __init__(self, debit):
        self.debit = debit
        
