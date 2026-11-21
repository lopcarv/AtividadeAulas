# Função media
def media(nota1, nota2):
    return (nota1 + nota2) / 2

# Matriz com alunos e notas
alunos = [
    ["Ana", 8, 7],
    ["Bruno", 9, 10],
    ["Carlos", 6, 8]
]

# Percorrendo a matriz
for aluno in alunos:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]

    resultado = media(nota1, nota2)

    print(f"Aluno: {nome}")
    print(f"Média: {resultado}")
    print("-" * 20)
