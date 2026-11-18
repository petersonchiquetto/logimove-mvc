CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    perfil VARCHAR(20) NOT NULL CHECK (perfil IN ('OPERADOR', 'GESTOR'))
);

CREATE TABLE veiculos (
    id_veiculo SERIAL PRIMARY KEY,
    placa VARCHAR(10) UNIQUE NOT NULL,
    modelo VARCHAR(80) NOT NULL,
    capacidade_kg NUMERIC(10, 2) NOT NULL CHECK (capacidade_kg > 0),
    status_operacional VARCHAR(20) NOT NULL DEFAULT 'DISPONIVEL'
        CHECK (status_operacional IN ('DISPONIVEL', 'EM_USO', 'MANUTENCAO'))
);

CREATE TABLE ordens_transporte (
    id_ordem SERIAL PRIMARY KEY,
    codigo_rastreio VARCHAR(30) UNIQUE NOT NULL,
    origem VARCHAR(100) NOT NULL,
    destino VARCHAR(100) NOT NULL,
    peso_carga_kg NUMERIC(10, 2) NOT NULL CHECK (peso_carga_kg > 0),
    status_ordem VARCHAR(20) NOT NULL DEFAULT 'PENDENTE'
        CHECK (status_ordem IN ('PENDENTE', 'EM_TRANSITO', 'CONCLUIDA', 'CANCELADA')),
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_veiculo INTEGER NOT NULL REFERENCES veiculos(id_veiculo) ON DELETE RESTRICT,
    id_usuario INTEGER NOT NULL REFERENCES usuarios(id_usuario) ON DELETE RESTRICT
);

INSERT INTO usuarios (nome, email, perfil) VALUES
('Operador Padrao', 'operador@logimove.com', 'OPERADOR'),
('Gestor Logistico', 'gestor@logimove.com', 'GESTOR');

INSERT INTO veiculos (placa, modelo, capacidade_kg, status_operacional) VALUES
('ABC1D23', 'VUC Mercedes-Benz Accelo', 3500.00, 'DISPONIVEL'),
('XYZ9K88', 'Fiorino Furgao', 650.00, 'DISPONIVEL');