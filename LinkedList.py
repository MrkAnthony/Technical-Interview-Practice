from typing import Optional


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node, name="List"):
    values = []
    current = node
    while current:
        values.append(str(current.val))
        current = current.next
    print(f"{name}: {' → '.join(values) if values else 'None'}")


# Create a simple list: 5 → 7 → 9
list1 = ListNode(5, ListNode(7, ListNode(9)))

print("Original list1:")
print_list(list1)

print("\n--- Doing: tail.next = list1 ---")
tail = ListNode(3)  # Just a dummy node with value 3
tail.next = list1
print_list(tail.next, "tail.next")  # Shows entire chain: 5 → 7 → 9

print("\n--- Doing: list1 = list1.next ---")
list1 = list1.next
print_list(list1, "list1 now")  # Shows: 7 → 9
print_list(tail.next, "tail.next still")  # Still shows: 5 → 7 → 9

print("\nNotice: tail.next still has the whole chain!")
print("But list1 moved forward, so on next iteration we'd work with 7 → 9")
