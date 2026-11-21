-- 1. Criação da Base de Dados
CREATE DATABASE IF NOT EXISTS sistema_escolar
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE sistema_escolar;

-- 2. Tabela de Alunos
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL,
    data_nascimento DATE NOT NULL,
    ativo TINYINT(1) DEFAULT 1,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Tabela de Disciplinas
CREATE TABLE IF NOT EXISTS disciplinas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL
);

-- 4. Tabela de Usuários (para o Login e Autenticação)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL,
    perfil ENUM('admin', 'professor', 'secretaria') NOT NULL,
    ativo TINYINT(1) DEFAULT 1
);

-- 5. Tabela de Matrículas (Relacionamento N:N entre Alunos e Disciplinas)
CREATE TABLE IF NOT EXISTS matriculas (
    aluno_id INT NOT NULL,
    disciplina_id INT NOT NULL,
    nota DECIMAL(4,2),
    PRIMARY KEY (aluno_id, disciplina_id),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id) ON DELETE CASCADE,
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id) ON DELETE CASCADE
);

-- 6. Tabela de Auditoria
CREATE TABLE IF NOT EXISTS auditoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    acao VARCHAR(255) NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE SET NULL
);