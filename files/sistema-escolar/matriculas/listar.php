<?php
// Inclui o ficheiro de ligação à base de dados
require_once "../config/conexao.php";

/*
|--------------------------------------------------------------------------
| CONSULTAR MATRÍCULAS
|--------------------------------------------------------------------------
| Procura as matrículas combinando os dados das tabelas de alunos 
| e disciplinas através da junção (JOIN).
*/
try {
    $sql = "
        SELECT 
            m.aluno_id, 
            m.disciplina_id, 
            m.nota, 
            m.media,
            a.nome AS nome_aluno, 
            d.nome AS nome_disciplina
        FROM matriculas m
        INNER JOIN alunos a ON m.aluno_id = a.id
        INNER JOIN disciplinas d ON m.disciplina_id = d.id
        ORDER BY a.nome ASC, d.nome ASC
    ";

    $stmt = $pdo->query($sql);
    $matriculas = $stmt->fetchAll();

} catch (PDOException $e) {
    die("Erro ao consultar matrículas: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestão de Matrículas - Sistema Escolar</title>
    <!-- Ligação correta à folha de estilos CSS -->
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>

    <h2>Matrículas Registradas</h2>

    <!-- Menu de Ações Rápidas com o link geral do boletim -->
    <div class="menu-acoes">
        <a href="cadastrar.php" class="botao">+ Nova Matrícula</a> | 
        <a href="boletim.php" class="botao">📋 Ver Boletim</a> | 
        <a href="../index.php">Página Inicial</a>
    </div>

    <br>

    <!-- Tabela de Exibição dos Dados -->
    <table>
        <thead>
            <tr>
                <th>Aluno</th>
                <th>Disciplina</th>
                <th>Nota Inicial</th>
                <th>Média Final</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            <?php if (count($matriculas) > 0): ?>
                <?php foreach ($matriculas as $m): ?>
                    <tr>
                        <td><?= htmlspecialchars($m['nome_aluno']) ?></td>
                        <td><?= htmlspecialchars($m['nome_disciplina']) ?></td>
                        <td><?= number_format($m['nota'], 2, ',', '.') ?></td>
                        <td>
                            <?= isset($m['media']) && $m['media'] !== null 
                                ? number_format($m['media'], 2, ',', '.') 
                                : '<span style="color: #888;">-</span>' ?>
                        </td>
                        <td>
                            <!-- LINK DO BOLETIM ADICIONADO AQUI -->
                            <a href="boletim.php?aluno_id=<?= $m['aluno_id'] ?>">Boletim</a> | 
                            <a href="editar.php?aluno_id=<?= $m['aluno_id'] ?>&disciplina_id=<?= $m['disciplina_id'] ?>">Editar</a> | 
                            <a href="excluir.php?aluno_id=<?= $m['aluno_id'] ?>&disciplina_id=<?= $m['disciplina_id'] ?>" 
                               onclick="return confirm('Tem certeza que deseja remover esta matrícula?');">
                               Excluir
                            </a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr>
                    <td colspan="5" style="text-align: center;">Nenhuma matrícula cadastrada no sistema.</td>
                </tr>
            <?php endif; ?>
        </tbody>
    </table>

</body>
</html>