#!/usr/bin/python3

import socket
HOST = "192.168.162.146"
PORT = 12000

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    print("\n\n Bem vindo ao jogo da velha!\n\n")

    jogador_1 = input("Digite o seu nickname: ")
    cliente.sendto(jogador_1.encode(),(HOST,PORT))

    jogador_2, endereco_ip_servidor = cliente.recvfrom(2048)

    mensagem, endereco_ip_servidor = cliente.recvfrom(2048)
    print(mensagem.decode())

    mensagem, endereco_ip_servidor = cliente.recvfrom(2048)
    print(mensagem.decode())

    #Iniciando o jogo
    while True:
        continuacao_rodada, endereco_ip_servidor = cliente.recvfrom(2048)
        print(continuacao_rodada.decode())
        if(continuacao_rodada.decode() == "0"):
            print(continuacao_rodada.decode())
            print("Saindooooo")
            break

        vez_do_jogador, endereco_ip_servidor = cliente.recvfrom(2048)
        vez_do_jogador = vez_do_jogador.decode()
        print(f"Vez do jogador {vez_do_jogador}.\nOlhe o tabuleiro e escolha uma opção:")


        tabuleiro, endereco_ip_servidor = cliente.recvfrom(2048)
        print(tabuleiro.decode())


        sua_vez = jogador_1 == vez_do_jogador
        print("a sua vez é",sua_vez)

        if(sua_vez == True):

            posicao = input("\n\nDigite a posicao: ")
            cliente.sendto(posicao.encode(),(HOST,PORT))

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
    elif(verificacao_winner.decode() == "0"):
        print(f"\n\nVencedor: {jogador_2}!")


    jogar_novamente = input("Deseja jogar novamente?\nDigite (y) para sim ou (n) para não: ")
    cliente.sendto(jogar_novamente.encode(),(HOST,PORT))