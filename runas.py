import random

def sorteia_carta():
    cartas = ['Fehu', 'Uruz', 'Thurisaz', 'Ansuz', 'Raidho', 'Kenaz', 'Gebo', 'Wunjo',
                'Hagalaz', 'Nauthiz', 'Isa', 'Jera', 'Wihwaz', 'Perthro', 'Algiz', 'Sowelo',
                'Tiewaz', 'Berkana', 'Ehwaz', 'Mannaz', 'Laguz', 'Inguz', 'Dagaz', 'Othala']
    carta_escolhida = random.choice(cartas)
    return carta_escolhida

if __name__ == "__main__":
    sorteia_carta()