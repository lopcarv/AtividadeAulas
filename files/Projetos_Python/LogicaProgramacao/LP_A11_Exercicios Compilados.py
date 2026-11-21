"""
============================================================
DISCIPLINA: LÓGICA DE PROGRAMAÇÃO
AULA 11: OPERADORES LÓGICOS (AND, OR, NOT)
PROFESSOR: LUIS CARVALHO

OBJETIVOS:
- Aplicar operadores lógicos em problemas reais.
- Construir expressões booleanas.
- Desenvolver sistemas simples de validação.
- Compreender o uso de AND, OR e NOT.

EXERCÍCIO 1 - MAIORIDADE E DOCUMENTO

Desenvolva um programa que permita o acesso somente
para pessoas que atendam simultaneamente aos dois critérios:

1. Possuir idade maior ou igual a 18 anos.
2. Possuir documento de identificação.

Caso ambas as condições sejam verdadeiras,
o sistema deve exibir:

"Acesso permitido"

Caso contrário:

"Acesso negado"

============================================================
"""

idade = int(input("Digite sua idade: "))
documento = input("Possui documento? (s/n): ")

if idade >= 18 and documento == "s":
    print("Acesso permitido")
else:
    print("Acesso negado")


"""
============================================================
EXERCÍCIO 2 - DESCONTO ESPECIAL

Desenvolva um programa que conceda desconto para clientes
que pertençam a pelo menos uma das categorias abaixo:

- Estudante
OU
- Idoso

Se o cliente atender a uma das condições,
o programa deverá exibir:

"Desconto concedido"

Caso contrário:

"Sem desconto"

Utilize obrigatoriamente o operador OR.

============================================================
"""

estudante = input("É estudante? (s/n): ")
idoso = input("É idoso? (s/n): ")

if estudante == "s" or idoso == "s":
    print("Desconto concedido")
else:
    print("Sem desconto")


"""
============================================================
EXERCÍCIO 3 - CONTA BANCÁRIA

Crie um sistema que permita acesso à conta bancária.

Regras:

1. A senha deve estar correta.
2. A conta não pode estar bloqueada.

Utilize os operadores:
- AND
- NOT

Se as regras forem satisfeitas:

"Acesso autorizado"

Caso contrário:

"Acesso negado"

============================================================
"""

senha = input("Digite a senha: ")

conta_bloqueada = False

if senha == "1234" and not conta_bloqueada:
    print("Acesso autorizado")
else:
    print("Acesso negado")


"""
============================================================
EXERCÍCIO 4 - SISTEMA ESCOLAR

Desenvolva um sistema que verifique se um aluno
foi aprovado.

Critérios para aprovação:

- Nota maior ou igual a 6.
- Frequência maior ou igual a 75%.

Quando as duas condições forem satisfeitas,
o programa deve exibir:

"Aluno aprovado"

Caso contrário:

"Aluno reprovado"

============================================================
"""

nota = float(input("Digite a nota: "))
frequencia = float(input("Digite a frequência (%): "))

if nota >= 6 and frequencia >= 75:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")


"""
============================================================
EXERCÍCIO 5 - SISTEMA DE EMPRÉSTIMO

Um banco deseja automatizar a análise inicial
de empréstimos.

O empréstimo será aprovado apenas quando:

1. O cliente possuir idade maior ou igual a 18 anos.
2. O salário for maior ou igual a R$ 2.000,00.

Caso aprovado:

"Empréstimo aprovado"

Caso contrário:

"Empréstimo recusado"

============================================================
"""

idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

if idade >= 18 and salario >= 2000:
    print("Empréstimo aprovado")
else:
    print("Empréstimo recusado")


"""
============================================================
DESAFIO - SISTEMA DE LOGIN

Desenvolva um sistema de autenticação simples.

Dados do sistema:

Usuário:
admin

Senha:
123

Condições para liberar o acesso:

1. O usuário informado deve ser igual a "admin".
2. A senha informada deve ser igual a "123".
3. A conta não pode estar bloqueada.

Saídas possíveis:

"Acesso liberado"
ou
"Acesso negado"

============================================================
"""

