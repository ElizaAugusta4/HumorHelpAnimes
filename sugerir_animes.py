def sugerir_animes(informacoes):
    sugeridos = []

    if informacoes['feliz'] == 'sim':
        sugeridos.append('comédia')
    if informacoes['triste'] == 'sim':
        sugeridos.append('drama')
    if informacoes['sentir_melhor'] == 'sim':
        sugeridos.append('romance')
    if informacoes['sentir_relaxado'] == 'sim':
        sugeridos.append('escolar')
    if informacoes['abordagem_seria'] == 'sim':
        sugeridos.append('psicológico')
    if informacoes['abordagem_leve'] == 'sim':
        sugeridos.append('aventura')
    if informacoes['abordagem_realista'] == 'sim':
        sugeridos.append('ação')
    if informacoes['abordagem_fantastica'] == 'sim':
        sugeridos.append('fantasia')
    if informacoes['abordagem_positiva'] == 'sim':
        sugeridos.append('harem')
    if informacoes['abordagem_sombria'] == 'sim':
        sugeridos.append('misterio')
    if informacoes['desenvolvimento_tempo'] == 'sim':
        sugeridos.append('shounen')
    if informacoes['desenvolvimento_rapido'] == 'sim':
        sugeridos.append('escolar')

    return sugeridos
