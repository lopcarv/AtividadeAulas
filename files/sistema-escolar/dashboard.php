<?php
// 1. Garante a verificação de sessão e a conexão PDO com a base de dados
require_once __DIR__ . "/config/verifica_sessao.php";
require_once __DIR__ . "/config/conexao.php";

// 2. Inclui o cabeçalho padrão com o logotipo e menu
include_once __DIR__ . "/includes/header.php";

// Inicialização das variáveis de contagem
$totalAlunos = 0;
$totalDisciplinas = 0;
$totalMatriculas = 0;
$ultimosAlunos = [];
$dadosGrafico = [];

try {
    // Busca o total de alunos cadastrados
    $stmt = $pdo->query("SELECT COUNT(*) FROM alunos");
    $totalAlunos = $stmt->fetchColumn();

    // Busca o total de disciplinas
    $stmt = $pdo->query("SELECT COUNT(*) FROM disciplinas");
    $totalDisciplinas = $stmt->fetchColumn();

    // Busca o total de matrículas
    $stmt = $pdo->query("SELECT COUNT(*) FROM matriculas");
    $totalMatriculas = $stmt->fetchColumn();

    // Busca os últimos 5 alunos cadastrados
    $stmt = $pdo->query("SELECT id, nome, email, criado_em FROM alunos ORDER BY id DESC LIMIT 5");
    $ultimosAlunos = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // Busca o total de alunos por disciplina para o gráfico
    $sqlGrafico = "SELECT d.nome AS disciplina, COUNT(m.aluno_id) AS total_alunos 
                   FROM disciplinas d 
                   LEFT JOIN matriculas m ON d.id = m.disciplina_id 
                   GROUP BY d.id";
    $stmtGrafico = $pdo->query($sqlGrafico);
    $dadosGrafico = $stmtGrafico->fetchAll(PDO::FETCH_ASSOC);

} catch (PDOException $e) {
    $erro = "Erro ao carregar dados do Dashboard: " . $e->getMessage();
}

// Prepara os dados para o gráfico em JavaScript
$labelsDisciplinas = array_column($dadosGrafico, 'disciplina');
$qtdMatriculas = array_column($dadosGrafico, 'total_alunos');
?>

<!-- Importação da biblioteca de gráficos Chart.js -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
    /* Estilos exclusivos do Dashboard */
    .dashboard-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
    }
    .card {
        background: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border-left: 5px solid #3498db;
    }
    .card.green { border-left-color: #2ecc71; }
    .card.orange { border-left-color: #f39c12; }
    .card h3 {
        margin: 0 0 10px 0;
        font-size: 14px;
        color: #7f8c8d;
        text-transform: uppercase;
    }
    .card .number {
        font-size: 28px;
        font-weight: bold;
        color: #2c3e50;
    }
    .dashboard-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
    }
    @media (max-width: 768px) {
        .dashboard-grid { grid-template-columns: 1fr; }
    }
    .panel {
        background: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
</style>

<main class="main-container">
    <h2>Dashboard Geral</h2>
    <p style="color: #7f8c8d; margin-bottom: 25px;">Bem-vindo ao painel de controlo do seu sistema escolar.</p>

    <!-- 1. BLOCO DE CARDS INDICADORES -->
    <div class="dashboard-cards">
        <div class="card">
            <h3>Total de Alunos</h3>
            <div class="number"><?= $totalAlunos ?></div>
        </div>
        <div class="card green">
            <h3>Disciplinas</h3>
            <div class="number"><?= $totalDisciplinas ?></div>
        </div>
        <div class="card orange">
            <h3>Matrículas Ativas</h3>
            <div class="number"><?= $totalMatriculas ?></div>
        </div>
    </div>

    <!-- 2. PAINEL DUPLO: GRÁFICO E ÚLTIMOS CADASTROS -->
    <div class="dashboard-grid">
        <!-- Gráfico de Alunos por Disciplina -->
        <div class="panel">
            <h3>Matrículas por Disciplina</h3>
            <canvas id="graficoMatriculas" height="200"></canvas>
        </div>

        <!-- Tabela de Últimos Alunos Cadastrados -->
        <div class="panel">
            <h3>Últimos Alunos Cadastrados</h3>
            <table border="0" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; margin-top: 10px;">
                <thead>
                    <tr style="border-bottom: 2px solid #ecf0f1; text-align: left; color: #7f8c8d;">
                        <th>Nome</th>
                        <th>E-mail</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (!empty($ultimosAlunos)): ?>
                        <?php foreach ($ultimosAlunos as $aluno): ?>
                            <tr style="border-bottom: 1px solid #ecf0f1;">
                                <td><strong><?= htmlspecialchars($aluno['nome']) ?></strong></td>
                                <td><?= htmlspecialchars($aluno['email']) ?></td>
                            </tr>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <tr><td colspan="2">Nenhum aluno recente.</td></tr>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</main>

<!-- 3. CONFIGURAÇÃO DO GRÁFICO JAVASCRIPT -->
<script>
    const ctx = document.getElementById('graficoMatriculas').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: <?= json_encode($labelsDisciplinas) ?>,
            datasets: [{
                label: 'Número de Alunos',
                data: <?= json_encode($qtdMatriculas) ?>,
                backgroundColor: '#3498db',
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: { beginAtZero: true, ticks: { stepSize: 1 } }
            }
        }
    });
</script>

</body>
</html>