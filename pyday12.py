# game_level=3
# def enemis_count():
#     enemies=["skeleton","zombie","alien"]
#     if game_level<5:
#         print(enemies[0])
# enemis_count()
# print(f"enemis in "+{game_level}+"are of "+{enemis_count()})
#guessing a number game 
from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(guess,answer,turns):
    if guess > answer :
        print("too high")
        return turns -1 
    elif guess < answer:
        print("too low")
        return turns -1
    else :
        print(f"you got it {answer}")
def set_difficulty():
    level=input("enter your level of difficulty to play:")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("welcome to number guessing game ")
    print("i think of a number 1 to 100")
    answer=randint(1,100)
    print(f"the correct anser is {answer}")
    turns=set_difficulty()
    guess=0
    while guess != answer:
        print(f"you have {turns} are turns left to guess a number")
        guess=int(input("enter a number:"))
        turns=check_answer(guess,answer,turns)
        if turns== 0:
            print("you have ran out of guess, u loose")
            return
        elif guess!=answer:
            print("guess again")
game()