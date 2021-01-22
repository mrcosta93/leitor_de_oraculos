import random

def sorteia_carta():
    maiores_menores = random.randrange(1, 78)
    if maiores_menores >= 23:
        carta_sorteada = sorteia_menores()
    else:
        carta_sorteada = sorteia_maiores()
    return carta_sorteada

def sorteia_menores():
    naipes = ['moedas', 'taças', 'espadas', 'bastões']
    naipe_escolhido = random.choice(naipes)
    numeros = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Rei', 'Rainha', 'Pajem', 'Cavaleiro']
    numero_escolhido = random.choice(numeros)
    resultado = numero_escolhido + ' de ' + naipe_escolhido
    return resultado

def sorteia_maiores():
    arcanos = ['O Louco', 'O Mago', 'A Sacerdotisa', 'A Imperatriz', 'O Imperador', 'O Hierofante', 'Os Amantes', 'A Carruagem', 'A Força', 'O Heremita', 'A Roda da Fortuna', 'A Justiça', 'O Enforcado', 
                'A Morte', 'A Temperança', 'O Diabo', 'A Torre', 'A Estrela', 'A Lua', 'O Sol', 'O Julgamento', 'O Mundo']
    arcano_escolhido = random.randrange(0, 22)
    resultado = "Arcano " + str(arcano_escolhido) + " - " + arcanos[arcano_escolhido]
    return resultado

if __name__ == "__main__":
    sorteia_carta()