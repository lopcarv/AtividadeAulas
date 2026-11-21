idade = int(input("Digite sua idade: "))

documento = input("Possui documento? (s/n): ")

if idade >= 18 and documento == "s":
    print("Acesso permitido")
else:
    print("Acesso negado")