
# User Management API

Esta é uma API RESTful desenvolvida em Python utilizando o framework FastAPI, com autenticação via AWS Cognito. A API gerencia usuários e seus acessos a um painel administrativo, fornecendo controle de acesso baseado em roles (admin e user) e possibilitando ativar/inativar usuários. A aplicação é implantada na AWS Lambda e exposta via API Gateway, e armazena os dados no banco de dados PostgreSQL.

## Estrutura

```bash
- app/
  - api/
    - __init__.py
    - admin.py  # Endpoints para admin
    - user.py   # Endpoints para usuário
    - auth.py   # Endpoints para autenticação
  - core/
    - __init__.py
    - config.py  # Configuração de banco de dados e AWS Cognito
    - security.py  # Lógica de autenticação e autorização
  - models/
    - __init__.py
    - user.py  # Model do usuário
  - db/
    - __init__.py
    - base.py  # Base para os modelos
    - session.py  # Sessão de banco de dados
  - main.py  # Inicialização do FastAPI
- Dockerfile
- requirements.txt
```

## Funcionalidades

### Administrador (Admin):
- **Criar, editar e remover usuários**.
- **Definir o status de um usuário (ativo/inativo)**.
- **Visualizar a lista de todos os usuários**.

### Usuário Comum (User):
- **Cadastrar-se, fazer login e editar seu próprio perfil**.
- **Visualizar e editar apenas suas próprias informações**.
- **Acesso é bloqueado quando marcado como inativo**.

## Endpoints

### Autenticação

- `POST /auth/login/`: Faz login de um usuário utilizando as credenciais do AWS Cognito.
- `POST /auth/logout/`: Faz o logout do usuário atual.

### Gerenciamento de Usuários (Admin)

- `GET /admin/users/`: Retorna a lista de todos os usuários.
- `POST /admin/users/`: Cria um novo usuário com nome, email, role e status.
- `PUT /admin/users/{user_id}/`: Atualiza as informações de um usuário.
- `DELETE /admin/users/{user_id}/`: Remove um usuário do sistema.

### Gerenciamento de Perfil (User)

- `GET /user/profile/`: Retorna as informações do perfil do próprio usuário.
- `PUT /user/profile/`: Atualiza as informações do próprio perfil.

## Requisitos

### Pré-requisitos

- Python 3.10+
- AWS Cognito (configurado para autenticação)
- PostgreSQL

### Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
boto3
pydantic
alembic
```

### Variáveis de Ambiente

Defina as seguintes variáveis no arquivo `.env`:

```
DATABASE_URL=postgresql://user:password@localhost:5432/db_name
AWS_COGNITO_POOL_ID=your_cognito_pool_id
AWS_COGNITO_CLIENT_ID=your_cognito_client_id
AWS_COGNITO_REGION=your_cognito_region
```

## Configuração

1. Clone o repositório:
   ```bash
   https://github.com/renan-meneses/user_management.git
   cd user_management
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados PostgreSQL e crie as tabelas:
   ```bash
   alembic upgrade head
   ```

5. Execute a aplicação localmente:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Acesse a documentação da API no Swagger:
   - Acesse `http://localhost:8000/docs` para visualizar e testar a API.

## Docker

Para rodar o projeto em um contêiner Docker, utilize o seguinte Dockerfile:

```bash
docker build -t fastapi-cognito-app .
docker run -d -p 8000:8000 fastapi-cognito-app
```

## Deploy na AWS Lambda

Este projeto pode ser implantado na AWS Lambda utilizando [Zappa](https://github.com/zappa/Zappa) ou [AWS Lambda + API Gateway](https://aws.amazon.com/api-gateway/).

1. Instale o Zappa:
   ```bash
   pip install zappa
   ```

2. Configure o Zappa:
   ```bash
   zappa init
   ```

3. Implante na AWS Lambda:
   ```bash
   zappa deploy dev
   ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou relatar issues.
