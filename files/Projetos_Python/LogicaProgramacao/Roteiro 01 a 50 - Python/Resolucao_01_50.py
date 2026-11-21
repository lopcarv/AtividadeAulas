#### Exercício 1: Cálculo de Bônus de Vendas
#####  Uma empresa decidiu dar um bônus de 10% sobre o faturamento total.
#####  Calcule o valor do bônus e o faturamento final após descontar esse bônus.

faturamento = 50000
percentual_bonus = 0.10

bonus = faturamento * percentual_bonus
faturamento_final = faturamento - bonus

print(f"Bônus: R$ {bonus:.2f}")
print(f"Faturamento após bônus: R$ {faturamento_final:.2f}")















# Exercício 2: Controle de Estoque de E-commerce
# Atualizar o estoque após vendas e reposição.

estoque = 250
vendidos = 78
recebidos = 100

estoque = estoque - vendidos + recebidos
print(f"Estoque final: {estoque} unidades")








# Exercício 3: Divisão de Cargas
# Descobrir quantos caminhões sairão cheios e quantas caixas sobrarão.

caixas = 1250
capacidade = 12

caminhoes_cheios = caixas // capacidade
caixas_restantes = caixas % capacidade

print(f"Caminhões cheios: {caminhoes_cheios}")
print(f"Caixas restantes: {caixas_restantes}")







# Exercício 4: Análise de Margem de Lucro
# Calcular imposto, lucro líquido e verificar se a meta foi atingida.

faturamento = 15000
custos = 5000
taxa_imposto = 0.15

imposto = faturamento * taxa_imposto
lucro = faturamento - custos - imposto
margem = lucro / faturamento

meta_atingida = margem > 0.30

print(f"Imposto: R$ {imposto:.2f}")
print(f"Lucro líquido: R$ {lucro:.2f}")
print(f"Margem de lucro: {margem:.2%}")
print(f"Meta atingida? {meta_atingida}")





# Exercício 5: Conversão de Tempo de Contrato
# Converter 40 meses para anos e meses.

meses = 40

anos = meses // 12
meses_restantes = meses % 12

print(f"{anos} anos e {meses_restantes} meses")










# Exercício 6: Relatório de Margem de Lucro
# Calcular lucro e margem de lucro do produto.

faturamento = 45000
custo = 23500

lucro = faturamento - custo
margem = lucro / faturamento

print(f"Lucro: R$ {lucro:,.2f}")
print(f"Margem de Lucro: {margem:.0%}")













# Exercício 7: Padronização de Dados de CRM
# Ajustar nome e e-mail.

nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "

nome = nome.strip().title()
email = email.strip().lower()

print("Nome:", nome)
print("E-mail:", email)













# Exercício 8: Migração de Servidor de E-mail
# Trocar domínio antigo pelo novo.

email = "andre_silva@empresa.com.br"

novo_email = email.replace("@empresa.com.br", "@grupocorp.com")

print("Novo e-mail:", novo_email)










# Exercício 9: Extração de Username para Log
# Extrair somente o nome antes do @.

email = "beatriz.oliveira@grupocorp.com"

posicao = email.find("@")

usuario = email[:posicao]

print("Usuário:", usuario)










# Exercício 10: Personalização de E-mail de Marketing
# Extrair o primeiro nome do cliente.

nome_completo = "lucas ferreira souza"

posicao_espaco = nome_completo.find(" ")

primeiro_nome = nome_completo[:posicao_espaco].title()

print(f"Olá, {primeiro_nome}, seja bem-vindo ao nosso clube!")





# Exercício 11: Calculadora de Imposto sobre Vendas
# Solicite o valor bruto da nota fiscal, limpe o texto,
# converta para float e calcule 15% de imposto.

valor = input("Digite o valor bruto (Ex: R$ 5.000,00): ")
valor = valor.replace("R$", "").replace(".", "").replace(",", ".").strip()
valor = float(valor)
imposto = valor * 0.15
print(f"Imposto calculado: R$ {imposto:.2f}")






# Exercício 12: Cadastro de Colaborador
# Extrair primeiro nome e padronizar e-mail.

nome_completo = input("Nome completo: ")
email = input("E-mail: ")

primeiro_nome = nome_completo.split()[0].title()
email = email.strip().lower()

print(
    f"Cadastro concluído: {primeiro_nome}. "
    f"E-mail de acesso: {email}"
)




