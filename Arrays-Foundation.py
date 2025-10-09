from collections import defaultdict

'''
UNDERSTAND
Write a function that takes in a string as a parameter and returns True if the string is a pangram and False if not

PLAN
- Having a lst of all the letters in the alpha
- then looping through the string and returning true if the string contains any of the elements in the array of alpha
- a count for each so that each letter must appear only once
- else we would return false

EDGE CASES
- Uppercase Or Lowercase

EXAMPLES
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))


'''


def is_pangram(my_str):
    alpha_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    string = my_str.lower()
    seen = set()

    for letter in string:
        if letter in alpha_lst:
            seen.add(letter)

    if len(seen) == 26:
        return True

    return False


my_str = "The quick brown fox jumps over the lazy dog"
'print(is_pangram(my_str))'

str2 = "The dog jumped"
'print(is_pangram(str2))'

'''
UNDERSTAND
Write a function that takes in a string as a parameter and returns the string reversed
PLAN
Simply use splicing to reverse the string and just return that
'''


def reverse_string(my_str):
    result = ''
    for i in range(len(my_str) - 1, -1, -1):
        result += my_str[i]
    return result


my_str = "live"
'print(reverse_string(my_str))'

'''
UNDERSTAND
- Need to create a function that takes in a lst of integers 
- Another lst of integers name sequence 
- need to determine whether the sequence list is a subsequence of the lst
- sequence -> lst
- A set of numbers that aren't necessarily adjacent but are in the same relative order as they appear in the list
- basically the numbers cannot go backwards only from left to right to be valid
EDGE CASES
- The number could be a duplicate
PLAN
- Iterating through sequence and lst
- make sure of any numbers that appear in sequence from left to right
- if the index is -1 then we return false else true
'''


def is_subsequence(lst, sequence):
    last_index = -1
    found = False

    for nums in sequence:
        for i in range(last_index + 1, len(lst)):
            if lst[i] == nums:
                last_index = i
                found = True
                break

        if not found:
            return False

    return True


lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
'print(is_subsequence(lst, sequence))'

'''
UNDERSTAND
- so we need to finish this function that takes in a list of keys and list of values as paramters.
- The function should return a dictionary where each item in keys is paired with a corresponding itme in values

keys[i] should be paired with values[i] in the dictionary where 

PLAN
- Iterate through each list starting at the first element in the lst
- and then for elements in the key lst we then would append that to the key of the dictionary
- and for elements in the values lst we would append that to the values in the dictionary
- then we would just return the dictionary
'''


def create_dictionary(keys, values):
    dict = {}
    for i, key in enumerate(keys):
        dict[key] = values[i]

    return dict


keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]

'print(create_dictionary(keys, values))'

'''
Write a function that takes in a dictionary and a key which would be the target as parameters.
The function would look for the target and when found it prints the key and it's associated values 

PLAN
- Loop through the dictionary
- potentially using the pop operator to retrieve the elements that are true and false
'''


def print_pair(dictionary, target):
    found = False
    for key, value in dictionary.items():
        if key == target:
            found = True
            return f"Key: {key} Value: {value}"

    if not found:
        return "This Pair Doesn't exist"


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
'''
print(print_pair(dictionary, "patrick"))
print(print_pair(dictionary, "plankton"))
print(print_pair(dictionary, "spongebob"))
'''


def index_to_value_map(lst):
    return dict(enumerate(lst))


lst = ["apple", "banana", "cherry"]
'print(index_to_value_map(lst))'
'''
UNDERSTAND
- Use the two pointer approach to reverse a list
PLAN
- Need to init pointers one pointer at the beginning of the list l = 0
- Another pointer the right one we would init it at the end of the lst r = len(lst) - 1
- we would loop through the lst with a while loop
- and swap the elements till it's completely reversed
- then return the lst
EDGE CASE
- the list is empty
'''

'''
UNDERSTAND
- Write a function that takes in a list of strings as a parameter and return the first palindromic string in the list
- if it reads the same forward and backwards
- if no such string return an empty string ""
PLAN
- Since the lst holds individual words i'll split it
- then use two pointers to see if the letters match up in corresponding ends
- if so return the word
- if not we would return ""
'''

'''
O(N^2)
'''


def first_palindrome(words):
    for word in words:

        if word == word[::-1]:
            return word

    return ""


words = ["abc", "car", "ada", "racecar", "cool"]
palindrome1 = first_palindrome(words)
'print(palindrome1)'

'''
write a function that takes in a sorted lst of integers as a parameter and removes the duplicates in place
such that each element only appears once.
'''


def remove_duplicates(nums):
    left = 0
    right = left + 1

    while right < len(nums):
        if nums[left] == nums[right]:
            del nums[right]

        if nums[left] != nums[right]:
            left += 1
            right += 1

    return nums and len(nums)


nums = [1, 1, 2, 3, 4, 4, 4, 5]

'''
UNDERSTAND
- write a function that takes in a string s as a parameter
- returns a string with all the vowels in the string reversed.
- They should remain in the same position
- I need to consider a e i o u but not y
- The vowels can appear in both lower and uppercase, more than once
PLAN
- I need to have an lst of the vowels
- I need to init the left and right pointer
- iterate through the string
- If an element is in the vowels lst we then would swap the letters
- else we just continue iterating
'''

'redo tmr'
'''
UNDERSTAND
- write a function that takes in a string s as a parameter and returns a string
- with all the vowels in the string reversed
- The consonants should remain in the same position
PLAN
- I'm going to create a lst of the vowels
- initialize our two points (left and right)
- going to convert the string into a lst
- set both pointers at the end of the string 
- if left pointer isn't a vowel we increment
- if the right pointer isn't a vowel we increment
- when it's a vowel we will swap the positions 
- join the elements in the lst to create a string
EDGE CASE
- The string can be empty
'''


def reverse_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    lst = list(s)
    left = 0
    right = len(s) - 1

    if not s:
        return "not found"

    while left < right:
        if lst[left] not in vowels:
            left += 1
            continue
        if lst[right] not in vowels:
            right -= 1
            continue
        else:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    return "".join(lst)


s1 = "hello"
'holle'
rev_s1 = reverse_vowels(s1)
print(rev_s1)

s2 = "leetcode"
'leotcede'
rev_s2 = reverse_vowels(s2)
print(rev_s2)

s3 = ""
rev_s3 = reverse_vowels(s3)
print(rev_s3)


def prefix_sum_practice(nums):
    n = len(nums)

    prefix = [0] * n
    prefix[0] = nums[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + nums[i]

    return prefix


arr = [1, 2, 3, 4, 5]
#print(prefix_sum_practice(arr))

test_input = [[] for i in range(6)]

retrieve = test_input[3].append(6)

#print(test_input)


def solution(a):
    n = len(a)
    b = []

    for i in range(n):
        left = a[i - 1] if i > 0 else 0
        current = a[i]
        right = a[i + 1] if i > n - 1 else 0
        b.append(left + current + right)

    return b


print(solution(arr))
