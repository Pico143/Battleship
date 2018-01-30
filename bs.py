import os
from random import randint
from time import sleep

def charToInt(char):
    return ord(char.lower())-96

def intTochar(int):
    return str(chr(97+int))

def switchPlayer(playerNumber, animation):
    if playerNumber == 1:
        if animation == 1:
            os.system('clear')
            print("""



                 ____   _                              ____
                | ___ \| |                           / __  \\
                | |_/ /| |  __ _  _   _   ___  _ __  `' / /'
                |  __/ | | / _` || | | | / _ \| '__|   / /
                | |    | || (_| || |_| ||  __/| |    ./ /___
                \_|    |_| \__,_| \__, | \___||_|    \_____/
                                   __/ |
                                  |___/

                                                    """)
            sleep(1.5)
            os.system('clear')

            if not start:

                os.system('clear')
                print("""



                 ____   _                              ____
                | ___ \| |                           / __  \\
                | |_/ /| |  __ _  _   _   ___  _ __  `' / /'
                |  __/ | | / _` || | | | / _ \| '__|   / /
                | |    | || (_| || |_| ||  __/| |    ./ /___
                \_|    |_| \__,_| \__, | \___||_|    \_____/
                                   __/ |
                                  |___/
             _                                        _      _
  ___  ___  | |_     _  _   ___   _  _   _ _     ___ | |_   (_)  _ __   ___
 (_-< / -_) |  _|   | || | / _ \ | || | | '_|   (_-< | ' \  | | | '_ \ (_-<
 /__/ \___|  \__|    \_, | \___/  \_,_| |_|     /__/ |_||_| |_| | .__/ /__/
                     |__/                                       |_|
                                                    """)

                sleep(2)
                os.system('clear')

        return 2
    else:
        if animation == 1:
            os.system('clear')
            print("""



                 ____   _                             __
                | ___ \| |                           /  |
                | |_/ /| |  __ _  _   _   ___  _ __  `| |
                |  __/ | | / _` || | | | / _ \| '__|  | |
                | |    | || (_| || |_| ||  __/| |    _| |_
                \_|    |_| \__,_| \__, | \___||_|    \___/
                                   __/ |
                                  |___/
                                                """)
            sleep(1.5)
            os.system('clear')

            if not start:
                os.system('clear')
                print("""



                 ____   _                             __
                | ___ \| |                           /  |
                | |_/ /| |  __ _  _   _   ___  _ __  `| |
                |  __/ | | / _` || | | | / _ \| '__|  | |
                | |    | || (_| || |_| ||  __/| |    _| |_
                \_|    |_| \__,_| \__, | \___||_|    \___/
                                   __/ |
                                  |___/
             _                                        _      _
  ___  ___  | |_     _  _   ___   _  _   _ _     ___ | |_   (_)  _ __   ___
 (_-< / -_) |  _|   | || | / _ \ | || | | '_|   (_-< | ' \  | | | '_ \ (_-<
 /__/ \___|  \__|    \_, | \___/  \_,_| |_|     /__/ |_||_| |_| | .__/ /__/
                     |__/                                       |_|

                                                        """)

                sleep(2)
                os.system('clear')

    return 1

def startScreen():
    os.system('clear')
    print("""
                   _           _   _   _           _     _
                  | |         | | | | | |         | |   (_)
                  | |__   __ _| |_| |_| | ___  ___| |__  _ _ __
                  | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \\
                  | |_) | (_| | |_| |_| |  __/\\__ \\ | | | | |_) |
                  |_.__/ \\__,_|\\__|\\__|_|\\___||___/_| |_|_| .__/
                                                          | |
                                                          |_|v.1.0

                                         # #  ( )
                                      ___#_#___|__
                                  _  |____________|  _
                           _=====| | |            | | |==== _
                     =====| |.---------------------------. | |====
       <--------------------'   .  .  .  .  .  .  .  .   '--------------/
         \\                                                             /
          \\_____________________________________________A&M___________/
      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                    Single player - 1           Multiplayer - 2
                                            """)
    return int(input())

