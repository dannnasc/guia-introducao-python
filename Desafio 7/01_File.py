"""
referencia: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# 1-Abra o arquivo do diretorio atual "foo.txt"
# Printe todo o conteudo do arquivo , então feche o arquivo
f = open('foo.txt', 'r', encoding="utf-8")
s=f.read()
print(s)
f.close()
# 2- Crie um arquivo chamado "bar.txt" 
# Abra o arquivo e conte quanta vezes a palavra "sir" aparece 
# Escreva no arquivo que voce criou quantas palavras foram encontradas
# Feche o arquivo
f = open('foo.txt', 'r', encoding="utf-8")
s=f.read()
counter=s.count('sir')
b = open('bar.txt', 'w', encoding="utf-8")
b.write(str(counter))
b.close()
f.close()

