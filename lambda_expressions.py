import os

## What is lambda function
# Small anonymous functions can be created with the lambda keyword.

def make_incrementor(x, n):
    lambda x : x + n

f = make_incrementor(2, 3)
print(f(0))
