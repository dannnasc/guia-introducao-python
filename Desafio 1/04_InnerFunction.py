# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor
def ext(a,b):
    def int(a,b):
        c=a+b
        return c
    return int(a,b)+5