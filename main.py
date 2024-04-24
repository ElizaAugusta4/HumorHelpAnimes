from coletar_infos import dadosTeste;
import time

def main():

    def tempo():
        time.sleep(3)

    print("\nBem-vindo ao quiz de animes!!!!\n")

    tempo()
    print("Responda com 's' ou 'sim' para sim e 'n' ou 'não' para não.\n")
    tempo()
    print("Vamos começar!!!\n\n\n")
    tempo()

    informacoes = dadosTeste()


if __name__ == "__main__":
    main()
