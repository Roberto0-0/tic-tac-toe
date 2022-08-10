#!/usr/bin/python3
import os
import random
import time

value = " "
matriz = [
    [" ", " ", " ",],
    [" ", " ", " ",],
    [" ", " ", " ",]]
       
    # 00 01 02
    # 10 11 12
    # 20 21 22

player_options = 0
plays = True

def showGame(matriz, value):
    print("%s | %s | %s"%(matriz[0][0], matriz[0][1], matriz[0][2]))
    print("--+---+--")
    print("%s | %s | %s"%(matriz[1][0], matriz[1][1], matriz[1][2]))
    print("--+---+--")
    print("%s | %s | %s"%(matriz[2][0], matriz[2][1], matriz[2][2]))

def verify(matriz, value):
    if((matriz[0][0] == value) and (matriz[0][1] == value) and (matriz[0][2] == value)): return True
    if((matriz[1][0] == value) and (matriz[1][1] == value) and (matriz[1][2] == value)): return True
    if((matriz[2][0] == value) and (matriz[2][1] == value) and (matriz[2][2] == value)): return True

    if((matriz[0][0] == value) and (matriz[1][0] == value) and (matriz[2][0] == value)): return True
    if((matriz[0][1] == value) and (matriz[1][1] == value) and (matriz[2][1] == value)): return True
    if((matriz[0][2] == value) and (matriz[1][2] == value) and (matriz[2][2] == value)): return True

    if((matriz[0][0] == value) and (matriz[1][1] == value) and (matriz[2][2] == value)): return True
    if((matriz[0][2] == value) and (matriz[1][1] == value) and (matriz[2][0] == value)): return True

    return False

def chack(matriz):
    if(matriz == "X" or matriz == "O"): return True

    return False

def main():
    global plays
    global value

    player_options = int(input("""\tJOGO DA VELHA\n[1] => X\n[2] => O\n: """))

    while plays == True:
        os.system("clear" or "cls")
        if(player_options-1%2==0):
            value = "X"
            player_options = 1
        elif(player_options-1%2==1):
            value = "O"
            player_options = 0

        line = int(input("Linha %s: "%(value)))
        column = int(input("Coluna %s: "%(value)))

        if(chack(matriz[line][column])): continue
        else: matriz[line][column] = value

        showGame(matriz, value)
        time.sleep(0.5)

        player_options += 1

        if(player_options == 10): plays = False
        if(verify(matriz, value) == True): plays = False

    if(verify(matriz, "X")): print("Jogador X ganhou!")
    else:
        if(verify(matriz, "O")): print("Jogador O ganhou!")
        else: print("Velha!")

main()
