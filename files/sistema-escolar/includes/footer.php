<?php
// includes/footer.php
?>
<style>
    /* Estilos do Rodapé */
    .site-footer {
        background-color: #1e293b;
        color: #cbd5e1;
        padding: 20px 0;
        margin-top: 40px;
        font-family: Arial, sans-serif;
        font-size: 14px;
        border-top: 4px solid #0d6efd;
    }

    .footer-container {
        max-width: 1100px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px;
        flex-wrap: wrap;
        gap: 15px;
    }

    .footer-info p {
        margin: 3px 0;
    }

    .footer-links a {
        color: #93c5fd;
        text-decoration: none;
        margin-left: 15px;
        transition: color 0.2s;
    }

    .footer-links a:hover {
        color: #ffffff;
        text-decoration: underline;
    }

    /* Oculta o rodapé na impressão de relatórios/boletins */
    @media print {
        .site-footer {
            display: none !important;
        }
    }
</style>

<footer class="site-footer">
    <div class="footer-container">
        <!-- Informações Institucionais -->
        <div class="footer-info">
            <p><strong>Sistema Escolar EETEPA</strong></p>
            <p>&copy; <?= date('Y') ?> Todos os direitos reservados.</p>
        </div>

        <!-- Links de Acesso Rápido -->
        <div class="footer-links">
            <a href="../index.php">Dashboard</a>
            <a href="../alunos/index.php">Alunos</a>
            <a href="../disciplinas/index.php">Disciplinas</a>
            <a href="../matriculas/index.php">Matrículas</a>
            <a href="../logout.php" style="color: #fca5a5;">Sair</a>
        </div>
    </div>
</footer>