# Exercício 13: Análise de Metas de Vendas
# Calcular o faturamento total e a média entre duas lojas.

loja_a = float(input("Faturamento Loja A: "))
loja_b = float(input("Faturamento Loja B: "))

total = loja_a + loja_b
media = total / 2

print(
    f"Total: R$ {total:,.2f} | "
    f"Média: R$ {media:,.2f}"
)



# Exercício 14: Dashboard de Vendas
# Exibir total, média, maior e menor venda.

vendas = [1500, 2000, 800, 3500, 1200]

total = sum(vendas)
media = total / len(vendas)
melhor = max(vendas)
pior = min(vendas)

print(f"Total vendido: R$ {total:.2f}")
print(f"Média diária: R$ {media:.2f}")
print(f"Maior venda: R$ {melhor:.2f}")
print(f"Menor venda: R$ {pior:.2f}")



# Exercício 15: Gestão de Estoque
# Adicionar, alterar, verificar e remover itens.

estoque = ["monitor", "teclado", "mouse", "headset"]

estoque.append("webcam")

indice = estoque.index("teclado")
estoque[indice] = "teclado mecanico"

print("Impressora está no estoque?")
print("impressora" in estoque)

estoque.remove("mouse")

print(estoque)





# Exercício 16: Organização de Preços
# Ordenar fretes e selecionar os dois maiores.

fretes = [50, 80, 20, 150, 40]

fretes.sort(reverse=True)

top_fretes = fretes[:2]

print("Fretes ordenados:", fretes)
print("Top fretes:", top_fretes)



# Exercício 17: Sistema de Logística
# Unir listas e localizar Sorocaba.

rota = ["Sao Paulo", "Campinas", "Jundiai", "Sorocaba"]

novas_cidades = ["Itu", "Valinhos"]

rota.extend(novas_cidades)

posicao = rota.index("Sorocaba")

print("Rota completa:", rota)
print("Posição:", posicao)

print(
    f"Sorocaba é a {posicao + 1}ª cidade da rota."
)



# Exercício 18: Atualização de Preços Interativa
# Atualizar o preço de um produto.

vinhos = ["Branco", "Tinto", "Champagne"]
precos = [100.0, 250.0, 500.0]

produto = input("Produto: ")

novo_preco = float(
    input("Novo preço: ")
)

indice = vinhos.index(produto)

precos[indice] = novo_preco

print("Produtos:", vinhos)
print("Preços:", precos)


# Exercício 19: Validação de Investimento
# Classificar o perfil do investidor.

valor = input("Valor do investimento: ")

valor = valor.replace(
    "R$", ""
).replace(
    ".", ""
).replace(
    ",", "."
).strip()

valor = float(valor)

if valor < 1000:
    print(
        "Perfil iniciante: "
        "Sugerimos Tesouro Direto"
    )

elif valor <= 5000:
    print(
        "Perfil moderado: "
        "Sugerimos Fundos Imobiliários"
    )

else:
    print(
        "Perfil arrojado: "
        "Sugerimos Ações"
    )


# Exercício 20: Controle de Acesso ao Sistema
# Verificar se o usuário é administrador.

admins = [
    "ana@empresa.com",
    "guilherme@empresa.com",
    "felipe@empresa.com"
]

email = input(
    "Digite seu e-mail: "
)

email = email.strip().lower()

if email in admins:
    print(
        "Acesso liberado! "
        "Bem-vindo ao painel de controle."
    )
else:
    print(
        "Acesso negado. "
        "Você não tem permissões de administrador."
    )


# Exercício 21: Cálculo de Desconto Progressivo
# Aplicar descontos conforme o valor da compra.

valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra >= 500:
    desconto = valor_compra * 0.15
elif valor_compra >= 200:
    desconto = valor_compra * 0.10
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")


# Exercício 22: Análise de Metas Combinadas
# O bônus só será concedido se o vendedor e a loja
# atingirem suas respectivas metas.

vendas_vendedor = float(input("Vendas do vendedor: "))
meta_vendedor = float(input("Meta do vendedor: "))

vendas_loja = float(input("Vendas da loja: "))
meta_loja = float(input("Meta da loja: "))

if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    bonus = vendas_vendedor * 0.20
else:
    bonus = 0

print(f"Seu bônus este mês é de: R$ {bonus:.2f}")


# Exercício 23: Sistema de Triagem de E-mails
# Direcionar automaticamente o chamado para o setor correto.

