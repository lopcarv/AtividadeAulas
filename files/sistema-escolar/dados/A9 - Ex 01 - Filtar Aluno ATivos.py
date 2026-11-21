import json

def filtrar_alunos_ativos(caminho_entrada, caminho_saida):
    """Lê um arquivo JSON, filtra os alunos ativos e salva em um novo arquivo."""
    try:
        with open(caminho_entrada, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)
        
        alunos_ativos = [aluno for aluno in alunos if aluno.get("ativo") is True]
        
        with open(caminho_saida, "w", encoding="utf-8") as arquivo:
            json.dump(alunos_ativos, arquivo, ensure_ascii=False, indent=4)
            
        print(f"Alunos ativos salvos com sucesso em: {caminho_saida}")
    except Exception as erro:
        print(f"Ocorreu um erro ao filtrar os alunos: {erro}")

if __name__ == "__main__":
    filtrar_alunos_ativos("alunos_exportados.json", "alunos_ativos.json")