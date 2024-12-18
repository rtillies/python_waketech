# Richard Tillies
# June 12, 2024
# Return the factorial of a non-negative integer

# import function from module
from mymodule import get_number

# main function
def main():
  number = get_number()
  fact = factorial(number)
  print_fact(number, fact)

# define factorial recursively
def factorial(n):
  if n <= 0:  # base case
    print(f'{n}! = 1')
    return 1
  else:       # recursive case
    print(f'{n}! = {n} * {n-1}!')
    return n * factorial(n-1)

# print factorial result
def print_fact(n, f):
  print(f'{n}! = {f:,d}')

# call main function
main()