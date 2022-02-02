#!/usr/bin/python3

import socket
HOST = "localhost"
PORT = 12000

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((HOST,PORT))

while True:
    print("Aguardando jogadores...")
    #Esperando os jogadores se conectarem

    #Jogador 1 se conectou
    jogador_1, endereco_ip_jogador_1 = servidor.recvfrom(2048)
    jogador_1 = jogador_1.decode()
    
    print(f"O jogador {jogador_1} entrou no jogo\nAguardando o proximo jogador...")

    #Jogador 2 se conectou
    jogador_2, endereco_ip_jogador_2 = servidor.recvfrom(2048)
    jogador_2 = jogador_2.decode()


    #Informando o jogador 1 que o jogador 2 entou no jogo
    servidor.sendto(jogador_2.encode(), endereco_ip_jogador_1)
    mensagem_para_jogadores = (f"O jogador {jogador_2} entrou no jogo\n")
    print(mensagem_para_jogadores)
    servidor.sendto(mensagem_para_jogadores.encode(), endereco_ip_jogador_1)

    #Informando o jogador 2 que o jogador 1 entou no jogo
    servidor.sendto(jogador_1.encode(), endereco_ip_jogador_2)
    mensagem_para_jogadores = (f"O jogador {jogador_1} entrou no jogo\n")
    print(mensagem_para_jogadores)
    servidor.sendto(mensagem_para_jogadores.encode(), endereco_ip_jogador_2)

    #Informando quais jogadores que estão jogando
    mensagem_para_jogadores = (f"Os jogadores são: {jogador_1} e {jogador_2}.\nIniciando o Jogo...\n")
    servidor.sendto(mensagem_para_jogadores.encode(), endereco_ip_jogador_1)
    servidor.sendto(mensagem_para_jogadores.encode(), endereco_ip_jogador_2)


    #Iniciando o jogo
    while True:
        #Inicia pelo jogador X (Jogador 1)
        jogador = "X"
        board = [
            "-","-","-",
            "-","-","-",
            "-","-","-"
        ]

        winner = None
        #Jogando enquanto não há ganhadores
        
        while(winner == None):
            #Indicando que podemos dar sequencia na rodada para os clients
            continuacao_rodada = "isso aquiiiii"
            servidor.sendto(continuacao_rodada.encode(), endereco_ip_jogador_1)
            servidor.sendto(continuacao_rodada.encode(), endereco_ip_jogador_2)

            #Informando a vez do jogador
            if(jogador == "X"):
                servidor.sendto(jogador_1.encode(), endereco_ip_jogador_1)
                servidor.sendto(jogador_1.encode(), endereco_ip_jogador_2)

            else:
                servidor.sendto(jogador_2.encode(), endereco_ip_jogador_1)
                servidor.sendto(jogador_2.encode(), endereco_ip_jogador_2)


            #Mostrando o tabuleiro
            tabuleiro = (f"Posições: |   Tabuleiro\n          |\n  0|1|2   |   {board[0]} | {board[1]} | {board[2]}\n  3|4|5   |   {board[3]} | {board[4]} | {board[5]}\n  6|7|8   |   {board[6]} | {board[7]} | {board[8]}")
            print("\n",tabuleiro)
            servidor.sendto(tabuleiro.encode(), endereco_ip_jogador_1)
            servidor.sendto(tabuleiro.encode(), endereco_ip_jogador_2)


            #Possibilitando a jogada do jogador da rodada
            if(jogador == "X"):
                #recebe a posicao escolhida
                posicao, endereco_ip_jogador_1 = servidor.recvfrom(2048)
                posicao = int(posicao.decode())

                #verifica se há esta posicao no tabuleiro
                if not 0 <= posicao <= 8:
                    print("Posicao inexistente\n")
                    posicao_verificada = "1"
                    servidor.sendto(posicao_verificada.encode(), endereco_ip_jogador_1)
                    continue
                #verifica se a posicao já não foi previamente escolhida
                if (board[posicao] != "-"):
                    print("Posicao ja ocupada\n")
                    posicao_verificada = "2"
                    servidor.sendto(posicao_verificada.encode(), endereco_ip_jogador_1)
                    continue
                else:
                    posicao_verificada = "0"
                    servidor.sendto(posicao_verificada.encode(), endereco_ip_jogador_1)
                    

            else:
                posicao, endereco_ip_jogador_2 = servidor.recvfrom(2048)
                posicao = int(posicao.decode())

                if not 0 <= posicao <= 8:
                    print("Posicao inexistente\n")
                    posicao_verificada = "1"
                    servidor.sendto(posicao_verificada.encode(), endereco_ip_jogador_2)
                    continue
            
                if (board[posicao] != "-"):
                    print("Posicao ja ocupada\n")
                    posicao_verificada = "2"
                    servidor.sendto(posicao_verificada.encode(), endereco_ip_jogador_2)
                    continue
                else:
                    posicao_verificada = "0"
                    servidor.sendto(posicao_verificada.encode(), endereco_ip_jogador_1)
                    

            #Aplicando a posicao escolhida no tabuleiro
            board[posicao] = jogador
            
            #verificando se há ganhadores
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
            

            #verificando se não esgostou os espaços
            if not "-" in board:
                print("Acabou os espaços")
                break

            #trocando de turno de jogadores
            if (jogador == "X"):
                jogador = "O"
            else:
                jogador = "X"



        #informando ao client que não terá mais rodadas
        continuacao_rodada = "0"
        servidor.sendto(continuacao_rodada.encode(), endereco_ip_jogador_1)
        servidor.sendto(continuacao_rodada.encode(), endereco_ip_jogador_2)
            
        #Mostrando o tabuleiro final
        print("\n\n")
        tabuleiro_final = (f"Posições: |   Tabuleiro final\n          |\n  0|1|2   |   {board[0]} | {board[1]} | {board[2]}\n  3|4|5   |   {board[3]} | {board[4]} | {board[5]}\n  6|7|8   |   {board[6]} | {board[7]} | {board[8]}")
        print(tabuleiro_final)
        servidor.sendto(tabuleiro_final.encode(), endereco_ip_jogador_1)
        servidor.sendto(tabuleiro_final.encode(), endereco_ip_jogador_2)

        #informando os ganhadores
        if(winner == "X"):
            print(f"\n\nVencedor: {jogador_1}!")
            verificacao_winner = "1"
        elif(winner == "O"):
            print(f"\n\nVencedor: {jogador_2}!")
            verificacao_winner = "2"
        else:
            print("Deu empate!")
            verificacao_winner = "0"

        servidor.sendto(verificacao_winner.encode(), endereco_ip_jogador_1)
        servidor.sendto(verificacao_winner.encode(), endereco_ip_jogador_2)


        #Verificando se haverá um novo jogo com cada jogador
        confirmacao_continuar = 0
        jogar_novamente_1, endereco_ip_jogador_1 = servidor.recvfrom(2048)
        confirmacao_continuar += 1
        jogar_novamente_2, endereco_ip_jogador_2 = servidor.recvfrom(2048)
        confirmacao_continuar += 1



        if(confirmacao_continuar.decode() == 2):
            continue
        else:
            break        