assunto = input("Digite o assunto: ").lower()

if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o Financeiro")

elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para a Logística")

else:
    print("Encaminhado para o Suporte Geral")


# Exercício 24: Atualização de Cadastro de Clientes
# Atualizar faturamento e adicionar novo cliente.

clientes = {
    "Lira": 5000,
    "Alon": 3000,
    "Julia": 4500
}

clientes["Alon"] += 1500

clientes["Marcos"] = 2000

print(clientes)


# Exercício 25: Consulta de Estoque Interativa
# Localizar produtos em um dicionário.

estoque = {
    "teclado": 50,
    "mouse": 120,
    "monitor": 30
}

produto = input("Produto: ").strip().lower()

if produto in estoque:
    print(f"Quantidade disponível: {estoque[produto]}")
else:
    print("Produto não encontrado no sistema")


# Exercício 26: Análise de Faturamento por Região
# Calcular total e média dos faturamentos.

vendas_regiao = {
    "Norte": 15000,
    "Sul": 22000,
    "Leste": 18000,
    "Oeste": 25000
}

valores = list(vendas_regiao.values())

total = sum(valores)
media = total / len(valores)

print(f"Faturamento total: R$ {total:.2f}")
print(f"Média por região: R$ {media:.2f}")


# Exercício 27: Média de Desempenho
# Calcular a média das notas da funcionária Paula.

desempenho = {
    "Lira": [8, 9, 7],
    "Paula": [10, 9, 10],
    "Tiago": [6, 7, 8]
}

notas_paula = desempenho["Paula"]

media = sum(notas_paula) / len(notas_paula)

print(f"A média de Paula foi {media:.2f}")


# Exercício 28: Limpeza de Banco de Dados
# Remover um produto obsoleto.

produtos = {
    "celular": 1500,
    "camera": 800,
    "radio": 200,
    "fone": 100
}

removido = produtos.pop("radio")

print(f"Produto removido: R$ {removido}")

print("celular" in produtos)


# Exercício 29: Automação de Convites
# Exibir uma contagem regressiva de 10 minutos.

for minuto in range(10, 0, -1):
    print(
        f"Lembrete: O treinamento de Python "
        f"começa em {minuto} minutos."
    )


# Exercício 30: Comissão Progressiva
# Calcular a comissão total recebida pelo vendedor.

vendas = [2000, 5000, 1000, 8000, 3000]

comissao_total = 0

for venda in vendas:

    if venda > 4000:
        comissao = venda * 0.10
    else:
        comissao = venda * 0.05

    comissao_total += comissao

print(
    f"Comissão total: R$ {comissao_total:.2f}"
)



# Exercício 31: Verificação de Estoque Crítico
# Identificar produtos com quantidade abaixo do estoque mínimo.

estoque_produtos = [
    "monitor",
    "teclado",
    "mouse",
    "headset",
    "gabinete"
]

estoque_quantidades = [5, 12, 2, 8, 15]

estoque_minimo = 8

for indice in range(len(estoque_produtos)):

    produto = estoque_produtos[indice]
    quantidade = estoque_quantidades[indice]

    if quantidade < estoque_minimo:
        print(
            f"ALERTA: O produto {produto} "
            f"está com apenas {quantidade} "
            f"unidades no estoque!"
        )


# Exercício 32: Análise de Custos Mensais
# Comparar gastos reais com a meta definida.

metas = {
    "jan": 1000,
    "fev": 1200,
    "mar": 1100
}

gastos = {
    "jan": 900,
    "fev": 1350,
    "mar": 1100
}

for mes in metas:

    if gastos[mes] <= metas[mes]:
        print(
            f"Mês {mes}: Dentro do orçamento."
        )

    else:
        diferenca = gastos[mes] - metas[mes]

        print(
            f"Mês {mes}: Orçamento "
            f"estourado em R$ {diferenca:.2f}"
        )



# Exercício 33: Reajuste Geral de Preços
# Aplicar aumento percentual em todos os produtos.

precos = {
    "celular": 1500,
    "tablet": 2500,
    "notebook": 5000
}

percentual = float(
    input("Percentual de aumento: ")
)

for produto in precos:

    precos[produto] = (
        precos[produto] *
        (1 + percentual / 100)
    )

print("\nNovo catálogo:")

for produto, preco in precos.items():

    print(
        f"{produto} -> "
        f"R$ {preco:.2f}"
    )


