import os

input_url = "https://adventofcode.com/2023/day/3/input"
def get_input():
    file = open("input_file")
    lines = file.read().splitlines()
    file.close()
    return lines

def process_input(line_list):
    num_coords = []
    sym_coords = {}
    count = 0
    for line in line_list:
        temp_num = []
        for i in range(len(line)):
            if(line[i].isdigit()):
                temp_num = temp_num + [i]
            elif(temp_num):
                num_coords.append((count, temp_num))
                temp_num = []
            if(not line[i].isdigit() and line[i] != "."):
                if(sym_coords.get(count) is None):
                    sym_coords[count] = []
                sym_coords[count] = sym_coords[count]  + [i]
        count += 1
    return num_coords, sym_coords

def check_num(y_coord, x_coord, sym_coord_list):
    above_nums = (y_coord - 1 , [x_coord - 1, x_coord, x_coord + 1] )
    below_nums = (y_coord + 1 , [x_coord - 1, x_coord, x_coord + 1] )
    adj_nums = (y_coord, [x_coord - 1, x_coord + 1] )
    
    for level in [above_nums, below_nums, adj_nums]:
        for x in level[1]:
            if(sym_coord_list.get(level[0]) is not None and x in sym_coord_list[level[0]]):
                return True
    return False

def check_nums(num_coord_list, sym_coord_list):
    target_nums = []
    for num_coord in num_coord_list:
        for num in num_coord[1]:
            if(check_num(num_coord[0], num, sym_coord_list)):
                target_nums.append(num_coord)
                break
    return target_nums

def get_nums(target_num_coords, line_list):
    return_list = []
    for num_coord in target_num_coords:
        num_str = ''
        for coord in num_coord[1]:
            num_str += line_list[num_coord[0]][coord]
        return_list.append(int(num_str))
    return return_list

def main():
    os.system("bash /c/Users/ptfsm/github/advent_of_code/get_input.sh {}".format(input_url))
    line_list = get_input()
    num_coord_list,sym_coord_list = process_input(line_list)
    target_num_coords = check_nums(num_coord_list, sym_coord_list)
    num_list = get_nums(target_num_coords, line_list)
    print(num_list)
    print(sum(num_list))

if __name__ == "__main__":
    main()
