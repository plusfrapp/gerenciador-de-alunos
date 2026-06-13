

CREATE TABLE IF NOT EXISTS alunos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nome      TEXT    NOT NULL,
    serie     INTEGER NOT NULL CHECK (serie IN (1, 2, 3)),
    turma     TEXT    NOT NULL CHECK (turma IN ('A', 'B')),
    p1        REAL    CHECK (p1 IS NULL OR (p1 >= 0.0 AND p1 <= 10.0)),
    p2        REAL    CHECK (p2 IS NULL OR (p2 >= 0.0 AND p2 <= 10.0)),
    situacao  TEXT    DEFAULT 'Cursando' CHECK (situacao IN ('Cursando', 'Aprovado', 'Reprovado'))
);

-- Índice para buscas por série/turma (operação mais frequente)
CREATE INDEX IF NOT EXISTS idx_alunos_serie_turma ON alunos (serie, turma);