<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Escolar EETEPA</title>
    <!-- Ligação ao CSS global -->
    <link rel="stylesheet" href="assets/css/style.css">
    
    <style>
        body {
            background-color: #f4f6f9;
            margin: 0;
            padding: 20px;
            font-family: Arial, Helvetica, sans-serif;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        /* Cabeçalho com Logótipo */
        .cabecalho {
            background-color: #0d6efd;
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            gap: 20px;
        }

        .logo-cabecalho {
            width: 60px;
            height: 60px;
            object-fit: contain;
            background: white;
            padding: 5px;
            border-radius: 6px;
        }

        .cabecalho-texto h1 {
            margin: 0;
            font-size: 26px;
            color: #ffffff;
        }

        .cabecalho-texto p {
            margin: 5px 0 0 0;
            opacity: 0.9;
        }

        /* Grade do Menu */
        .grid-menu {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        /* Cartões do Menu */
        .card-menu {
            background: white;
            padding: 25px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            align-items: center;
            border-top: 4px solid #0d6efd;
        }

        .card-menu:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }

        /* Contentor dos Ícones em Imagem */
        .card-icon-img {
            width: 64px;
            height: 64px;
            object-fit: contain;
            margin-bottom: 15px;
        }

        .card-titulo {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
        }

        .card-descricao {
            font-size: 13px;
            color: #666;
            margin-bottom: 20px;
        }

        .btn-card {
            display: inline-block;
            background-color: #0d6efd;
            color: white !important;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            width: 80%;
            transition: background 0.2s;
        }

        .btn-card:hover {
            background-color: #084298;
        }
    </style>
</head>
<body>

<div class="container">

    <!-- Cabeçalho Principal com Logo -->
    <div class="cabecalho">
        <img src="assets/img/logo.svg" alt="Logótipo Sistema Escolar" class="logo-cabecalho">
        <div class="cabecalho-texto">
            <h1>Sistema Escolar EETEPA</h1>
            <p>Painel de Gestão Académica</p>
        </div>
    </div>

    <h2>Menu Principal</h2>

    <!-- Grade de Opções do Menu -->
    <div class="grid-menu">

        <!-- Opção 1: Alunos -->
        <div class="card-menu">
            <img src="assets/img/alunos.svg" alt="Ícone Alunos" class="card-icon-img">
            <div class="card-titulo">Alunos</div>
            <div class="card-descricao">Cadastrar, editar, pesquisar e gerir registos de alunos.</div>
            <a href="alunos/listar.php" class="btn-card">Gerenciar</a>
        </div>

        <!-- Opção 2: Disciplinas -->
        <div class="card-menu">
            <img src="assets/img/disciplinas.svg" alt="Ícone Disciplinas" class="card-icon-img">
            <div class="card-titulo">Disciplinas</div>
            <div class="card-descricao">Gerir matérias e cargas horárias do sistema escolar.</div>
            <a href="disciplinas/listar.php" class="btn-card">Gerenciar</a>
        </div>

        <!-- Opção 3: Matrículas -->
        <div class="card-menu">
            <img src="assets/img/matriculas.svg" alt="Ícone Matrículas" class="card-icon-img">
            <div class="card-titulo">Matrículas</div>
            <div class="card-descricao">Vincular alunos às disciplinas e lançar notas acadêmicas.</div>
            <a href="matriculas/listar.php" class="btn-card">Gerenciar</a>
        </div>

        <!-- Opção 4: Boletim -->
        <div class="card-menu">
            <img src="assets/img/boletim.svg" alt="Ícone Boletim" class="card-icon-img">
            <div class="card-titulo">Boletim Escolar</div>
            <div class="card-descricao">Visualizar e imprimir o desempenho escolar dos alunos.</div>
            <a href="matriculas/boletim.php" class="btn-card">Visualizar</a>
        </div>

    </div>

</div>

</body>
</html>