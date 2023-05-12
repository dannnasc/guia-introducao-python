import os

def exibir_menu():
    print("******* Gerenciador de Filmes ******* \n")
    print("1. Inserir novo filme\n")
    print("2. Ver filmes por gênero\n")
    print("3. Buscar filme por nome\n")
    print("4. Sair\n")

def inserir_filme():
    generos = ["Aventura", "Comedia", "Acao", "Drama", "Terror", "Fantasia"]
    nome = input("Digite o nome do filme: \n")
    data = input("Digite a data de visualização (DD/MM/AAAA): ")
    nota = input("Digite a nota do filme (0-10): ")
    genero = input("Digite o gênero do filme: ")
    
    if genero not in generos:
        print("Gênero inválido.")
    
    arquivo = genero.lower() + ".txt"
    
    with open(arquivo, "a") as f:
        f.write(f"{nome},{data},{nota}\n")
    
    print("Filme inserido com sucesso.\n")

def ver_filmes_por_genero():
    generos = ["Aventura", "Comedia", "Acao", "Drama", "Terror", "Fantasia"]
    print("=== Filmes por Gênero ===\n")
    for i, genero in enumerate(generos):
        arquivo = genero.lower() + ".txt"
        if os.path.exists(arquivo):
            print(f" {i}. {genero}")
    
    escolha = int(input("Selecione o número do gênero para ver os filmes: \n"))
    genero_escolhido = generos[escolha]
    arquivo = genero_escolhido.lower() + ".txt"
    
    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            filmes = f.readlines()
            for filme in filmes:
                nome, data, nota = filme.strip().split(",")
                print(f"Nome: {nome} | Data: {data} | Nota: {nota}")
    else:
        print("Não há filmes nesse gênero.")

def buscar_filme_por_nome():
    nome_busca = input("Digite o nome do filme a ser buscado: ")
    generos = ["Aventura", "Comedia", "Acao", "Drama", "Terror", "Fantasia"]
    filmes_encontrados = []
    
    for genero in generos:
        arquivo = genero.lower() + ".txt"
        if os.path.exists(arquivo):
            with open(arquivo, "r") as f:
                filmes = f.readlines()
                for filme in filmes:
                    nome, data, nota = filme.strip().split(",")
                    if nome.lower() == nome_busca.lower():
                        filmes_encontrados.append((genero, nome, data, nota))
    
    if filmes_encontrados:
        print("=== Filmes Encontrados ===")
        for genero, nome, data, nota in filmes_encontrados:
            print(f"Gênero: {genero} | Nome: {nome} | Data: {data} | Nota: {nota}")
    else:
        print("Nenhum filme encontrado.")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: \n")
        
        if opcao == "1":
            inserir_filme()
        if opcao == "2":
            ver_filmes_por_genero()
        if opcao == "3":
            buscar_filme_por_nome()
        if opcao == "4":
            print("Saindo\n")
            break
if __name__ == "__main__":
    main()
