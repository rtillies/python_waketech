def print_write(file, text):
  f = open("demofile2.txt", "a")
  print(text)
  f.write(text)
  f.close()


def calc_addends(comp, number):
  # left = 0 #, middle, right = 0
  # [count, lcount, mcount, rcount] = 0
  filename = str(comp) + "diamonds" + str(number) + "left.csv"
  f = open(filename, "w")
  f.write("Player,Left,Partner,Right\n")
  counts = [0,0,0,0,0,0,0,0,0]
  raw_count = 0
  equal = 0
  player = [0,0,0,0,0,0,0,0,0]
  partner = [0,0,0,0,0,0,0,0,0]
  for left in range(number+1):
    for middle in range(number - left + 1):
      right = number - left - middle
      # print()
      f.write(f"{comp},{left},{middle},{right}\n")
      counts[0] += 1 # all count
      raw_count += 1 # all count

      # Player: cutting before everyone
      # print("Player:")
      if comp < left and comp < middle and comp < right:
        counts[1] += 1
        player[1] += 1
        print("Player  All:  ", comp, left, middle, right)
      
      # Player: Less than both opponents
      elif comp < left and comp < right:
        counts[2] += 1
        player[2] += 1
        print("Player  Opps: ", comp, left, middle, right)

      # Player: Less than left, equal to right
      elif comp < left and comp == right:
        counts[3] += 1
        player[3] += 1
        print("Player  Left: ", comp, left, middle, right)

      # Partner: cutting before everyone
      # print("Partner:")
      if middle < left and middle < comp and middle < right: 
        counts[4] += 1
        partner[1] += 1
        print("Partner All:  ", comp, left, middle, right)
      
      # Partner: Less than both opponents
      # print("Partner: Less than both opponents")
      elif middle < left and middle < right:
        counts[5] += 1
        partner[2] += 1
        print("Partner Opps: ", comp, left, middle, right)

      # Partner: Less than right, equal to left
      elif middle < right and middle == left:
        counts[6] += 1
        partner[3] += 1
        print("Partner Right:", comp, left, middle, right)

      if comp == middle and comp < left and comp < right:
        counts[7] += 1
        equal += 1
        counts[2] -= 1 # remove from player opps
        counts[5] -= 1 # remove from partner opps
        # player[2] -= 1 # remove from player opps
        # partner[2] -= 1 # remove from partner opps
        print("Partner Same: ", comp, left, middle, right)

  player_cuts = sum(player)
  partner_cuts = sum(partner)

  print(f"\n{comp} diamonds, {number} left, Total count {counts[0]}")
  print(f"Player:  Less than all  : {player[1]:>2} {player[1] * 100 / raw_count:>6.2f}%")
  print(f"Player:  Less than opps : {player[2]:>2} {player[2] * 100 / raw_count:>6.2f}%")
  print(f"Player:  Less than left : {player[3]:>2} {player[3] * 100 / raw_count:>6.2f}%")
  print(f"Player Cuts:  {sum(player):>2} {sum(player) * 100 / raw_count:>6.2f}%\n")

  print(f"Partner: Less than all  : {partner[1]:>2} {partner[1] * 100 / raw_count:>6.2f}%")
  print(f"Partner: Less than opps : {partner[2]:>2} {partner[2] * 100 / raw_count:>6.2f}%")
  print(f"Partner: Less than right: {partner[3]:>2} {partner[3] * 100 / raw_count:>6.2f}%")
  print(f"Partner Cuts:  {sum(partner):>2} {sum(partner) * 100 / raw_count:>6.2f}%\n")
  print(f"Player = Partner {equal:>2} {equal * 100 / raw_count:>6.2f}%\n")
  # print(f"Less than all:  ", counts[2], f"{counts[2] * 100 / counts[0]:.2f}%")

# for x in range(11):
#   calc_addends(3,x)

max = 12
# for x in range(max+1):
#   calc_addends(x,max-x)
# calc_addends(0,12) # 0 diamonds
# calc_addends(1,11) # 1 diamond
calc_addends(2,10) # 2 diamonds
# calc_addends(3,9)  # 3 diamonds
# calc_addends(4,8)  # 4 diamonds
# calc_addends(5,7)  # 5 diamonds
# calc_addends(6,6)  # 6 diamonds
# calc_addends(7,5)  # 7 diamonds