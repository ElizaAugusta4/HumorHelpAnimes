from coletar_infos import coletar_informacoes;
from sugerir_animes import sugerir_animes;

def main():
    informacoes = coletar_informacoes()
    sugeridos = sugerir_animes(informacoes)

    print("Com base nas suas preferências, aqui estão algumas sugestões de animes:")
    for genero in sugeridos:
        print(genero)

if __name__ == "__main__":
    main()
