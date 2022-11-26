# Takes a list of lists containing strings and convert them all in integers. It returns a list of lists of integers
def str_to_int(list_of_lists):
  int_lists = []
  for line in list_of_lists:
    splitted_line = line.split('x')
    int_lists.append(splitted_line)
  for list in int_lists:
    for i in range(len(list)):
      list[i] = int(list[i])
  return int_lists

#Takes a single box dimensions and calculates the smalles side area
def smallest_side_area(box_dimensions):
  sides_areas = []
  sides_areas.append(box_dimensions[0] * box_dimensions[1])
  sides_areas.append(box_dimensions[1] * box_dimensions[2])
  sides_areas.append(box_dimensions[2] * box_dimensions[0])
  return min(sides_areas)

#Takes a single box dimensions and calculates how many square feet of paper are needed
def wrap_calculator(box_dimensions):
  l = box_dimensions[0]
  w = box_dimensions[1]
  h = box_dimensions[2]
  box_area = 2*l*w + 2*w*h + 2*h*l
  return box_area

#Takes the list of box dimensions and calculates the total square feet of paper needed
def total_paper_calc(int_lists):
  total_square_feet = 0
  for dimensions in int_lists:
    total_square_feet += wrap_calculator(dimensions) + smallest_side_area(dimensions)
  return total_square_feet

with open('inputs/input_day01.txt') as input:
  areas_list = input.readlines()

list_of_dimensions = str_to_int(areas_list)
total_paper_need = total_paper_calc(list_of_dimensions)
print(total_paper_need)
