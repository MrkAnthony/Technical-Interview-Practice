def repeat_hello(n):
    if n > 0:
        print("Hello Recursion")
        repeat_hello(n - 1)

# repeat_hello(5)

def iterative_hello(n):
    for i in range(n):
        print("Hello Iterative")

 # iterative_hello(5)

'''
UNDERSTAND
Given the base case and recursive case, write a function factorial() that returns the factorial of a non-negative integer n
The factorial of a number is the product of all numbers between 1 and n.
BASE CASE
- The smallest number we can find a factorial of is 0. By definition, the factorial of 0 is 1.
- We can restate the problem to say that the factorial of n is n * the factorial of n-1.
'''
def factorial(n):
    if n < 1:
        return 1

    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

'''
UNDERSTAND
write a function sum_list() that calculates the sum of all values in a list recursively
what is the time complexity of the function and space complexity

Plan
- Have a count and decrement each time we call the function recursively 
- The base case would if the count is less than the len(lst) then we would just return 
- each time we call the function we would decrement
'''

def sum_list(lst):

    if len(lst) == 0:
        return 0

    return lst[0] + sum_list(lst[1:])

lst = [3, 5, 6, 7, 8]

print(sum_list(lst))



