# Global Variables
loss_value = 0
draw_value = 3
win_value = 6
player_one = []
player_two = []


# Rock, Paper, Scissors
with open("dayTwoInput.txt", "r") as file:
    game_input = file.readlines()
    #print(game_input)

    # Create Player input
    for input in game_input:
        player_one_input, player_two_input = input.split(" ")


        if player_one_input == "A":
            player_one_score = 1
        elif player_one_input == "B":
            player_one_score = 2
        else:
            player_one_score = 3


        if player_two_input == "X\n":
            player_two_score = 1
        elif player_two_input == "Y\n":
            player_two_score = 2
        else:
            player_two_score = 3


        # Paper Victories
        if player_one_score == 1 and player_two_score == 2:
            player_two.append(player_two_score + win_value)
            player_one.append(player_one_score)
        elif player_two_score == 1 and player_one_score == 2:
            player_one.append(player_one_score + win_value)
            player_two.append(player_two_score)
        # Rock Victories
        elif player_one_score == 1 and player_two_score == 3:
            player_one.append(player_one_score + win_value)
            player_two.append(player_two_score)
        elif player_two_score == 1 and player_one_score == 3:
            player_two.append(player_two_score + win_value)
            player_one.append(player_one_score)
        # Scissor Victories
        elif player_one_score == 3 and player_two_score == 2:
            player_one.append(player_one_score + win_value)
            player_two.append(player_two_score)
        elif player_two_score == 3 and player_one_score == 2:
            player_two.append(player_two_score + win_value)
            player_one.append(player_one_score)
        # Draw
        elif player_one_score == player_two_score:
            player_one.append(player_one_score + draw_value)
            player_two.append(player_two_score + draw_value)


player_one_sum = sum(player_one)
player_two_sum = sum(player_two)


print(f"Player One Total Score: {player_one_sum}")
print(f"Player two Total Score: {player_two_sum}")
        

        




