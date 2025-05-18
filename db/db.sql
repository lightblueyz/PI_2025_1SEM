use BD180225116;

create table sustentabilidade ( 
 id int primary key auto_increment,
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
 carona TINYINT(1)
 );


create table status (
 id_data int,
 sit_ener varchar(50),
 sit_agua varchar(50),
 sit_resid varchar(50),
 sit_tran varchar(50),
 sit_geral varchar(50)
);

create table media (
 id_media int primary key auto_increment,
 media_agua FLOAT,
 media_energia FLOAT, 
 media_residuos FLOAT 
)


select * from sustentabilidade;
select * from status;
select * from media;

ALTER TABLE status
ADD CONSTRAINT fk_id
FOREIGN KEY (id_data) REFERENCES sustentabilidade(id);