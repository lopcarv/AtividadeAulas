# ==========================================
# AULA: CONTROLE, REPETIÇÃO, DADOS E MODULARIZAÇÃO
# Prof. Luis Carvalho
# ==========================================

# ------------------------------------------
# 1. IF SIMPLES
# ------------------------------------------

idade = 18

if idade >= 18:
    print("Pode dirigir")


# ------------------------------------------
# 2. IF / ELSE
# ------------------------------------------

nota = 6

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# ------------------------------------------
# 3. POSITIVO OU NEGATIVO
# ------------------------------------------

numero = float(input("Digite um número: "))

if numero >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")


# ------------------------------------------
# 4. IF / ELIF / ELSE
# ------------------------------------------

idade = int(input("Digite a idade: "))

if idade < 18:
    print("Menor")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")


# ------------------------------------------
# 5. CLASSIFICAÇÃO DE NOTAS
# ------------------------------------------

nota = float(input("Digite a nota: "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
elif nota >= 5:
    print("Regular")
else:
    print("Insuficiente")


# ------------------------------------------
# 6. FOR COM RANGE
# ------------------------------------------

for i in range(5):
    print(i)


# ------------------------------------------
# 7. WHILE COM SENHA
# ------------------------------------------

senha = ""

while senha != "123":
    senha = input("Senha: ")

print("Acesso permitido.")


# ------------------------------------------
# 8. MOSTRAR NÚMEROS DE 1 A 10
# ------------------------------------------

for numero in range(1, 11):
    print(numero)


# ------------------------------------------
# 9. CONTAGEM REGRESSIVA
# ------------------------------------------

for numero in range(10, 0, -1):
    print(numero)

print("Fim!")


# ------------------------------------------
# 10. PERCORRER LISTA
# ------------------------------------------

alunos = ["Ana", "João", "Carlos"]

for aluno in alunos:
    print(aluno)


# ------------------------------------------
# 11. VALIDAÇÃO DE NOTA
# ------------------------------------------

nota = float(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Nota inválida.")
    nota = float(input("Digite novamente: "))

print("Nota válida:", nota)


# ------------------------------------------
# 12. VARIÁVEL
# ------------------------------------------

nome = "Luis"


# ------------------------------------------
# 13. LISTA
# ------------------------------------------

alunos = ["Ana", "João", "Carlos"]

print(alunos[0])
print(alunos[1])
print(alunos[2])


# ------------------------------------------
# 14. MATRIZ
# ------------------------------------------

notas = [
    [8, 7],
    [9, 10],
    [6, 8]
]


# ------------------------------------------
# 15. EXERCÍCIO DE DISCIPLINAS
# ------------------------------------------

disciplinas = [
    "Português",
    "Matemática",
    "Programação",
    "Banco de Dados",
    "Redes"
]

print("Lista:", disciplinas)
print("Primeira:", disciplinas[0])
print("Última:", disciplinas[-1])


# ------------------------------------------
# 16. MATRIZ COM ALUNOS
# ------------------------------------------

alunos = ["Ana", "João", "Maria"]

notas = [
    [8, 7],
    [9, 10],
    [6, 8]
]

print(alunos[0], notas[0])
print(alunos[1], notas[1])
print(alunos[2], notas[2])


# ------------------------------------------
# 17. MATRIZ COM FOR
# ------------------------------------------

alunos = ["Ana", "João", "Maria"]

notas = [
    [8, 7],
    [9, 10],
    [6, 8]
]

for indice in range(len(alunos)):
    print(
        alunos[indice],
        "P1:", notas[indice][0],
        "P2:", notas[indice][1]
    )


# ------------------------------------------
# 18. PRODUTOS E PREÇOS
# ------------------------------------------

produtos = ["Teclado", "Mouse", "Monitor"]
precos = [80.00, 45.00, 900.00]

for indice in range(len(produtos)):
    print(produtos[indice], "-", precos[indice])


# ------------------------------------------
# 19. FUNÇÃO SIMPLES
# ------------------------------------------

def saudacao():
    print("Bem-vindo")

saudacao()


# ------------------------------------------
# 20. FUNÇÃO COM PARÂMETRO
# ------------------------------------------

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Luis")


# ------------------------------------------
# 21. FUNÇÃO COM RETORNO
# ------------------------------------------

def soma(a, b):
    return a + b

resultado = soma(10, 5)
print(resultado)


# ------------------------------------------
# 22. CALCULAR MÉDIA
# ------------------------------------------

def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = calcular_media(n1, n2)

print(f"Média: {media:.1f}")


# ------------------------------------------
# 23. SISTEMA DE APROVAÇÃO
# ------------------------------------------

alunos = ["Ana", "João", "Carlos"]
notas = [8.0, 5.5, 7.0]

def verificar(nota):
    if nota >= 7:
        return "Aprovado"

    return "Reprovado"

for indice in range(len(alunos)):
    aluno = alunos[indice]
    nota = notas[indice]
    situacao = verificar(nota)

    print(aluno, "-", nota, "-", situacao)


# ------------------------------------------
# 24. APROVADO / RECUPERAÇÃO / REPROVADO
# ------------------------------------------

alunos = ["Ana", "João", "Carlos"]
notas = [8.0, 5.5, 4.0]

def verificar(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

for indice in range(len(alunos)):
    print(
        alunos[indice],
        "-",
        notas[indice],
        "-",
        verificar(notas[indice])
    )


# ------------------------------------------
# 25. DESAFIO PRÁTICO - CADASTRO DE ALUNOS
# ------------------------------------------

alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado com sucesso.")

def listar_alunos():
    print("\nALUNOS CADASTRADOS")

    for aluno in alunos:
        print(aluno)

def pesquisar_aluno():
    nome_pesquisa = input("\nNome para pesquisa: ")

    if nome_pesquisa in alunos:
        print("Aluno encontrado.")
    else:
        print("Aluno não encontrado.")

for contador in range(3):
    cadastrar_aluno()

listar_alunos()
pesquisar_aluno()


# ------------------------------------------
# 26. QUANTIDADE DEFINIDA PELO USUÁRIO
# ------------------------------------------

quantidade = int(input("Quantidade de alunos: "))

for contador in range(quantidade):
    cadastrar_aluno()


# ------------------------------------------
# 27. DESAFIO FINAL - MÉDIA DA TURMA
# ------------------------------------------

def calcular_media(valores):
    return sum(valores) / len(valores)

notas = []

for contador in range(5):
    nota = float(input(f"Digite a {contador + 1}ª nota: "))
    notas.append(nota)

print("\nNotas cadastradas:")

for nota in notas:
    print(nota)

media = calcular_media(notas)

print(f"Média: {media:.1f}")

if media >= 7:
    print("A turma alcançou a média.")
else:
    print("A turma não alcançou a média.")