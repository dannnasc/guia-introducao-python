# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 
n=int(input("Entre  a number: "))
def primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(primo(n))
