from sugerir_animes import *;


def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (sim/s ou não/n): ").lower()
    if resposta == "sim" or resposta == "s":
        return True
    elif resposta == "não" or resposta == "nao" or resposta == "n":
        return False
    else:
        print("Resposta inválida. Por favor, responda com 'sim'/'s' ou 'não'/'n'.")
        return fazer_pergunta(pergunta)


def dadosTeste():
    if fazer_pergunta("Você assiste anime quando está feliz?"):
        if fazer_pergunta("Você assiste Shounen quando está feliz?"):
            if fazer_pergunta("Você assiste Seinen?"):
                if fazer_pergunta("Você assiste ação?"):
                    if fazer_pergunta("Você assiste Isekai?"):
                        if fazer_pergunta("Você assiste Sci-fi?"):
                            lista_animes.update(lista_animes_shounen)
                            lista_animes.update(lista_animes_seinen)
                            lista_animes.update(lista_animes_acao)
                            lista_animes.update(lista_animes_sci_fi)
                            exibir_lista_animes(lista_animes)
                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                return print("Sucesso, animes recomendados com exito")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                        else:
                            lista_animes.update(lista_animes_shounen)
                            lista_animes.update(lista_animes_seinen)
                            lista_animes.update(lista_animes_acao)
                            lista_animes.update(lista_animes_isekai)
                            exibir_lista_animes(lista_animes)
                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                return print("Sucesso, animes recomendados com exito")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                    else:
                        lista_animes.update(lista_animes_shounen)
                        lista_animes.update(lista_animes_seinen)
                        lista_animes.update(lista_animes_acao)
                        exibir_lista_animes(lista_animes)
                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                            return print("Sucesso, animes recomendados com exito")
                        else:
                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                else:
                    lista_animes.update(lista_animes_shounen)
                    lista_animes.update(lista_animes_seinen)
                    exibir_lista_animes(lista_animes)
                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                        return print("Sucesso, animes recomendados com exito")
                    else:
                        if fazer_pergunta("Que tal animes mais leves?"):
                            if fazer_pergunta("Que tal Aventura?"):
                                if fazer_pergunta("Que tal Comédia?"):
                                    lista_animes.update(lista_animes_aventura)
                                    lista_animes.update(lista_animes_comedia)
                                    exibir_lista_animes(lista_animes)
                                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                        return print("Sucesso, animes recomendados com exito")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                                else:
                                    exibir_lista_animes(lista_animes_aventura)
                                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                        return print("Sucesso, animes recomendados com exito")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                            else:
                                if fazer_pergunta("Que tal de Faroeste?"):
                                    exibir_lista_animes(lista_animes_faroeste)
                                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                        return print("Sucesso, animes recomendados com exito")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                        else:
                            return print("Infelizmente não cosneguimos ajudar no momento :(")
            else:
                if fazer_pergunta("Você assiste Josei?"):
                    exibir_lista_animes(lista_animes_josei)
                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                        return print("Sucesso, animes recomendados com exito")
                    else:
                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                else:
                    if fazer_pergunta("Você assiste Kodomo?"):
                        exibir_lista_animes(lista_animes_kodomo)
                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                            return print("Sucesso, animes recomendados com exito")
                        else:
                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                    else:
                        return print("Infelizmente não cosneguimos ajudar no momento :(")
        else:
            if fazer_pergunta("Você assiste Gêneros alternativos?"):
                if fazer_pergunta("Você assiste Shoujo quando está feliz?"):
                    if fazer_pergunta("Você assiste ação?"):
                        if fazer_pergunta("Você assiste Isekai?"):
                            if fazer_pergunta("Você assiste Sci-fi?"):
                                lista_animes.update(lista_animes_shounen)
                                lista_animes.update(lista_animes_seinen)
                                lista_animes.update(lista_animes_acao)
                                lista_animes.update(lista_animes_sci_fi)
                                exibir_lista_animes(lista_animes)
                                if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                    return print("Sucesso, animes recomendados com exito")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                            else:
                                lista_animes.update(lista_animes_shounen)
                                lista_animes.update(lista_animes_seinen)
                                lista_animes.update(lista_animes_acao)
                                lista_animes.update(lista_animes_isekai)
                                exibir_lista_animes(lista_animes)
                                if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                    return print("Sucesso, animes recomendados com exito")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                        else:
                            lista_animes.update(lista_animes_shounen)
                            lista_animes.update(lista_animes_seinen)
                            lista_animes.update(lista_animes_acao)
                            exibir_lista_animes(lista_animes)
                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                return print("Sucesso, animes recomendados com exito")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                    else:
                        lista_animes.update(lista_animes_shounen)
                        lista_animes.update(lista_animes_seinen)
                        exibir_lista_animes(lista_animes)
                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                            return print("Sucesso, animes recomendados com exito")
                        else:
                            if fazer_pergunta("Que tal animes mais leves?"):
                                if fazer_pergunta("Que tal Aventura?"):
                                    if fazer_pergunta("Que tal Comédia?"):
                                        lista_animes.update(lista_animes_aventura)
                                        lista_animes.update(lista_animes_comedia)
                                        exibir_lista_animes(lista_animes)
                                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                            return print("Sucesso, animes recomendados com exito")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                    else:
                                        exibir_lista_animes(lista_animes_aventura)
                                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                            return print("Sucesso, animes recomendados com exito")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                else:
                                    if fazer_pergunta("Que tal de Faroeste?"):
                                        exibir_lista_animes(lista_animes_faroeste)
                                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                            return print("Sucesso, animes recomendados com exito")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
            else:
                if fazer_pergunta("Você assiste Kodomo?"):
                    exibir_lista_animes(lista_animes_kodomo)
                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                        return print("Sucesso, animes recomendados com exito")
                    else:
                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                else:
                    return print("Infelizmente não cosneguimos ajudar no momento :(")
    else:
        if fazer_pergunta("Você assiste anime quando está triste?"):
            if fazer_pergunta("Você assiste Shounen quando está triste?"):
                if fazer_pergunta("Você assiste Seinen?"):
                    if fazer_pergunta("Você assiste Drama?"):
                        if fazer_pergunta("Você assiste Isekai?"):
                            if fazer_pergunta("Você assiste Sci-fi?"):
                                lista_animes.update(lista_animes_shounen)
                                lista_animes.update(lista_animes_seinen)
                                lista_animes.update(lista_animes_drama)
                                lista_animes.update(lista_animes_sci_fi)
                                exibir_lista_animes(lista_animes)
                                if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                    return print("Sucesso, animes recomendados com exito")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                            else:
                                lista_animes.update(lista_animes_shounen)
                                lista_animes.update(lista_animes_seinen)
                                lista_animes.update(lista_animes_drama)
                                lista_animes.update(lista_animes_isekai)
                                exibir_lista_animes(lista_animes)
                                if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                    return print("Sucesso, animes recomendados com exito")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                        else:
                            lista_animes.update(lista_animes_shounen)
                            lista_animes.update(lista_animes_seinen)
                            lista_animes.update(lista_animes_drama)
                            exibir_lista_animes(lista_animes)
                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                return print("Sucesso, animes recomendados com exito")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                    else:
                        lista_animes.update(lista_animes_shounen)
                        lista_animes.update(lista_animes_seinen)
                        exibir_lista_animes(lista_animes)
                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                            return print("Sucesso, animes recomendados com exito")
                        else:
                            if fazer_pergunta("Que tal animes mais leves?"):
                                if fazer_pergunta("Que tal Romance?"):
                                    if fazer_pergunta("Que tal Fantasia?"):
                                        lista_animes.update(lista_animes_romance)
                                        lista_animes.update(lista_animes_fantasia)
                                        exibir_lista_animes(lista_animes)
                                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                            return print("Sucesso, animes recomendados com exito")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                    else:
                                        exibir_lista_animes(lista_animes_romance)
                                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                            return print("Sucesso, animes recomendados com exito")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                else:
                                    if fazer_pergunta("Que tal de vida_escolar?"):
                                        exibir_lista_animes(lista_animes_vida_escolar)
                                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                            return print("Sucesso, animes recomendados com exito")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                else:
                    if fazer_pergunta("Você assiste Josei?"):
                        exibir_lista_animes(lista_animes_josei)
                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                            return print("Sucesso, animes recomendados com exito")
                        else:
                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                    else:
                        if fazer_pergunta("Você assiste Kodomo?"):
                            exibir_lista_animes(lista_animes_kodomo)
                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                return print("Sucesso, animes recomendados com exito")
                            else:
                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                        else:
                            return print("Infelizmente não cosneguimos ajudar no momento :(")
            else:
                if fazer_pergunta("Você assiste Gêneros alternativos?"):
                    if fazer_pergunta("Você assiste Shoujo quando está triste?"):
                        if fazer_pergunta("Você assiste Drama?"):
                            if fazer_pergunta("Você assiste Isekai?"):
                                if fazer_pergunta("Você assiste Sci-fi?"):
                                    lista_animes.update(lista_animes_shounen)
                                    lista_animes.update(lista_animes_seinen)
                                    lista_animes.update(lista_animes_drama)
                                    lista_animes.update(lista_animes_sci_fi)
                                    exibir_lista_animes(lista_animes)
                                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                        return print("Sucesso, animes recomendados com exito")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                                else:
                                    lista_animes.update(lista_animes_shounen)
                                    lista_animes.update(lista_animes_seinen)
                                    lista_animes.update(lista_animes_drama)
                                    lista_animes.update(lista_animes_isekai)
                                    exibir_lista_animes(lista_animes)
                                    if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                        return print("Sucesso, animes recomendados com exito")
                                    else:
                                        return print("Infelizmente não cosneguimos ajudar no momento :(")
                            else:
                                lista_animes.update(lista_animes_shounen)
                                lista_animes.update(lista_animes_seinen)
                                lista_animes.update(lista_animes_drama)
                                exibir_lista_animes(lista_animes)
                                if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                    return print("Sucesso, animes recomendados com exito")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                        else:
                            lista_animes.update(lista_animes_shounen)
                            lista_animes.update(lista_animes_seinen)
                            exibir_lista_animes(lista_animes)
                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                return print("Sucesso, animes recomendados com exito")
                            else:
                                if fazer_pergunta("Que tal animes mais leves?"):
                                    if fazer_pergunta("Que tal Romance?"):
                                        if fazer_pergunta("Que tal Fantasia?"):
                                            lista_animes.update(lista_animes_romance)
                                            lista_animes.update(lista_animes_fantasia)
                                            exibir_lista_animes(lista_animes)
                                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                                return print("Sucesso, animes recomendados com exito")
                                            else:
                                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                                        else:
                                            exibir_lista_animes(lista_animes_romance)
                                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                                return print("Sucesso, animes recomendados com exito")
                                            else:
                                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                                    else:
                                        if fazer_pergunta("Que tal de Vida_escolar?"):
                                            exibir_lista_animes(lista_animes_vida_escolar)
                                            if fazer_pergunta("Você ira assistir algum dessa lista?"):
                                                return print("Sucesso, animes recomendados com exito")
                                            else:
                                                return print("Infelizmente não cosneguimos ajudar no momento :(")
                                        else:
                                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                                else:
                                    return print("Infelizmente não cosneguimos ajudar no momento :(")
                else:
                    if fazer_pergunta("Você assiste Kodomo?"):
                        exibir_lista_animes(lista_animes_kodomo)
                        if fazer_pergunta("Você ira assistir algum dessa lista?"):
                            return print("Sucesso, animes recomendados com exito")
                        else:
                            return print("Infelizmente não cosneguimos ajudar no momento :(")
                    else:
                        return print("Infelizmente não cosneguimos ajudar no momento :(")
        else:
            print("Encerrando o quiz...")
