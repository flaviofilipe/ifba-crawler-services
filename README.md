# IFBA CRAWLER SERVICES
Serviços responsáveis por baixar as notícias do site https://portal.ifba.edu.br/conquista, salvar no banco de dados local e disponibilizar uma api REST com estas informações

## Serviços
- API: Serviço responsável por prover uma api REST em Flask para salvar e listar todas as notícias;
- Crawler: Serviço responsável por acessar o site do IFBA, pegar as notícias e enviar para a API;
-  Database: Configuração do banco de dados PostregreSQL com a criação das tabelas necessárias.

## Pré-requisitos
- Docker
- Docker Compose

## Execução
```
docker-compose up -d
```
Ao levantar todos os seerviços pela primeira vez será criado o banco de dados e o serviço de crawler irá inserir as notícias pela primeira vez.

Para executar somente o crawler:
```
docker-compose up --build -d ff-crawler
```

## API 
### [POST] Payload Example
**Route:** */*

```
[
	{

		"title": "notice 1",

		"link": "https://link.test",

		"date": "29/03/2022 14h51"
	},
	{

		"title": "notice 2",

		"link": "https://link.test",

		"date": "30/04/2022 10h30"
	}
]

```