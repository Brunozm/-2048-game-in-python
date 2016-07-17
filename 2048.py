# -*- coding: cp1252 -*-
#Jogo 2048
#
#Criado por Bruno Zarjitsky
#Estudante de Meteorologia UFRJ
#Programo pq gosto
#Pretendo fazer Ciencia da Computação
#Brunozmoraes@hotmail.com
#
from random import choice


#função para dar update no mapa
def mapa():
    global mascara1
    #atualiza o mapa
    mascara1='-----------------------------\n'+\
             '| '+attm['y1']+' | '+attm['y2']+' | '+attm['y3']+' | '+attm['y4']+' |\n'+\
             '-----------------------------\n'+\
             '| '+attm['y5']+' | '+attm['y6']+' | '+attm['y7']+' | '+attm['y8']+' |\n'+\
             '-----------------------------\n'+\
             '| '+attm['y9']+' | '+attm['y10']+' | '+attm['y11']+' | '+attm['y12']+' |\n'+\
             '-----------------------------\n'+\
             '| '+attm['y13']+' | '+attm['y14']+' | '+attm['y15']+' | '+attm['y16']+' |\n'+\
             '-----------------------------\n'


#soma os numeros das colunas quando o comando é w
def somacolw():
    #percorre as colunas
    for i in range(len(colunas)):
        #cria um contador para evitar um bug na hora de somar
        debug=0
        #soma os elementos nas posições 1 e 2 da coluna
        if op[colunas[i][0]]==op[colunas[i][1]] and op[colunas[i][0]]!=' ':
            op[colunas[i][0]]=str(int(op[colunas[i][0]])+int(op[colunas[i][1]]))
            op[colunas[i][1]]=' '
            debug+=1
        #soma os elementos nas posições 1 e 3 da coluna caso a posição 2 seja vazia
        if op[colunas[i][0]]==op[colunas[i][2]] and op[colunas[i][0]]!=' ' and op[colunas[i][1]]==' ' and debug==0:
            op[colunas[i][0]]=str(int(op[colunas[i][0]])+int(op[colunas[i][2]]))
            op[colunas[i][2]]=' '
            debug+=1
        #soma os elementos nas posições 1 e 4 da coluna caso as posição 2 e 3 seja vazia
        if op[colunas[i][0]]==op[colunas[i][3]] and op[colunas[i][1]]==' ' and op[colunas[i][2]]==' ' and op[colunas[i][0]]!=' ' and debug==0:
            op[colunas[i][0]]=str(int(op[colunas[i][0]])+int(op[colunas[i][3]]))
            op[colunas[i][3]]=' '
            debug+=1
        #soma os elementos nas posições 2 e 3 da coluna
        if op[colunas[i][1]]==op[colunas[i][2]] and op[colunas[i][1]]!=' ':
            op[colunas[i][1]]=str(int(op[colunas[i][1]])+int(op[colunas[i][2]]))
            op[colunas[i][2]]=' '
            debug+=1
        #soma os elementos nas posições 2 e 4 da coluna caso a posição 3 seja vazia
        if op[colunas[i][1]]==op[colunas[i][3]] and op[colunas[i][1]]!=' ' and op[colunas[i][2]]==' ' and debug==0:
            op[colunas[i][1]]=str(int(op[colunas[i][1]])+int(op[colunas[i][3]]))
            op[colunas[i][3]]=' '
            debug+=1
        #soma os elementos nas posições 3 e 4 da coluna
        if op[colunas[i][2]]==op[colunas[i][3]] and op[colunas[i][2]]!=' ':
            op[colunas[i][3]]=str(int(op[colunas[i][2]])+int(op[colunas[i][3]]))
            op[colunas[i][2]]=' '
            debug+=1
  


