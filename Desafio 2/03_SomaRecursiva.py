# Defina a função soma_nat de forma recursiva que recebe como argumento um número natural  n  e devolve a soma de todos os números naturais até  n .

def soma_nat(n):
    if n==0:
        return 0
    return (soma_nat(n-1))+ n