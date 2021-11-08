# this is a game - guess the right word
import random
from module import *
# create a random integer
random_pint = int(random.randrange(0, 500))
# input player's name
player_name = input("Hello, can you input your name please?\n")
print(f"Thank you {player_name}. Now I have created a number, you will guess this number\n")

# hint function
hint = input("BTW, I can kindly give you a hint:\nDo you want to know? (y or n)\n")
while hint != "y" or "n":
    input("y or n only \n")
    if hint == "y" or "n":
        break 
        
# give the first number
if hint == "y":
    num_list = seperate_int(random_pint)
    first_num = return_element(num_list)
    print(f"the 1st character of the number is {first_num}")
elif hint == "n":
    print("Alright, I like human who don't take advyantage of me!\n")

# player inputs the number
while True:
    try:
        player_number = int(input(f"{player_name}, please give me a number between 0 - 500:\n"))
    except ValueError:
        print("Wrong input!")
    else:
        if player_number >= 0 and player_number <= 500:
            break
if int(player_number) > int(random_pint):
    print("Too large!")
if int(player_number) < int(random_pint): 
    print("Too small")
elif player_number == random_pint:
    print("Congrats, you guess the right number!")
