<?php
require_once "../config/conexao.php";

$mensagem = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Captura e limpa os valores digitados no formulário
    $nome          = trim($_POST["nome"] ?? "");
    $carga_horaria = intval($_POST["carga_horaria"] ?? 0);

    // Valida se o nome foi preenchido e se a carga horária é maior que zero
    if (!empty($nome) && $carga_horaria > 0) {
        try {
            // Insere a nova disciplina no banco de dados
            $sql = "INSERT INTO disciplinas (nome, carga_horaria) VALUES (:nome, :carga_horaria)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([
                ':nome'          => $nome,
                ':carga_horaria' => $carga_horaria
            ]);

            // Redireciona para a listagem após salvar
            header("Location: listar.php");
            exit;

        } catch (PDOException $e) {
            $mensagem = "Erro ao cadastrar disciplina: " . $e->getMessage();
        }
    } else {
        $mensagem = "Por favor, preencha o nome e uma carga horária válida.";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastrar Disciplina</title>
</head>
<body>
    <h2>Cadastrar Nova Disciplina</h2>

    <?php if (!empty($mensagem)): ?>
        <p style="color: red;"><?= htmlspecialchars($mensagem) ?></p>
    <?php endif; ?>

    <form action="cadastrar.php" method="POST">
        <label for="nome">Nome da Disciplina:</label><br>
        <input type="text" id="nome" name="nome" placeholder="Ex: Matemática" required><br><br>

        <label for="carga_horaria">Carga Horária (em horas):</label><br>
        <input type="number" id="carga_horaria" name="carga_horaria" min="1" placeholder="Ex: 80" required><br><br>

        <button type="submit">Salvar Disciplina</button>
        <a href="listar.php">Voltar para a Lista</a>
    </form>
</body>
</html>