def endScreen(playerNumber):
    os.system('clear')
    if playerNumber == 1:
        print("""\n\n\n\n\n\n
      _____    _                                   __                                _
     |  __ \  | |                                 /_ |                              | |
     | |__) | | |   __ _   _   _    ___   _ __     | |   __      __   ___    _ __   | |
     |  ___/  | |  / _` | | | | |  / _ \ | '__|    | |   \ \ /\ / /  / _ \  | '_ \  | |
     | |      | | | (_| | | |_| | |  __/ | |       | |    \ V  V /  | (_) | | | | | |_|
     |_|      |_|  \__,_|  \__, |  \___| |_|       |_|     \_/\_/    \___/  |_| |_| (_)
                            __/ |
                           |___/                                                      """)
    else:
        print("""\n\n\n\n\n\n
      _____    _                                   ___                                 _
     |  __ \  | |                                 |__ \                               | |
     | |__) | | |   __ _   _   _    ___   _ __       ) |   __      __   ___    _ __   | |
     |  ___/  | |  / _` | | | | |  / _ \ | '__|     / /    \ \ /\ / /  / _ \  | '_ \  | |
     | |      | | | (_| | | |_| | |  __/ | |       / /_     \ V  V /  | (_) | | | | | |_|
     |_|      |_|  \__,_|  \__, |  \___| |_|      |____|     \_/\_/    \___/  |_| |_| (_)
                            __/ |
                           |___/
                              """)
    sleep(messageTime)
    os.system('clear')

#Liczy wystąpienia danego znaku w tablicy wybranego gracza
def countLetter(playerNumber,letter):
    Matrix = chooseMatrix(playerNumber)
    counter = 0
    for i in range(w):
        for j in range(h):
            if Matrix[i][j] == letter:
                counter += 1
    return counter

def chooseMatrix(playerNumber):
    if playerNumber == 1:
        return Matrix1
    elif playerNumber == 2:
        return Matrix2
    elif playerNumber == 3:
        return Matrix3
    elif playerNumber == 4:
        return Matrix4
    print("Something went wrong")
    exit(1)

def showMatrix(playerNumber, start):

    os.system('clear')
    if start:
        Matrix = chooseMatrix(playerNumber+2)
    else:
        Matrix = chooseMatrix(playerNumber)

    print("\n\t\t\t\tPlayer",playerNumber)
    print("\n\t\t  A   B   C   D   E   F   G   H   I   J")
    print("\n\t\t-----------------------------------------")

    for i in range(10):
        for j in range(10):
            if j == 0:
                print("\t",i+1,"\t", end='')
            print("|",Matrix[i][j],"", end='')
            if j == 9 and i == 8 and start:
                print("|\tOpponent's lives: ",
                20-countLetter(switchPlayer(playerNumber,0),'X'),
                "/ 20", end='')
            elif j == 9:
                print("|",end='')


        print("\n\t\t-----------------------------------------")
    print("\n")



