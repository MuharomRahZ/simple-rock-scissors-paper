import random as rd

rsp = {
    1:"Paper",
    2:"Scissors",
    3:"Rock"
}

player1 = {
    "name": "Player 1",
    "status": "-"
}

player2 = {
    "name": "Player 2",
    "status": "-"
}

def mainMenu():
    try:
        print(f"===================================")
        print(f"WELCOME TO ROCK, SCISSORS, & PAPER!")
        print(f"This program will help you play rock, scissors, & paper")
        print(f"---CHOOSE MENU---\n1. MANAGE PLAYERS\n2. PLAY\n3. EXIT")
        menu = int(input("Enter your choice: "))
        opsiMainMenu(menu)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def opsiMainMenu(menu):
    if menu == 1:
        managePlayer()
    elif menu == 2:
        playOption()
    elif menu == 3:
        print(f"=============================")
        print(f"===You have chosen to exit===")
        print(f"====Thank you for playing====")
        print(f"=============================")
    else:
        print(f"Invalid choice")
        mainMenu()

def opsiManagePlayer(menu):
    if menu == 1:
        viewPlayer()
    elif menu == 2:
        addPlayer()
    elif menu == 3:
        rewritePlayer()
    elif menu == 4:
        mainMenu()
    else:
        print(f"Invalid choice")
        managePlayer()
    

def managePlayer():
    try:
        print(f"=================================")
        print(f"You have chosen to manage players")
        print(f"---CHOOSE MENU---\n1. VIEW PLAYERS\n2. ADD PLAYERS\n3. REWRITE PLAYERS & STATUS\n4. BACK")
        menu = int(input("Enter your choice: "))
        opsiManagePlayer(menu)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)



def viewPlayer():
    print(f"===========================================")
    print(f"You have chosen to view the list of players")
    print(f"The list of players is:")
    print(f"Player 1 Name: {player1['name']}")
    print(f"Player 1 Status: {player1['status']}")
    print()
    print(f"Player 2 Name: {player2['name']}")
    print(f"Player 2 Status: {player2['status']}")
    menu = int(input("Enter your choice: "))
    opsiManagePlayer(menu)

def addPlayer():
    print(f"==============================")
    print(f"You have chosen to add players")
    player1['name'] = input("Enter the name of player 1: ")
    player2['name'] = input("Enter the name of player 2: ")
    print(f"You have added {player1['name']} and {player2['name']} to the list of players")
    menu = int(input("Enter your choice: "))
    opsiManagePlayer(menu)

def rewritePlayer():
    print(f"===========================================")
    print(f"You have chosen to rewrite players & status")
    player1['name'] = "Player 1"
    player1['status'] = "-"
    player2['name'] = "Player 2"
    player2['status'] = "-"
    print(f"You have rewritten players name & status to the list of players")
    menu = int(input("Enter your choice: "))
    opsiManagePlayer(menu)

def playOption():
    try:
        print(f"=======================")
        print(f"You have chosen to play")
        print(f"---CHOOSE MENU---\n1. ROLL & RE-ROLL\n2. BACK")
        menu = int(input("Enter your choice: "))
        playOptionMenu(menu)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def playOptionMenu(menu):
    if menu == 1:
        roll()
    elif menu == 2:
        mainMenu()
    else:
        print(f"Invalid choice")
        playOption()

def roll():
    print(f"=================================")
    print(f"You have chosen to roll & re-roll")
    print(f"---------------------------------")
    player1['status'] = rsp[rd.randint(1,3)]
    player2['status'] = rsp[rd.randint(1,3)]
    print(f"{player1['name']} has rolled {player1['status']}")
    print(f"{player2['name']} has rolled {player2['status']}")
    print(f"---------------------------------")
    print(f"Results:")
    if player1['status'] == rsp[1] and player2['status'] == rsp[2]:
        print(player2['name'], " WON | ",player1['name'], " LOST")
    elif player1['status'] == rsp[2] and player2['status'] == rsp[1]:
        print(player1['name'], " WON | ",player2['name'], " LOST")
    elif player1['status'] == rsp[2] and player2['status'] == rsp[3]:
        print(player2['name'], " WON | ",player1['name'], " LOST")
    elif player1['status'] == rsp[3] and player2['status'] == rsp[2]:
        print(player1['name'], " WON | ",player2['name'], " LOST")
    elif player1['status'] == rsp[3] and player2['status'] == rsp[1]:
        print(player2['name'], " WON | ",player1['name'], " LOST")
    elif player1['status'] == rsp[1] and player2['status'] == rsp[3]:
        print(player1['name'], " WON | ",player2['name'], " LOST")
    else:
        print(player1['name'], " & ",player2['name']," both TIED. Please do RE-ROLL!")
    menu = int(input("Enter your choice: "))
    playOptionMenu(menu)

