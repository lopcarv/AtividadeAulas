<?php
// 1. Garante a proteção de sessão e a conexão com a base de dados
require_once __DIR__ . "/../config/verifica_sessao.php";
require_once __DIR__ . "/../config/conexao.php";

// 2. Inclui o cabeçalho visual padrão do sistema
include_once __DIR__ . "/../includes/header.php";

$alunos = [];
$erro = null;

try {
    // Consulta buscando exatamente as colunas confirmadas no MySQL
    $sql = "SELECT id, nome, matricula, email, cpf, data_nascimento, ativo 
            FROM alunos 
            ORDER BY nome ASC";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();
    $alunos = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    $erro = "Erro ao consultar a base de dados: " . $e->getMessage();
}
?>

<main class="main-container">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <h2>Gestão de Alunos</h2>
        <a href="cadastrar.php" class="btn-primary">+ Cadastrar Aluno</a>
    </div>

    <!-- Mensagem de erro caso ocorra falha no SQL -->
    <?php if ($erro): ?>
        <div style="background-color: #f8d7da; color: #721c24; padding: 12px; border-radius: 4px; margin-bottom: 20px;">
            <?= htmlspecialchars($erro) ?>
        </div>
    <?php endif; ?>

    <!-- Tabela de Alunos -->
    <table border="1" cellpadding="10" cellspacing="0" style="width: 100%; border-collapse: collapse; background: #ffffff;">
        <thead>
            <tr style="background-color: #2c3e50; color: #ffffff; text-align: left;">
                <th>ID</th>
                <th>Matrícula</th>
                <th>Nome</th>
                <th>E-mail</th>
                <th>CPF</th>
                <th>Data Nasc.</th>
                <th>Status</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            <?php if (!empty($alunos)): ?>
                <?php foreach ($alunos as $aluno): ?>
                    <tr>
                        <td><?= htmlspecialchars($aluno['id']) ?></td>
                        <td><strong><?= htmlspecialchars($aluno['matricula']) ?></strong></td>
                        <td><?= htmlspecialchars($aluno['nome']) ?></td>
                        <td><?= htmlspecialchars($aluno['email']) ?></td>
                        <td><?= htmlspecialchars($aluno['cpf'] ?? 'Não informado') ?></td>
                        <td>
                            <!-- Formata a data de YYYY-MM-DD para DD/MM/YYYY -->
                            <?= $aluno['data_nascimento'] ? date('d/m/Y', strtotime($aluno['data_nascimento'])) : '-' ?>
                        </td>
                        <td>
                            <span style="color: <?= $aluno['ativo'] ? 'green' : 'red' ?>; font-weight: bold;">
                                <?= $aluno['ativo'] ? 'Ativo' : 'Inativo' ?>
                            </span>
                        </td>
                        <td>
                            <a href="editar.php?id=<?= $aluno['id'] ?>" style="color: #3498db; margin-right: 10px;">Editar</a>
                            <a href="excluir.php?id=<?= $aluno['id'] ?>" style="color: #e74c3c;" onclick="return confirm('Tem certeza que deseja excluir este aluno?');">Excluir</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr>
                    <td colspan="8" style="text-align: center; padding: 20px;">Nenhum aluno cadastrado até o momento.</td>
                </tr>
            <?php endif; ?>
        </tbody>
    </table>
</main>

</body>
</html>