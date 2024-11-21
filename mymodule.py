# Richard Tillies
# June 12, 2024
# Module of common functions

# Return a non-negative integer
def get_number():
  n = 0
  while(n <= 0):
    try:
      n = int(input('Enter a non-negative integer: '))
    except ValueError:  # cannot convert to int
      print(" Error: Please enter an integer value")
    if(n <= 0):          # number less than zero
      print(" Error: Please enter a value greater than zero")
  return n
      