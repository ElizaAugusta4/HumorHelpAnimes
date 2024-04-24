from PIL import Image
import requests
from io import BytesIO
import os

# Dicionário contendo os animes e as URLs das imagens
lista_animes_shounen = {
    "Naruto": "animes/naruto.jpeg",
    "One Piece": "animes/one piece.jpeg",
    "Bleach": "animes/bleach.jpeg"
    # Adicione mais animes conforme necessário
}
lista_animes_shoujo = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_seinen = {
    "Anime seinen 1": "url_imagem_1",
    "Anime seinen 2": "url_imagem_2",
    "Anime seinen 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_josei = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_kodomo = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_isekai = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_vida_escolar = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_comedia = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_aventura = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_acao = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_romance = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_fantasia = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_sci_fi = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_faroeste = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}
lista_animes_drama = {
    "Anime 1": "url_imagem_1",
    "Anime 2": "url_imagem_2",
    "Anime 3": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes = {}

base_path = os.path.abspath("animes") + os.sep

def exibir_lista_animes(lista):
    for anime, filename in lista.items():
        print(anime)
        img = Image.open(filename)
        img.show()


