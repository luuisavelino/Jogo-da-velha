#!/usr/bin/python3




print("\n\n Bem vindo ao jogo da velha!\n\n")

jogador_1 = input("Player 1 (X) - Digite o seu nickname: ")
jogador_2 = input("Player 2 (O) - Digite o seu nickname: ")

while True:
    
    jogador = "X"
    board = [
        "-","-","-",
        "-","-","-",
        "-","-","-"
    ]

    winner = None

    while(winner == None):
        
        print("Posições: |   Tabuleiro")
        print("          |")
        print(f"  0|1|2   |   {board[0]} | {board[1]} | {board[2]}")
        print(f"  3|4|5   |   {board[3]} | {board[4]} | {board[5]}")
        print(f"  6|7|8   |   {board[6]} | {board[7]} | {board[8]}")

        posicao = int(input("\n\nDigite a posicao que deseja jogar: "))

        if not 0 <= posicao <= 8:
            print("Posicao inexistente\n")
            continue
        
        if (board[posicao] != "-"):
            print("Posicao ja ocupada\n")
            continue

        board[posicao] = jogador
        
        
        if (
            (board[0] == "X" and board[1] == "X" and board[2] == "X") or
            (board[3] == "X" and board[4] == "X" and board[5] == "X") or
            (board[6] == "X" and board[7] == "X" and board[8] == "X") or
            (board[0] == "X" and board[3] == "X" and board[6] == "X") or
            (board[1] == "X" and board[4] == "X" and board[7] == "X") or
            (board[2] == "X" and board[5] == "X" and board[8] == "X") or
            (board[0] == "X" and board[4] == "X" and board[8] == "X") or
            (board[2] == "X" and board[4] == "X" and board[6] == "X")
        ):
            winner = "X"

        if (
            (board[0] == "O" and board[1] == "O" and board[2] == "O") or
            (board[3] == "O" and board[4] == "O" and board[5] == "O") or
            (board[6] == "O" and board[7] == "O" and board[8] == "O") or
            (board[0] == "O" and board[3] == "O" and board[6] == "O") or
            (board[1] == "O" and board[4] == "O" and board[7] == "O") or
            (board[2] == "O" and board[5] == "O" and board[8] == "O") or
            (board[0] == "O" and board[4] == "O" and board[8] == "O") or
            (board[2] == "O" and board[4] == "O" and board[6] == "O")
        ):
            winner = "O"
        

        if not "-" in board:
            break

            
        if (jogador == "X"):
            jogador = "O"
        else:
            jogador = "X"

    print("\n\n")
    print("Posições: |   Tabuleiro")
    print("          |")
    print(f"  0|1|2   |   {board[0]} | {board[1]} | {board[2]}")
    print(f"  3|4|5   |   {board[3]} | {board[4]} | {board[5]}")
    print(f"  6|7|8   |   {board[6]} | {board[7]} | {board[8]}")

    if(winner == "X"):
        print(f"\n\nVencedor: {jogador_1}!")
    elif(winner == "O"):
        print(f"\n\nVencedor: {jogador_2}!")
    else:
        print("Deu empate!")



    jogar_novamente = input("Deseja jogar novamente?\nDigite (y) para sim ou (n) para não: ")
    if(jogar_novamente == "y"):
        continue
    else:
        break        

