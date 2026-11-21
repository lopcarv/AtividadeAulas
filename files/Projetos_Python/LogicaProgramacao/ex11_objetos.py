# Classe
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Nota: {self.nota}")


# Objetos
aluno1 = Aluno("Carlos", 8)
aluno2 = Aluno("Joana", 6)
aluno3 = Aluno("Pedro", 4)
aluno4 = Aluno("Lucas", 10)
aluno5 = Aluno("Maria", 5)

# Lista de objetos
alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

# Exibindo os dados
print("=== Lista de Alunos ===")
for aluno in alunos:
    aluno.exibir_dados()

# Maior nota
maior_nota = max(alunos, key=lambda aluno: aluno.nota)
print(f"\nMaior nota: {maior_nota.nome} ({maior_nota.nota})")

# Menor nota
menor_nota = min(alunos, key=lambda aluno: aluno.nota)
print(f"Menor nota: {menor_nota.nome} ({menor_nota.nota})")

# Quantidade de objetos
print(f"\nQuantidade de objetos criados: {len(alunos)}")

# Quantidade de atributos
print("Quantidade de atributos da classe Aluno: 2 (nome e nota)")