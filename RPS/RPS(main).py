import random

list = ['Rock','Paper','Scissor']
player1_wins = 0
player1_lose = 0
name = 0 
check_name = 0

def underline(func):
    def wrapper():
        print(f"Robot selection : {random_entekhab}")
        print("---------------------------")
        func()
        print("---------------------------")
        print("Your statistics")
        print(f"Your winnings = {player1_wins}")
        print(f"Your losses = {player1_lose}")
    return wrapper

@underline
def win():
    global player1_lose
    global player1_wins
    print('You won the game')
    player1_wins =+ 1
    player1_lose = player1_lose  

@underline
def lose():
    global player1_lose
    global player1_wins
    print('You lose the game')
    player1_wins = player1_wins
    player1_lose =+ 1

@underline
def draw():
    global player1_lose
    global player1_wins
    print('You have draw the game shodi')
    player1_wins = player1_wins
    player1_lose = player1_lose 

while True:
    try:
        if check_name == 0:
            if name == 0:
                player1_name = input("Enter player 1 name :")

                name =+ 1

        game_round = input(int("Enter the number of game rounds:"))
        for i in range(0, game_round):
            entekhab = int(input('entkhab kon\n1)Rock\n2)Paper\n3)Scissor\n===>'))

            random_entekhab = random.choice(list)

            if entekhab == 1:
                if random_entekhab == 'Rock':
                    draw()
                elif random_entekhab == 'Paper':
                    lose()         
                elif random_entekhab == 'Scissor':
                    win()

            if entekhab == 2:
                if random_entekhab == 'Rock':
                    win()
                elif random_entekhab == 'Paper':
                    draw()
                elif random_entekhab == 'Scissor':
                    lose()

            if entekhab == 3:
                if random_entekhab == 'Rock':
                    lose()
                elif random_entekhab == 'Paper':
                    win()
                elif random_entekhab == 'Scissor':
                    draw()
 
    except:
        print('''
        Your text must be a number.
        If you are in the game mode selection stage, the number must be one or two.
        If you are in the rock, paper and scissors selection stage,the number should be one,two or three.
        If you want the program Close it by pressing ctrl + c.
        ''')
