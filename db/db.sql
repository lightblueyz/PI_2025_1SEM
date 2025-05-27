use BD180225116;


-- Remove as tabelas, se existirem, na ordem correta (devido às chaves estrangeiras)
DROP TABLE IF EXISTS status;
DROP TABLE IF EXISTS sustentabilidade;
DROP TABLE IF EXISTS media;

-- Cria a tabela principal com os dados coletados
CREATE TABLE sustentabilidade ( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    data_reg DATE,
    energia FLOAT,
    agua FLOAT,
    residuos_r FLOAT,
    residuos_nr FLOAT,
    transporte_p TINYINT(1),
    bicicleta TINYINT(1),
    caminhada TINYINT(1),
    carro_c TINYINT(1),
    carro_e TINYINT(1),
    carona TINYINT(1)
);

-- Cria a tabela de status com chave estrangeira referenciando sustentabilidade.id
CREATE TABLE status (
    id_data INT,
    sit_ener VARCHAR(50),
    sit_agua VARCHAR(50),
    sit_resid VARCHAR(50),
    sit_tran VARCHAR(50),
    sit_geral VARCHAR(50),
    CONSTRAINT fk_id FOREIGN KEY (id_data) REFERENCES sustentabilidade(id)
);

-- Cria a tabela de médias
CREATE TABLE media (
    id_media INT PRIMARY KEY,
    media_agua FLOAT,
    media_energia FLOAT, 
    media_residuos FLOAT 
);

-- Insere o registro base para as médias
INSERT INTO media (id_media) VALUES (1);

-- Verifica se está tudo certo
SELECT * FROM sustentabilidade;
SELECT * FROM status;
SELECT * FROM media;