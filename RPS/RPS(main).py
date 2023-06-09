import random


list = ['Rock','Paper','scissor']

player1_wins = 0
player1_lose = 0

name = 0 



while True:
    try:
        if name == 0:
            player1_name = input("Enter player 1 name :")

            name =+ 1

        entekhab = int(input('entkhab kon\n1)Rock\n2)Paper\n3)scissor\n===>'))

        random_entekhab = random.choice(list)

        if entekhab == 1 and random_entekhab == 'Rock':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You have tied the game shodi')
            print('---------------------------')

            player1_wins = player1_wins
            player1_lose = player1_lose   

            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue
            else:
                continue                    
            
            

        if entekhab == 1 and random_entekhab == 'Paper':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You lose the game')
            print('---------------------------')
            player1_wins = player1_wins
            player1_lose =+ 1
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")     

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue                     
            
            else:
                continue           
            

        if entekhab == 1 and random_entekhab == 'scissor':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You won the game')
            print('---------------------------')
            player1_wins =+ 1
            player1_lose = player1_lose        
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")      

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue            

        if entekhab == 1 and random_entekhab == 'Rock':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You have tied the game shodi')
            print('---------------------------')
            player1_wins = player1_wins
            player1_lose = player1_lose

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue    
    
        if entekhab == 2 and random_entekhab == 'Rock':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You won the game')
            print('---------------------------')
            player1_wins =+ 1
            player1_lose = player1_lose
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")  

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue

        if entekhab == 2 and random_entekhab == 'Paper':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You have tied the game shodi')
            print('---------------------------')
            player1_wins = player1_wins
            player1_lose = player1_lose
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue

        if entekhab == 2 and random_entekhab == 'scissor':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You lose the game')
            print('---------------------------')
            player1_wins = player1_wins
            player1_lose =+ 1
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")  

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue

        if entekhab == 3 and random_entekhab == 'Rock':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You lose the game')
            print('---------------------------')
            player1_wins = player1_wins
            player1_lose =+ 1
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")     

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue

        if entekhab == 3 and random_entekhab == 'Paper':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You won the game')
            print('---------------------------')
            player1_wins =+ 1
            player1_lose = player1_lose
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")  

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue

        if entekhab == 3 and random_entekhab == 'scissor':
            print(f"Robot selection : {random_entekhab}")
            print("---------------------------")
            print('You have tied the game shodi')
            print('-------------------------')
            player1_wins = player1_wins
            player1_lose = player1_lose
            
            print("Your statistics")
            print(f"Your winnings = {player1_wins}")
            print(f"Your losses = {player1_lose}")     

            name_check = int(input(
                "are you need change your name?\nAlert if you change your name all statistics = 0\n1)Yes\n2)No\n===>"
                ))
            if name_check == 1:
                name = 0
                player1_wins = 0
                player1_lose = 0
                continue      
            
            else:
                continue

    except Exception as error:
        print('''
        Your text must be a number.
        If you are in the game mode selection stage, the number must be one or two.
        If you are in the rock, paper and scissors selection stage,the number should be one,two or three.
        If you want the program Close it by pressing ctrl + c.
        ''')