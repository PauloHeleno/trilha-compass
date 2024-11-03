
# etapa 1
def encontrar_ator_com_mais_filmes(arquivo_csv):
    try:
        with open(arquivo_csv, "r") as arquivo:
            linhas = arquivo.readlines()

        maior_quantidade_filmes = 0
        ator_ou_atriz_maior_numero_filmes = ''

        for linha in linhas[1:]:
            conteudo = linha.strip().split(",")

            try:
                numero_filmes = int(conteudo[2])
            except ValueError:
                try:
                    numero_filmes = int(conteudo[3])
                except (ValueError, IndexError):
                    continue

            if numero_filmes > maior_quantidade_filmes:
                maior_quantidade_filmes = numero_filmes
                ator_ou_atriz_maior_numero_filmes = conteudo[0]

        conteudo = f'Ator/atriz com maior numero de filmes: {ator_ou_atriz_maior_numero_filmes}, quantidade: {maior_quantidade_filmes}'

        with open("etapa-1.txt", "w") as arquivo_resultado:
            arquivo_resultado.write(conteudo)
        
        return ator_ou_atriz_maior_numero_filmes, maior_quantidade_filmes


    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return None, 0

#etapa 2

def media_receita_bilheteira(arquivo_csv):
    try:
        with open(arquivo_csv, "r") as arquivo:
            linhas = arquivo.readlines()

        total_gross = 0.0
        contador_filmes = 0

        for linha in linhas[1:]: 
            conteudo = linha.strip().split(",")

            try:
                gross = float(conteudo[5])
            except ValueError:
                try:
                    gross = float(conteudo[6])
                except (ValueError, IndexError):
                    continue

            total_gross += gross
            contador_filmes += 1

        if contador_filmes > 0:  
            media = total_gross / contador_filmes
        else:
            media = 0.0  

        with open("etapa-2.txt", "w") as arquivo_resultado:
            arquivo_resultado.write(f"Media da receita de bilheteria bruta dos principais filmes: {media:.2f}")

        return media

    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return 0.0



#etapa 3

def ator_ou_atriz_maior_media_bilheteria_bruta():

    try:
        with open("actors.csv", "r") as arquivo:

            linhas = arquivo.readlines()

        ator_ou_atriz = ""
        maior_media = 0.0

        for linha in linhas[1:]: 
            conteudo = linha.strip().split(",")

            try:
                int(conteudo[2])
                average_per_movie = float(conteudo[3])
                pessoa = conteudo[0]

            except ValueError:
                try:
                    average_per_movie = float(conteudo[4])
                    pessoa = conteudo[0] + conteudo[1]
                except (ValueError, IndexError):
                    continue

            if average_per_movie > maior_media:
                maior_media = average_per_movie
                ator_ou_atriz = pessoa

        with open("etapa-3.txt", "w") as arquivo_resultado:
            arquivo_resultado.write(f"Ator/atriz com maior media de receita de bilheteria bruta por filme: {ator_ou_atriz}, media: {maior_media} ")

        return ator_ou_atriz, maior_media


    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return None

# etapa4

def aparicoes_filmes():

    try:
        with open("actors.csv", "r") as arquivo:

            linhas = arquivo.readlines()

        dicionario = {}

        for linha in linhas[1:]: 
            conteudo = linha.strip().split(",")

            try:
                int(conteudo[2])
                movie = conteudo[4]

            except ValueError:
                try:
                    movie = conteudo[5]
                    
                except (ValueError, IndexError):
                    continue

            if movie not in dicionario:
                dicionario[movie] = 1
            else:
                dicionario[movie] += 1

        with open("etapa-4.txt", "w") as arquivo_resultado:
            for movie, quantidade in sorted(dicionario.items(), key=lambda item: item[1], reverse=True):
                arquivo_resultado.write(f"O filme {movie} aparece {quantidade} vez(es) no dataset\n")


        return None
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return None
    
#etapa 5

def atores_receita_bruta():
    try:
        with open("actors.csv", "r") as arquivo:

            linhas = arquivo.readlines()

        dicionario = {}
        ator_ou_atriz = ''

        for linha in linhas[1:]: 
            conteudo = linha.strip().split(",")

            try:
                int(conteudo[2])
                totalGross = float(conteudo[1])
                ator_ou_atriz = conteudo[0]

            except ValueError:
                try:
                    totalGross = float(conteudo[2])
                    ator_ou_atriz = conteudo[0] + ',' + conteudo[1]
                    
                except (ValueError, IndexError):
                    continue

            dicionario[ator_ou_atriz] = totalGross
                    
        with open("etapa-5.txt", "w") as arquivo_resultado:
            for ator_ou_atriz, receita in sorted(dicionario.items(), key=lambda item: item[1], reverse=True):
                arquivo_resultado.write(f"{ator_ou_atriz} - {receita}\n")


        return None
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return None
            
        
if __name__ == "__main__":
    
    print(encontrar_ator_com_mais_filmes("actors.csv"))
    print(media_receita_bilheteira("actors.csv"))
    print(ator_ou_atriz_maior_media_bilheteria_bruta())
    print(aparicoes_filmes())
    print(atores_receita_bruta())