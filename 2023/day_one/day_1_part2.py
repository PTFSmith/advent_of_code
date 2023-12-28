import os

input_url = "https://adventofcode.com/2023/day/1/input"
number_map = { 
    "one" : "1", 
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9" 
}

def get_input():
    file = open("input_file")
    lines = file.readlines()
    return lines

def get_first_num(line):
    max_index = len(line) - 1
    i = 0
    while i < len(line):
        if(line[i].isdigit()):
            return line[i]
        if( i+3 <= max_index) and (not number_map.get(line[i:i+3]) is None):
            return number_map[line[i:i+3]]
        if( i+4 <= max_index) and (not number_map.get(line[i:i+4]) is None):
            return number_map[line[i:i+4]]
        if( i+5 <= max_index) and (not number_map.get(line[i:i+5]) is None):
            return number_map[line[i:i+5]]
        i += 1

def get_last_num(line):
    max_index = len(line) - 1
    i = len(line) - 1
    while i >= 0 :
        if(line[i].isdigit()):
            return line[i]
        if( i+3 <= max_index) and (not number_map.get(line[i:i+3]) is None):
            return number_map[line[i:i+3]]
        if( i+4 <= max_index and (not number_map.get(line[i:i+4]) is None)):
            return number_map[line[i:i+4]]
        if( i+5 <= max_index and (not number_map.get(line[i:i+5])is None)):
            return number_map[line[i:i+5]]
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
