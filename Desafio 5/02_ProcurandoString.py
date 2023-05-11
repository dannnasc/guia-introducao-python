#   Faça um funcão que leia o nome de uma pessoa
#   e diga se ela tem "Silva" no nome.

s="Daniel"
def has_silva(s):
    if "Silva" in s:
        print("Tem Silva")
    else:
        print("Não tem Silva")
        
        
print(has_silva(s))