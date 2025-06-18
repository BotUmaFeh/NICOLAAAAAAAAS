print ("Digite 8 números: ")
lista = []
lista10 = []
cont = 1
while cont <= 8:
    numero = int(input())
    lista.append(numero)
    cont = cont + 1
for i in lista:
    if i > 10:
        lista10.append(i)
print(lista10)