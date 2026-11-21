salario = float(input("Digite o salário: R$ "))
paga_imposto = salario > 1200.00
if paga_imposto:
    print("Deve pagar imposto.")
else:
    print("Não deve pagar imposto.")