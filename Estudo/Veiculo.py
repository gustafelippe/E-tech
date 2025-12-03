# class Veiculo:
#     #Classe PAI (GUS)
#     def __init__(self, cor: str, modelo: str):
#         self.cor = cor
#         self.modelo = modelo
#     def descricao(self)-> str:
#         return f"{self.cor} {self.modelo}"
# class Carro(Veiculo):
#     def __init__(self, cor: str, modelo: str,ano: int, portas: int):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.portas = portas
#     def descricao(self)-> str:
#         return (f" - Modelo: {self.modelo}  \n"
#                 f"COR: {self.cor} \n"
#                 f"ANO: {self.ano} \n"
#                 f"PORTAS: {self.portas }")
#
# lista_carros=[] #coloeção de carros
#
# for i in range(1,5): #Cadastro de carros (4)
#     modelo = input("Qual o modelo do carro: ")
#     cor=input("Qual o cor do carro: ")
#     ano= int(input("Qual o ano do carro: "))
#     portas=int(input("Quantos portas: "))
#     carro_uno = (Carro(cor, modelo, ano, portas))  # criando uma instancia da classe carro
#     lista_carros.append(carro_uno) #adicionando o carro na lista
#
# for carro in lista_carros: #Exibir descrição dos carros
#     print (carro.descricao())

#Questão 3
class Funcionario:
    def __init__(self, sexo : str , nome: str):
        self.sexo = sexo
        self.nome = nome
    def descricao(self)->str:
        return f"{self.homem} e {self.mulher}"

class adicionar(Funcionario):
    def __init__(self, sexo : str, nome : str, salarios: float):
        self.sexo = sexo
        self.nome = nome
        self.salarios = salarios
    def descricao(self)->str:
        return f"{self.sexo}, {self.salarios}, {self.nome}"

lista_funcionarios = []


for i in range(adicionar):
     print(f"------------- {i+1} usuario-----------")
     nome = input(f"Digite seu nome: ")
     sexo = input(f"Digite seu sexo (M/F): ")
     salario = float(input(f"Digite seu salário (R$): "))