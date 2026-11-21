# Desafio 10.1 (Sigla de Aeroporto)
cidade = "Capanema"
sigla = cidade[:3].upper() + "-PA"
print("Código regional:", sigla)

# Desafio 10.2 (Código de Lote)
categoria = "eletronicos"
ano = "2026"
codigo_lote = categoria[:4].upper() + ano[-2:]
print("Código do lote:", codigo_lote)

# Desafio 11.1 (Cálculo de Comissão sobre Boleto)
valor_str = input("Digite o valor do boleto (Ex: R$ 1.250,50): ")
valor_limpo = valor_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
valor = float(valor_limpo)
liquido = valor - (valor * 0.035)
print(f"Valor líquido: R$ {liquido:.2f}")

# Desafio 11.2 (Conversor de Orçamento)
orcamento_str = input("Digite o orçamento (Ex: R$ 3.400,00): ")
orcamento_limpo = orcamento_str.replace("R$", "").replace(".", "").replace(",", ".").strip()
orcamento = float(orcamento_limpo)
parcela = orcamento / 4
print(f"4 parcelas de: R$ {parcela:.2f}")

# Desafio 12.1 (Gerador de E-mail Corporativo)
nome_completo = input("Nome completo: ")
partes = nome_completo.strip().lower().split()
primeiro = partes[0]
ultimo = partes[-1]
email = f"{primeiro}.{ultimo}@empresa.com.br"
print("E-mail gerado:", email)

# Desafio 12.2 (Crachá de Evento)
nome = input("Digite seu nome completo: ")
cargo = input("Digite seu cargo: ")
primeiro_nome = nome.strip().split()[0].upper()
cargo_formatado = cargo.strip().title()
print(f"--- CRACHÁ ---\nNome: {primeiro_nome}\nCargo: {cargo_formatado}")

# Desafio 13.1 (Fechamento Trimestral)
janeiro = float(input("Faturamento de Janeiro: "))
fevereiro = float(input("Faturamento de Fevereiro: "))
marco = float(input("Faturamento de Março: "))
total_trimestre = janeiro + fevereiro + marco
media_mensal = total_trimestre / 3
print(f"Total: R$ {total_trimestre:,.2f} | Média: R$ {media_mensal:,.2f}")

# Desafio 13.2 (Rateio de Despesas)
energia = float(input("Valor da conta de energia: "))
internet = float(input("Valor da conta de internet: "))
total_contas = energia + internet
por_socio = total_contas / 3
print(f"Total Geral: R$ {total_contas:,.2f} | Por Sócio: R$ {por_socio:,.2f}")


# Desafio 14.1 (Conversor de Velocidade)
kmh = float(input("Velocidade em km/h: "))
ms = kmh / 3.6
print(f"Velocidade em m/s: {ms:.2f}")

# Desafio 14.2 (Cálculo de IMC)
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

# Desafio 15.1 (Cálculo de Frete por Peso)
carga = input("Nome da carga: ")
peso_unitario = float(input("Peso de cada caixa (kg): "))
qtd_caixas = int(input("Quantidade de caixas: "))
peso_total = peso_unitario * qtd_caixas
custo_frete = peso_total * 2.50
print(f"Carga: {carga} | Peso Total: {peso_total}kg | Frete: R$ {custo_frete:.2f}")

# Desafio 15.2 (Orçamento de Reforma)
material = input("Nome do material: ")
preco_m2 = float(input("Preço por m²: "))
qtd_m2 = float(input("Quantidade de m²: "))
valor_total = (preco_m2 * qtd_m2) * 1.10
print(f"Orçamento para {material} (com 10% de margem): R$ {valor_total:.2f}")

# Desafio 16.1 (Monitoramento de Temperaturas)
temperaturas = [28.5, 31.0, 26.8, 33.2, 29.4, 30.1, 27.5]
media = sum(temperaturas) / len(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)
amplitude = maior - menor
print(f"Média: {media:.2f}°C | Máx: {maior}°C | Mín: {menor}°C | Amplitude: {amplitude:.2f}°C")

# Desafio 16.2 (Análise de Notas da Turma)
notas = [7.5, 8.0, 6.0, 9.5, 5.5, 8.5]
total_alunos = len(notas)
media_turma = sum(notas) / total_alunos
print(f"Alunos: {total_alunos} | Média: {media_turma:.2f} | Maior: {max(notas)} | Menor: {min(notas)}")

# Desafio 17.1 (Fila de Atendimento)
fila = ["Ana", "Bruno", "Carla", "Daniel"]
fila.append("Eduardo")
indice_carla = fila.index("Carla")
fila[indice_carla] = "Carla Silva"
print("Marcos está na fila?", "Marcos" in fila)
fila.remove("Ana")
print("Fila final:", fila)

# Desafio 17.2 (Catálogo de Cursos)
cursos = ["Excel", "Word", "PowerPoint", "Access"]
cursos.append("Python")
cursos.remove("Access")
indice_excel = cursos.index("Excel")
cursos[indice_excel] = "Excel Avançado"
print("Power BI está no catálogo?", "Power BI" in cursos)
print("Cursos atualizados:", cursos)


# Desafio 18.1 (Pódio de Pontuação)
pontos = [450, 820, 310, 950, 670, 740]
pontos.sort(reverse=True)
podio = pontos[:2] # ou [:3] conforme o desafio
print("Ranking completo:", pontos)
print("Pódio:", podio)

# Desafio 18.2 (Menores Cotações)
orcamentos = [12500, 9800, 14200, 8900, 11000]
orcamentos.sort()
melhores_propostas = orcamentos[:2]
print("Orçamentos ordenados:", orcamentos)
print("Melhores propostas:", melhores_propostas)

# Desafio 19.1 (Unificação de Turnos)
turno_manha = ["Lucas", "Mariana", "Pedro"]
turno_tarde = ["Sofia", "Rafael", "Beatriz"]
turno_manha.extend(turno_tarde)
posicao = turno_manha.index("Rafael")
print("Escala geral:", turno_manha)
print(f"Rafael é o {posicao + 1}º colaborador da escala geral.")

# Desafio 19.2 (Cronograma de Módulos)
modulo_1 = ["Lógica", "Variáveis", "Strings"]
modulo_2 = ["Listas", "Dicionários", "Funções"]
modulo_1.extend(modulo_2)
pos_listas = modulo_1.index("Listas")
print(f"Listas está na aula {pos_listas + 1}.")

# Desafio 20.1 (Controle de Salários)
funcionarios = ["João", "Maria", "Carlos"]
salarios = [2500.0, 3200.0, 2800.0]

nome_busca = input("Nome do funcionário para atualizar: ").title()
novo_salario = float(input("Novo salário: "))

indice = funcionarios.index(nome_busca)
salarios[indice] = novo_salario

print("Funcionários:", funcionarios)
print("Salários atualizados:", salarios)

# Desafio 20.2 (Atualização de Estoque por Produto)
itens = ["Cadeira", "Mesa", "Luminária"]
quantidades = [15, 8, 25]

item_busca = input("Nome do item para atualizar estoque: ").title()
nova_qtd = int(input("Nova quantidade: "))

idx = itens.index(item_busca)
quantidades[idx] = nova_qtd

print("Itens:", itens)
print("Quantidades atualizadas:", quantidades)


