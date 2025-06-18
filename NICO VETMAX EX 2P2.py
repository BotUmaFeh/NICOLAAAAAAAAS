livros = ["Autodefesa Psíquica", "50 Tons de Cinza", "Kama Sutra"]
while True:
    print(livros)
    livro = input("Digite o livro: ").capitalize()
    livros.pop(0)
    livros.insert(0, livro)