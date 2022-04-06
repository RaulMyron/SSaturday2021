lista_chess = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
lista_chess[0][0] = 'o'
#print(lista_chess)

chess_lista = [['-']*3]*3 #cuidado, objeto autorefenciado
chess_lista[0][0]='o'
#print(chess_lista)

chess_list = [['-' for x in range(3)] for x in range(3)]
chess_list[0][0] = 'o'
#print(chess_list)

meu_xadrez = []
for l in range(3):
    meu_xadrez.append(['-']*3)
#meu_xadrez[0][0] = 'o'
#print(meu_xadrez)

def minha_funcao_verificar(entrada):
    return True

for contador in range(9):
    if contador%2==0: #se for par
        entrada = input(f'Por falor insira a coordenada de x: ')
        if(entrada == '-1'):
            break
        x,y = entrada.split()
        if(minha_funcao_verificar(entrada)):
            meu_xadrez[int(x)][int(y)] = 'x'
            #verifica se ganhou
            print("voce quer realmente fazer essa jogada?")
            confirmacao = input()
            if(confirmacao == 'Não'):
                print("ENTREI AQUI")
                meu_xadrez[int(x)][int(y)] = '-'
        else:
            print("valor invalido vc perdeu")
    else:
        entrada = input(f'Por falor insira o valor de o: ')
        if(entrada == '-1'):
            break
        if(minha_funcao_verificar(entrada)):
            x,y = entrada.split()
            meu_xadrez[int(x)][int(y)] = 'o'
            #verifica se ganhou
        else:
            print("valor invalido vc perdeu")

print("*"*7)

for sublista in meu_xadrez:
    #print(*sublista)
    print('',*sublista,sep='|',end='|\n')
    
print("*"*7)