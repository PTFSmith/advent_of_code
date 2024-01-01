import os

input_url = "PUT URL HERE"
def get_input():
    file = open("input_file")
    lines = file.readlines()
    file.close()
    return lines

def main():
    os.system("bash /c/Users/ptfsm/github/advent_of_code/get_input.sh {}".format(input_url))
    line_list = get_input()

if __name__ == "__main__":
    main()
