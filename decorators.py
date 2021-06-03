"""
in python, there are 2 types of decorators:
1. function
2. class

a decorator is a callable object that make changes to another callable objects.

"""


def wrapper(func):
    print("=== welcome ===")

    def action(x):
        func(x)
        print("=== good bye ==")

    return action

@wrapper
def greetings(x):
    print('Hello Mr,', x)


# greetings('rihan')

def checker(func):
    def helper(num):
        if num < 0 or type(num) is not int:
            return False
        return func(num) # throws error without return- findout later.
    
    return helper

@checker
def factorial(num):
    if num == 0 or num == 1: 
        return 1

    return num * factorial(num-1)


print(factorial(10))
