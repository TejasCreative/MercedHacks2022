from random import *
import os
import time
import select
import random
import sys
from collections import namedtuple
from pprint import pprint
import random
import requests

#===============Variables===============

passing = False
tryText = ""
fails = 0

#===============Functions (Code for the Captchas!)===============

def colorCap():
    def colored(r, g, b, text):
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    user = 0
    random_number = random.randint(0,16777215)
    hex_number1 =format(random_number,'x')


    base_url_hex = "https://www.thecolorapi.com/id?hex="

    base_url_rgb = "https://www.thecolorapi.com/id?rgb="

    first_url_hex = base_url_hex + hex_number1


    first_hex_data = requests.get(first_url_hex).json()


    r1 = first_hex_data['rgb']['r']
    g1 = first_hex_data['rgb']['g']
    b1 = first_hex_data['rgb']['b']


    op1 = random.randint(0,1)
    op2 = random.randint(0,1)
    op3 = random.randint(0,1)
    g2 = 0
    r2 = 0
    b2 = 0
    val1 = random.randint(0,30)
    val2 = random.randint(0,30)
    val3 = random.randint(0,30)

    if(r1 >val1 and (r1+val1 <= 255)):
        if(op1 == 0):
            r2 = r1 - val1
        if(op1 == 1):
            r2 = r1 + val1

    if(g1 >val2 and (g1+val2 <= 255)):
        if(op1 == 0):
            g2 = g1 - val2
        if(op1 == 1):
            g2 = g1 + val2

    if(b1 > val3 and (b1+val3 <= 255)):
        if(op1 == 0):
            b2 = b1 - val3
        if(op1 == 1):
            b2 = b1 + val3


    rgb2 = str(r2) + "," + str(g2) + "," + str(b2)
    seccond_url_rgb = base_url_rgb + rgb2



    seccond_rgb_data = requests.get(seccond_url_rgb).json()
    hex_number2 = seccond_rgb_data['hex']['clean']

    random_number = random.randint(0,16777215)
    hex_number3 =format(random_number,'x')

    third_url_hex = base_url_hex + hex_number3

    third_hex_data = requests.get(third_url_hex).json()


    r3 = third_hex_data['rgb']['r']
    g3 = third_hex_data['rgb']['g']
    b3 = third_hex_data['rgb']['b']



    order = random.randint(0,5)

    if(order == 0):
        print(colored(r1, g1, b1, 'Color 1'))
        print(colored(r2, g2, b2, 'Color 2'))
        print(colored(r3, g3, b3, 'Color 3'))
        user = int(input("Enter the number of the color that does not belong : "))
        if(user == 3):
            return True
        else:
            return False

    if(order == 1):
        print(colored(r1, g1, b1, 'Color 1'))
        print(colored(r3, g3, b3, 'Color 2'))
        print(colored(r2, g2, b2, 'Color 3'))
        user = int(input("Enter the number of the color that does not belong : "))
        if(user == 2):
            return True
        else:
            return False

    if(order == 2):
        print(colored(r2, g2, b2, 'Color 1'))
        print(colored(r1, g1, b1, 'Color 2'))
        print(colored(r3, g3, b3, 'Color 3'))
        user = int(input("Enter the number of the color that does not belong : "))
        if(user == 3):
            return True
        else:
            return False

    if(order == 3):
        print(colored(r2, g2, b2, 'Color 1'))
        print(colored(r3, g3, b3, 'Color 2'))
        print(colored(r1, g1, b1, 'Color 3'))
        user = int(input("Enter the number of the color that does not belong : "))
        if(user == 2):
            return True
        else:
            return False
    if(order == 4):
        print(colored(r3, g3, b3, 'Color 1'))
        print(colored(r1, g1, b1, 'Color 2'))
        print(colored(r2, g2, b2, 'Color 3'))
        user = int(input("Enter the number of the color that does not belong : "))
        if(user == 1):
            return True
        else:
            return False
    if(order == 5):
        print(colored(r3, g3, b3, 'Color 1'))
        print(colored(r2, g2, b2, 'Color 2'))
        print(colored(r1, g1, b1, 'Color 3'))
        user = int(input("Enter the number of the color that does not belong : "))
        if(user == 1):
            return True
        else:
            return False

