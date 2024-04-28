from coletar_infos import dadosTeste;
import time
import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load("musica.mp3")

# Inicia a reprodução da música
pygame.mixer.music.play(-1) # O parâmetro -1 faz a música tocar em loop

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




# Interrompe a música
pygame.mixer.music.stop()

# Limpa os recursos do mixer
pygame.mixer.quit()
