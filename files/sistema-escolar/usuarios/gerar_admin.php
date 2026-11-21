<?php
// Inclui a conexão com a base de dados
require_once "../config/conexao.php";

try {
    // 1. Limpa o utilizador 'admin' anterior se existir
    $stmtDelete = $pdo->prepare("DELETE FROM usuarios WHERE usuario = 'admin'");
    $stmtDelete->execute();

    // 2. Define o utilizador e a senha em texto limpo
    $usuario = 'admin';
    $senhaLimpa = 'admin123';

    // 3. Gera o hash seguro no próprio servidor PHP
    $senhaHash = password_hash($senhaLimpa, PASSWORD_DEFAULT);

    // 4. Insere o administrador com alterar_senha = 0
    $sql = "INSERT INTO usuarios (usuario, senha, alterar_senha) VALUES (:usuario, :senha, 0)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([
        ':usuario' => $usuario,
        ':senha'   => $senhaHash
    ]);

    echo "<h2 style='color: green;'>Administrador criado com sucesso!</h2>";
    echo "<p><strong>Utilizador:</strong> admin</p>";
    echo "<p><strong>Senha:</strong> admin123</p>";
    echo "<p><a href='login.php'>Clique aqui para fazer Login</a></p>";

} catch (PDOException $e) {
    echo "<h2 style='color: red;'>Erro ao criar administrador:</h2> " . $e->getMessage();
}
?>