"""
#########################
#  2022 Advent of Code  #
#  Challenge One Part 1 #
#########################

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: 
they'd like to know how many Calories are being carried by the Elf carrying the most Calories. 
In the example above, this is 24000 (carried by the fourth Elf).
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

# Global Varialbes
total_calories = 0
line_total_list = []


# File Object Content Manager
with open("puzzle_input.txt", 'r') as file:
    file_contents = file.readlines()

    # Itterate through file contents convert str to int 
    for line in file_contents:
        if line.strip():
            line = int(line)
            # Add to total calories
            total_calories = line + total_calories
        else:
            # When a blank line is found append the total to list
            line_total_list.append(total_calories)
            # clear counters for the next itteration
            total_calories = 0

# Sort the list from greatest to least
line_total_list.sort(reverse=True)

# Now that the list is sorted we can print the value in the first position
# of the list
print("The answer to challenge one part one is: " + str(line_total_list[0]) + "\n")

# Part two of the day 1 Challenge calculate the top 3 elves total calories
top_three = line_total_list[0] + line_total_list[1] + line_total_list[2]


print("The top three elves are carrying: " + str(top_three))
