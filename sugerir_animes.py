from PIL import Image
import requests
from io import BytesIO
import os

# Dicionário contendo os animes e as URLs das imagens
lista_animes_shounen = {
    "Naruto": "animes/naruto.jpeg",
    "One Piece": "animes/one piece.jpeg",
    "Bleach": "animes/bleach.jpeg",
    "Dragon Ball": "animes/dragon ball.jpeg",
    "Demon Slayer": ""

    # Adicione mais animes conforme necessário
}

lista_animes_shoujo = {
    "Pretty Guardian Sailor Moon": "",
    "Cardcaptor Sakura": "",
    "Puella Magi Madoka Magica": "",
    "Shugo Chara! ": "",
    "Princess Tutu": ""
}

lista_animes_seinen = {
    "Golden Kamuy": "",
    "Akira": "",
    "One Punch Man": "",
    "Orange": "",
    "Seishun Buta Yarō": ""
}

lista_animes_josei = {
    "Descending Stories: Showa Genroku Rakugo Shinju": "",
    "Chihayafuru": "",
    "Nodame Cantabile. Paradise Kiss": "",
    "Natsuyuki Rendezvous": "",
    "Usagi Drop": ""
}

lista_animes_kodomo = {
    "Hamtaru": "",
    "Pokemon": "",
    "Beyblade": "",
    "Doraemon ": "",
    "Heidi": ""
}

lista_animes_isekai = {
    "The Faraway Paladin": "",
    "Mushoku Tensei: Jobless Reincarnation": "",
    "Parallel World Pharmacy": "",
    "Tensei Shitara Suraimu Datta Ken": "",
    "Overlord": ""
}

lista_animes_vida_escolar = {
    "Little Witch Academia": "",
    "The Familiar of Zero": "",
    "The Irregular at Magic High School": "",
    "Yamada-kun and the Seven Witches": "",
    "Haikyu!": ""
}

lista_animes_comedia = {
    "Yamato Nadeshiko Shichihenge": "",
    "Kaichou wa Maid-sama!: Omake da yo!": "",
    "Kaichou wa Maid-sama!: Goshujinsama to Asonjao": "",
    "Princess Princess": "",
    "Vampire Knight: Gekiai no Portrait": ""
}

lista_animes_aventura = {
    "Fullmetal Alchemist": "",
    "Tensei Shitara Suraimu Datta Ken": "",
    "The Seven Deadly Sins": "",
    "Magi: The Labyrinth of Magic": "",
    "Mo Dao Zu Shi": ""
}

lista_animes_acao = {
    "D.N.Angel": "",
    "Sabage-bu!": "",
    "Hakkenden: Touhou Hakken Ibun": "",
    "Honoo no Mirage": "",
    "JoJo's Bizarre Adventure ": ""
}

lista_animes_romance = {
    "Yubisaki to Renren": "",
    "3D Kanojo: Real Girl 2nd Season": "",
    "My Love Story": "",
    "Fruits Basket: Prelude": "",
    "Versailles no Bara": "",
    "Hiyokoi": ""
}

lista_animes_fantasia = {
    "Fruits Basket ": "",
    "X": "",
    "Shugo Chara! Party!": "",
    "Mayonaka no Occult Koumuin": "",
    "Fairy Tail": ""
}

lista_animes_sci_fi = {
    "Orange": "",
    "Tokyo Mew Mew": "",
    "Orange: Mirai": "",
    "7 Seeds": "",
    "Kiseijū: Sei no Kakuritsu ": "",
    "Serial Experiments Lain": ""

}

lista_animes_faroeste = {
    "Cowboy Bebop": "",
    "Wild Arms – Twilight Venom": "",
    "Grenadier": "",
    "Gun x Sword": "",
    "Trigun": ""
}

lista_animes_drama = {
    "Fruits Basket: The Final": "",
    "Vampire Knight Guilty": "",
    "Fruits Basket: Prelude": "",
    "Versailles no Bara": "",
    "Kageki Shoujo!": ""

}

lista_animes = {}

base_path = os.path.abspath("animes") + os.sep

def exibir_lista_animes(lista):
    for anime, filename in lista.items():
        print(anime)
    print("\n")
    lista.clear()

