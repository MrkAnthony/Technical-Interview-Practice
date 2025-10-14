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


class Counter:
    def __init__(self):
        self.count = 0
        self.decrement = 1

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


practice = Counter()
practice.set_count(200)
print(practice.get_count())
print(practice.reset())
practice.set_count(205)
print(practice.decrement_count())
print(practice.increment())

