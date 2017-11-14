create database LMS_Impacta
use LMS_Impacta

create table cadastro_aluno(
id int not null
,nome varchar(200) not null
,endereço varchar(200) not null
,email varchar(100) not null
,sexo char(20) not null
,dt_nascimento date not null
,ra int not null
,telefone int not null
,curso varchar(50) not null
,senha int not null
,rep_senha int  not null
,CONSTRAINT pkcadastro_aluno primary key(id)
);

select * from cadastro_aluno