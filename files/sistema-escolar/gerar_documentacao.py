from pathlib import Path
from datetime import datetime

# CAMINHO DA PASTA DO SISTEMA
PROJETO = Path("sistema-escolar")

ARQUIVO_SAIDA = "DOCUMENTACAO_SISTEMA_ESCOLAR.md"

EXTENSOES = {
    ".php",
    ".py",
    ".js",
    ".css",
    ".sql",
    ".md",
    ".txt",
    ".html"
}

LINGUAGENS = {
    ".php": "php",
    ".py": "python",
    ".js": "javascript",
    ".css": "css",
    ".sql": "sql",
    ".md": "markdown",
    ".txt": "text",
    ".html": "html"
}


def gerar_arvore(pasta, prefixo=""):
    itens = sorted(
        pasta.iterdir(),
        key=lambda x: (x.is_file(), x.name.lower())
    )

    resultado = []

    for indice, item in enumerate(itens):

        ultimo = indice == len(itens) - 1

        conector = "└── " if ultimo else "├── "

        resultado.append(
            prefixo + conector + item.name
        )

        if item.is_dir():

            extensao = "    " if ultimo else "│   "

            resultado.extend(
                gerar_arvore(
                    item,
                    prefixo + extensao
                )
            )

    return resultado


with open(
    ARQUIVO_SAIDA,
    "w",
    encoding="utf-8"
) as doc:

    doc.write("# DOCUMENTAÇÃO DO SISTEMA ESCOLAR\n\n")

    doc.write(
        f"Data da geração: "
        f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
    )

    doc.write("## Estrutura do Projeto\n\n")

    doc.write("```text\n")

    doc.write(PROJETO.name + "/\n")

    for linha in gerar_arvore(PROJETO):
        doc.write(linha + "\n")

    doc.write("```\n\n")

    total_arquivos = 0

    for arquivo in sorted(PROJETO.rglob("*")):

        if not arquivo.is_file():
            continue

        if arquivo.suffix.lower() not in EXTENSOES:
            continue

        total_arquivos += 1

        try:

            conteudo = arquivo.read_text(
                encoding="utf-8"
            )

        except:

            try:

                conteudo = arquivo.read_text(
                    encoding="latin1"
                )

            except Exception as erro:

                conteudo = (
                    f"Erro ao ler arquivo: {erro}"
                )

        linguagem = LINGUAGENS.get(
            arquivo.suffix.lower(),
            "text"
        )

        caminho_relativo = arquivo.relative_to(PROJETO)

        doc.write(
            f"# Arquivo: {caminho_relativo}\n\n"
        )

        doc.write(
            f"**Tamanho:** "
            f"{arquivo.stat().st_size} bytes\n\n"
        )

        doc.write(
            f"```{linguagem}\n"
        )

        doc.write(conteudo)

        doc.write("\n```\n\n")

        doc.write("---\n\n")

    doc.write("## Estatísticas\n\n")

    doc.write(
        f"- Total de arquivos: {total_arquivos}\n"
    )

print(
    f"Documentação gerada com sucesso: "
    f"{ARQUIVO_SAIDA}"
)