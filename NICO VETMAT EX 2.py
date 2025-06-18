fila = ["João", "Maria", "Raymond"]
while True:
    print(fila)
    nome = input("Digite seu nome: ").capitalize()
    fila.append(nome)
    fila.pop(0)