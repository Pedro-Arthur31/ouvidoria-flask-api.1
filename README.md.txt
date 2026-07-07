# Sistema de Ouvidoria API

API REST desenvolvida em **Python** utilizando **Flask**, **MySQL** e **JWT**, com arquitetura em camadas (Routes, Services e Validators).

O objetivo do projeto é simular um sistema de ouvidoria onde usuários podem registrar reclamações, acompanhar seu andamento e receber respostas de administradores.

---

## Tecnologias Utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- MySQL
- PyMySQL
- Werkzeug
- REST API
- JWT Authentication
- SQLAlchemy ORM

---

## Arquitetura do Projeto

```
ouvidoria/

├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── models/
│   ├── usuario.py
│   ├── reclamacao.py
│   └── resposta.py
│
├── routes/
│   ├── auth_routes.py
│   ├── usuario_routes.py
│   ├── reclamacao_routes.py
│   └── resposta_routes.py
│
├── services/
│   ├── usuario_service.py
│   ├── reclamacao_service.py
│   └── resposta_service.py
│
├── validators/
│   ├── usuario_validator.py
│   ├── reclamacao_validator.py
│   └── resposta_validator.py
│
├── utils/
│   ├── decorators.py
│   ├── security.py
│   └── status.py
│
└── README.md
```

---

# Funcionalidades

## Autenticação

- Login utilizando JWT
- Tokens com expiração
- Controle de permissões
- Perfil Administrador
- Perfil Usuário

---

## Usuários

- Criar usuário
- Listar usuários (Administrador)
- Buscar usuário
- Atualizar usuário
- Excluir usuário
- Visualizar próprio perfil

---

## Reclamações

- Criar reclamação
- Listar reclamações
- Buscar reclamação
- Atualizar reclamação
- Excluir reclamação
- Alterar status

Status disponíveis:

- aberta
- em_andamento
- respondida
- fechada

---

## Respostas

- Criar resposta
- Listar respostas
- Buscar resposta
- Atualizar resposta
- Excluir resposta

Quando uma resposta é cadastrada, o status da reclamação é atualizado automaticamente para **respondida**.

---

# Segurança

A aplicação utiliza autenticação JWT.

Permissões implementadas:

- Usuário visualiza apenas suas próprias reclamações.
- Usuário pode editar apenas suas próprias reclamações.
- Administrador pode visualizar todas as reclamações.
- Apenas administradores podem responder reclamações.
- Apenas administradores podem alterar o status das reclamações.
- Reclamações fechadas não podem ser editadas.

---

# Arquitetura Utilizada

O projeto segue uma arquitetura em camadas.

```
Cliente

↓

Routes

↓

Validators

↓

Services

↓

Models

↓

Banco de Dados MySQL
```

Cada camada possui uma responsabilidade específica.

### Routes

Responsáveis por receber as requisições HTTP e retornar as respostas da API.

### Validators

Realizam validações dos dados recebidos antes da regra de negócio.

### Services

Contêm toda a lógica de negócio da aplicação.

### Models

Representam as tabelas do banco de dados utilizando SQLAlchemy.

---

# Banco de Dados

Banco utilizado:

MySQL

Tabelas:

- usuarios
- reclamacoes
- respostas

Relacionamentos:

- Um usuário possui várias reclamações.
- Uma reclamação pertence a um usuário.
- Uma reclamação possui várias respostas.
- Um administrador pode responder várias reclamações.

---

# Como executar o projeto

## 1. Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/ouvidoria-flask-api.git
```

---

## 2. Entre na pasta

```bash
cd ouvidoria-flask-api
```

---

## 3. Crie um ambiente virtual

Windows

```bash
python -m venv .venv
```

Ativar

```bash
.venv\Scripts\activate
```

Linux

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Configure o banco de dados

Crie um banco chamado:

```
ouvidoria_db
```

Configure a conexão em:

```
config.py
```

---

## 6. Execute o projeto

```bash
python app.py
```

A aplicação ficará disponível em:

```
http://127.0.0.1:5000
```

---

# Principais Endpoints

## Autenticação

```
POST /login
```

---

## Usuários

```
POST /usuarios

GET /usuarios

GET /usuarios/{id}

PUT /usuarios/{id}

DELETE /usuarios/{id}

GET /me
```

---

## Reclamações

```
POST /reclamacoes

GET /reclamacoes

GET /reclamacoes/{id}

PUT /reclamacoes/{id}

DELETE /reclamacoes/{id}

PATCH /reclamacoes/{id}/status

GET /minhas-reclamacoes
```

---

## Respostas

```
POST /respostas

GET /reclamacoes/{id}/respostas

GET /respostas/{id}

PUT /respostas/{id}

DELETE /respostas/{id}
```

---

# Melhorias Futuras

- Flask-Migrate
- Swagger/OpenAPI
- Docker
- Testes automatizados com Pytest
- Deploy em nuvem (Render ou Railway)
- Front-end em React

---

# Desenvolvido por

**Pedro Arthur**

Estudante de Sistemas de Informação.

Desenvolvedor Back-end Python em formação.

Tecnologias estudadas:

- Python
- Flask
- SQLAlchemy
- MySQL
- APIs REST
- JWT
- Git
- GitHub

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos e de portfólio.