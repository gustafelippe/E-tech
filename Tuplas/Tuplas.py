# #Exercicio 1
# coordenadas = (10.5, 20.3)
#
# coordenadas.append(30)
#
# print("tupla original: ", coordenadas) ## Vai dar erro, pq a tupla é imutavel

#Exercicio 2
# Dada a tupla registro_aulas, encontre e imprima:
# O número de vezes que a string "Phyton" aparece
# na tupla, usando o método count()
# O índice da primeira ocorrência da string "SLQ",
# usando o método index()

# registro_aulas = ("Python", "SQL", "Java", "Python", "Web")
#
# contagem_python = registro_aulas.count("Python")
# print(contagem_python)
#
# indice_sql = registro_aulas.index("SQL")
# print(registro_aulas[indice_sql])

# Exercicio 3
#
# registro1 = ("Ana", 28, "São Paulo")
# registro2 = ("Pedro", 35, "Rio de Janeiro")
#
# registros =  [registro1, registro2]
# print(f"1. Lista Inicial: {registros}")
#
# indice = registros[1][0]
# print(f"2. Segunda Lista:", indice)
#
# registro3 = ("Carla", 22, "Recife")
# registros.append(registro3)
# print(registros)
qtd = int(input("Quantos números deseja informar? "))

soma_pares = 0
soma_impares = 0

for i in range(qtd):
    num = int(input(f"Digite o {i + 1}º número: "))

    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print("\nSoma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
