import os

input_url = "https://adventofcode.com/2023/day/2/input"

def get_input():
    file = open("input_file")
    lines = file.read().splitlines()
    file.close()
    return lines

def check_trick(trick,colour_map):
    for num_colour in trick.split(","):
        num = int(num_colour.split(" ")[1])
        colour = num_colour.split(" ")[2]
        if(colour_map[colour] < num):
            colour_map[colour] =  num

def multiply_list(num_list):
    result = 1
    for num in num_list:
        result *= num
    return result

def process_game(game_line):
    colour_map = {
        'red' : 0,
        'blue' : 0,
        'green' : 0
        }

    for trick in game_line.split(";"):
        check_trick(trick,colour_map)

    return multiply_list(colour_map.values()) 

def process_lines(line_list):
    cumu_game_numbers = 0
    for line in line_list:
        game_num = process_game(line.split(":")[1])
        cumu_game_numbers += int(game_num)
    return cumu_game_numbers

def main():
    os.system("bash /c/Users/ptfsm/github/advent_of_code/get_input.sh {}".format(input_url))
    line_list = get_input()
    print(process_lines(line_list))

if __name__ == "__main__":
    main()
