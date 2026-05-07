import random
vezes=int(input("Digite a quantidade de números aleatórios: "))
for n in range(10):
    sequencia = [random.randint(1, 101) for i in range(vezes)]
print(sequencia)  