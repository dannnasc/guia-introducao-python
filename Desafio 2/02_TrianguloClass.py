# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.
X=8
Y=9
Z=10
if not abs(Y-Z) < X < Y+Z and abs(X-Z) < Y < X+Z and abs(X-Y) < Z < X+Y : 
    print("Não forma um triângulo")
if X==Y and X==Z and Y==Z:
    print("Equilátero")
if X==Y or X==Z or Y==Z:
    print("Isósceles")
if X!=Y and X!=Z and Y!=Z:
    print("Escaleno")
