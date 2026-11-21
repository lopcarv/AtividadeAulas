<?php

require_once "../config/conexao.php";

$aluno_id = intval($_GET['aluno_id'] ?? 0);
$disciplina_id = intval($_GET['disciplina_id'] ?? 0);

$mensagem = "";

$sql = "
    SELECT
        m.*,
        a.nome AS aluno,
        d.nome AS disciplina
    FROM matriculas m
    INNER JOIN alunos a
        ON a.id = m.aluno_id
    INNER JOIN disciplinas d
        ON d.id = m.disciplina_id
    WHERE
        m.aluno_id = :aluno_id
    AND
        m.disciplina_id = :disciplina_id
";

$stmt = $pdo->prepare($sql);

$stmt->execute([
    ':aluno_id' => $aluno_id,
    ':disciplina_id' => $disciplina_id
]);

$matricula = $stmt->fetch();

if(!$matricula){
    die("Matrícula não encontrada.");
}

if($_SERVER["REQUEST_METHOD"] == "POST"){

    $nota = floatval($_POST["nota"]);
    $media = floatval($_POST["media"]);

    if($nota < 0 || $nota > 10){

        $mensagem = "A nota deve estar entre 0 e 10.";

    }else{

        $sql = "
            UPDATE matriculas
            SET
                nota = :nota,
                media = :media
            WHERE
                aluno_id = :aluno_id
            AND
                disciplina_id = :disciplina_id
        ";

        $stmt = $pdo->prepare($sql);

        $stmt->execute([
            ':nota' => $nota,
            ':media' => $media,
            ':aluno_id' => $aluno_id,
            ':disciplina_id' => $disciplina_id
        ]);

        header("Location: listar.php");
        exit;
    }
}

?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <title>Editar Matrícula</title>
</head>

<body>

<h2>Editar Matrícula</h2>

<?php if(!empty($mensagem)): ?>
    <p style="color:red;">
        <?= $mensagem ?>
    </p>
<?php endif; ?>

<form method="POST">

    <label>Aluno</label>

    <input
        type="text"
        value="<?= htmlspecialchars($matricula['aluno']) ?>"
        disabled
    >

    <br><br>

    <label>Disciplina</label>

    <input
        type="text"
        value="<?= htmlspecialchars($matricula['disciplina']) ?>"
        disabled
    >

    <br><br>

    <label>Nota</label>

    <input
        type="number"
        name="nota"
        min="0"
        max="10"
        step="0.01"
        value="<?= $matricula['nota'] ?>"
        required
    >

    <br><br>

    <label>Média</label>

    <input
        type="number"
        name="media"
        min="0"
        max="10"
        step="0.01"
        value="<?= $matricula['media'] ?>"
    >

    <br><br>

    <button type="submit">
        Atualizar
    </button>

    <a href="listar.php">
        Cancelar
    </a>

</form>

</body>
</html>