usuario_correto = "admin"
senha_correta = "123"

usuario = input("Usuário: ")
senha = input("Senha: ")

bloqueado = False

if usuario == usuario_correto and senha == senha_correta and not bloqueado:
    print("Acesso liberado")
else:
    print("Acesso negado")


"""
============================================================
EXERCÍCIO EXTRA 1 - CONTROLE DE ENTRADA EM EVENTO

Uma pessoa poderá entrar em um evento se:

- Possuir 16 anos ou mais.
OU
- Estiver acompanhada de um responsável.

Se qualquer uma das condições for verdadeira,
permitir a entrada.

Caso contrário, negar a entrada.

============================================================
"""

idade = int(input("Digite sua idade: "))
acompanhado = input("Está acompanhado? (s/n): ")

if idade >= 16 or acompanhado == "s":
    print("Entrada permitida")
else:
    print("Entrada não permitida")


"""
============================================================
EXERCÍCIO EXTRA 2 - SISTEMA DE BIBLIOTECA

Um aluno poderá realizar empréstimos somente quando:

- O cadastro estiver ativo.
- Não possuir multas pendentes.

Se ambas as condições forem verdadeiras:

"Empréstimo autorizado"

Caso contrário:

"Empréstimo bloqueado"

============================================================
"""

cadastro_ativo = True
possui_multa = False

if cadastro_ativo and not possui_multa:
    print("Empréstimo autorizado")
else:
    print("Empréstimo bloqueado")


"""
============================================================
EXERCÍCIO EXTRA 3 - APROVAÇÃO DE BOLSA

Um estudante receberá bolsa de estudos quando:

- Média final maior ou igual a 8.
- Frequência maior ou igual a 90%.
- Não possuir reprovação anterior.

Caso todos os critérios sejam atendidos:

"Bolsa aprovada"

Caso contrário:

"Bolsa não aprovada"

============================================================
"""

media = float(input("Digite a média: "))
frequencia = float(input("Digite a frequência: "))
reprovacao = input("Possui reprovação anterior? (s/n): ")

if media >= 8 and frequencia >= 90 and reprovacao == "n":
    print("Bolsa aprovada")
else:
    print("Bolsa não aprovada")


"""
============================================================
EXERCÍCIO EXTRA 4 - LOGIN COM MÚLTIPLOS USUÁRIOS

Desenvolva um sistema que permita acesso para
qualquer um dos usuários abaixo:

Usuário: admin | Senha: 123
Usuário: joao  | Senha: 456
Usuário: maria | Senha: 789

Caso uma combinação válida seja encontrada:

"Login realizado"

Caso contrário:

"Usuário ou senha inválidos"

============================================================
"""

usuario = input("Usuário: ")
senha = input("Senha: ")

if (usuario == "admin" and senha == "123") or \
   (usuario == "joao" and senha == "456") or \
   (usuario == "maria" and senha == "789"):
    print("Login realizado")
else:
    print("Usuário ou senha inválidos")


"""
============================================================
EXERCÍCIO EXTRA 5 - ELEGIBILIDADE PARA CNH

Uma pessoa poderá iniciar o processo para obtenção
da Carteira Nacional de Habilitação (CNH) quando:

1. Possuir idade igual ou superior a 18 anos.
2. Souber ler e escrever.

Caso ambas as condições forem satisfeitas:

"Pode tirar CNH"

Caso contrário:

"Não pode tirar CNH"

============================================================
"""

idade = int(input("Digite sua idade: "))
alfabetizado = input("Sabe ler e escrever? (s/n): ")

if idade >= 18 and alfabetizado == "s":
    print("Pode tirar CNH")
else:
    print("Não pode tirar CNH")