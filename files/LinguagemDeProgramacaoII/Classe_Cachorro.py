class Cachorro:
    def __init__(self, raca, pais):
        self.raca = raca
        self.pais = pais

c1 = Cachorro("Labrador", "Canadá")
c2 = Cachorro("Poodle", "França")
c3 = Cachorro("Beagle", "Inglaterra")

cachorros = [c1, c2, c3]

for cachorro in cachorros:
    print(f"Raça: {cachorro.raca} | País: {cachorro.pais}")