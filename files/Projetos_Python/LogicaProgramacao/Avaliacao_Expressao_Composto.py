# Exercício 3.5 - Avaliação de Expressão Composta

tabela = [
    {"A": 1, "B": 2, "C": True, "D": False},
    {"A": 10, "B": 3, "C": False, "D": False},
    {"A": 5, "B": 1, "C": True, "D": True},
]

for i, linha in enumerate(tabela, start=1):
    A = linha["A"]
    B = linha["B"]
    C = linha["C"]
    D = linha["D"]

    resultado = (A > B and C) or D

    print(f"Linha {i}: {resultado}")