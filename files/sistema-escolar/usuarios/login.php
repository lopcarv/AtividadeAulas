<?php
// 1. Inicia a sessão no PHP
session_start();

// 2. Inclui o ficheiro de conexão com a base de dados
require_once "../config/conexao.php";

$erro = "";

// 3. Processa o envio do formulário
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $usuario = trim($_POST['usuario'] ?? '');
    $senha   = trim($_POST['senha'] ?? '');

    if (!empty($usuario) && !empty($senha)) {
        try {
            // CORREÇÃO: Procura apenas pela coluna 'nome' ou 'usuario' na tabela
            // Ajuste 'usuario' para 'nome' caso a tua coluna se chame 'nome'
            $sql = "SELECT * FROM usuarios WHERE usuario = :usuario LIMIT 1";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([':usuario' => $usuario]);
            $dadosUsuario = $stmt->fetch(PDO::FETCH_ASSOC);

            // Se não encontrou pela coluna 'usuario', tenta pela coluna 'nome' (Fallback de segurança)
            if (!$dadosUsuario) {
                $sql = "SELECT * FROM usuarios WHERE nome = :usuario LIMIT 1";
                $stmt = $pdo->prepare($sql);
                $stmt->execute([':usuario' => $usuario]);
                $dadosUsuario = $stmt->fetch(PDO::FETCH_ASSOC);
            }

            // Valida a palavra-passe e inicia a sessão
            if ($dadosUsuario && password_verify($senha, $dadosUsuario['senha'])) {
                
                $_SESSION['usuario_id']   = $dadosUsuario['id'];
                $_SESSION['usuario_nome'] = $dadosUsuario['nome'] ?? $dadosUsuario['usuario'];

                // Redireciona diretamente para o Dashboard
                header("Location: ../dashboard.php");
                exit();

            } else {
                $erro = "Utilizador ou palavra-passe incorretos.";
            }
        } catch (PDOException $e) {
            $erro = "Erro no sistema: " . $e->getMessage();
        }
    } else {
        $erro = "Preencha todos os campos para entrar.";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Sistema Escolar</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 100%; max-width: 350px; }
        .login-card h2 { margin-top: 0; text-align: center; color: #0d6efd; }
        .form-group { margin-bottom: 15px; }
        .form-group label { display: block; margin-bottom: 5px; font-weight: bold; }
        .form-group input { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        button { width: 100%; padding: 10px; background-color: #0d6efd; color: white; border: none; border-radius: 4px; font-size: 16px; cursor: pointer; }
        button:hover { background-color: #0b5ed7; }
        .erro { color: red; font-size: 14px; text-align: center; margin-bottom: 15px; }
    </style>
</head>
<body>

    <div class="login-card">
        <h2>Sistema Escolar</h2>
        
        <?php if (!empty($erro)): ?>
            <div class="erro"><?= htmlspecialchars($erro) ?></div>
        <?php endif; ?>

        <form method="POST" action="login.php">
            <div class="form-group">
                <label for="usuario">Utilizador</label>
                <input type="text" id="usuario" name="usuario" required autofocus placeholder="Digite seu usuário">
            </div>
            
            <div class="form-group">
                <label for="senha">Palavra-passe</label>
                <input type="password" id="senha" name="senha" required placeholder="Digite sua senha">
            </div>

            <button type="submit">Entrar</button>
        </form>
    </div>

</body>
</html>