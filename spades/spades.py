def get_option():
  print("Choose Ruleset")
  print(1, "Joker Joker Deuce Deuce")
  print(2, "Joker Joker Deuce Ace")
  print(3, "Joker Joker Ace")
  print(4, "Ace High")
  number = int(input("Enter 1-4: "))
  
  while number < 1 or number > 4:
    print("Invalid option")
    number = int(input("Enter 1-4: "))

  return number

def set_count(option):
  spades = diamonds = clubs = hearts = 13
  match option:
    case 1: # JJDD
      spades = 16
      diamonds = clubs = hearts = 12
    case 2: # JJDA
      spades = 15
      clubs = hearts = 12
    case 3: # JJDA
      spades = 15
      clubs = hearts = 12
    # case _:
    #   spades = spades

  print("Total:   ", spades + diamonds + clubs + hearts)
  return (spades, diamonds, clubs, hearts)

def display_count(spades, diamonds, clubs, hearts):
  print("spades:  ", spades)
  print("diamonds:", diamonds)
  print("clubs:   ", clubs)
  print("hearts:  ", hearts)

def get_hand():
  total = 0
  while(total != 13):
    s = int(input("How many spades? "))
    d = int(input("How many diamonds? "))
    c = int(input("How many clubs? "))
    h = int(input("How many hearts? "))
    total = s + d + c + h
    print("Total:   ", total)
    if(total != 13):
      print("Invalid hand")

  return (s, d, c, h)

def display_hand(s, d, c, h, label):
  print(f"{label}: {s: >3}{d: >3}{c: >3}{h: >3}")

def hand_header():
  print("Suits:  S  D  C  H")

def calc_remaining(suit, hand):
  return suit - hand

def main():
  # Get spades rules
  option = get_option()
  (spades, diamonds, clubs, hearts) = set_count(option)
  # display_count(spades, diamonds, clubs, hearts)

  # Get suit count within hand
  (s, d, c, h) = get_hand()

  # Determine remaining cards in deck
  rs = calc_remaining(spades, s)
  rd = calc_remaining(diamonds, d)
  rc = calc_remaining(clubs, c)
  rh = calc_remaining(hearts, h)

  # Display Hand
  hand_header()
  display_hand(s, d, c, h, "Hand")
  display_hand(rs, rd, rc, rh, "Left")

  # Get all additives up to a number
  # def calc_addends(number):


# Run main
main()