import random
# Baralhos possíveis
import tarot
import servidores
import lenormand
import runas
# Tiragens possíveis
import tiragens

def escolha_jogo():
    tipo = 0
    while tipo < 1 or tipo > 6:
        tipo = int(input("Escolha qual tiragem você deseja:\n1) Simples (3 cartas)\n2) Cruz celta (10 cartas)\n3) Templo de mercúrio (8 cartas)\n4) Templo de afrodite (7 cartas)\n5) Templo de marte (5 cartas)\n6) Livre\n"))
    return tipo

def escolhe_baralho():
    escolha = 0
    while escolha < 1 or escolha > 4:
        escolha = int(input("\nEscoha qual baralho você deseja usar:\n1) Tarot\n2) 40 Servidores\n3) Lenormand\n4) Runas\n"))
        if escolha == 1:
            baralho = tarot
        elif escolha == 2:
            baralho = servidores
        elif escolha == 3:
            baralho = lenormand
        elif escolha == 4:
            baralho = runas
        else:
            print("Entre com uma opção válida")
    return baralho

def jogar():
    baralho = escolhe_baralho()
    tipo = escolha_jogo()
    if tipo == 1:
        tiragens.simples(baralho)
    elif tipo == 2:
        tiragens.celta(baralho)
    elif tipo == 3:
        tiragens.templo_de_mercurio(baralho)
    elif tipo == 4:
        tiragens.templo_de_afrodite(baralho)
    elif tipo == 5:
        tiragens.templo_de_marte(baralho)
    elif tipo == 6:
        quantidade = int(input("Escolha quantas cartas você quer tirar: "))
        i = 1
        while i <= quantidade:
            carta = baralho.sorteia_carta()
            print("Carta " + str(i) + ": " + carta)
            i += 1

repetir = True
jogar()
while repetir:
    replay = input("Deseja sair? Se sim, digite 'sair'. Se não, digite qualquer outra tecla. ").lower()
    if replay == 'sair':
        repetir = False
        break
    else:
        jogar()