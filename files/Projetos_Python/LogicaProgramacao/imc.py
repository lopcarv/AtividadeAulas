nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
peso = float(input("Digite o seu peso : "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)
mensagem = f"Olá, {nome}! Você tem {idade} anos e o seu IMC é {imc:.2f}."
print(mensagem)