def randoCap():
    def dont():
        array=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        char=random.choice(array)
        a=random.randint(1, 3)
        if a==1:
            print("Write anything With "+char)
            b1=(input("first input with "+char+":")).lower()
            b2=(input("second input with "+char+":")).lower()
            b3=(input("thrid input with "+char+":")).lower()
            if (char in b1) and (char in b2) and (char in b3):
                return True
            else:
                return False
        elif a==2:
            print("Write anything Without "+char)
            b1=(input("first input without "+char+":")).lower()
            b2=(input("second input without "+char+":")).lower()
            b3=(input("thrid input without "+char+":")).lower()
            if (char not in b1) and (char not in b2) and (char not in b3):
                return True
            else:
                return False
        else:
            print("Don't do anything \n")
            oOgabOoga, o, e=select.select([sys.stdin], [], [], 10)
            if not oOgabOoga:
                return True
            else:
                sys.stdin.readline().strip()
                return False
    return dont()

def polyCap():
    dimension=4
    def eachrow(piece, row):
        line=""
        for column in range(1,dimension+1):
            if piece[(row-1)*dimension+column]==1:
                line = line + "■" + " "
            else:
                line = line + " " + " "
        return line + "  |   "
    def eachline(row,piecerows):
        wholeline=""
        for everypiece in piecerows:
            wholeline += eachrow(everypiece,row)
        return wholeline
    def drawpieces(pieces):
        spaces = (dimension-1)*" "
        if len(pieces) > 1:
            for i in range(len(pieces)):
                print(spaces+ str(i+1) + spaces + "   |"+(4-len(str(i+2)))*" ", end = "")
        print()
        row = 1
        while(row<=dimension):
            print(eachline(row,pieces))
            row+=1
    def combinePieces(piece1,piece2):   
        combinedpiece = {}
        for i in piece1:
            combinedpiece[i]=piece1[i]^piece2[i]
        return tuple([combinedpiece])
    def total(piece):
        total=0
        for i in piece:
            total+=piece[i]
        return total
    def generatePieces(numberofPieces,leftovers=(), filled=False):
        pieces = []
        piece = {}
        if filled:
            for i in range(1,dimension**2+1):
                piece[i]=1
            pieces.append(piece)
            return tuple(pieces)
        else:
            for x in range(numberofPieces):
                piece = {}
                if x<dimension-1:
                    for i in range(1,dimension**2+1):
                        if randint(0,dimension-x)==0 and leftovers[0][i]==1:
                            piece[i]=1
                        else:
                            piece[i]=0
                    leftovers = combinePieces(leftovers[0],piece)
                elif x==dimension-1:
                    piece = leftovers[0]
                else:
                    for i in range(1,dimension**2+1):
                        if randint(0,2)==1:
                            piece[i]=1
                        else:
                            piece[i]=0
                pieces.append(piece)
            return tuple(pieces)
    def polyominoes():
        box = generatePieces(1, filled = True)
        keepgenerating = True
        print("Generating Puzzle...")
        #pieces=generatePieces(2*dimension,leftovers = box)
        while keepgenerating:
            pieces=generatePieces(2*dimension,leftovers = box)
            for eachpiece in pieces:
                if dimension-1<total(eachpiece)<(dimension**2)/2:
                    keepgenerating=False
                else:
                    keepgenerating=True
                    break
        l = list(pieces)
        shuffle(l)
        pieces = tuple(l)
        current = combinePieces(box[0],box[0])
        moves =0
        while not current[0]==box[0]:
            os.system("cls")
            print("Current")
            drawpieces(current)
            print((len(pieces)*((dimension+1)*2+4)-3)*"_" + "\dimension")
            drawpieces(pieces)
            selection = 0
            attempt=current
            while selection==0: #or not total(attempt[0])==total(pieces[selection-1])+total(current[0]):
                selection = input("Choose a box: ")
                try:
                    selection = int(selection)
                except ValueError: 
                    selection =0
                try:
                    attempt = combinePieces(pieces[selection-1],current[0])
                except IndexError:
                    selection = 0
            current = attempt
            moves+=1
        os.system("cls")
        drawpieces(current)
        drawpieces(pieces)
        print("You solved it in", moves, "moves")
        if moves<2**dimension:
            print("This is normal for a human!")
            time.sleep(2)
            return True
        else:
            print("TOO MANY MOVES")
            time.sleep(2)
            return False
    return polyominoes()

