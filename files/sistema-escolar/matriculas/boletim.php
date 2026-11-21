<?php
session_start();
require_once "../config/conexao.php";

// Captura o ID do aluno enviado pela URL ou formulário (Padrão: Aluno 1)
$aluno_id = intval($_GET['aluno_id'] ?? 1); 

// 1. Busca os dados do Aluno
$sql_aluno = "SELECT id, nome, matricula, email FROM alunos WHERE id = :id LIMIT 1";
$stmt_aluno = $pdo->prepare($sql_aluno);
$stmt_aluno->execute([':id' => $aluno_id]);
$aluno = $stmt_aluno->fetch(PDO::FETCH_ASSOC);

// Busca a lista de todos os alunos para o menu de seleção
$todos_alunos = $pdo->query("SELECT id, nome FROM alunos WHERE ativo = 1 ORDER BY nome ASC")->fetchAll(PDO::FETCH_ASSOC);

// 2. Busca as disciplinas e notas do aluno selecionado
$sql_notas = "SELECT d.nome AS disciplina, d.carga_horaria, m.nota, m.media 
              FROM matriculas m 
              INNER JOIN disciplinas d ON m.disciplina_id = d.id 
              WHERE m.aluno_id = :aluno_id 
              ORDER BY d.nome ASC";

$stmt_notas = $pdo->prepare($sql_notas);
$stmt_notas->execute([':aluno_id' => $aluno_id]);
$boletim = $stmt_notas->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Boletim Escolar - <?= htmlspecialchars($aluno['nome'] ?? 'Aluno') ?></title>
    <link rel="stylesheet" href="../assets/css/style.css">
    
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f9; margin: 0; padding: 20px; }
        .boletim-container { max-width: 800px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .cabecalho-boletim { text-align: center; border-bottom: 2px solid #0d6efd; padding-bottom: 15px; margin-bottom: 20px; }
        .cabecalho-boletim h1 { margin: 5px 0; color: #0d6efd; }
        .dados-aluno { margin-bottom: 20px; font-size: 16px; background: #f8f9fa; padding: 15px; border-radius: 5px; }
        .tabela-boletim { width: 100%; border-collapse: collapse; margin-top: 10px; }
        .tabela-boletim th, .tabela-boletim td { border: 1px solid #ccc; padding: 10px; text-align: left; }
        .tabela-boletim th { background-color: #0d6efd; color: white; }
        .aprovado { color: green; font-weight: bold; }
        .recuperacao { color: red; font-weight: bold; }
        .acoes { margin-bottom: 20px; text-align: right; }

        /* Estilo exclusivo para Impressão */
        @media print {
            .no-print, nav, header, .acoes { display: none !important; }
            body { background: #fff; padding: 0; }
            .boletim-container { box-shadow: none; padding: 0; width: 100%; }
        }
    </style>
</head>
<body>

    <div class="boletim-container">
        
        <!-- Controles que não saem na impressão -->
        <div class="acoes no-print">
            <form method="GET" action="boletim.php" style="display: inline-block; float: left;">
                <label for="aluno_id">Selecionar Aluno:</label>
                <select name="aluno_id" id="aluno_id" onchange="this.form.submit()">
                    <?php foreach ($todos_alunos as $a): ?>
                        <option value="<?= $a['id'] ?>" <?= $a['id'] == $aluno_id ? 'selected' : '' ?>>
                            <?= htmlspecialchars($a['nome']) ?>
                        </option>
                    <?php endforeach; ?>
                </select>
            </form>

            <button onclick="window.print()">🖨️ Imprimir</button>
            <a href="index.php" style="margin-left: 10px;">Voltar</a>
        </div>

        <div style="clear: both;"></div>

        <!-- Cabeçalho Oficial do Boletim -->
        <div class="cabecalho-boletim">
            <h1>SISTEMA ESCOLAR EETEPA</h1>
            <p>Boletim de Desempenho Acadêmico</p>
        </div>

        <!-- Informações do Aluno -->
        <?php if ($aluno): ?>
            <div class="dados-aluno">
                <strong>Nome do Aluno:</strong> <?= htmlspecialchars($aluno['nome']) ?><br>
                <strong>Matrícula:</strong> <?= htmlspecialchars($aluno['matricula']) ?> | 
                <strong>E-mail:</strong> <?= htmlspecialchars($aluno['email']) ?>
            </div>

            <!-- Tabela de Notas e Situação -->
            <table class="tabela-boletim">
                <thead>
                    <tr>
                        <th>Disciplina</th>
                        <th>Carga Horária</th>
                        <th>Nota / Média</th>
                        <th>Situação</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (count($boletim) > 0): ?>
                        <?php foreach ($boletim as $item): ?>
                            <?php 
                                $notaFinal = $item['media'] ?? $item['nota'] ?? 0;
                                $situacao = ($notaFinal >= 7.0) ? "Aprovado" : "Recuperação";
                                $classeSituacao = ($notaFinal >= 7.0) ? "aprovado" : "recuperacao";
                            ?>
                            <tr>
                                <td><?= htmlspecialchars($item['disciplina']) ?></td>
                                <td><?= htmlspecialchars($item['carga_horaria']) ?>h</td>
                                <td><?= number_format($notaFinal, 2, ',', '.') ?></td>
                                <td class="<?= $classeSituacao ?>"><?= $situacao ?></td>
                            </tr>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <tr>
                            <td colspan="4">Nenhuma disciplina ou nota registrada para este aluno.</td>
                        </tr>
                    <?php endif; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p class="erro">Aluno não encontrado.</p>
        <?php endif; ?>

    </div>

</body>
</html>