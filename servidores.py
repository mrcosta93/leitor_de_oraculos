import random

def sorteia_carta():
    cartas = ['A Aventureira', 'A Balanceadora', 'A Carnal', 'A Casta', 'O Maestro', 'O Contemplador', 'A Dançarina', 'A Morta', 'O Exaurido', 'O Desesperado', 'O Diabo', 'O Explorador', 'O Olho', 
                'O Pai', 'O Reparador', 'A Afortunada', 'O Guardião de Portal', 'O Doador', 'O Guru', 'A Curandeira', 'A Ideia', 'O Levitador', 'A Bibliotecária', 'Os Enamorados', 'O Mestre', 'A Mídia', 
                'O Mensageiro', 'O Monge', 'A Lua', 'A Mãe', 'O Adversário', 'O Planeta', 'O Protetor', 'A Manifestante', 'O Abridor de Caminhos', 'O Santo', 'A Vidente', 'O Sol', 'O Pensador', 'A Bruxa']
    carta_escolhida = random.choice(cartas)
    return carta_escolhida

if __name__ == "__main__":
    sorteia_carta()