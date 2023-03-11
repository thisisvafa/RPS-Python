# import random
from random import randint

print("rock...")
print("paper...")
print("scissors...")
print("..................................................................")

# randomNumber = random.randint(0, 2)
randomNumber = randint(0, 2)
computerMove = 'rock'

if randomNumber == 0:
    computerMove = 'rock'
elif randomNumber == 1:
    computerMove = 'paper'
elif randomNumber == 2:
    computerMove = 'scissors'

Player_1 = input("Player_1 , Make your move: ")
print(f"Player_2 , Make your move: {computerMove}")
Player_2 = computerMove

if Player_1 == Player_2:
    print('thats tie ...')
elif Player_1 == 'rock':
    if Player_2 == 'scissors':
        print('player_1 wins! ...')
    elif Player_2 == 'paper':
        print('player_2 wins! ...')
elif Player_1 == 'paper':
    if Player_2 == 'rock':
        print('player_1 wins! ...')
    elif Player_2 == 'scissors':
        print('player_2 wins! ...')
elif Player_1 == 'scissors':
    if Player_2 == 'paper':
        print('player_1 wins! ...')
    elif Player_2 == 'rock':
        print('player_2 wins! ...')
else:
    print('somthing went wrong ...')



# if Player_1 == 'rock' and Player_2 == 'scissors':
#     print('player_1 wins! ...')
# elif Player_1 == 'rock' and Player_2 == 'paper':
#     print('player_2 wins! ...')
# elif Player_1 == 'paper' and Player_2 == 'rock':
#     print('player_1 wins! ...')
# elif Player_1 == 'paper' and Player_2 == 'scissors':
#     print('player_2 wins! ...')
# elif Player_1 == 'scissors' and Player_2 == 'paper':
#     print('player_1 wins! ...')
# elif Player_1 == 'scissors' and Player_2 == 'rock':
#     print('player_2 wins! ...')
# elif Player_1 == Player_2:
#     print('thats tie ...')
# else:
#     print('somthing went wrong ...')