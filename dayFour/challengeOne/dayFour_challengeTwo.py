# Global Variables
input_list = []
area_one_list_clean = []
area_two_list_clean = []
replace_delimeter = ", "
score = 0
range_one_list = []
range_two_list = []


# Main Program
with open("dayFourInput.txt", "r") as puzzle_input:
    puzzle_data = puzzle_input.readlines()

    
    for line in puzzle_data:
        line = line.strip("\n")
        input_list.append(line)
        area_one_input, area_two_input = line.split(",")
        area_one_list_clean.append(area_one_input.replace("-", replace_delimeter))
        area_two_list_clean.append(area_two_input.replace("-", replace_delimeter))


for (line_one, line_two) in zip(area_one_list_clean, area_two_list_clean):
    a, b = line_one.split(",")
    x, y = line_two.split(",")
    begin_range_one = int(a)
    end_range_one = int(b)
    range_one = range(begin_range_one, end_range_one)
    begin_range_two = int(x)
    end_range_two = int(y)
    range_two = range(begin_range_two, end_range_two)


    for (num_one, num_two) in zip(range_one, range_two):
        range_one_list.append(num_one)
        range_two_list.append(num_two)
        match = (set(range_one_list) & set(range_two_list))


        if match != "":
            score = score + 1
            range_one_list = []
            range_two_list = []
            break
    
    
print(score)