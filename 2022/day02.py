with open("inputs/input_day02.txt") as input:
  f = input.readlines()

splitted_games = []
for game in f:
  splitted_games.append(game.split())
  
#Part 1
points_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3, 'WIN': 6, 'DRAW': 3, 'LOSE': 0}

my_points = 0
elf_points = 0

for game in splitted_games:
  elf_choice = game[0]
  my_choice = game[1]
  if elf_choice == 'A':
    if my_choice == 'X':
      my_points += points_dict['X'] + points_dict['DRAW']
    elif my_choice == 'Y':
      my_points += points_dict['Y'] + points_dict['WIN']
    else:
      my_points += points_dict['Z']
  elif elf_choice == 'B':
    if my_choice == 'X':
      my_points += points_dict['X']
    elif my_choice == 'Y':
      my_points += points_dict['Y'] + points_dict['DRAW']
    else:
      my_points += points_dict['Z'] + points_dict['WIN']
  elif elf_choice == 'C':
    if my_choice == 'X':
      my_points += points_dict['X'] + points_dict['WIN']
    elif my_choice == 'Y':
      my_points += points_dict['Y']
    else:
      my_points += points_dict['Z'] + points_dict['DRAW']

print(my_points)

#Part 2
lose_dict = {'A': 'scissors', 'B': 'rock', 'C': 'paper'}
win_dict = {'A': 'paper', 'B': 'scissors', 'C': 'rock'}
draw_dict = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
new_points_dict = {'A': 1, 'B': 2, 'C': 3, 'rock': 1, 'paper': 2, 'scissors': 3, 'WIN': 6, 'DRAW': 3, 'LOSE': 0}


for game in splitted_games:
  elf_choice = game[0]
  end_game = game[1]
  if end_game == 'X':
    my_choice = lose_dict[elf_choice]
    my_points += new_points_dict[my_choice]
  elif end_game == 'Y':
    my_choice = draw_dict[elf_choice]
    my_points += new_points_dict[my_choice]  + new_points_dict['DRAW']
  elif end_game == 'Z':
    my_choice = win_dict[elf_choice]
    my_points += new_points_dict[my_choice]  + new_points_dict['WIN']

print(my_points)