# Exercício 34: Padronizador de Nomes de Produtos
# Criar uma função para padronizar textos.

def padronizar_texto(texto):
    return texto.strip().title()

produtos_baguncados = [
    " iphone 13 ",
    "MACBOOK PRO ",
    " aIrPoDs Pro",
    "iPad mini ",
    " caixa de som bluetooth "
]

for produto in produtos_baguncados:
    print(
        padronizar_texto(produto)
    )


# Exercício 35: Calculadora de Imposto Sobre Serviço

def calcular_iss(valor):

    if valor > 5000:
        return valor * 0.05

    else:
        return valor * 0.03

nota1 = 8000
nota2 = 2000

print(
    f"ISS da nota 1: "
    f"R$ {calcular_iss(nota1):.2f}"
)

print(
    f"ISS da nota 2: "
    f"R$ {calcular_iss(nota2):.2f}"
)



# Exercício 36: Analisador de Margem de Lucro
# Avaliar se a margem é saudável.

def analisar_margem(
        faturamento,
        custo):

    lucro = faturamento - custo

    margem = lucro / faturamento

    if margem >= 0.30:
        return "Margem Saudável"

    return "Margem Baixa"

resultado = analisar_margem(
    10000,
    6000
)

print(resultado)

# Exercício 37: Verificador de Meta

def quem_bateu_meta(
        vendedores,
        meta):

    for nome, valor in vendedores.items():

        if valor >= meta:

            print(
                f"Vendedor {nome} "
                f"bateu a meta!"
            )

equipe_vendas = {
    "João": 12000,
    "Maria": 9500,
    "Ricardo": 10000,
    "Fernanda": 15200,
    "Paulo": 5000
}

meta_objetivo = 10000

quem_bateu_meta(
    equipe_vendas,
    meta_objetivo
)


# Exercício 37: Verificador de Meta

def quem_bateu_meta(
        vendedores,
        meta):

    for nome, valor in vendedores.items():

        if valor >= meta:

            print(
                f"Vendedor {nome} "
                f"bateu a meta!"
            )

equipe_vendas = {
    "João": 12000,
    "Maria": 9500,
    "Ricardo": 10000,
    "Fernanda": 15200,
    "Paulo": 5000
}

meta_objetivo = 10000

quem_bateu_meta(
    equipe_vendas,
    meta_objetivo
)


# Exercício 37: Verificador de Meta

def quem_bateu_meta(
        vendedores,
        meta):

    for nome, valor in vendedores.items():

        if valor >= meta:

            print(
                f"Vendedor {nome} "
                f"bateu a meta!"
            )

equipe_vendas = {
    "João": 12000,
    "Maria": 9500,
    "Ricardo": 10000,
    "Fernanda": 15200,
    "Paulo": 5000
}

meta_objetivo = 10000

quem_bateu_meta(
    equipe_vendas,
    meta_objetivo
)


# Exercício 38: Conversor de Moeda Interativo

def converter_para_real(
        preco_dolar,
        cotacao):

    return preco_dolar * cotacao


def processar_lista_precos(
        precos,
        cotacao):

    for preco in precos:

        valor_real = (
            converter_para_real(
                preco,
                cotacao
            )
        )

        print(
            f"O item custa "
            f"R$ {valor_real:.2f}"
        )

precos_usd = [100, 50, 250]

processar_lista_precos(
    precos_usd,
    5.20
)


# Exercício 39: Localização de Entregas
# Utilizar unpacking em uma tupla.

coordenadas = (
    -23.5505,
    -46.6333
)

latitude, longitude = coordenadas

print(
    f"Iniciando entrega. "
    f"Latitude: {latitude}, "
    f"Longitude: {longitude}"
)


# Exercício 40: Resumo de Folha de Pagamento
# Retornar múltiplos valores usando tupla.

def calcular_folha(
        salario_bruto):

    desconto = salario_bruto * 0.10

    salario_liquido = (
        salario_bruto - desconto
    )

    return desconto, salario_liquido


desconto, salario_liquido = (
    calcular_folha(5000)
)

print(
    f"Desconto: R$ {desconto:.2f} | "
    f"Salário Líquido: "
    f"R$ {salario_liquido:.2f}"
)



# Exercício 40: Resumo de Folha de Pagamento
# Retornar múltiplos valores usando tupla.

