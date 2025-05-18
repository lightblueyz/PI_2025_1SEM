def avaliar(valor, baixo, moderado):
    if valor < baixo:
        return "🟢 Alta Sustentabilidade"
    elif baixo <= valor <= moderado:
        return "🟡 Sustentabilidade Moderada"
    else:
        return "🔴 Baixa Sustentabilidade"
