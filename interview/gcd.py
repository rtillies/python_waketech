# Richard Tillies
# June 12, 2024
# Return the greatest common divisor of two integers

from mymodule import get_number

def main():
  first = get_number()
  second = get_number()
  larger, smaller = switch_numbers(first, second)
  print_gcd(larger, smaller)

def switch_numbers(x,y):
  if x < y:
    return y,x
  return x,y

def gcd(x,y):
  z = x % y
  if z == 0:  # base case: x is divisible by y
    return y
  else:       # recursive case
    return gcd(x, z)

def print_gcd(x,y):
  print(f'The GCD of {x} and {y} is {gcd(x,y)}')


# Call main function
main()