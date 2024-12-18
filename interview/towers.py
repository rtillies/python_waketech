# Richard Tillies
# June 12, 2024
# Return the moves to solve Towers of Hanoi

from mymodule import get_number

def main():
  discs = get_number()
  start = "left"
  temp = "middle"
  stop = "right"
  counter = move(discs, start, stop, temp)
  print(f'Moved {discs} discs in {counter} moves')

def move(n, start, stop, temp):
  if n == 0:  # base case
    return 0
  else:       # recursive case
    pre = move(n-1, start, temp, stop)
    print(f'Move disc from {start} to {stop}')
    post = move(n-1, temp, stop, start)
    return pre + post + 1


# Call main function
main()