from collections import namedtuple
import math
import requests
from pprint import pprint
import json
import random

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
        #return True
        print("Correct")
    else:
        print("Wrong")
        #return False

if(order == 1):
    print(colored(r1, g1, b1, 'Color 1'))
    print(colored(r3, g3, b3, 'Color 2'))
    print(colored(r2, g2, b2, 'Color 3'))
    user = int(input("Enter the number of the color that does not belong : "))
    if(user == 2):
        #return True
        print("Correct")
    else:
        print("Wrong")
        #return False

if(order == 2):
    print(colored(r2, g2, b2, 'Color 1'))
    print(colored(r1, g1, b1, 'Color 2'))
    print(colored(r3, g3, b3, 'Color 3'))
    user = int(input("Enter the number of the color that does not belong : "))
    if(user == 3):
        #return True
        print("Correct")
    else:
        print("Wrong")
        #return False

if(order == 3):
    print(colored(r2, g2, b2, 'Color 1'))
    print(colored(r3, g3, b3, 'Color 2'))
    print(colored(r1, g1, b1, 'Color 3'))
    user = int(input("Enter the number of the color that does not belong : "))
    if(user == 2):
        #return True
        print("Correct")
    else:
        print("Wrong")
        #return False
if(order == 4):
    print(colored(r3, g3, b3, 'Color 1'))
    print(colored(r1, g1, b1, 'Color 2'))
    print(colored(r2, g2, b2, 'Color 3'))
    user = int(input("Enter the number of the color that does not belong : "))
    if(user == 1):
        #return True
        print("Correct")
    else:
        print("Wrong")
        #return False
if(order == 5):
    print(colored(r3, g3, b3, 'Color 1'))
    print(colored(r2, g2, b2, 'Color 2'))
    print(colored(r1, g1, b1, 'Color 3'))
    user = int(input("Enter the number of the color that does not belong : "))
    if(user == 1):
        #return True
        print("Correct")
    else:
        print("Wrong")
        #return False


#return False