'''
Przyjmuje numer aktywnego gracza oraz informację czy jest to AI.
Pozwala na wczytanie przez gracza współrzędnych celu ostrzału, lub w przypadku AI losuje je.
Sprawdza czy można oddać strzał w to miejsce i wyświetla informację o trafieniu lub pudle.
Gdy jeden z graczy zniszczy wszystkie statki przeciwnika, uruchamia funkcję odpowiedzialną za zakończenie rozgrywki.
'''
def shoot(playerNumber, AI):

    again = True
    letterList = ['A','B','C','D','E']

    while again:
        showMatrix(playerNumber,start)
        print('Player ',playerNumber,' is shooting\n')

        if AI:
            X = randint(0,9)
            Y = randint(0,9)
        else:
            while True:
                chosenField = input ("Choose target: ")
                if chosenField == 'bye':
                    endScreen(1)
                    exit(0)
                if not len(chosenField) == 2 and not len(chosenField) == 3:
                    print ("You need to provide a field in a format: Letter + Number (e.g. A2). Try again!")
                    sleep(messageTime)
                    continue
                try:
                    X = charToInt(chosenField[0])
                except KeyError:
                        print ("Accepted values for X coordinate are A-J. Try again.")
                        sleep(messageTime)
                        continue
                try:
                    if len(chosenField) == 2:
                        Y = int(chosenField[1])
                    else:
                        Y = int(chosenField[1] + chosenField[2])
                except ValueError:
                    print ("Y coordinate has to be a number between 1 and 10. Try again.")
                    sleep(messageTime)
                    continue
                if Y < 1 or Y > 10:
                    print ("Accepted values for Y coordinate are 1-10. Try again.")
                    sleep(messageTime)
                    continue
                if X < 1 or X > 10:
                    print ("Accepted values for X coordinate are A-J. Try again.")
                    sleep(messageTime)
                    continue
                break
            temp = Y
            Y = X-1
            X = temp-1


        while True:

            Matrix = chooseMatrix(playerNumber+2)

            if Matrix[X][Y] in ['X','O']:
                if activePlayer == 1:
                    print("You've already shot here")
                    sleep(messageTime)
                break

            Matrix = chooseMatrix(switchPlayer(playerNumber,0))

            if Matrix[X][Y] in letterList:
                shipType = Matrix[X][Y]
                Matrix[X][Y] = 'X'
                Matrix = chooseMatrix(playerNumber+2)
                Matrix[X][Y] = 'X'
                showMatrix(playerNumber,start)

                if countLetter(switchPlayer(playerNumber,0),shipType) == 0:
                    print("Hit and drown!")
                else:
                    print("Nice shot!")
                sleep(messageTime)


            else:
                Matrix = chooseMatrix(playerNumber+2)
                Matrix[X][Y] = 'O'
                showMatrix(playerNumber,start)
                print("You missed...\n")
                sleep(messageTime+2)
                again = False
                break


            if countLetter(switchPlayer(playerNumber,0), 'X') == 20:
                endScreen(playerNumber)
                exit(0)
            break

