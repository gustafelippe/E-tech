# # #Questão 1
# # Dada uma lista de valores inteiros criar um programa para somar
# # os valores pares e valores ímpares:
#
# quantidade_cont = int(input("Quantos números você quer que percorra? "))
# soma_par = 0
# soma_impar = 0
#
# for i in range(quantidade_cont):
#     numeros = int(input(f"Digite {i+1} número: "))
#     if numeros % 2 == 0:
#         soma_par += numeros
#     else:
#         soma_impar += numeros
#
# print(soma_par)
# print(soma_impar)

# #Questão 2
# Dada uma palavra criar uma programa para retornar a
# quantidade de vogais e quantidade de consoantes:

# palavras = input("Quantos palavras?")
#
# vogais = "aeiou"
# quantidade_vogais = 0
# quantidade_consoantes = 0
#
# for letra in palavras:
#     if letra in vogais:
#         quantidade_vogais += 1
#     else:
#         quantidade_consoantes += 1
#
# print(f"Quantidade de consoantes: {quantidade_consoantes}")
# print(f"Quantidade de vogais: {quantidade_vogais}")

#Questão 3
# Criar um programa para adicionar funcionários. Os funcionários
# devem ter nome, sexo e salário o programa deve retornar a
# soma de salários dos homens e soma dos salários das mulheres:

# adicionar = int(input("Quantos usuários você quer adicionar: "))
# soma_homem = 0
# soma_mulher = 0
#
# for i in range(adicionar):
#     print(f"------------- {i+1} usuario-----------")
#     nome = input(f"Digite seu nome: ")
#     sexo = input(f"Digite seu sexo (M/F): ")
#     salario = float(input(f"Digite seu salário (R$): "))
#
#     if sexo == "M":
#         soma_homem += salario
#     elif sexo == "F":
#         soma_mulher += salario
#     else:
#         print("Usuario invalido")
# print(f"-------------SALÁRIOS-----------------")
# print(f"A soma do salário dos homens: ", soma_homem)
# print(f"A soma do salário das mulheres: ", soma_mulher)


