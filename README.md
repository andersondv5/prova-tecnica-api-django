# Sistema de Gestão Cursos e Disciplinas - API Django
API RESTful para gestão de instituições de ensino, cursos, disciplinas, professores, alunos e matrículas.


# Tecnologias
>Django 4.2 + Django REST Framework

>PostgreSQL

>Docker + Docker Compose

>DRF Spectacular (Documentação)


# Instalação Rápida

### Clone o repositório
git clone https://github.com/andersondv5/prova-tecnica-api-django.git
cd prova-tecnica-api-django

### Configure ambiente
cp .env.example .env
### Edite o .env se necessário

### Execute
docker-compose up --build -d

## Migrações
docker-compose exec web python manage.py migrate

### Superusuário (opcional)
docker-compose exec web python manage.py createsuperuser

# Acesso

>API: http://localhost:8000/api/

>Documentação: http://localhost:8000/api/docs/

>Admin: http://localhost:8000/admin/

>Frontend: http://localhost:8000/

# Endpoints da API


| Recurso       | Endpoint                  | Métodos HTTP          |
|---------------|---------------------------|-----------------------|
| Instituições  | `/api/institutions/`      | `GET`, `POST`, `PUT`, `DELETE` |
| Cursos        | `/api/courses/`           | `GET`, `POST`, `PUT`, `DELETE` |
| Disciplinas   | `/api/disciplines/`       | `GET`, `POST`, `PUT`, `DELETE` |
| Professores   | `/api/teachers/`          | `GET`, `POST`, `PUT`, `DELETE` |
| Alunos        | `/api/students/`          | `GET`, `POST`, `PUT`, `DELETE` |
| Matrículas    | `/api/enrollments/`       | `GET`, `POST`, `PUT`, `DELETE` |

# Exemplo de Uso

### Listar instituições
>curl http://localhost:8000/api/institutions/

### Criar instituição
>curl -X POST http://localhost:8000/api/institutions/ \
  >-H "Content-Type: application/json" \
  >-d '{"name": "Universidade Teste", "code": "UNTEST"}'

#Comandos Úteis

### Ver logs
docker-compose logs web

### Parar serviços
docker-compose down

### Acessar container
docker-compose exec web bash

### Migrações
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate

## Estrutura do Projeto Backend

- **backend/**
  - **catalog/**: App principal do projeto
  - **backend/**: Configurações globais (settings, urls, etc.)
  - **requirements.txt**: Lista de dependências do Python
  - **Dockerfile**: Instruções para construir a imagem Docker da aplicação

# Desenvolvido por
Anderson - GitHub

