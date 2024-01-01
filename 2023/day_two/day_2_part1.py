import os

input_url = "https://adventofcode.com/2023/day/2/input"
colour_map = {
        'red' : 12,
        'blue' : 14,
        'green' : 13
        }

def get_input():
    file = open("input_file")
    lines = file.read().splitlines()
    file.close()
    return lines

def valid_trick(trick):
    for num_colour in trick.split(","):
        num = int(num_colour.split(" ")[1])
        colour = num_colour.split(" ")[2]
        if(colour_map[colour] < num):
            return False
    return True

def process_game(game_line):
    for trick in game_line.split(";"):
        if(not valid_trick(trick)):
            return False
    return True

def process_lines(line_list):
    cumu_game_numbers = 0
    for line in line_list:
        game_num = line.split(":")[0].split(" ")[1]
        if(process_game(line.split(":")[1])):
            cumu_game_numbers += int(game_num)
    return cumu_game_numbers

def main():
    os.system("bash /c/Users/ptfsm/github/advent_of_code/get_input.sh {}".format(input_url))
    line_list = get_input()
    print(process_lines(line_list))

if __name__ == "__main__":
    main()
