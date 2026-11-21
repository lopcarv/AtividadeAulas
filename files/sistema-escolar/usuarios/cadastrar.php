<?php
session_start();

// O ../ serve para subir um nível e encontrar a pasta config
require_once "../config/conexao.php";

// Proteção: Apenas utilizadores logados podem cadastrar novos utilizadores
if (!isset($_SESSION['usuario_id'])) {
    header("Location: login.php");
    exit;
}

$mensagem = "";
$sucesso = false;

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $usuario = trim($_POST["usuario"] ?? "");
    $senhaPadrao = $_POST["senha_padrao"] ?? "";

    if (empty($usuario) || empty($senhaPadrao)) {
        $mensagem = "Preencha o nome do utilizador e a senha padrão.";
    } else {
        try {
            // Verificação de duplicados
            $stmtCheck = $pdo->prepare("SELECT id FROM usuarios WHERE usuario = :usuario");
            $stmtCheck->execute([':usuario' => $usuario]);

            if ($stmtCheck->rowCount() > 0) {
                $mensagem = "Este nome de utilizador já existe.";
            } else {
                $senhaHash = password_hash($senhaPadrao, PASSWORD_DEFAULT);

                $sql = "INSERT INTO usuarios (usuario, senha, alterar_senha) VALUES (:usuario, :senha, 1)";
                $stmt = $pdo->prepare($sql);
                $stmt->execute([
                    ':usuario' => $usuario,
                    ':senha'   => $senhaHash
                ]);

                $sucesso = true;
                $mensagem = "Utilizador '{$usuario}' criado com sucesso!";
            }
        } catch (PDOException $e) {
            $mensagem = "Erro ao cadastrar: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Cadastrar Utilizador - Sistema Escolar</title>
    <!-- O ../ sublinha que o CSS está na pasta assets na raiz -->
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

    <h2>Cadastrar Novo Utilizador</h2>

    <?php if (!empty($mensagem)): ?>
        <p style="color: <?= $sucesso ? 'green' : 'red'; ?>;"><?= htmlspecialchars($mensagem) ?></p>
    <?php endif; ?>

    <form method="POST" action="">
        <label for="usuario">Nome de Utilizador:</label><br>
        <input type="text" id="usuario" name="usuario" placeholder="Ex: joao_silva" required><br><br>

        <label for="senha_padrao">Senha Padrão (Temporária):</label><br>
        <input type="text" id="senha_padrao" name="senha_padrao" value="123456" required><br><br>

        <button type="submit">Criar Utilizador</button>
        <a href="../index.php">Voltar ao Painel Principal</a>
    </form>

</body>
</html>