# Defina a função div que recebe como argumentos dois números naturais  m  e  n  e 
# devolve o resultado da divisão inteira de  m  por  n . 

# div(7,2)
# Esperado: 3
def div(m,n):
    if m<n:
        return 0
    return div(m-n,n) + 1
print("",div(7,2))