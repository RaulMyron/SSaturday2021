lista = []
while True:
    entrada = int(input())
    if(entrada == -1):
        break
    else:
        lista.append(entrada)

print(lista.sort())