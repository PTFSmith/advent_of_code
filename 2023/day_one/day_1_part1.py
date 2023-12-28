import os

input_url = "https://adventofcode.com/2023/day/1/input"
def get_input():
    file = open("input_file")
    lines = file.readlines()
    return lines

def get_first_num(line):
    i = 0
    while i < len(line):
        if(line[i].isdigit()):
            return line[i]
        i += 1

def get_last_num(line):
    i = len(line) - 2
    while i >= 0 :
        if(line[i].isdigit()):
            return line[i]
        i -= 1

def get_num_list(line_list):
    num_list = []
    for line in line_list:
        first = get_first_num(line)
        last = get_last_num(line)
        num_list.append(int(first + last))
    return num_list

def main():
    os.system("bash /c/Users/ptfsm/github/advent_of_code/get_input.sh {}".format(input_url))
    line_list = get_input()
    number_list = get_num_list(line_list)
    print(sum(number_list))

if __name__ == "__main__":
    main()
