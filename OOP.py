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




def test_leave_method_basic_removal():
    print("Running: test_leave_method_basic_removal")
    manager = ParkingLotManager(3)
    try:
        assert manager.park(1)
        assert manager.park(2)
        assert manager.park(3)
        assert manager.leave(2)
        parked = set(manager.get_parked())
        assert parked == {1, 3}, f"Expected {{1,3}}, got {parked}"
        print("✅ PASSED\n")
    except AssertionError as e:
        print(f"❌ FAILED: {e}\n")


def test_leave_method_car_not_present():
    print("Running: test_leave_method_car_not_present")
    manager = ParkingLotManager(3)
    try:
        manager.park(10)
        manager.park(11)
        assert not manager.leave(99)
        parked = set(manager.get_parked())
        assert parked == {10, 11}
        print("✅ PASSED\n")
    except AssertionError as e:
        print(f"❌ FAILED: {e}\n")


def test_leave_method_double_leave():
    print("Running: test_leave_method_double_leave")
    manager = ParkingLotManager(3)
    try:
        manager.park(42)
        assert manager.leave(42)
        assert not manager.leave(42)
        assert set(manager.get_parked()) == set()
        print("✅ PASSED\n")
    except AssertionError as e:
        print(f"❌ FAILED: {e}\n")


def test_leave_method_empty_lot():
    print("Running: test_leave_method_empty_lot")
    manager = ParkingLotManager(2)
    try:
        assert not manager.leave(5)
        assert manager.get_parked() == [] or set(manager.get_parked()) == set()
        print("✅ PASSED\n")
    except AssertionError as e:
        print(f"❌ FAILED: {e}\n")


def test_leave_method_mixed_sequence():
    print("Running: test_leave_method_mixed_sequence")
    manager = ParkingLotManager(3)
    try:
        assert manager.park(10)
        assert manager.park(11)
        assert manager.park(12)
        assert manager.leave(11)
        assert manager.park(13)
        assert not manager.leave(15)
        assert manager.leave(10)
        parked = set(manager.get_parked())
        assert parked == {12, 13}, f"Expected {{12,13}}, got {parked}"
        print("✅ PASSED\n")
    except AssertionError as e:
        print(f"❌ FAILED: {e}\n")


def run_all_leave_tests():
    test_leave_method_basic_removal()
    test_leave_method_car_not_present()
    test_leave_method_double_leave()
    test_leave_method_empty_lot()
    test_leave_method_mixed_sequence()


# Run all tests
run_all_leave_tests()

