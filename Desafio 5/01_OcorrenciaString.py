#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

s=str(input("Entre  a sentence: "))

print(s.count('A'))
print(s.find('A'))
print(s.rfind('A'))