valor_compra = float(input("Digite o valor da compra: R$ "))

if valor_compra > 1000:
    desconto = valor_compra * 0.10
elif valor_compra > 300:
    desconto = valor_compra * 0.008
elif valor_compra > 100:
    desconto = valor_compra * 0.005
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")