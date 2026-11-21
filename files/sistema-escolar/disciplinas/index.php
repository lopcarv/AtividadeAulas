<?php
// 1. Início da sessão e inclusão da conexão
session_start();

// Garante que o usuário está logado (se não estiver, vai para o login)
if (!isset($_SESSION['usuario_id'])) {
    header("Location: ../usuarios/login.php");
    exit();
}

// Inclui o arquivo de conexão PDO com o banco de dados
require_once "../config/conexao.php"; 

$mensagem = "";
$erro = "";

// 2. Lógica para cadastrar uma nova disciplina ao enviar o formulário
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['cadastrar'])) {
    $nome = trim($_POST['nome']);
    $carga_horaria = intval($_POST['carga_horaria']);

    if (!empty($nome) && $carga_horaria > 0) {
        try {
            $sql = "INSERT INTO disciplinas (nome, carga_horaria) VALUES (:nome, :carga_horaria)";
            $stmt = $pdo->prepare($sql);
            $stmt->execute([
                ':nome' => $nome,
                ':carga_horaria' => $carga_horaria
            ]);
            $mensagem = "Disciplina cadastrada com sucesso!";
        } catch (PDOException $e) {
            $erro = "Erro ao cadastrar: " . $e->getMessage();
        }
    } else {
        $erro = "Preencha todos os campos corretamente.";
    }
}

// 3. Consulta para listar todas as disciplinas cadastradas
try {
    $sql_listar = "SELECT * FROM disciplinas ORDER BY nome ASC";
    $stmt_listar = $pdo->query($sql_listar);
    $disciplinas = $stmt_listar->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    $disciplinas = [];
    $erro = "Erro ao carregar disciplinas: " . $e->getMessage();
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão de Disciplinas - Sistema Escolar</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
        /* Estilos básicos para organização da tela */
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f6f9; }
        header { display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 15px 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        header nav a { margin: 0 10px; text-decoration: none; color: #333; font-weight: bold; }
        .container { padding: 30px; max-width: 900px; margin: 0 auto; }
        .card { background: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 20px; }
        form input, form button { padding: 10px; margin-right: 10px; border: 1px solid #ccc; border-radius: 4px; }
        form button { background-color: #007bff; color: white; border: none; cursor: pointer; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        table th, table td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        table th { background-color: #f8f9fa; }
        .sucesso { color: green; }
        .erro { color: red; }
    </style>
</head>
<body>

    <!-- Cabeçalho idêntico à interface informada -->
    <header>
        <div class="logo">
            <strong>Sistema Escolar</strong>
        </div>
        <nav>
            <a href="../index.php">Dashboard</a>
            <a href="../alunos/index.php">Alunos</a>
            <a href="index.php" style="color: #007bff;">Disciplinas</a>
            <a href="../matriculas/index.php">Matrículas</a>
        </nav>
        <div>
            Olá, <strong><?= htmlspecialchars($_SESSION['usuario_nome'] ?? 'admin') ?></strong> | 
            <a href="../logout.php" style="color: red; text-decoration: none;">Sair</a>
        </div>
    </header>

    <div class="container">
        <h2>Gestão de Disciplinas</h2>

        <!-- Exibição de Mensagens de Alerta -->
        <?php if (!empty($mensagem)): ?>
            <p class="sucesso"><?= htmlspecialchars($mensagem) ?></p>
        <?php endif; ?>
        <?php if (!empty($erro)): ?>
            <p class="erro"><?= htmlspecialchars($erro) ?></p>
        <?php endif; ?>

        <!-- Formulário para Cadastrar Disciplina -->
        <div class="card">
            <h3>Nova Disciplina</h3>
            <form method="POST" action="index.php">
                <input type="text" name="nome" placeholder="Nome da Disciplina (ex: Matemática)" required>
                <input type="number" name="carga_horaria" placeholder="Carga Horária (horas)" required min="1">
                <button type="submit" name="cadastrar">Salvar Disciplina</button>
            </form>
        </div>

        <!-- Tabela de Listagem de Disciplinas -->
        <div class="card">
            <h3>Disciplinas Cadastradas</h3>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome da Disciplina</th>
                        <th>Carga Horária</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (count($disciplinas) > 0): ?>
                        <?php foreach ($disciplinas as $d): ?>
                            <tr>
                                <td><?= htmlspecialchars($d['id']) ?></td>
                                <td><?= htmlspecialchars($d['nome']) ?></td>
                                <td><?= htmlspecialchars($d['carga_horaria']) ?>h</td>
                            </tr>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <tr>
                            <td colspan="3">Nenhuma disciplina cadastrada ainda.</td>
                        </tr>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
<!-- Inclui o rodapé automaticamente -->
    <?php include_once __DIR__ . "/../includes/footer.php"; ?>

</body>
</html>