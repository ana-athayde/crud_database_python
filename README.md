# crud_database_python

CREATE TABLE materiais(
	idmate int not null auto_increment,
	reciclado boolean not null,
	cor varchar(50) not null,
	tipo varchar(50) not null,
	PRIMARY KEY (idmate)
);

CREATE TABLE cidades(
	idcida int not null auto_increment,
	nome varchar(50) not null,
	estado varchar(50) not null,
	tam int not null,
	PRIMARY KEY (idcida)
);

CREATE TABLE filiais (
	idfilial int not null auto_increment,
	nome varchar(50) not null,
	fone varchar(50) not null,
	rua varchar(50) not null,
	numero int not null,
	bairro varchar(50) not null,
	idcida int,
	idmate int,
	PRIMARY KEY (idfilial),
	FOREIGN KEY (idcida) REFERENCES cidades(idcida),
	FOREIGN KEY (idmate) REFERENCES materiais(idmate)
);

CREATE TABLE maquinas (
	idmaq int not null auto_increment,
	tpmaterial varchar(50) not null,
	anocompra date not null, 
	anoulrev date not null,
	nome varchar(50) not null,
	tipo varchar(50) not null,
	valor double not null,
	descricao varchar(50) not null,
	idfilial int,
	PRIMARY KEY (idmaq),
	FOREIGN KEY (idfilial) REFERENCES filiais(idfilial)
);


INSERT INTO materiais(reciclado, cor, tipo)
VALUES (1, 'azul', 'papel');

INSERT INTO materiais(reciclado, cor,  tipo)
VALUES (0, 'amarelo', 'metal');


INSERT INTO materiais(reciclado, cor, tipo)
VALUES (1, 'vermelho', 'plastico');

INSERT INTO materiais(reciclado, cor,  tipo)
VALUES (0, 'verde', 'vidro');

INSERT INTO materiais(reciclado, cor, tipo)
VALUES (1, 'marrom', 'isopor');


INSERT INTO cidades(nome, estado, tam)
VALUES ('Joinville', 'Santa_Catarina', 597658);

INSERT INTO cidades(nome, estado, tam)
VALUES ('Florianopolis', 'Santa_Catarina', 508826);

INSERT INTO cidades(nome, estado, tam)
VALUES ('Curitiba', 'Parana', 1948626);

INSERT INTO cidades(nome, estado, tam)
VALUES ('Blumenau', 'Santa_Catarina', 361855);

INSERT INTO cidades(nome, estado, tam)
VALUES ('Porto_Alegre', 'Rio_Grande_do_Sul', 1492530);


INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate)
VALUES ('Plasticlagem', '32457689', 'Rua_Bem-Te-Vi', 140, 'Paraiso', 5, 3);

INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate)
VALUES ('Metaclagem', '23546798', 'Rua_Beija-Flor', 237, 'Gaiola', 2, 2);

INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate)
VALUES ('Papeclagem', '66758942', 'Rua_dos_Pardais', 565, 'Colina', 3, 1);

INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate)
VALUES ('Recividro', '78432298', 'Rua_Andorinha', 720, 'Alameda', 4, 4);

INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate)
VALUES ('Recipor', '69732432', 'Rua_Tartaruguetes', 84, 'Malxitesque', 1, 5);


INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)
VALUES ('metal', '2017-03-14', '2019-08-30', 'metaleira', 'fixa', 500000.0, 'recicla metal', 2);

INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)
VALUES ('metal', '2017-03-16', '2019-09-29', 'metalia', 'não fixa', 70000.0, 'recicla metal', 2);

INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)
VALUES ('plastico', '2015-05-05', '2020-04-03', 'plastiqueira', 'fixa', 250000, 'recicla plastico', 1);

INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)
VALUES ('papel', '2019-11-08', '2022-06-29', 'papelona', 'fixa', 300000, 'recicla papel', 3);

INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)
VALUES ('vidro', '2013-02-14', '2018-04-17', 'vidrada', 'fixa', 480000, 'recicla vidro', 4);


INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)
VALUES ('isopor', '2017-09-27', '2021-12-12', 'isoponilda', 'fixa', 570000, 'recicla isopor', 5);





UPDATE materiais
SET cor = 'roxo'
WHERE idmate = 1;

UPDATE materiais
SET reciclado = 1
WHERE idmate = 2;

UPDATE materiais
SET reciclado = 0
WHERE cor = 'vermelho' and idmate = 3;

UPDATE materiais
SET cor = 'rosa'
WHERE tipo = 'isopor' and  idmate = 5;

UPDATE materiais
SET reciclado = 0
WHERE idmate = 5;

UPDATE cidades
SET tam = 598000
WHERE idcida = 1;

UPDATE cidades
SET tam = 509000
WHERE idcida = 2;

UPDATE cidades
SET tam = 1949000
WHERE idcida = 3;

UPDATE cidades
SET tam = 362000
WHERE idcida = 4;

UPDATE cidades
SET tam = 1493000
WHERE idcida = 5;

UPDATE filiais 
SET bairro = 'Bosque'
WHERE idfilial = 5;

UPDATE filiais 
SET numero = 450
WHERE idfilial = 2;

UPDATE filiais 
SET fone = '32165498'
WHERE idfilial = 3;

UPDATE filiais 
SET bairro = 'Tropical'
WHERE idfilial = 4;

UPDATE filiais 
SET rua = 'Rua_Quero-Quero'
WHERE idfilial = 5;

UPDATE maquinas 
SET valor = 525000
WHERE idmaq = 1;

UPDATE maquinas 
SET descricao = 'recicla diversos tipos de plastico'
WHERE idmaq = 2;

UPDATE maquinas 
SET tipo = 'modular'
WHERE idmaq = 5;

UPDATE maquinas 
SET anoulrev = '2022-03-18'
WHERE idmaq = 4;

UPDATE maquinas 
SET anoulrev = '2022-06-01'
WHERE idmaq = 1;

SELECT maquinas.nome 
FROM filiais
JOIN maquinas ON maquinas.idFilial = filiais.idFilial
WHERE filiais.idFilial = 2;

SELECT filiais.nome 
FROM filiais
JOIN maquinas ON maquinas.idFilial = filiais.idFilial
WHERE maquinas.valor = (SELECT max(valor) FROM maquinas);
