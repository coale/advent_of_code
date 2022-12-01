def calories_lists(str_list):
  calories_list = [[] for item in str_list if item == "\n"]
  calories_list.append([])
  sum_list = []
  i = 0
  for str in str_list:
    if str != "\n":
       calories_list[i].append(int(str.strip()))
    elif str == "\n":
      i += 1
  for elve in calories_list:
    sum_list.append(sum(elve))
  return sum_list

def sum_first_three(sum_list):
  sum_list.sort(reverse=True)
  return sum_list[0] + sum_list[1] + sum_list[2]

with open("inputs/input_day01.txt") as input:
  f = input.readlines()

sum_list = calories_lists(f)
max_sum = max(sum_list)
first_three = sum_first_three(sum_list)
