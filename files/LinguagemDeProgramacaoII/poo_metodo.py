class Aluno:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_situacao(self):
        if self.nota >= 7:
            return "Aprovado"

        return "Reprovado"


# Testando
aluno = Aluno("Mauricio", 6)

print(f"Aluno: {aluno.nome}, Nota: {aluno.nota}, Situação: {aluno.verificar_situacao()}")