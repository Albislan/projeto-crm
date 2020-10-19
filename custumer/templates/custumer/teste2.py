texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
letras = []
for letra in texto:
    total = 0
    if letra == " " or letra == "," or letra == ".":
        del(letra)
    else:
        letras.extend(letra)

print(len(letras))        
        
