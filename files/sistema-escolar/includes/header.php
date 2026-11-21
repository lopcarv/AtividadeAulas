<?php
// Garante que a sessão esteja ativa para exibir os dados do usuário
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Define o caminho base do projeto para recursos estáticos (CSS, Imagens)
$baseUrl = "/sistema-escolar";
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Escolar</title>
    <style>
        /* Estilização do Menu Superior e do Logotipo */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background-color: #f4f6f9;
        }
        .header-bg {
            background-color: #ffffff;
            border-bottom: 2px solid #e0e0e0;
            padding: 10px 20px;
        }
        .nav-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 1200px;
            margin: 0 auto;
        }
        .brand-logo {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: #2c3e50;
        }
        /* Ajuste do tamanho do logotipo */
        .brand-logo img {
            height: 40px; /* Altura ideal para barra de navegação */
            width: auto;
            object-fit: contain;
        }
        .brand-logo h1 {
            font-size: 20px;
            margin: 0;
            color: #3498db;
        }
        .nav-menu {
            display: flex;
            gap: 15px;
            list-style: none;
            margin: 0;
            padding: 0;
        }
        .nav-menu a {
            text-decoration: none;
            color: #333;
            font-weight: bold;
            padding: 6px 10px;
            border-radius: 4px;
        }
        .nav-menu a:hover {
            background-color: #3498db;
            color: white;
        }
        .user-info {
            font-size: 14px;
        }
        .main-container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
        }
    </style>
</head>
<body>

<header class="header-bg">
    <div class="nav-container">
        <!-- ÁREA DO LOGOTIPO E NOME DO SISTEMA -->
        <a href="<?= $baseUrl ?>/index.php" class="brand-logo">
            <img src="<?= $baseUrl ?>/assets/img/logo.png" alt="Logo Sistema Escolar">
            <h1>Sistema Escolar</h1>
        </a>

        <!-- MENU DE NAVEGAÇÃO -->
        <nav>
            <ul class="nav-menu">
                <li><a href="<?= $baseUrl ?>/dashboard.php">Dashboard</a></li>
                <li><a href="<?= $baseUrl ?>/alunos/index.php">Alunos</a></li>
                <li><a href="<?= $baseUrl ?>/disciplinas/index.php">Disciplinas</a></li>
                <li><a href="<?= $baseUrl ?>/matriculas/index.php">Matrículas</a></li>
            </ul>
        </nav>

        <!-- SESSÃO DO USUÁRIO -->
        <div class="user-info">
            Olá, <strong><?= htmlspecialchars($_SESSION['usuario_nome'] ?? 'admin') ?></strong> | 
            <a href="<?= $baseUrl ?>/logout.php" style="color: #e74c3c; text-decoration: none;">Sair</a>
        </div>
    </div>
</header>