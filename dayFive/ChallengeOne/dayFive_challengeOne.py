 # Global Variables
list_one = ["G", "D", "V", "Z", "J", "S", "B"]
list_two = ["Z", "S", "M", "G", "V", "P"]
list_three = ["C", "L", "B", "S", "W", "T", "Q", "F"]
list_four = ["H", "J", "G", "W", "M", "R", "V", "Q"]
list_five = ["C", "L", "S", "N", "F", "M", "D"]
list_six = ["R", "G", "C", "D"]
list_seven = ["H", "G", "T", "R", "J", "D", "S", "Q"]
list_eight = ["P", "F", "V"]
list_nine = ["D", "R", "S", "T", "J"]
command_list = []
move_command = []
from_command = []
to_command = []



def crane_function(from_work_list, to_work_list, move_comm):
    list_end = len(from_work_list)
    list_start = list_end - move_comm
    for num in reversed(range(list_start, list_end)):
        result = from_work_list[num]
        to_work_list.append(result)
        from_work_list.remove(result)


# Main Program
with open("input.txt", "r") as puzzle:
    puzzle_input = [line.rstrip("\n") for line in puzzle]


for input in puzzle_input:
    input = str(input)
    input = input.replace("move ", "")
    input = input.replace(" from ", "")
    input = input.replace(" to ", "")
    move_command.append(int(input[0]))
    from_command.append(int(input[1]))
    to_command.append(int(input[2]))


for (f_comm, to_comm, move_comm) in zip(from_command, to_command, move_command):
    if f_comm == 1:
        from_work_list = list_one
    elif f_comm == 2:
        from_work_list = list_two
    elif f_comm == 3:
        from_work_list = list_three
    elif f_comm == 4:
        from_work_list = list_four
    elif f_comm == 5:
        from_work_list = list_five
    elif f_comm == 6:
        from_work_list = list_six
    elif f_comm == 7:
        from_work_list = list_seven
    elif f_comm == 8:
        from_work_list = list_eight
    elif f_comm == 9:
        from_work_list = list_nine


    if to_comm == 1:
        to_work_list = list_one
    elif to_comm == 2:
        to_work_list = list_two
    elif to_comm == 3:
        to_work_list = list_three
    elif to_comm == 4:
        to_work_list = list_four
    elif to_comm == 5:
        to_work_list = list_five
    elif to_comm == 6:
        to_work_list = list_six
    elif to_comm == 7:
        to_work_list = list_seven
    elif to_comm == 8:
        to_work_list = list_eight
    elif to_comm == 9:
        to_work_list = list_nine   


    crane_function(from_work_list, to_work_list, move_comm)


   # print(f"{list_one[-1]}{list_two[-1]}{list_three[-1]}{list_four[-1]}{list_five[-1]}{list_six[-1]}{list_seven[-1]}{list_eight[-1]}{list_nine[-1]}")