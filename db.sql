use BD180225116;

create table sustentabilidade ( 
 id_data int primary key auto_increment,
 data_reg date,
 energia FLOAT,
 agua FLOAT,
 residuos_r FLOAT,
 residuos_nr FLOAT,
 transporte_p TINYINT(1),
 bicicleta TINYINT(1),
 caminhada TINYINT(1),
 carro_c TINYINT(1),
 carro_e TINYINT(1),
 carona TINYINT(1),
 sit_ener varchar(50),
 sit_agua varchar(50),
 sit_resid varchar(50),
 sit_tran varchar(50),
 sit_geral varchar(50));