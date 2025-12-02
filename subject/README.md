# To-Do List API - Technical Exercise

## 📌 Context and Purpose

You are tasked with building a simple **To-Do List API** using Django and Django REST Framework. This API will power a dashboard feature allowing users to manage personal tasks across projects and categories.

> You are encouraged to take initiative and go beyond the minimum. Consider anything that would make the project more robust or easier to maintain.

The goal is to assess your understanding of:

- Django models and relationships
- Django REST Framework viewsets and seriailzers
- CRUD operations and data visualization
- RESTful API design and JSON structure
- Django coding conventions and project best practices

---

## 🚀 Setup Instructions

You can use any project layout you’re comfortable with.

Please include **basic instructions** in your `README` on how to run the API using the Django development server.

> Tip: providing a `docker-compose.yml` setup can make your project even easier to run.

---

## 🗃️ Models and Fields

### Tasks

Represents an individual to-do item, and must have the following fields:

- `id` primary key
- `title`
- `description`
- `status` (must be one of the following: `not_started`, `in_progress`, `done`)
- `due_date`
- `project`
- `categories`
- `created_at`
- `updated_at`

> A **task** can belong to multiple **categories**.
> Each **task** must belong to one **project**.

### Category

Represents a task category, and must have the following fields:

- `id` primary key
- `name`

> A **category** can have multiple **tasks**.

### Project

Represents a collection of related tasks.

- `id` primary key
- `title`
- `description`

> A **project** can have multiple **tasks**.

---

## 📦 API Endpoints

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| GET    | `/api/projects/`      | List all projects  |
| POST   | `/api/projects/`      | Create new project |
| GET    | `/api/projects/{id}/` | Retrieve a project |
| PUT    | `/api/projects/{id}/` | Update a project   |
| DELETE | `/api/projects/{id}/` | Delete a project   |

| Method | Endpoint           | Description     |
| ------ | ------------------ | --------------- |
| GET    | `/api/tasks/`      | List all tasks  |
| POST   | `/api/tasks/`      | Create a task   |
| GET    | `/api/tasks/{id}/` | Retrieve a task |
| PUT    | `/api/tasks/{id}/` | Update a task   |
| DELETE | `/api/tasks/{id}/` | Delete a task   |

| Method | Endpoint                | Description         |
| ------ | ----------------------- | ------------------- |
| GET    | `/api/categories/`      | List all categories |
| POST   | `/api/categories/`      | Create new category |
| GET    | `/api/categories/{id}/` | Retrieve a category |
| PUT    | `/api/categories/{id}/` | Update a category   |
| DELETE | `/api/categories/{id}/` | Delete a category   |

## 📥 Write JSON Examples

### Create Task

```json
{
  "title": "string",
  "description": "string",
  "status": "not_started",
  "due_date": "2025-05-19T10:29:26.928Z",
  "project_id": 0,
  "categories_ids": [0]
}
```

### Create Category

```json
{
  "name": "string"
}
```

### Create Project

```json
{
  "title": "string",
  "description": "string"
}
```

## 📤 Read JSON Examples

### Tasks (detailed)

```json
{
  "id": 0,
  "title": "string",
  "description": "string",
  "status": "not_started",
  "due_date": "2025-05-19T10:22:17.784Z",
  "project": {
    "title": "string",
    "description": "string"
  },
  "categories": ["string"],
  "created_at": "2025-05-19T10:22:17.784Z",
  "updated_at": "2025-05-19T10:22:17.784Z"
}
```

### Categories (detailed)

```json
{
  "id": 0,
  "name": "string"
}
```

### Projects (detailed)

```json
{
  "id": 0,
  "title": "string",
  "description": "string"
}
```

## ✨ Bonus (Optional)

These are **not required**, but a thoughtful implementation is appreciated:

- Filter tasks by `project`, `category`, or `status`.
- Add `completed_at` timestamp (auto-set when `status` is set to `done`).
- Include field `tasks_count` in the project read response.
