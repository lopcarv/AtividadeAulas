estudante = input("É estudante? (s/n): ")
idoso = input("É idoso? (s/n): ")

if estudante == "s" or idoso == "s":
    print("Desconto concedido")
else:
    print("Sem desconto")