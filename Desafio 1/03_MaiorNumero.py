# Escreva uma função para encontrar o maior entre 3 numeros

def Max(a,b,c):
    if a>b and a>c:
        maior=a
        return maior
    if b>a and b>c: 
        maior=b
        return maior
    return c
print(Max(1,3,3))    
    