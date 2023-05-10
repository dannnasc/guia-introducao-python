#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')
v=[]

a=map(lambda x:list(filter(lambda l: l in "aeiou", x)) , frutas)
print (frutas,"\n",list(a))