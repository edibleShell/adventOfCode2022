# Global Variables
common_characters = []
lowercase_dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
"i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18,
"s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
uppercase_dic = {"A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33,
"H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42,
"Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}
score_list = []
compare_list = []
swap_list = []

# Read Ruck contents
with open("ruck_contents.txt", "r") as ruck:
    rucksack = ruck.readlines()

    # Review each Item in the rucksack
    for item in rucksack:
        # Clean up the items
        item = item.strip("\n")
        if len(swap_list) > 0:
            compare_list.append(swap_list[0])
            swap_list = []
    

        if len(compare_list) <= 2:
            compare_list.append(item)
        elif len(compare_list) != 0:
                swap_list.append(item)
                for char in compare_list[0]:
                    if char in compare_list[1] and char in compare_list[2]:
                        common_characters.append(char)
                        break
                compare_list = []


for char in common_characters:
    if char in lowercase_dic:
        score_list.append(lowercase_dic[char])
    elif char in uppercase_dic:
        score_list.append(uppercase_dic[char])
    else:
        print("character not found")


score_list_sum = sum(score_list)


print(score_list_sum)
