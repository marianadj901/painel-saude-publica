CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    idade INT NOT NULL,
    faixa_etaria VARCHAR(20) NOT NULL
);

CREATE TABLE bairros (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE atendimentos (
    id SERIAL PRIMARY KEY,
    paciente_id INT REFERENCES pacientes(id),
    bairro_id INT REFERENCES bairros(id),
    diagnostico VARCHAR(100),
    data DATE
);