def avaliar(valor, baixo, moderado):
    if valor < baixo:
        return "AltaSustentabilidade"
    elif baixo <= valor <= moderado:
        return "SustentabilidadeModerada"
    else:
        return "BaixaSustentabilidade"