mainMenu()


# [unused code]:
# print(f"WELCOME TO ROCK, SCISSORS, & PAPER!")
# print(f"This program will help you play rock, scissors, & paper")
# print(f"---CHOOSE MENU---\n1. MANAGE PLAYERS\n2. PLAY\n3. EXIT")
# menu = int(input("Enter your choice: "))
# if menu == 1:
#     print(f"You have chosen to manage players")
#     print(f"---CHOOSE MENU---\n1. VIEW PLAYERS\n2. ADD PLAYERS\n3. REWRITE PLAYERS & STATUS\n4. BACK")
#     menu = int(input("Enter your choice: "))
#     if menu == 1:
#         print(f"You have chosen to view the list of players")
#         print(f"The list of players is:")
#         print(f"Player 1: {player1['name']}")
#         print(f"Player 2: {player2['name']}")
#         print("==========================================================")
#         print(f"---CHOOSE MENU---\n1. VIEW PLAYERS\n2. ADD PLAYERS\n3. REWRITE PLAYERS & STATUS\n4. BACK")
#         menu = int(input("Enter your choice: "))
#     elif menu == 2:
#         print(f"You have chosen to add players")
#         player1['name'] = input("Enter the name of player 1: ")
#         player2['name'] = input("Enter the name of player 2: ")
#         print(f"You have added {player1['name']} and {player2['name']} to the list of players")
#         print("==========================================================")
#         print(f"---CHOOSE MENU---\n1. VIEW PLAYERS\n2. ADD PLAYERS\n3. REWRITE PLAYERS & STATUS\n4. BACK")
#         menu = int(input("Enter your choice: "))
#     elif menu == 3:
#         print(f"You have chosen to rewrite players")
#         player1['name'] = "Player 1"
#         player2['name'] = "Player 2"
#         player1['status'] = "-"
#         player2['status'] = "-"
#         print(f"You have rewritten {player1['name']} and {player2['name']} to the list of players")
#         print("==========================================================")
#         print(f"---CHOOSE MENU---\n1. VIEW PLAYERS\n2. ADD PLAYERS\n3. REWRITE PLAYERS & STATUS\n4. BACK")
#         menu = int(input("Enter your choice: "))
#     elif menu == 4:
#         print(f"You have chosen to go back")
#         print(f"---CHOOSE MENU---\n1. MANAGE PLAYERS\n2. PLAY\n3. EXIT")
#         menu = int(input("Enter your choice: "))
# elif menu == 2:
#     print(f"You have chosen to play")
#     print(f"---CHOOSE MENU---\n1. ROLL & RE-ROLL\n2. BACK")
#     menu = int(input("Enter your choice: "))
#     if menu == 1:
#         print(f"You have chosen to roll & re-roll")
#         player1['status'] = rsp[rd.randint(1,3)]
#         player2['status'] = rsp[rd.randint(1,3)]
#         print(f"You have rolled {player1['name']} and {player2['name']}")
#         print(f"{player1['name']} has rolled {player1['status']}")
#         print(f"{player2['name']} has rolled {player2['status']}")
#         if player1['status'] == rsp[1] and player2['status'] == rsp[2]:
#             print(player2['name'], " WON over ",player1['name'])
#         elif player1['status'] == rsp[2] and player2['status'] == rsp[1]:
#             print(player1['name'], " WON over ",player2['name'])
#         elif player1['status'] == rsp[2] and player2['status'] == rsp[3]:
#             print(player2['name'], " WON over ",player1['name'])
#         elif player1['status'] == rsp[3] and player2['status'] == rsp[2]:
#             print(player1['name'], " WON over ",player2['name'])
#         elif player1['status'] == rsp[3] and player2['status'] == rsp[1]:
#             print(player2['name'], " WON over ",player1['name'])
#         elif player1['status'] == rsp[1] and player2['status'] == rsp[3]:
#             print(player1['name'], " WON over ",player2['name'])
#         else:
#             print(player1['name'], " & ",player2['name']," both TIED. Please do RE-ROLL!")
#         menu = int(input("Enter your choice: "))
#     elif menu == 2:
#         print(f"You have chosen to go back")
#         print(f"---CHOOSE MENU---\n1. MANAGE PLAYERS\n2. PLAY\n3. EXIT")
#         menu = int(input("Enter your choice: "))
# elif menu == 3:
#     print(f"You have chosen to exit")
#     print(f"Thank you for playing")