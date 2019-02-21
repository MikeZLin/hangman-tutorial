import subprocess
import random

def getWord():
    with open("words.txt") as f:
        lines = f.read().splitlines()
    return random.choice(lines)
def get_alphabet():
    return [chr(i) for i in range(65,91)]
def get_lower():
    return list(map(str.lower,get_alphabet()))
        
def pHang(n):
    tmp = subprocess.call('cls',shell=True)
    gal = [['---- '],
           ['|  | '],
           ['|    '],
           ['|    '],
           ['|    ']]
    if n < 6:
        gal[2] = ['|  o ']
    if n < 5:
        gal[3] = ['| /  ']
    if n < 4:
        gal[3] = ['| / \\']
    if n < 3:
        gal[3] = ['| /|\\']
    if n < 2:
        gal[4] = ['| /  ']
    if n < 1:
        gal[4] = ['| / \\']
    for i in gal:
        print(''.join(i))
    print("You have {} live(s) left".format(n))


