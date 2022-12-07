# Global Variables
common_characters = []
lowercase_dic = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
"i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18,
"s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
uppercase_dic = {"A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33,
"H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42,
"Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}
section_one_list = []
section_two_list = []
score_list = []


# Read Ruck contents
with open("ruck_contents.txt", "r") as ruck:
    rucksack = ruck.readlines()

    # Review each Item in the rucksack
    for item in rucksack:
        # Clean up the items
        item = item.strip("\n")
        item_len = len(item)

        # Section 1
        half_len = int(item_len/2)
        section_one = item[0:half_len]
        section_one_list.append(section_one)

        # Section 2 
        full_len = half_len * 2
        section_two = item[half_len:full_len]
        section_two_list.append(section_two)


        for char in section_one:
            if char in section_two:
                common_characters.append(char)
                break


for char in common_characters:
    if char in lowercase_dic:
        score_list.append(lowercase_dic[char])
    elif char in uppercase_dic:
        score_list.append(uppercase_dic[char])
    else:
        print("character not found")


score_list_sum = sum(score_list)


print(score_list_sum)


        