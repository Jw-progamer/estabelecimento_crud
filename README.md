# Crud Estabelecimentos
Prova de conceito de um backend Crud. Este projeto é um exercicio.

## Para preparar o sistema:

São necessários 2 arquivos .env

* um fica na raiz do projeto, no mesmo nível do docker-compose
* Outro fica dentro da pasta backend, em source, no mesmo nível do manager.py

Em envs vemos as amostras do que deve preencher ambos os arquivos. No .env da raiz, replicamos o conteudo dos samples, preenchndo as informações desejadas. Já ao que pertence ao backend, além das informações do sample, preenchemos os dados pertinentes as configurações do settings.py do projeto Django.

Exemplo do composer da raíz

```env
#Variaveis pgadmin
PGADMIN_DEFAULT_EMAIL=seu_email
PGADMIN_DEFAULT_PASSWORD=suasenha
#Variáveis postgresql
POSTGRES_PASSWORD=senha banco de dados
POSTGRES_USER=usuario --
POSTGRES_DB=nome -- 
```
Exemplo do .env do backend

```env
#Variaveis pgadmin
PGADMIN_DEFAULT_EMAIL=seu_email
PGADMIN_DEFAULT_PASSWORD=suasenha
#Variáveis postgresql
POSTGRES_PASSWORD=senha banco de dados
POSTGRES_USER=usuario --
POSTGRES_DB=nome -- 
#variaveis settings
DEBUG=true
SECRET_KEY=chave 
```

Os dois composes só serão necessários caso você queria usar o postgresql do composer. Caso já possua sua infraestrutura postgresql, basta preenche o .env do backend, para sua infraestrutura.

Caso não possua e deseje utilizar o do composer, você dever executar o comando "docker-compose up" para inicar o banco e um admim para gerencia-lo com mais facilidade

## Para preparar a aplicação backend

Depois de rodar o composer, em outro terminal ou aba, se for o caso, navege para /backend, lá execute alguns comandos:

* python manage.py para preparar as migratios, se for o caso

* python manage.py migrate para setar as tabelas no banco.

* python manage.py createsuperuser para criar um usuario . Util para depurar

* python manage.py runerver para rodar a aplicação de fato, na porta 8000. se colocar um numero permitido após runserver, este será a porta da aplicação

Com isso a aplicação backend estará funcionando.

## Para preparar o aplicação frontend

Depois de rodar o composer e o backend, em outro terminal ou aba, se for o caso, navege para /frontend, lá execute alguns comandos:

* npm install para instalar as bibliotecas necessárias

* npm run serve para inicar o front. O terminal erá exibir a url para poder acessar o site

### Desafio 2

O script do desafio 2 estar na raiz do projeto, chamado datilografia.py . Para executar, basta digitar:

```bash
python datilografia.py <numero de casos>
```