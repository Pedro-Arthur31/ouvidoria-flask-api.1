# Sistema de Ouvidoria API REST

## Sobre o Projeto

O Sistema de Ouvidoria API REST é uma aplicação backend desenvolvida para gerenciamento de manifestações, permitindo que usuários registrem reclamações e administradores acompanhem, analisem e respondam às solicitações.

O projeto foi desenvolvido utilizando Python e Flask, seguindo os princípios de uma API REST, com autenticação baseada em JWT, integração com banco de dados MySQL e documentação interativa através do Swagger.

A aplicação tem como objetivo aplicar conceitos utilizados no desenvolvimento de sistemas reais, como organização de código, segurança, persistência de dados, controle de acesso e disponibilização de serviços através de APIs.

---

# Objetivos do Projeto

O desenvolvimento desta aplicação teve como principais objetivos:

- Criar uma API REST completa utilizando Flask;
- Implementar operações CRUD;
- Integrar uma aplicação backend com banco de dados relacional;
- Aplicar autenticação e autorização utilizando JWT;
- Documentar os endpoints da API;
- Realizar deploy da aplicação em ambiente cloud.

---

# Tecnologias Utilizadas

## Backend

- Python
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Werkzeug Security
- PyMySQL

## Banco de Dados

- MySQL
- MySQL Workbench
- Aiven Cloud Database

## Documentação e Testes

- Swagger / Flasgger
- Postman

## Ferramentas

- PyCharm
- Git
- GitHub
- Render

---

# Arquitetura do Projeto

O projeto foi organizado seguindo uma estrutura modular, separando responsabilidades entre modelos, rotas, configurações e conexão com banco de dados.

```
ouvidoria-flask-api
│
├── app.py
│
├── models
│   ├── usuario.py
│   ├── reclamacao.py
│   └── resposta.py
│
├── routes
│   ├── usuario_routes.py
│   ├── reclamacao_routes.py
│   └── resposta_routes.py
│
├── database
│   └── db.py
│
├── config
│   └── config.py
│
├── requirements.txt
│
└── README.md
```

---

# Funcionalidades Implementadas

## Gerenciamento de Usuários

A API permite:

- Cadastro de usuários;
- Autenticação através de login;
- Consulta de usuários;
- Atualização de informações;
- Exclusão de usuários.

---

## Gerenciamento de Reclamações

Funcionalidades disponíveis:

- Cadastro de reclamações;
- Listagem de reclamações;
- Consulta individual;
- Atualização de status;
- Associação entre usuário e reclamação.

Status disponíveis:

```
Aberta
Em análise
Resolvida
```

---

## Gerenciamento de Respostas

Administradores podem:

- Responder reclamações;
- Registrar histórico de respostas;
- Associar respostas às reclamações existentes.

---

# Autenticação e Segurança

A aplicação utiliza JWT (JSON Web Token) para controle de acesso às rotas protegidas.

O fluxo de autenticação funciona da seguinte forma:

1. O usuário envia email e senha;
2. A API valida as credenciais;
3. O servidor gera um token JWT;
4. O token deve ser enviado nas próximas requisições autenticadas.

Exemplo:

```
Authorization: Bearer TOKEN
```

As senhas são armazenadas utilizando hash de segurança, evitando o armazenamento de informações sensíveis em texto puro.

---

# Modelo do Banco de Dados

## Usuários

Tabela:

```
usuarios
```

Principais campos:

- id
- nome
- email
- senha
- perfil
- data_criacao


Relacionamento:

```
Usuário possui várias reclamações.
```

---

## Reclamações

Tabela:

```
reclamacoes
```

Principais campos:

- id
- titulo
- descricao
- status
- usuario_id
- data_criacao


Relacionamento:

```
Usuário 1:N Reclamações
```

---

## Respostas

Tabela:

```
respostas
```

Principais campos:

- id
- mensagem
- administrador_id
- reclamacao_id
- data_resposta


Relacionamentos:

```
Administrador 1:N Respostas

Reclamação 1:N Respostas
```

---

# Documentação da API

A API possui documentação utilizando Swagger, permitindo visualizar e testar todos os endpoints disponíveis.

A documentação apresenta:

- Rotas disponíveis;
- Métodos HTTP utilizados;
- Estrutura das requisições;
- Respostas da API;
- Autenticação JWT.

Acesso:

```
/apidocs/
```

Exemplo:

```
https://seu-dominio.com/apidocs/
```

---

# Principais Endpoints

## Usuários

### Criar usuário

```
POST /usuarios
```

### Login

```
POST /login
```

### Listar usuários

```
GET /usuarios
```

### Buscar usuário por ID

```
GET /usuarios/{id}
```

### Atualizar usuário

```
PUT /usuarios/{id}
```

### Remover usuário

```
DELETE /usuarios/{id}
```

---

# Como Executar o Projeto

## Clonar o repositório

```bash
git clone https://github.com/seu-usuario/ouvidoria-flask-api.git
```

---

## Criar ambiente virtual

```bash
python -m venv venv
```

Ativar ambiente:

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

---

## Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configurar variáveis de ambiente

Criar um arquivo:

```
.env
```

Adicionar:

```env
DATABASE_URL=mysql+pymysql://usuario:senha@host:porta/database

JWT_SECRET_KEY=sua_chave_secreta
```

---

## Executar aplicação

```bash
python app.py
```

Aplicação disponível em:

```
http://localhost:5000
```

Swagger:

```
http://localhost:5000/apidocs/
```

---

# Deploy

A aplicação foi preparada para execução em ambiente cloud utilizando:

- Render para hospedagem da API;
- Aiven para hospedagem do banco MySQL.

Configuração de produção:

```
gunicorn app:app
```

---

# Evidências do Projeto

Adicionar imagens:

```
assets/
│
├── swagger.png
├── mysql.png
├── postman.png
└── arquitetura.png
```

Sugestões:

- Tela da documentação Swagger;
- Estrutura das tabelas no MySQL Workbench;
- Testes realizados no Postman;
- Arquitetura da aplicação.

---

# Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conhecimentos em:

- Desenvolvimento backend com Python;
- Criação de APIs REST;
- Framework Flask;
- ORM com SQLAlchemy;
- Banco de dados MySQL;
- Autenticação JWT;
- Segurança de senhas;
- Git e GitHub;
- Deploy em ambiente cloud;
- Documentação de APIs.

---

# Autor

Pedro Arthur da Silva Santos

Estudante de Sistemas de Informação

Desenvolvedor Full Stack Júnior

Tecnologias:

Python | Flask | Django | APIs REST | MySQL | Git

---

# Licença

Este projeto está disponível sob a licença MIT.