def prIntro():
    os.system("cls")
    print("___________________________________")
    print("|                                 |")
    print("|        Oh, so you're NOT        |")
    print("|            a robot?             |")
    print("|                                 |")
    print("|            PROVE IT!            |")
    print("|    'Captcha' - Your Interest    |")
    print("|     (Press enter to solve!)     |")
    print("|                                 |")
    print("|_________________________________|")

def printFail():
    global tryText
    os.system("color 04")
    fail = ["F","A","I","L","U","R","E"]
    ftext = "\t\t"
    for i in range(7):
        os.system("cls")
        ftext += fail[i]
        print("""
    ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣿⣿⠿⠿⠿⠿⣿⣿⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣤⣾⣿⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠈⠉⠛⠿⣿⣷⣤⡀⠀⠀⠀⠀
    ⠀⠀⠀⣴⣿⡿⠋⢁⣴⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡈⠙⢿⣿⣦⠀⠀⠀
    ⠀⢠⣾⣿⠏⢀⣴⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣤⡀⠹⣿⣷⡄⠀
    ⢀⣿⣿⠃⠀⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⡿⠀⠘⣿⣿⡀
    ⣼⣿⠇⠀⠀⠀⠉⢿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀ ⠸⣿⣧
    ⣿⡟⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀ ⢻⣿
    ⣿⡇        ⢉⣿⣿⣿⣿⣿⣿⣿⣿⣋        ⢸⣿
    ⣿⣧⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀ ⠀⣼⣿
    ⢻⣿⡆⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀ ⢰⣿⡟
    ⠈⣿⣿⡄⠀⣴⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣦⠀⢠⣿⣿⠃
    ⠀⠘⢿⣿⣆⠈⠻⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠟⠁⣰⣿⡿⠃⠀
    ⠀⠀⠀⠻⣿⣷⣄⡈⠻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠟⢁⣠⣾⣿⠟⠀⠀⠀
    ⠀⠀⠀⠀⠈⠛⢿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣿⡿⠛⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⣿⣿⣶⣶⣶⣶⣿⣿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀""")
        print(ftext)
        if(ftext != "\t\tFAILURE"):
            time.sleep(.2)
        else:
            time.sleep(1)
    tryText = "Let's try that again, shall we?"

def printSuccess():
    os.system("color 02")
    success = ["S","U","C","C","E","S","S","!"]
    passText = "\t    "
    for i in range(8):
        passText += success[i]
        print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢶⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣧⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣧⠀⠀⣠⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣦⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
        print(passText)
        if(passText != "\t    SUCCESS!"):
            time.sleep(.2)
            os.system("cls")
        else:
            time.sleep(1)
    print("We don't think you're a robot, so you're free to go! Unless..\nYou'd like to do another captcha?? 0_0")
    time.sleep(1)
    os.system("color 07")

def detectBot():
    os.system("cls")
    os.system("color 0E")
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣆⠀⠀⠀⠀⠀⢠⣾⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣧⠀⠀⠀⢠⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣴⣶⣶⣶⣿⣿⣿⣷⣶⣶⣿⣿⣿⣷⣶⣶⣶⣦⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣶⣿⠀⠀⡠⠶⠶⢤⡀⠀⠀⢀⣤⠲⠶⢄⠀⠀⣿⣶⣦⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⣿⠀⢸⡃⣎⢹⡆⡇⠀⠀⢸⢰⡏⢱⠌⡇⠀⣿⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣀⣿⠀⠈⠳⣬⣭⠶⠃⠀⠀⠘⠷⣭⡥⠞⠁⠀⣿⣀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠻⠿⣿⠀⠀⣴⠶⠶⠶⠶⠶⠶⠶⠶⠶⣦ ⠀⠀⣿⠿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠃⠀⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠿⠶⣶⡶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣶⡶⠾⠿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⠷⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠟⠀⠀⠀⠀⠀⠀⠀⠀
You're... One of them, aren't you??
         BEGONE!!!!!""")
    time.sleep(1)
    os.system("color 07")
    quit()

#===============Main Code===============

prIntro()
input()
while not passing:
    os.system("cls")
    os.system("color 07")
    i = randint(0,2)
    print(tryText)
    if fails == 3:
        detectBot()
    if i == 0:
        if(colorCap()):
            passing = True
    elif i == 1:
        if(randoCap()):
            passing = True
    else:
        if(polyCap()):
            passing = True
    if not passing:
        printFail()
        fails += 1

os.system("cls")
printSuccess()
