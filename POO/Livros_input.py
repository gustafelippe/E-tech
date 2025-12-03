class Livros:
    def __init__(self, titulo_dado, autor_dado):
        self.titulo = titulo_dado
        self.autor = autor_dado

    def exibir_info(self):
        print(f"Livro Cadastrado: {self.titulo} - {self.autor}")
print("-" * 40)
print("  Cadastro de novo Livro (1/2)")
print("-" * 40)

titulo_a = input("Digite o titulo do autor: ")
autor_a = input("Digite o autor do autor: ")

livro_a = Livros(titulo_a, autor_a)

print("-" * 40)
print("  Cadastro de novo Livro (2/2) ")
print("-" * 40)

titulo_b = input("Digite o titulo do livro: ")
autor_b = input("Digite o autor do autor: ")

livro_b = Livros(titulo_b, autor_b)

print("\n" + "-" * 40)
print("Verificação final: o Poder do 'Self'")
print("-" * 40)

livro_a.exibir_info()
livro_b.exibir_info()

print("\n --- Acessando atributos Diretamente---")
print(f"titulo no objeto A: {livro_a.titulo}")
print(f"autor no objeto B: {livro_b.titulo}")
print(f"autor no objeto A: {livro_a.autor}")
print(f"autor no objeto B: {livro_b.autor}")