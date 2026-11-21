# ==========================================================
# MÓDULO 2 - DESVIOS CONDICIONAIS ANINHADOS E MÚLTIPLOS
# EXEMPLOS COMPLETOS DA AULA
# Linguagem: Python
# ==========================================================


# ==========================================================
# EXEMPLO 1 - CONDICIONAL SIMPLES (IF)
# ==========================================================

idade = 20

if idade >= 18:
    print("Maior de idade")


# ==========================================================
# EXEMPLO 2 - CONDICIONAL COMPOSTA (IF/ELSE)
# ==========================================================

idade = 15

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")


# ==========================================================
# EXEMPLO 3 - USO INCORRETO DE VÁRIOS IF
# ==========================================================

nota = 9

if nota >= 9:
    print("A")

if nota >= 7:
    print("B")

if nota >= 5:
    print("C")


# ==========================================================
# EXEMPLO 4 - USO CORRETO DO ELIF
# ==========================================================

input_nota = input("Digite a nota: ")
nota = float(input_nota)

if nota >= 9:
    print("Conceito A")

elif nota >= 7:
    print("Conceito B")

elif nota >= 5:
    print("Conceito C")

else:
    print("Conceito D")


# ==========================================================
# EXEMPLO 5 - CLASSIFICAÇÃO POR FAIXA ETÁRIA
# ==========================================================

idade = int(input("Digite a idade: "))

if idade < 12:
    print("Criança")

elif idade < 18:
    print("Adolescente")

elif idade < 60:
    print("Adulto")

else:
    print("Idoso")


# ==========================================================
# EXEMPLO 6 - CLASSIFICAÇÃO DE CLIENTES
# ==========================================================

saldo = 1500

if saldo >= 5000:
    print("Cliente Premium")

elif saldo >= 2000:
    print("Cliente Ouro")

elif saldo >= 1000:
    print("Cliente Prata")

else:
    print("Cliente Comum")


# ==========================================================
# EXEMPLO 7 - CONDIÇÃO ANINHADA SIMPLES
# ==========================================================

idade = 20
habilitado = True

if idade >= 18:

    if habilitado:
        print("Pode dirigir")


# ==========================================================
# EXEMPLO 8 - SISTEMA DE LOGIN
# ==========================================================

usuario = "admin"
senha = "1234"

if usuario == "admin":

    if senha == "1234":
        print("Acesso autorizado")

    else:
        print("Senha incorreta")

else:
    print("Usuário não encontrado")


# ==========================================================
# EXEMPLO 9 - FINANCIAMENTO
# ==========================================================

idade = 30
salario = 3500

if idade >= 18:

    if salario >= 3000:
        print("Financiamento aprovado")

    else:
        print("Salário insuficiente")

else:
    print("Menor de idade")


# ==========================================================
# EXEMPLO 10 - CRÉDITO COM TRÊS NÍVEIS
# ==========================================================

idade = 25
salario = 4000
nome_limpo = True

if idade >= 18:

    if salario >= 3000:

        if nome_limpo:
            print("Crédito aprovado")

        else:
            print("Restrição no CPF")

    else:
        print("Salário insuficiente")

else:
    print("Menor de idade")


# ==========================================================
# EXEMPLO 11 - SISTEMA ESCOLAR
# ==========================================================

nota = float(input("Digite a nota: "))
frequencia = int(input("Digite a frequência (%): "))

if nota >= 7:

    if frequencia >= 75:
        print("Aprovado")

    else:
        print("Reprovado por falta")

else:
    print("Reprovado por nota")


# ==========================================================
# EXEMPLO 12 - LOJA VIRTUAL
# ==========================================================

valor_compra = 800

if valor_compra >= 1000:
    desconto = 0.20

elif valor_compra >= 500:
    desconto = 0.10

elif valor_compra >= 200:
    desconto = 0.05

else:
    desconto = 0

print(f"Desconto aplicado: {desconto * 100:.0f}%")


# ==========================================================
# EXEMPLO 13 - ORDEM INCORRETA DOS TESTES
# ==========================================================

nota = 9

if nota >= 5:
    print("C")

elif nota >= 7:
    print("B")

elif nota >= 9:
    print("A")


# ==========================================================
# EXEMPLO 14 - ORDEM CORRETA DOS TESTES
# ==========================================================

nota = 9

if nota >= 9:
    print("A")

elif nota >= 7:
    print("B")

elif nota >= 5:
    print("C")

else:
    print("D")


# ==========================================================
# EXEMPLO 15 - CLASSIFICADOR DE IMC
# ==========================================================

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

print(f"IMC calculado: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")

elif imc < 25:
    print("Peso normal")

elif imc < 30:
    print("Sobrepeso")

elif imc < 35:
    print("Obesidade Grau I")

elif imc < 40:
    print("Obesidade Grau II")

else:
    print("Obesidade Grau III")


# ==========================================================
# EXERCÍCIO RESOLVIDO 1 - SITUAÇÃO DO ALUNO
# ==========================================================

media = float(input("Digite a média: "))

if media >= 7:
    print("Aprovado")

elif media >= 5:
    print("Recuperação")

else:
    print("Reprovado")


# ==========================================================
# EXERCÍCIO RESOLVIDO 2 - LOCAÇÃO DE VEÍCULOS
# ==========================================================

idade = int(input("Idade: "))
cnh = input("Possui CNH válida (S/N)? ")

if idade >= 21:

    if cnh.upper() == "S":
        print("Locação autorizada")

    else:
        print("CNH obrigatória")

else:
    print("Idade mínima não atendida")


# ==========================================================
# EXERCÍCIO RESOLVIDO 3 - EMPRÉSTIMO
# ==========================================================

idade = int(input("Idade: "))
salario = float(input("Salário: "))
tempo_empresa = int(input("Tempo de empresa (anos): "))

if idade >= 18:

    if salario >= 2500:

        if tempo_empresa >= 2:
            print("Empréstimo aprovado")

        else:
            print("Pouco tempo de empresa")

    else:
        print("Salário insuficiente")

else:
    print("Menor de idade")


# ==========================================================
# EXERCÍCIO RESOLVIDO 4 - CLASSIFICADOR INTELIGENTE
# ==========================================================

nome = input("Nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))

if idade < 12:
    faixa = "Criança"

elif idade < 18:
    faixa = "Adolescente"

elif idade < 60:
    faixa = "Adulto"

else:
    faixa = "Idoso"

if renda <= 3000:

    if idade >= 18:
        beneficio = "Elegível ao programa social"

    else:
        beneficio = "Não elegível (menor de idade)"

else:
    beneficio = "Não elegível"

print("\nRELATÓRIO")
print("-" * 40)
print("Nome:", nome)
print("Faixa Etária:", faixa)
print("Renda:", renda)
print("Situação:", beneficio)


# ==========================================================
# EXERCÍCIO RESOLVIDO  - 
# ==========================================================

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra > 1000:
    desconto = valor_compra * 0.10
elif valor_compra > 300:
    desconto = valor_compra * 0.08
elif valor_compra > 100:
    desconto = valor_compra * 0.05
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")