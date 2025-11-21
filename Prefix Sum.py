class PrefixSum:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
            print(self.prefix)

    def rangeSum(self, left, right):
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return (preRight - preLeft)


lst = [1, -2, 4, 5, 7]

obj = PrefixSum(lst)

print(obj.rangeSum(1, 3))
from collections import defaultdict

'''
UNDERSTAND
- Given an array of integers (nums) and an integer k, return the total number of subarrays whose sum equals k
- If we have a prefix sum at index i, what previous prefix sum would you need to have seen to know there's a subarray ending at i with sum k
PLAN
- Using the hashmap to map the key and the lst of subarrays
- we calculate the prefix sum and store it then we check the hashmap if k in hashmap then we append that subarray to a res lst until we reach the end of the array
TIME COMPLEXITY: O(N) SPACE COMPLEXITY: O(N)
'''


def SubarraySumEqualsK(arr, k) -> int:
    prefix_map = defaultdict(int)
    prefix_map[0] = 1  # Important! Handle subarrays starting from index 0

    total = 0 # Current position sum
    count = 0

    for num in arr:
        total += num  # Current Prefix Sum

        if (total - k) in prefix_map:
            count += prefix_map[total - k]
            print(prefix_map)

        prefix_map[total] += 1

    return count


arr_test = [1, 1, 1]
print(SubarraySumEqualsK(arr_test, 2))
