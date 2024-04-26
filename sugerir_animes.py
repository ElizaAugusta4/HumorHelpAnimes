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
    "Sailor Moon": "url_imagem_1",
    "Cardcaptor Sakura": "url_imagem_2",
    "Fairy Tail": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_seinen = {
    "Death Note": "url_imagem_1",
    "Monster": "url_imagem_2",
    "Ghost in the Shell": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_josei = {
    "The Promised Neverland": "url_imagem_1",
    "Your Name": "url_imagem_2",
    "The Garden of Words": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_kodomo = {
    "Pokémon": "url_imagem_1",
    "Yu-Gi-Oh!": "url_imagem_2",
    "Digimon": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_isekai = {
    "Overlord": "url_imagem_1",
    "Re:Zero": "url_imagem_2",
    "Tate no Yuusha no Nariagari": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_vida_escolar = {
    "GTO": "url_imagem_1",
    "Assassination Classroom": "url_imagem_2",
    "Mirai Nikki": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_comedia = {
    "AoTenshi": "url_imagem_1",
    "Genshiken": "url_imagem_2",
    "Azumanga Daioh": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_aventura = {
    "One Piece": "url_imagem_1",
    "Naruto": "url_imagem_2",
    "Attack on Titan": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_acao = {
    "Naruto": "url_imagem_1",
    "One Piece": "url_imagem_2",
    "Attack on Titan": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_romance = {
    "Clannad": "url_imagem_1",
    "Steins;Gate": "url_imagem_2",
    "Your Name": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_fantasia = {
    "Sailor Moon": "url_imagem_1",
    "Fairy Tail": "url_imagem_2",
    "The Irregular at Magic High School": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_sci_fi = {
    "Death Note": "url_imagem_1",
    "Ghost in the Shell": "url_imagem_2",
    "Neon Genesis Evangelion": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_faroeste = {
    "Cowboy Bebop": "url_imagem_1",
    "Samurai Champloo": "url_imagem_2",
    "Astro Boy": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes_drama = {
    "Death Note": "url_imagem_1",
    "Monster": "url_imagem_2",
    "Ghost in the Shell": "url_imagem_3"
    # Adicione mais animes conforme necessário
}

lista_animes = {}

base_path = os.path.abspath("animes") + os.sep

def exibir_lista_animes(lista):
    for anime in lista.items():
        print(anime[0])
