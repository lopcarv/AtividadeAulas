# Exercício 3.1 [2]
numeros = [5, 5.0, 4.3, -2, 100, 1.333]

for valor in numeros:
    tipo = "inteiro" if isinstance(valor, int) else "ponto flutuante"
    print(f"O número {valor} é do tipo: {tipo}")
