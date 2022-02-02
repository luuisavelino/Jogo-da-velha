#!/usr/bin/python3

import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('',12000))

while True:
    jogador_1, endereco_ip_client = servidor.recvfrom(2048)
    jogador_1 = jogador_1.decode()
    print(jogador_1)

    jogador_2, endereco_ip_client = servidor.recvfrom(2048)
    jogador_2 = jogador_2.decode()
    print(jogador_2)


    while True:
        jogador = "X"
        board = [
            "-","-","-",
            "-","-","-",
            "-","-","-"
        ]

        winner = None

        while(winner == None):
            continuacao_rodada = "1"
            servidor.sendto(continuacao_rodada.encode(), endereco_ip_client)

            if(jogador == "X"):
                servidor.sendto(jogador_1.encode(), endereco_ip_client)
            else:
                servidor.sendto(jogador_2.encode(), endereco_ip_client)

            tabuleiro = (f"Posições: |   Tabuleiro\n          |\n  0|1|2   |   {board[0]} | {board[1]} | {board[2]}\n  3|4|5   |   {board[3]} | {board[4]} | {board[5]}\n  6|7|8   |   {board[6]} | {board[7]} | {board[8]}")
            servidor.sendto(tabuleiro.encode(), endereco_ip_client)

            posicao, endereco_ip_client = servidor.recvfrom(2048)
            posicao = int(posicao.decode())


            if not 0 <= posicao <= 8:
                #print("Posicao inexistente\n")
                posicao_verificada = "1"
                servidor.sendto(posicao_verificada.encode(), endereco_ip_client)
                continue
            
            if (board[posicao] != "-"):
                #print("Posicao ja ocupada\n")
                posicao_verificada = "2"
                servidor.sendto(posicao_verificada.encode(), endereco_ip_client)
                continue

            posicao_verificada = "0"

            servidor.sendto(posicao_verificada.encode(), endereco_ip_client)
            
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

        
        continuacao_rodada = "0"
        servidor.sendto(continuacao_rodada.encode(), endereco_ip_client)
            

        print("\n\n")
        tabuleiro_final = (f"Posições: |   Tabuleiro\n          |\n  0|1|2   |   {board[0]} | {board[1]} | {board[2]}\n  3|4|5   |   {board[3]} | {board[4]} | {board[5]}\n  6|7|8   |   {board[6]} | {board[7]} | {board[8]}")
        servidor.sendto(tabuleiro_final.encode(), endereco_ip_client)



        if(winner == "X"):
            #print(f"\n\nVencedor: {jogador_1}!")
            verificacao_winner = "1"
        elif(winner == "O"):
            #print(f"\n\nVencedor: {jogador_2}!")
            verificacao_winner = "2"
        else:
            #print("Deu empate!")
            verificacao_winner = "0"

        servidor.sendto(verificacao_winner.encode(), endereco_ip_client)


        jogar_novamente, endereco_ip_client = servidor.recvfrom(2048)
        if(jogar_novamente.decode() == "y"):
            continue
        else:
            break        