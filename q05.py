vezes=int(input("Digite a quantidade de números: "))
valores = []

if vezes > 0:
    for i in range(vezes):
        num= int(input(f"Digite o valor {i+1}:"))
        valores.append(num)
        soma=sum(valores)
        media=soma/vezes
        maior=max(valores)
        menor=min(valores)
        cont=0
    for g in valores:
        if g > media:
            cont+=1

print(f"A soma é: {soma}")
print(f"A média é: {media}")               
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"A quantidade de números acima da média é: {cont}")