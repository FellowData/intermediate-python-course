def main():
  import os
  print('Hello, ' + os.getlogin() + '! How are you?')
  
  import random
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  players = int(input('How many players are there ? '))
  names =["Paul","Jacques"]
  names.clear()
  for i in range (0,players):
    names.append(str(input(f'What is your name, player {i+1} : ')))
  dice_sums = [0,0]
  dice_sums.clear()
  for playerCount in range (0,players):
    dice_sum = 0
    for i in range(0,dice_rolls):
      roll = random.randint(1,dice_size)
      dice_sum += roll
      if roll == 1:
        print(f'{names[playerCount]} rolled a {roll}! Critical Fail')
      elif roll == dice_size:
        print(f'{names[playerCount]} rolled a {roll}! Critical Success')
      else:
        print(f'{names[playerCount]} rolled a {roll}')
    #print(f'{names[playerCount]} has rolled a total of {dice_sum}')
    dice_sums.append(dice_sum)

  for i in range (0,players):
    print(f'{names[i]} has rolled a total of {dice_sums[i]}')
if __name__== "__main__":
  main()