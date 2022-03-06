from random import *
import os
import time
import select
import random

#===============Variables===============

passing = False
tryText = ""
fails = 0

#===============Functions (Code for the Captchas!)===============

def colorCap():
    f = input("colorCap: Pass?")
    if f == "y":
        return True
    else:
        return False

def randoCap():
    f = input("randoCap: Pass?")
    if f == "y":
        return True
    else:
        return False

def polyCap():
    f = input("polyCap: Pass?")
    if f == "y":
        return True
    else:
        return False

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
    if fails == 2:
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