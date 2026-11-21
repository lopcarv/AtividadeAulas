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

