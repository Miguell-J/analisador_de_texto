import string
from collections import Counter


def analisar_texto(texto):
    """
    Analisa o texto fornecido e calcula a contagem de palavras, a frequência de palavras
    e a frequência de letras.

    Parameters
    ----------
    texto : str
        Texto a ser analisado

    Returns
    -------
    tuple
        Contagem de palavras, frequência de palavras e frequência de letras
    """

    # Remove a pontuação do texto
    tratamento = str.maketrans('', '', string.punctuation)
    texto_tratado = texto.translate(tratamento)

    palavras = texto_tratado.split()
    contagem_palavras = len(palavras)
    frequencia_palavras = Counter(palavras)

    # Converte o texto para minúsculas e conta a frequência das letras
    frequencia_letras = Counter(texto_tratado.lower())

    return contagem_palavras, frequencia_palavras, frequencia_letras


texto = "Olá mundo! Este é um teste. Olá novamente."
contagem_palavras, frequencia_palavras, frequencia_letras = analisar_texto(texto)
print(f"Contagem de palavras: {contagem_palavras}")
print(f"Frequência de palavras: {frequencia_palavras}")
print(f"Frequência de letras: {frequencia_letras}")
