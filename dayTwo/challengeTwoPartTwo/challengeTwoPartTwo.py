# Global Variables
draw_value = 3
win_value = 6
player_one = []
player_two = []


# Challenge Two Part Two
with open("challengeTwoInput.txt", "r") as file:
    game_input = file.readlines()


    for input in game_input:
        player_one_input, player_two_input = input.split(" ")
        
        
        # Determine Player two losses
        if player_two_input == "X\n" and player_one_input == "A":
            player_two.append(3)
            player_one.append(1 + win_value)
        elif player_two_input == "X\n" and player_one_input == "B":
            player_two.append(1)
            player_one.append(2 + win_value)
        elif player_two_input == "X\n" and player_one_input == "C":
            player_two.append(2)
            player_one.append(3 + win_value)
        

        # Determine Player two Draws
        if player_two_input == "Y\n" and player_one_input == "A":
            player_two.append(1 + draw_value)
            player_one.append(1 + draw_value)
        elif player_two_input == "Y\n" and player_one_input == "B":
            player_two.append(2 + draw_value)
            player_one.append(2 + draw_value)
        elif player_two_input == "Y\n" and player_one_input == "C":
            player_two.append(3 + draw_value)
            player_one.append(3 + draw_value)


        # Determine Player two Victories
        if player_two_input == "Z\n" and player_one_input == "A":
            player_two.append(2 + win_value)
            player_one.append(1)
        elif player_two_input == "Z\n" and player_one_input == "B":
            player_two.append(3 + win_value)
            player_one.append(2)
        elif player_two_input == "Z\n" and player_one_input == "C":
            player_two.append(1 + win_value)
            player_one.append(3)


player_one_sum = sum(player_one)
player_two_sum = sum(player_two)


print(f"Player One Total Score: {player_one_sum}")
print(f"Player Two Total Score: {player_two_sum}")