create table Cursos(
IdCursos int not null identity (1,1)
,NomeCursos varchar (100) not null
,Semestres varchar (5)
,constraint pkCursos primary key (IdCursos)
)

create table Disciplinas(
IdDisciplinas int not null identity (1,1)
,NomeDisciplina varchar (100) not null
,CargaHoraria char (5) not null
,constraint pkDisciplinas primary key (IdDisciplinas)
)

create table DisciplinasdosCursos(
IdCursos int not null
,IdDisciplinas int not null
,constraint pkDisciplinasdosCursos primary key (IdCursos, IdDisciplinas)
)
