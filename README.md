# Projeto Ações


Projeto de estudo,

Tem como objetivo criar uma base de dados de métricas e informações sobre a Bolsa de Valores.
Assim foi empregado durante o projeto APIs e Scrappers para a coleta, PostgreSQL para o armazenamento das informações  e Dockers para a execução do projeto

1) SQLALCHEMY
	A bliblioteca relaciona objetos python com tabelas sql e ajuda na comunicação dos dois (ORM, Mapeamento Objeto-Relacional)
	Tudo isso é feito através da engine, na qual temos que referenciar a localização da mesma (meu caso localhost) e é através dela
	que acontece a comunicação com a DB, no caso de operações ORM, é necessário uma layer a mais (temos que criar uma sessão)
	
