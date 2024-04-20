def coletar_informacoes():
    print("Você assiste anime quando está feliz? (sim/não)")
    feliz = input().lower()
    print("Você assiste Shounen quando está feliz? (sim/não)")
    shounen_feliz = input().lower()
    print("Você assiste anime quando está triste? (sim/não)")
    triste = input().lower()
    print("Você assiste Shounen quando está triste? (sim/não)")
    shounen_triste = input().lower()
    print("Você assiste anime para se sentir melhor? (sim/não)")
    sentir_melhor = input().lower()
    print("Você assiste anime para se sentir mais relaxado? (sim/não)")
    sentir_relaxado = input().lower()
    print("Você assiste anime com uma abordagem mais séria? (sim/não)")
    abordagem_seria = input().lower()
    print("Você assiste anime com uma abordagem mais leve e divertida? (sim/não)")
    abordagem_leve = input().lower()
    print("Você assiste anime com uma abordagem mais realista? (sim/não)")
    abordagem_realista = input().lower()
    print("Você assiste anime com uma abordagem mais fantástica? (sim/não)")
    abordagem_fantastica = input().lower()
    print("Você assiste anime com uma abordagem mais positiva? (sim/não)")
    abordagem_positiva = input().lower()
    print("Você assiste anime com uma abordagem mais sombria? (sim/não)")
    abordagem_sombria = input().lower()
    print("Você assiste anime com uma trama que se desenvolve ao longo do tempo? (sim/não)")
    desenvolvimento_tempo = input().lower()
    print("Você assiste anime com uma trama que se desenrola rapidamente? (sim/não)")
    desenvolvimento_rapido = input().lower()

    return {
        'feliz': feliz,
        'shounen_feliz': shounen_feliz,
        'triste': triste,
        'shounen_triste': shounen_triste,
        'sentir_melhor': sentir_melhor,
        'sentir_relaxado': sentir_relaxado,
        'abordagem_seria': abordagem_seria,
        'abordagem_leve': abordagem_leve,
        'abordagem_realista': abordagem_realista,
        'abordagem_fantastica': abordagem_fantastica,
        'abordagem_positiva': abordagem_positiva,
        'abordagem_sombria': abordagem_sombria,
        'desenvolvimento_tempo': desenvolvimento_tempo,
        'desenvolvimento_rapido': desenvolvimento_rapido
    }
