# Função para calcular a média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Função para verificar a situação
def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

# Matriz
alunos = [
    ["Ana", 8, 7],
    ["Bruno", 4, 6],
    ["Carlos", 3, 4],
    ["Maria", 10, 9]
]

# Percorrendo a matriz
for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]

    media = calcular_media(nota1, nota2)

    print(f"Aluno: {nome}")
    print(f"Média: {media:.1f}")
    print(f"Situação: {situacao(media)}")
    print("-" * 20)