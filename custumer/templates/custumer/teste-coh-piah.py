import re
texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def separa_palavras(frase):
    return frase.split()

def conta_palavras(texto):
    sep_palavras = separa_palavras(texto)
    return len(sep_palavras)


def conta_sentencas(texto):
    sep_sentencas = separa_sentencas(texto)
    return len(sep_sentencas)


def conta_letras(texto):
    letras = []
    for letra in texto:
        total = 0
        if letra == " " or letra == "," or letra == ".":
            del(letra)
        else:
            letras.extend(letra)
    return len(letras)    


def tam_med_sentenca(texto):
    sentencas = conta_sentencas(texto)
    letras = conta_letras(texto)
    return letras / sentencas   

def conta_frases(texto):
    cont_fra = separa_frases(texto)
    return len(cont_fra)     



def calcula_assinatura(texto):
    tam_med_palavras = conta_letras(texto) / conta_palavras(texto) #wal_texto#
    type_token = n_palavras_diferentes(separa_palavras(texto)) / conta_palavras(texto)
    hapax = n_palavras_unicas(separa_palavras(texto)) / conta_palavras(texto)
    tam_med_sent = tam_med_sentenca(texto)
    complex_sentenca = conta_frases(texto) / conta_sentencas(texto)
    tam_med_frase = conta_letras(texto) / conta_frases(texto)
    return [tam_med_palavras, type_token, hapax, tam_med_sent, complex_sentenca, tam_med_frase]

#verificar erro nessa função com o enunciado e o teste#