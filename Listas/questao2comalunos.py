lista = ['Raul','Ester',2002,2004,2006,12,False,True,[1,2]]
lista_com_int = []

for elemento in lista:
    if type(elemento) == int:
        lista_com_int.append(elemento)
        
print(lista_com_int)
        