<?php
    <?php
ini_set('display_errors', 1);
error_reporting(E_ALL);


    
    require_once "../config/conexao.php";

    $sql = "SELECT * FROM alunos ORDER BY nome ASC";
    $stmt = $pdo->query($sql);
    $alunos = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Alunos</title>
</head>
<body>

    <h1>Lista de Alunos</h1>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Matrícula</th>
        </tr>

        <?php if (!empty($alunos)): ?>
            <?php foreach($alunos as $a): ?>
            <tr>
                <td><?= htmlspecialchars($a['id']); ?></td>
                <td><?= htmlspecialchars($a['nome']); ?></td>
                <td><?= htmlspecialchars($a['email']); ?></td>
                <td><?= htmlspecialchars($a['matricula']); ?></td>
            </tr>
            <?php endforeach; ?>
        <?php else: ?>
            <tr>
                <td colspan="4">Nenhum aluno cadastrado.</td>
            </tr>
        <?php endif; ?>
    </table>

</body>
</html>