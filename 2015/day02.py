# Part 1

def parse_sizes(input_list):
    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip('\n').split('x')
        for j in range(3):
            input_list[i][j] = int(input_list[i][j])
    return input_list

def calculate_total_wrap(int_list):
    total = 0
    for list in int_list:
        l = list[0]
        w = list[1]
        h = list[2]
        side1 = l*w
        side2 = w*h
        side3 = h*l
        smallest_side = min([side1, side2, side3])
        total += 2*side1 + 2*side2 + 2*side3 + smallest_side
    return total

with open ("inputs/input_day02.txt") as input:
    list_of_sizes = input.readlines()
    parsed_list = parse_sizes(list_of_sizes)
    total_wrap = calculate_total_wrap(parsed_list)
    print(total_wrap)

# Part 2

def calculate_ribbon(int_list):
    total = 0
    for list in int_list:
        l = list[0]
        w = list[1]
        h = list[2]
        bow = l * w * h
        total += (2 * min(l+w, w+h, h+l)) + bow
    return total

with open("inputs/input_day02.txt") as input:
    list_of_sizes = input.readlines()
    parsed_list = parse_sizes(list_of_sizes)
    total_ribbon = calculate_ribbon(parsed_list)
    print(total_ribbon)