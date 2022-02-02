#!/usr/bin/python3

import socket
endereco_ip="192.168.162.146"


cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print("\n\n Bem vindo ao jogo da velha!\n\n")

    jogador_1 = input("Player 1 (X) - Digite o seu nickname: ")
    cliente.sendto(jogador_1.encode(),(endereco_ip,12000))

    jogador_2 = input("Player 2 (O) - Digite o seu nickname: ")
    cliente.sendto(jogador_2.encode(),(endereco_ip,12000))

    
    while True:
        continuacao_rodada, endereco_ip_servidor = cliente.recvfrom(2048)
        if(continuacao_rodada.decode() == "0"):
            break
        
        print("\n\n")
        vez_do_jogador, endereco_ip_servidor = cliente.recvfrom(2048)
        print(f"Vez do jogador {vez_do_jogador.decode()}.\nOlhe o tabuleiro e escolha uma opção:")


        tabuleiro, endereco_ip_servidor = cliente.recvfrom(2048)
        print(tabuleiro.decode())

        posicao = input("\n\nDigite a posicao: ")
        cliente.sendto(posicao.encode(),(endereco_ip,12000))

        posicao_verificada, endereco_ip_servidor = cliente.recvfrom(2048)
        if(posicao_verificada.decode()=="1"):
            print("Posicao inexistente\n")
        if(posicao_verificada.decode()=="2"):
            print("Posicao ja ocupada\n")


    

    tabuleiro_final, endereco_ip_servidor = cliente.recvfrom(2048)
    print(tabuleiro_final.decode())

        
    verificacao_winner, endereco_ip_servidor = cliente.recvfrom(2048)
    if(verificacao_winner.decode() == "1"):
        print(f"\n\nVencedor: {jogador_1}!")
    elif(verificacao_winner.decode() == "2"):
        print(f"\n\nVencedor: {jogador_2}!")
    elif(verificacao_winner.decode() == "O"):
        print(f"\n\nVencedor: {jogador_2}!")


    jogar_novamente = input("Deseja jogar novamente?\nDigite (y) para sim ou (n) para não: ")
    cliente.sendto(jogar_novamente.encode(),(endereco_ip,12000))