-- Criação Tabelas

CREATE TABLE tb_cliente (
	idCliente     int PRIMARY KEY,
	nomeCliente   varchar(100),
	cidadeCliente varchar(40),
	estadoCliente varchar(40),
	paisCliente   varchar(40)
);

CREATE TABLE tb_combustivel (
	idCombustivel		int PRIMARY KEY,
	tipoCombustivel		varchar(20)
);

CREATE TABLE tb_carro (
	idCarro			int PRIMARY KEY,
	kmCarro			int,
	classiCarro		varchar(50),
	marcaCarro    	varchar(80),
	modeloCarro   	varchar(80),
	anoCarro		int,
	idCombustivel	int,
	FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
);

CREATE TABLE tb_vendedor (
	idVendedor int PRIMARY key,
	nomeVendedor varchar(15),
	sexoVendedor smallint,
	estadoVendedor varchar(40)
);

CREATE TABLE tb_locacao (
	idlocacao		int PRIMARY KEY,
	idVendedor		int,
	idCliente		int,
	idCarro			int,
	dataLocacao		datetime,
	horaLocacao		time,
	qtdDiaria		int,
	vlrDiaria		decimal(18,2),
	dataEntrega		date,
	horaEntrega		time,
	FOREIGN KEY (idCliente) REFERENCES tb_cliente(idCliente),
	FOREIGN key (idCarro) REFERENCES tb_carro(idCarro),
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
);

-- Consultas Tabelas

SELECT * FROM tb_carro car;

SELECT * from tb_cliente cli;

SELECT * from tb_combustivel com;

SELECT * from tb_locacao loc;

SELECT * from tb_vendedor ven;

-- Criação views

CREATE VIEW dim_locacao AS
SELECT loc.idlocacao as id_locacao,
    loc.idCliente as id_cliente,
    loc.idCarro as id_carro,
    loc.idVendedor as id_vendedor,
    car.idCombustivel AS id_combustivel,
    loc.qtdDiaria as quantidade_diaria,
    loc.vlrDiaria as valor_diaria,
    loc.dataLocacao as data_locacao,
    loc.horaEntrega as hora_entrega
FROM tb_locacao loc
JOIN tb_carro car ON loc.idCarro = car.idCarro;


CREATE VIEW dim_cliente AS
SELECT DISTINCT cli.idCliente as id_cliente,
	cli.nomeCliente as nome_cliente,
    cli.cidadeCliente as cidade_cliente,
    cli.estadoCliente as estado_cliente,
    cli.paisCliente as pais_cliente
FROM tb_cliente cli;

CREATE VIEW dim_vendedor AS
SELECT ven.idVendedor as id_vendedor,
	ven.nomeVendedor as nome_vendedor,
    ven.sexoVendedor as sexo_vendedor,
    ven.estadoVendedor as estado_vendedor
FROM tb_vendedor ven;

CREATE VIEW dim_carros AS
SELECT 
    car.idCarro as id_carro,
    car.kmCarro as km_carro,
    car.classiCarro as classi_carro,
    car.marcaCarro as marca_carro,
    car.modeloCarro as modelo_carro,
    car.anoCarro as ano_carro,
    car.idCombustivel AS id_combustivel
FROM tb_carro car;


CREATE VIEW dim_combustivel AS
SELECT DISTINCT
	com.idCombustivel AS id_combustivel,
	com.tipoCombustivel AS tipo_combustivel
FROM tb_combustivel com;

CREATE VIEW dim_data AS
SELECT DISTINCT
	loc.dataLocacao as data_locacao,
    strftime('%Y', loc.dataLocacao) as ano_locacao,
    strftime('%m', loc.dataLocacao) as mes_locacao,
    strftime('%W', loc.dataLocacao) as semana_locacao,
    strftime('%d', loc.dataLocacao) as dia_locacao
FROM tb_locacao loc;

-- Consultas views

SELECT * FROM dim_locacao loc;

SELECT * FROM dim_carros car;

SELECT * FROM dim_cliente cli;

SELECT * FROM dim_data data;

SELECT * FROM dim_vendedor ven;