def calcular_folha(
        salario_bruto):

    desconto = salario_bruto * 0.10

    salario_liquido = (
        salario_bruto - desconto
    )

    return desconto, salario_liquido


desconto, salario_liquido = (
    calcular_folha(5000)
)

print(
    f"Desconto: R$ {desconto:.2f} | "
    f"Salário Líquido: "
    f"R$ {salario_liquido:.2f}"
)



# Exercício 41: Processamento de Vendas por Unidade
# Utilizar unpacking diretamente no laço para calcular
# o valor total vendido de cada produto.

vendas_dia = [
    ("Monitor", 900, 2),
    ("Teclado", 150, 5),
    ("Mouse", 80, 10)
]

for produto, preco_unitario, quantidade in vendas_dia:

    total = preco_unitario * quantidade

    print(
        f"Produto: {produto} | "
        f"Total: R$ {total:.2f}"
    )


# Exercício 42: Performance de Vendas Regionais
# Criar uma função que retorne total e média.

def analisar_vendas(vendas):

    total = sum(vendas)
    media = total / len(vendas)

    return total, media


dados_filiais = {
    "Matriz": [10000, 15000, 20000],
    "Filial Sul": [5000, 7000]
}

for filial, vendas in dados_filiais.items():

    total, media = analisar_vendas(vendas)

    print(
        f"Filial {filial} -> "
        f"Total: R$ {total:.2f}, "
        f"Média: R$ {media:.2f}"
    )


# Exercício 43: Gestão de Chamados de Suporte
# Retornar a quantidade de chamados e o maior tempo de espera.

def resumo_chamados(tempos):

    quantidade = len(tempos)
    maior_tempo = max(tempos)

    return quantidade, maior_tempo


tempos = [15, 45, 10, 120, 30]

quantidade, maior_tempo = resumo_chamados(tempos)

print(
    f"Foram registrados {quantidade} chamados. "
    f"O maior tempo de espera foi de "
    f"{maior_tempo} minutos."
)


# Exercício 44
# Calcular o valor total de uma lista de vendas.

def calcular_total(vendas):

    return sum(vendas)

vendas = [1500, 2000, 1800, 2500]

total = calcular_total(vendas)

print(f"Total vendido: R$ {total:.2f}")


# Exercício 45
# Encontrar o maior valor registrado.

valores = [120, 350, 220, 980, 410]

maior = max(valores)

print(f"Maior valor encontrado: {maior}")


# Exercício 46
# Calcular a média de notas de uma turma.

notas = [8.5, 7.0, 9.5, 6.0, 10]

media = sum(notas) / len(notas)

print(f"Média da turma: {media:.2f}")


# Exercício 47
# Contar quantos produtos existem na lista.

produtos = [
    "Monitor",
    "Mouse",
    "Teclado",
    "Headset",
    "Webcam"
]

quantidade = len(produtos)

print(
    f"Quantidade de produtos: "
    f"{quantidade}"
)


# Exercício 48
# Mostrar produtos com preço superior a R$ 500.

produtos = {
    "Monitor": 900,
    "Mouse": 120,
    "Teclado": 250,
    "Notebook": 3500,
    "Webcam": 450
}

for produto, preco in produtos.items():

    if preco > 500:

        print(
            f"{produto} - "
            f"R$ {preco:.2f}"
        )


# Exercício 49
# Exibir total, média, maior e menor venda.

vendas = [2000, 3500, 1500, 4200, 2800]

total = sum(vendas)
media = total / len(vendas)
maior = max(vendas)
menor = min(vendas)

print(f"Total: R$ {total:.2f}")
print(f"Média: R$ {media:.2f}")
print(f"Maior venda: R$ {maior:.2f}")
print(f"Menor venda: R$ {menor:.2f}")


# Exercício 50
# Gerar um relatório contendo nome e salário.

funcionarios = {
    "Ana": 2500,
    "Carlos": 3200,
    "Marcos": 4100,
    "Juliana": 3800
}

for nome, salario in funcionarios.items():

    print(
        f"Funcionário: {nome} | "
        f"Salário: R$ {salario:.2f}"
    )



# Exercício 50
# Gerar um relatório contendo nome e salário.

funcionarios = {
    "Ana": 2500,
    "Carlos": 3200,
    "Marcos": 4100,
    "Juliana": 3800
}

for nome, salario in funcionarios.items():

    print(
        f"Funcionário: {nome} | "
        f"Salário: R$ {salario:.2f}"
    )



