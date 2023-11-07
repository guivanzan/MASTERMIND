import numpy as np
from random import randint

def checaVitoria(lista):

    #checando na horizontal
    for i in range(3):
        j = 0
        if lista[j] == lista[j+1] == lista[j+2]:
            return True
        j = j + 3

    #checando na vertical
    for i in range(3):
        if lista[i] == lista[i+3] == lista[i+6]:
            return True
        
    #casos particulares: diagonais
    if lista[0] == lista[4] == lista[8]:
        return True
    elif lista[2] == lista[4] == lista[6]:
        return True
    
    #nenhuma vitória
    else:
        return False


def jogoDaVelha():
    
    tabuleiro =  [[1],[2],[3],
                  [4],[5],[6],
                  [7],[8],[9],]
    
    tabuleiroPrint = np.array(tabuleiro).reshape(3,3)
    print(tabuleiroPrint)

    p_count = 0
    jogadas_p = []
    jogadas_bot = []

    while p_count < 6:  
        
        if len(jogadas_bot) + len(jogadas_p) == 9:
            break
        p1 = int(input('Onde quer jogar? ')) - 1

        while p1 in jogadas_p or p1 in jogadas_bot:
            p1 = int(input('Onde quer jogar? ')) - 1

        tabuleiro[p1][0] = 'X'
        jogadas_p.append(p1)

        tabuleiroPrint = np.array(tabuleiro).reshape(3,3)

        print(tabuleiroPrint)

        if checaVitoria(tabuleiro):
            print('você ganhou!')
            break

        p_count = p_count+1

        if p_count == 5:
            break
        else:
            p1_bot = randint(0,8)
            while p1_bot in jogadas_p or p1_bot in jogadas_bot:
                p1_bot = randint(0,8)

            jogadas_bot.append(p1_bot)
            tabuleiro[p1_bot][0] = 'O'

            tabuleiroPrint = np.array(tabuleiro).reshape(3,3)

            print('')
            print(tabuleiroPrint)

            if checaVitoria(tabuleiro):
                print('você perdeu! :(')
                break   

    print('Fim do jogo')


jogoDaVelha()
    
    