def setupShips(playerNumber):

    positions = chooseMatrix(playerNumber)

    ships = ["Destroyer","Submarine", "Cruiser", "Battleship", "Carrier"]
    dict = {"0" : "A", "1": "B", '2': "C", "3": "D", "4" : "E"} # do przypisywania liter do statku (A jako destroyer, B jako submarine etc.)
    fieldList = {"A": 1, "B": 2 , "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I" : 9, "J" : 10} # do konwersji inputu, na przykład, "A10" na int
    i = 2
    while i<7:
        overlap=0
        item=ships[i-2] # linia 336 (pojawiać się będzie właściwa nazwa statku)
        while True:

            os.system('clear')
            showMatrix(playerNumber, False)
            if playerNumber == 2 and gameMode == 1: # jeżeli statki dodaje AI
                Z = randint(0,1)
                if Z:
                    Z = "H"
                else:
                    Z = "V"
                field = ["x","y","z"]
                if Z == "H":
                    field[0] = intTochar(randint(0,10-i))
                    temp = int(randint(0,10))
                else:
                    field[0] = intTochar(randint(0,10))
                    temp = int(randint(0,(10-i)))
                if temp == 10:
                    temp = str(temp)
                    field[1] = temp[0]
                    field[2] = temp[1]
                else:
                    temp = str(temp)
                    field[1] = temp[0]
                    del field[2]
            else: #jeżeli statki dodaje gracz
                field = input ("Input position of your {}: ".format(item))
            if not len(field) == 2 and not len(field) == 3: # zabezpieczenie przed podaniem złego formatu pola
                if not gameMode == 1 or playerNumber == 1: #komunikat wyświetla się tylko graczowi, nie podczas dodawania przez komputer
                    print ("You need to provide a field in a format: Letter + Number (e.g. A2). Try again!")
                    sleep(messageTime)
                continue
            X = field[0].upper()
            try:
                X = fieldList[X] #sprawdzenie czy pierwszy znak to A-J; jeżeli nie, pojawi się w słowniku keyerror
            except KeyError:
                    if not gameMode == 1 or playerNumber == 1:
                        print ("Accepted values for X coordinate are A-J. Try again.")
                        sleep(messageTime)
                    continue
            try:
                if len(field) == 2:
                    Y = int(field[1])
                else:
                    try:
                        Y = int(field[1] + field[2])
                    except TypeError: #typeerror może się pojawić, gdyż z konieczności gracz podaje stringa (np "A5"), a komputer może losować tylko liczby
                        ''.join(field)
                        Y = int(field[1] + field[2])

            except ValueError: #jeżeli gracz poda na drugim miejscu coś innego niż liczbę (np. "AA" zamiast "A5")
                if not gameMode == 1 or playerNumber == 1:
                    print ("Y coordinate has to be a number between 1 and 10. Try again.")
                    sleep(messageTime)
                continue
            if Y < 1 or Y > 10:
                if not gameMode == 1 or playerNumber == 1:
                    print ("Accepted values for Y coordinate are 1-10. Try again.")
                    sleep(messageTime)
                continue
            break
        while True: #pętla, w której gracz ma podać orientację statku (horizontal, vertical) i w której weryfikowana jest jej poprawność (nawet w turze AI)
            os.system('clear')
            showMatrix(playerNumber, False)
            if not int(gameMode) == 1 or playerNumber == 1:
                Z = input ("Input orientation of your ship (H, V): ")
            Z = Z.upper()
            if not Z == "H" and not Z == "V":
                print ("Wrong orientation! It has to be H for \"Horizontal\" or V for \"Vertical\"!")
                sleep(messageTime)
                continue
            break
        if Z == "H": # w tym if else sprawdzane jest, czy statek zmieści się na planszy przy podanej orientacji
            if X - 2 + i > 9:
                print ("Your ship is sticking out of the board! Try again.")
                sleep(messageTime)
                continue
        else:
            if Y - 2 + i > 9:
                print ("Your ship is sticking out of the board! Try again.")
                sleep(messageTime)
                continue
        for a in range (i): # sprawdzanie, czy statek potencjalnie nie będzie nakładać się z innym
            if Z == "H":
                if not positions[Y-1][X-1+a] == "~":
                    if gameMode == 2 or playerNumber == 1:
                        print ("Your ship is overlapping with another one. Try again.")
                        sleep(messageTime)
                    overlap = 1 #overlap pozwala na wykonanie "continue" w dużej pętli
                    break
            if Z == "V":
                if not positions[Y-1+a][X-1] == "~":
                    if gameMode == 2 or playerNumber == 1:
                        print ("Your ship is overlapping with another one. Try again.")
                        sleep(messageTime)
                    overlap = 1
                    break
        if overlap == 1:
            continue
        for a in range (i): #dodawanie statku
            if Z == "H":
                positions[Y-1][X-1+a] = dict[str(i-2)]
            elif Z == "V":
                positions[Y-1+a][X-1] = dict[str(i-2)]
        i+=1
    os.system('clear')
    showMatrix(playerNumber, False)
    sleep(messageTime)

########################################################

w = 10
h = 10
messageTime = 2
Matrix1 = [['~' for x in range(w)] for y in range(h)]
Matrix2 = [['~' for x in range(w)] for y in range(h)]
Matrix3 = [['~' for x in range(w)] for y in range(h)]
Matrix4 = [['~' for x in range(w)] for y in range(h)]

start = False
gameMode = startScreen()
activePlayer = 2

if gameMode == 1:
    setupShips(activePlayer)
    activePlayer = switchPlayer(activePlayer,1)
    setupShips(activePlayer)
    start = True
    while True:
        shoot(activePlayer, False)
        activePlayer = switchPlayer(activePlayer,1)
        shoot(activePlayer, True)
        activePlayer = switchPlayer(activePlayer,1)
else:
    activePlayer = switchPlayer(activePlayer,1)
    setupShips(activePlayer)
    activePlayer = switchPlayer(activePlayer,1)
    setupShips(activePlayer)
    start = True
    while True:
        activePlayer = switchPlayer(activePlayer,1)
        shoot(activePlayer, False)
