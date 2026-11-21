--
-- disciplinas
--

INSERT INTO disciplinas (nome, carga_horaria) VALUES
('Português',80),
('História',60),
('Física',80),
('Química',80),
('Biologia',80),
('Inglês',60),
('Informática',100),
('Educação Física',40),
('Projeto Integrador',120);

--
-- Gerar 100 alunos
--


DELIMITER $$

CREATE PROCEDURE gerar_alunos()
BEGIN

DECLARE contador INT DEFAULT 1;

WHILE contador <= 100 DO

INSERT INTO alunos (
    nome,
    matricula,
    email,
    data_nascimento,
    ativo
)
VALUES (
    CONCAT('Aluno ', contador),
    CONCAT('MAT', LPAD(contador,5,'0')),
    CONCAT('aluno',contador,'@escola.com'),
    DATE_SUB(
        CURDATE(),
        INTERVAL FLOOR(RAND()*7000) DAY
    ),
    1
);

SET contador = contador + 1;

END WHILE;

END$$

DELIMITER ;

CALL gerar_alunos();

DROP PROCEDURE gerar_alunos;

--
-- Gerar Popular matrículas
--

DELIMITER $$

CREATE PROCEDURE gerar_matriculas()
BEGIN

DECLARE aluno INT DEFAULT 1;
DECLARE disciplina INT;

WHILE aluno <= 100 DO

SET disciplina = 1;

WHILE disciplina <= 5 DO

INSERT IGNORE INTO matriculas(
    aluno_id,
    disciplina_id,
    nota,
    media
)
VALUES(
    aluno,
    FLOOR(1 + RAND()*11),
    ROUND(RAND()*10,2),
    NULL
);

SET disciplina = disciplina + 1;

END WHILE;

SET aluno = aluno + 1;

END WHILE;

END$$

DELIMITER ;

CALL gerar_matriculas();

DROP PROCEDURE gerar_matriculas;