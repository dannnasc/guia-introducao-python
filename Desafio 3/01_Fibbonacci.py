# Os números de Fibonacci são representados pela sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ]
# onde cada valor é calculado pela soma dos dois anteriores. 
# Faça um programa que gere e imprima os primeiros 10 valores desta sequência utilizando for ou while.
a,b=0,1
for i in range(0,10):
    print(a, " ")
    a, b = b, a + b
