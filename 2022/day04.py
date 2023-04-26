with open('inputs/input_day01.txt') as input:
  f = input.read()
pairs = f.split('\n')

# Part 1
for i in range(len(pairs) - 1):
  pairs[i] = pairs[i].split(',')
  pairs[i] = [i.split('-') for i in pairs[i]]

count_overlapping = 0

for pair in pairs[:1000]:
  if int(pair[1][0]) >= int(pair[0][0]) and int(pair[1][1]) <= int(pair[0][1]):
    count_overlapping += 1
  elif int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
    count_overlapping += 1

print(count_overlapping)