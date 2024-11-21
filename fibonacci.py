# Richard Tillies
# June 12, 2024
# Return the first n numbers of the Fibonacci sequence

from mymodule import get_number

def main():
  number = get_number()
  print_series(number)

def fibonacci(n):
  if n == 0:    # base case n=0
    return 0
  elif n == 1:  # base case n=1
    return 1
  else:         # recursive case
    return fibonacci(n-1) + fibonacci(n-2)

def print_series(n):
  series = []
  for x in range(1, n+1):
    series.append(fibonacci(x))

  print(f'The first {n} Fibonacci numbers are:')
  print(series)

# Call main function
main()