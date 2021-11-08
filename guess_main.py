# this is a game - guess the right word
import random
from module import *

# input player's name
player_name = input("Hello, can you input your name please?\n")
print(f"Thank you {player_name}. Now I have created a number, you will guess this number\n")
print("But you can choose the maximum and the minimum positive integer.")
maximum_num = int(input("Can you tell me the maximum number?"))
minimum_num = int(input("Can you tell me the minimum number?"))
# create a random integer
random_pint = create_random_num(minimum_num,maximum_num)
# hint function
while True:
    hint = input("I can give you a hint:\nDo you want to know? (input y or n)\n")
    if hint == "y" or hint == "n":
        break 
# give the first number
if hint == "y":
    num_list = seperate_int(random_pint)
    first_num = return_element(num_list)
    print(f"the first character of the number is {first_num}")
elif hint == "n":
    print("Alright, I like human who don't take advyantage of me!\n")

# player inputs the number
i = 0
while True:
    try:
        player_number = int(input(f"{player_name}, please give me a number between {maximum_num} and {minimum_num}:\n"))
        i = i+1
    except ValueError:
        print("Wrong input!")
    else:
        if player_number >= minimum_num and player_number <= maximum_num:
            if int(player_number) > int(random_pint):
                print("Too large!")
            if int(player_number) < int(random_pint): 
                print("Too small")
            elif player_number == random_pint:
                print("Congrats, you guess the right number!")
                break


print(f"{player_name}, you guessed {i} times altogether. Very well!")
# result
