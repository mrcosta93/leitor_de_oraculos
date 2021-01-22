import random

def sorteia_carta():
    cartas = ['Cavaleiro', 'Trevo', 'Navio', 'Casa', 'Árvore', 'Nuvens', 'Serpente', 'Caixão', 'Buquê', 'Foice', 'Chicotes', 'Corujas', 'Criança', 
                'Raposa', 'Urso', 'Estrelas', 'Cegonhas', 'Cão', 'Torre', 'Jardim', 'Montanha', 'Caminhos', 'Ratos', 'Coração', 'Anel', 'Livro', 
                'Carta', 'Cavalheiro', 'Dama', 'Lírios', 'Sol', 'Lua', 'Chave', 'Peixes', 'Âncora', 'Cruz']
    carta_escolhida = random.choice(cartas)
    return carta_escolhida

if __name__ == "__main__":
    sorteia_carta()