#soma os numeros das colunas quando o comando é s
def somacols():
    for i in range(len(colunas)):
        debug=0
        if op[colunas[i][2]]==op[colunas[i][3]] and op[colunas[i][2]]!=' ':
            op[colunas[i][3]]=str(int(op[colunas[i][2]])+int(op[colunas[i][3]]))
            op[colunas[i][2]]=' '
            debug+=1
        if op[colunas[i][1]]==op[colunas[i][3]] and op[colunas[i][1]]!=' ' and op[colunas[i][2]]==' ' and debug==0:
            op[colunas[i][3]]=str(int(op[colunas[i][1]])+int(op[colunas[i][3]]))
            op[colunas[i][1]]=' '
            debug+=1
        if op[colunas[i][0]]==op[colunas[i][3]] and op[colunas[i][1]]==' ' and op[colunas[i][2]]==' ' and op[colunas[i][0]]!=' ' and debug==0:
            op[colunas[i][3]]=str(int(op[colunas[i][0]])+int(op[colunas[i][3]]))
            op[colunas[i][0]]=' '
            debug+=1
        if op[colunas[i][1]]==op[colunas[i][2]] and op[colunas[i][1]]!=' ':
            op[colunas[i][2]]=str(int(op[colunas[i][1]])+int(op[colunas[i][2]]))
            op[colunas[i][1]]=' '
            debug+=1
        if op[colunas[i][0]]==op[colunas[i][2]] and op[colunas[i][0]]!=' ' and op[colunas[i][1]]==' ' and debug==0:
            op[colunas[i][2]]=str(int(op[colunas[i][0]])+int(op[colunas[i][2]]))
            op[colunas[i][0]]=' '
            debug+=1
        if op[colunas[i][0]]==op[colunas[i][1]] and op[colunas[i][0]]!=' ':
            op[colunas[i][0]]=str(int(op[colunas[i][0]])+int(op[colunas[i][1]]))
            op[colunas[i][1]]=' '
            debug+=1
            


#soma os numeros das linhas quando o comando é d
def somalind():
    for i in range(len(linhas)):
        debug=0
        if op[linhas[i][2]]==op[linhas[i][3]] and op[linhas[i][2]]!=' ':
            op[linhas[i][3]]=str(int(op[linhas[i][2]])+int(op[linhas[i][3]]))
            op[linhas[i][2]]=' '
            debug+=1
        if op[linhas[i][1]]==op[linhas[i][3]] and op[linhas[i][1]]!=' ' and op[linhas[i][2]]==' ' and debug==0:
            op[linhas[i][3]]=str(int(op[linhas[i][1]])+int(op[linhas[i][3]]))
            op[linhas[i][1]]=' '
            debug+=1
        if op[linhas[i][0]]==op[linhas[i][3]] and op[linhas[i][1]]==' ' and op[linhas[i][2]]==' ' and op[linhas[i][0]]!=' ' and debug==0:
            op[linhas[i][3]]=str(int(op[linhas[i][0]])+int(op[linhas[i][3]]))
            op[linhas[i][0]]=' '
            debug+=1
        if op[linhas[i][1]]==op[linhas[i][2]] and op[linhas[i][1]]!=' ':
            op[linhas[i][2]]=str(int(op[linhas[i][1]])+int(op[linhas[i][2]]))
            op[linhas[i][1]]=' '
            debug+=1
        if op[linhas[i][0]]==op[linhas[i][2]] and op[linhas[i][0]]!=' ' and op[linhas[i][1]]==' ' and debug==0:
            op[linhas[i][2]]=str(int(op[linhas[i][0]])+int(op[linhas[i][2]]))
            op[linhas[i][0]]=' '
            debug+=1
        if op[linhas[i][0]]==op[linhas[i][1]] and op[linhas[i][0]]!=' ':
            op[linhas[i][0]]=str(int(op[linhas[i][0]])+int(op[linhas[i][1]]))
            op[linhas[i][1]]=' '
            debug+=1


#soma os numeros das linhas quando o comando é a
def somalina():
    for i in range(len(linhas)):
        debug=0
        if op[linhas[i][0]]==op[linhas[i][1]] and op[linhas[i][0]]!=' ':
            op[linhas[i][0]]=str(int(op[linhas[i][0]])+int(op[linhas[i][1]]))
            op[linhas[i][1]]=' '
            debug+=1
        if op[linhas[i][0]]==op[linhas[i][2]] and op[linhas[i][0]]!=' ' and op[linhas[i][1]]==' ' and debug==0:
            op[linhas[i][0]]=str(int(op[linhas[i][0]])+int(op[linhas[i][2]]))
            op[linhas[i][2]]=' '
            debug+=1
        if op[linhas[i][0]]==op[linhas[i][3]] and op[linhas[i][1]]==' ' and op[linhas[i][2]]==' ' and op[linhas[i][0]]!=' ' and debug==0:
            op[linhas[i][0]]=str(int(op[linhas[i][0]])+int(op[linhas[i][3]]))
            op[linhas[i][3]]=' '
            debug+=1
        if op[linhas[i][1]]==op[linhas[i][2]] and op[linhas[i][1]]!=' ':
            op[linhas[i][1]]=str(int(op[linhas[i][1]])+int(op[linhas[i][2]]))
            op[linhas[i][2]]=' '
            debug+=1
        if op[linhas[i][1]]==op[linhas[i][3]] and op[linhas[i][1]]!=' ' and op[linhas[i][2]]==' ' and debug==0:
            op[linhas[i][1]]=str(int(op[linhas[i][1]])+int(op[linhas[i][3]]))
            op[linhas[i][3]]=' '
            debug+=1
        if op[linhas[i][2]]==op[linhas[i][3]] and op[linhas[i][2]]!=' ':
            op[linhas[i][3]]=str(int(op[linhas[i][2]])+int(op[linhas[i][3]]))
            op[linhas[i][2]]=' '
            debug+=1


