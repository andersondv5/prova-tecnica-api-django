# Prova Técnica API Django

Repositório da prova técnica para a vaga de Desenvolvedor Júnior, contendo uma API RESTful para gerenciar recursos de uma instituição de ensino.

## 🚀 Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Backend:**
  - <a href="https://www.python.org/" target="_blank">Python</a>
  - <a href="https://www.djangoproject.com/" target="_blank">Django 4.2</a>
  - <a href="https://www.django-rest-framework.org/" target="_blank">Django REST Framework (DRF)</a>
- **Banco de dados:**
  - <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a>
- **Orquestração e virtualização:**
  - <a href="https://www.docker.com/" target="_blank">Docker</a>
  - <a href="https://docs.docker.com/compose/" target="_blank">Docker Compose</a>
- **Documentação da API:**
  - <a href="https://drf-spectacular.readthedocs.io/en/latest/" target="_blank">DRF Spectacular</a>

## 💻 Instalação e Execução

Siga os passos abaixo para configurar e rodar o projeto localmente:

### Pré-requisitos

- Docker e Docker Compose instalados na sua máquina.

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/andersondv5/prova-tecnica-api-django.git](https://github.com/andersondv5/prova-tecnica-api-django.git)
    cd prova-tecnica-api-django
    ```

2.  **Execute o Docker Compose:**
    ```bash
    docker-compose up -d --build
    ```

3.  **Realize as migrações do banco de dados:**
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

4.  **Crie um superusuário (opcional, para acessar o painel de administração):**
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```

## 🗺️ Endpoints e URLs

Após a execução, os seguintes URLs estarão disponíveis:

- **API:** [http://localhost:8000/api/](http://localhost:8000/api/)
- **Documentação da API:** <a href="http://localhost:8000/api/schema/docs/" target="_blank">http://localhost:8000/api/schema/docs/</a>
- **Painel de Administração:** [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 🔑 Endpoints da API

A API oferece os seguintes endpoints para gerenciamento dos recursos:

- `/institutions/`: Gerencia instituições (`GET`, `POST`, `PUT`, `DELETE`)
- `/courses/`: Gerencia cursos (`GET`, `POST`, `PUT`, `DELETE`)
- `/disciplines/`: Gerencia disciplinas (`GET`, `POST`, `PUT`, `DELETE`)
- `/professors/`: Gerencia professores (`GET`, `POST`, `PUT`, `DELETE`)
- `/students/`: Gerencia alunos (`GET`, `POST`, `PUT`, `DELETE`)
- `/enrollments/`: Gerencia matrículas (`GET`, `POST`, `PUT`, `DELETE`)

## 📝 Exemplo de Uso

Você pode testar a API usando ferramentas como `curl` ou Postman.

**Criar uma nova instituição:**
```bash
curl -X POST \
  http://localhost:8000/api/institutions/ \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Universidade de Exemplo",
    "city": "São Paulo"
  }'
```

# 📂 Estrutura do Projeto

O projeto segue a seguinte estrutura de diretórios:

* `backend/`: Contém o projeto principal Django.
* `catalog/`: Aplicação Django responsável pelos modelos e views da API.
* `requirements.txt`: Lista as dependências do projeto.
* `Dockerfile`: Instruções para criar a imagem Docker do backend.
* `docker-compose.yml`: Arquivo para orquestração de contêineres Docker (backend e banco de dados).

# 🤝 Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests para este projeto.
