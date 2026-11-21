import json

def filtrar_clientes_por_cidade(caminho_entrada, cidade_desejada, caminho_saida):
    try:
        with open(caminho_entrada, "r", encoding="utf-8") as arquivo:
            clientes = json.load(arquivo)

        clientes_filtrados = [
            cliente
            for cliente in clientes
            if cliente.get("endereco_debito", {}).get("cidade", "").lower()
            == cidade_desejada.lower()
        ]

        with open(caminho_saida, "w", encoding="utf-8") as arquivo:
            json.dump(clientes_filtrados, arquivo, ensure_ascii=False, indent=4)

        print(f"{len(clientes_filtrados)} clientes encontrados em {cidade_desejada}")
        print(f"Arquivo salvo em: {caminho_saida}")

    except Exception as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    filtrar_clientes_por_cidade(
        "clientes.json",
        "Belém",
        "clientes_belem.json"
    )