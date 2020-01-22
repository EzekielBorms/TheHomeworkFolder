'''
attempt to make a pig game, not complete
'''
import random

player_points = 0
cpu_points = 0
hold_player = 0
hold_cpu = 0

print("Welcome to PIG! \n RULES \n  If you roll '1': No new points, next player's turn \n  If you roll '2-6': either roll again 'r' or hold 'h' \n  If hold: sum of all rolls is added to score & turn passes to other players \n       !!!!FIRST TO 100 OR MORE POINTS WINS!!!!")

print("It is your turn to roll the dice.")

while player_points < 100 and cpu_points < 100: # while both are under 100
    user_turn = input("Enter 'r' to roll or 'h' to hold: ")
    if user_turn == 'r':
        roll = random.randint(1,6)
        if roll != 1:
            hold_player += roll
            print("You rolled:", roll ,"\nYour score:", hold_player)
        else:
            print("You rolled:", roll ,"\n" "0 points earned""\n""Current score:", player_points)

    elif user_turn == 'h':
        player_points += hold_player
        print("You have chosen to hold \nYour score:", player_points)


while player_points < 100 and cpu_points < 100:
    if hold_cpu < 20:
        roll = random.randint(1,6)
    elif roll != 1:
		hold_cpu += roll
		print("CPU rolled:", roll ,"\nCPU score:", hold_player)
    else:
        print("CPU rolled:", roll ,"\n" "0 points earned""\n""Current score:", player_points)