#funçao que move os numeros pelo mapa
def movimento():
    global comando
    comando=''
    #estabelece as possiveis combinações
    possiveis=['w','s','a','d']
    while comando not in possiveis:
        #pergunta para onde quer mover os numeros
        comando=raw_input()
    #verifica se o comando é para cima
    if comando=='w':
        somacolw()
        #percorre a lista 'colunas'
        for i in range(len(colunas)):
            #percorre uma coluna da lista 'colunas'
            for j in range(len(colunas[i])):
                #verifica se a posição selecionada é dif de ' '
                if op[colunas[i][j]]!=' ':
                    #percorre a mesma coluna acima procurando um espaço vazio
                    for w in range(len(colunas[i])):
                        #verifica se o espaço está vazio
                        if j<=w:
                          continue
                        if op[colunas[i][w]]==' ':
                            #move o numero para cima
                            op[colunas[i][w]]=op[colunas[i][j]]
                            op[colunas[i][j]]=' '
                            break
    if comando=='s':
        #percorre a lista 'colunas'
        somacols()
        for i in range(len(colunas)):
            #percorre uma coluna da lista 'colunas'
            for j in range((len(colunas[i])-1),-1,-1):
                #verifica se a posição selecionada é dif de ' '
                if op[colunas[i][j]]!=' ':
                    #percorre a mesma coluna acima procurando um espaço vazio
                    for w in range((len(colunas[i])-1),-1,-1):
                        #verifica se o espaço está vazio
                        if j>=w:
                          continue  
                        if op[colunas[i][w]]==' ':
                            #move o numero para baixo
                            op[colunas[i][w]]=op[colunas[i][j]]
                            op[colunas[i][j]]=' '
                            break
    if comando=='a':
        somalina()
        #percorre a lista 'linhas'
        for i in range(len(linhas)):
            #percorre uma coluna da lista 'linhas'
            for j in range(len(linhas[i])):
                #verifica se a posição selecionada é dif de ' '
                if op[linhas[i][j]]!=' ':
                    #percorre a mesma coluna acima procurando um espaço vazio
                    for w in range(len(linhas[i])):
                        #verifica se o espaço está vazio
                        if j<=w:
                          continue
                        if op[linhas[i][w]]==' ':
                            #move o numero para esquerda
                            op[linhas[i][w]]=op[linhas[i][j]]
                            op[linhas[i][j]]=' '
                            break
    if comando=='d':
        somalind()
        #percorre a lista 'linhas'
        for i in range(len(linhas)):
            #percorre uma coluna da lista 'linhas'
            for j in range((len(linhas[i])-1),-1,-1):
                #verifica se a posição selecionada é dif de ' '
                if op[linhas[i][j]]!=' ':
                    #percorre a mesma coluna acima procurando um espaço vazio
                    for w in range((len(linhas[i])-1),-1,-1):
                        #verifica se o espaço está vazio
                        if j>=w:
                          continue  
                        if op[linhas[i][w]]==' ':
                            #move o numero para direita
                            op[linhas[i][w]]=op[linhas[i][j]]
                            op[linhas[i][j]]=' '
                            break


                        
#verifica derrota
def der():
    global continuidade
    #define um avaliador
    continuidade=False
    #percorrer a lista de linhas
    for i in range(len(linhas)):
        #verifica se precisa continuar avaliando
        if continuidade==True:
            break
        #percorre as linhas
        for w in range(len(linhas[i])-1):
            #verifica se tem 2 numeros iguais lado a lado
            if op[linhas[i][w]]==op[linhas[i][w+1]]:
                continuidade=True
                break
            elif op[colunas[i][w]]==op[colunas[i][w+1]]:
                continuidade=True
                break

                
