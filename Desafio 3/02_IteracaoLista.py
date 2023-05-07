# Faça um programa que receba 5 números e retorne o maior e o menor numero, a soma e a média dos números.
total=0
maior=0
menor=0
lista = [1,77,87,-5, 10]
for i in lista:
    if i>maior:
        maior=i
    if i<menor:
        menor=i
    total=total+i

print("Maior:",maior)
print("Menor:",menor)
print("Soma",total)
print("Média",total/(len(lista)))

