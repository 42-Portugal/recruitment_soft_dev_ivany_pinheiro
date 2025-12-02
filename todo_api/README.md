## 🐳 **Como Rodar o Projeto (Docker compose)**

Pré-requisitos:

* Docker
* Docker Compose

### 🔧 **Subir o servidor**

```bash
docker compose up --build
```

>[!IMPORTANT]
> A API ficará disponível em: `http://localhost:8000/api/`

### ▶️ **Rodar migrações**

```bash
docker compose run todo migrate
```
> [!TIP]
> Pode ser criado um superusuário (opcional): `docker compose run todo createsuperuser`


## 🖥️ **Como Rodar o Projeto (sem Docker)**

Pré-requisitos:

* Python 3.13+
* Virtualenv

### Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Aplicar migrações

```bash
python manage.py migrate
```

### Rodar o servidor

```bash
python manage.py runserver
```

>[!IMPORTANT]
> A API ficará disponível em: `http://localhost:8000/api/`


<!-- 
## ERD (Entidade–Relacionamento)

```mermaid
erDiagram
    PROJECT ||--o{ TASK : has
    TASKCATEGORY }o--|| CATEGORY : has
    TASKCATEGORY }o--|| TASK : has

    PROJECT {
        uuid id PK
        string title
        string description
    }

    CATEGORY {
        uuid id PK
        string name
    }

    TASK {
        uuid id PK
        string title
        string description
        string status
        datetime due_date
        datetime created_at
        datetime updated_at
        datetime completed_at
        int project_id FK
    }

    TASKCATEGORY {
        uuid id_task PK, FK
        uuid id_category PK, FK
    }
```
 -->