#inicia o jogo
def jogo():
    global op, listaletra, trocanum, trocaletra, linhas, colunas, attm
    #define oque tem em cada posição do mapa
    op={'x1':' ', 'x2':' ', 'x3':' ', 'x4':' ', 'x5':' ', 'x6':' ',\
        'x7':' ', 'x8':' ','x9':' ', 'x10':' ', 'x11':' ', 'x12':' ',\
        'x13':' ', 'x14':' ', 'x15':' ', 'x16':' '}
    #define o mapa em branco
    attm={'y1':'    ', 'y2':'    ', 'y3':'    ', 'y4':'    ', 'y5':'    ',\
          'y6':'    ', 'y7':'    ', 'y8':'    ','y9':'    ', 'y10':'    ',\
          'y11':'    ','y12':'    ', 'y13':'    ', 'y14':'    ', 'y15':'    ',\
          'y16':'    '}
    #crias as listas de x e de y
    lisy=['y1','y2','y3','y4','y5','y6','y7','y8','y9','y10','y11',\
          'y12','y13','y14','y15','y16']
    lisx=['x1','x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10',\
          'x11', 'x12', 'x13', 'x14', 'x15', 'x16']
    #teste col1: 2 8 2  col2:8 4  col3:4 4  col4: 4
    #cria as listas de linhas e colunas
    linhas=[['x1','x2','x3','x4'],['x5','x6','x7','x8'],\
            ['x9','x10','x11','x12'],['x13','x14','x15','x16']]
    colunas=[['x1','x5','x9','x13'],['x2','x6','x10','x14'],\
             ['x3','x7','x11','x15'],['x4','x8','x12','x16']]
    #cria a lista de posições que não tem numeros
    listaletra=[]
    #adiciona as posições sem numeros na lista
    for i in op.keys():
        if op[i]==' ':
            listaletra.append(i)
    #coloca 2 numeros aleatorios dentro de duas posições aleatorias
    trocanum=choice(['2','4','2'])
    trocaletra=choice(listaletra)
    op[trocaletra]=trocanum
    listaletra.remove(trocaletra)
    trocanum=choice(['2','4','2'])
    trocaletra=choice(listaletra)
    op[trocaletra]=trocanum
    #padroniza o tamanho dos espaços para entrarem no mapa
    for i in range(16):
        attm[lisy[i]]=' '*(4-len(op[lisx[i]]))+op[lisx[i]]
    #da update no mapa
    mapa()
    #mostra o mapajogo
    print mascara1
    while True:
        #loop para verificar se a jogada é possivel
        while True:
            #salva uma lista para verificar se o jogo vai se alterar depois
            # do movimento
            salvo=op.values()
            #roda a função movimento
            movimento()
            #se não tiver alteração no mapa depois do movimento este movimento
            #se torna invalido
            if op.values()!=salvo:
                break
        #zera a listaletra para entrar as novas op
        listaletra=[]
        #coloca as op disponiveis em listaletra
        for i in op.keys():
            if op[i]==' ':
                listaletra.append(i)
        #escolhe um numero para colocar no mapa
        trocanum=choice(['2','4','2'])
        #escolhe a op para posicionar o numero no mapa
        trocaletra=choice(listaletra)
        #troca o espaço vazio por um numero
        op[trocaletra]=trocanum
        #padroniza o tamanho dos espaços para entrarem no mapa
        for i in range(16):
            attm[lisy[i]]=' '*(4-len(op[lisx[i]]))+op[lisx[i]]
        #roda a função mapa
        mapa()
        #mostra o mapa
        print mascara1
        #verifica se o jogador chegou em 2048
        if '2048' in op.values():
            print'########################\n'+\
                '# PARABENS VOCE GANHOU #\n########################'
            raw_input()
            break
        #verifica se o mapa está completo
        if len(listaletra)==1:
            #roda a função derrota
            der()
            #verifica se o jogador pode continuar
            if continuidade==False:
                #define um maior
                maior=2
                #procura o maior
                for i in range(16):
                    if int(op[lisx[i]])>maior:
                        #define o novo maior
                        maior=int(op[lisx[i]])
                #mostra o record
                print 'SEU RECORD FOI: %i ' %(maior)
                raw_input()
                #finaliza o jogo
                break
        


def main():
    jogo()

if __name__=='__main__':
    main()
