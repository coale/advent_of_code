import string

with open("inputs/input_day03.txt") as input:
  f = input.readlines()

#Part 1
lower_upper_alphabet = [letter for letter in string.ascii_lowercase] + [letter for letter in string.ascii_uppercase]
values_dict = {key:value for key, value in zip(lower_upper_alphabet, range(1, 53))}

def divide_comp(line):
  first_comp = set()
  second_comp = set()
  half_line = round(len(line.rstrip()) / 2)
  first_half = line[:half_line]
  second_half = line[half_line:]
  for letter in first_half:
    first_comp.add(letter)
  for letter in second_half:
    second_comp.add(letter)
  misplaced = first_comp.intersection(second_comp)
  for item in misplaced:
    return item

total_priority = 0
for line in f:
  total_priority += values_dict[divide_comp(line)]
print(total_priority)

#Part 2
list_of_groups = [[] for item in range(1, 101)]
i = 0
for line in f:
  if len(list_of_groups[i]) == 3:
    i += 1
    list_of_groups[i].append(line)
  else:
    list_of_groups[i].append(line)

def find_groups(list):
  elf1 = set()
  elf2 = set()
  elf3 = set()
  for letter in list[0][:-1]:
    elf1.add(letter)
  for letter in list[1][:-1]:
    elf2.add(letter)
  for letter in list[2][:-1]:
    elf3.add(letter)
  badge = elf1.intersection(elf2, elf3)
  for item in badge:
    return item

total_badge_priority = 0
for list in list_of_groups:
  total_badge_priority += values_dict[find_groups(list)]
print(total_badge_priority)
