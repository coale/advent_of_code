import string

with open("input.txt") as input:
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
