# Richard Tillies
# June 12, 2024
# Return the factorial of a non-negative integer

# import function from module
from mymodule import get_number


# define factorial recursively
def factorial(n):
  result = 1
  if n <= 0:  # base case
    print(f'{n}! = 1')
    return result
  else:       # recursive case
    print(f'{n}! = {n} * {n-1}!')
    return n * factorial(n-1)

# print factorial result
def print_fact(n, f):
  print(f'{n}! = {f:,d}')

# call main function
# main function
# print(result)
number = get_number()
fact = factorial(number)
print_fact(number, fact)
