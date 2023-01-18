# 1. Project description
Main goal of the project - show my current development skills. The project includes all best practices I have learned so far.

# 2. Requirements structure
Technical requirements structure containes:
- Entities description:
    - User entity
    - Task entity
- Authentication
- Resources description:
    - Users resource:
        - create
        - read
        - update
    - Tasks resource:
        - create
        - read
        - update
        - delete
- Components required for testing
- Continuous integration
- Technology stack

# 3. Entities description
The section provides description of project entities. All entities should be added to admin panel.

## 3.1 User entity
The entity should provide the following fields:
- user_id - integer
- username - string - max length 64
- email - string
- password - string
- about_me - string
- avatar_url - str

User avatar should be provided through [Gravatar](https://en.gravatar.com/).

## 3.2 Task entity
The entity should provide the following fields:
- task_id - integer
- description - string
- is_done - boolean
- task priority - string 
- user_id - integer

Task priority should be one of ['High', 'Medium', 'Low']

# 4. Authentication 
The authentication flow shoud be privided with [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/).

# 5. Resources description
The section provides description of project resources.

## 5.1 Users resource
- Create
    - url: /users/
    - body: user entity data
    - response: new user entity
    - status code: 201
- Read
    - list:
        - url: /users/
        - response: list of user entity
        - status code: 200
    - one:
        - url: /users/{user_id}/
        - response: user entity
        - status code: 200
- Update
    - url: /users/{user_id}/
    - authentication is required
    - body: user entity data
    - response: updated user entity
    - status code: 200

## 5.2 Tasks resource
- Create 
    - url: /tasks/
    - authentication is required
    - body: task entity data
    - response: new task entity
    - status code: 201
- Read
    - list:
        - url: /tasks/
        - response: list of task entity
        - status code: 200
    - one:
        - url: /tasks/{task_id}/
        - response: task entity
        - status code: 200
- Update
    - url: /tasks/{task_id}/
    - authentication is required
    - body: task entity data
    - response: updated task entity
    - status code: 200
- Delete
    - url: /tasks/{task_id}/
    - authentication is required
    - response: updated task entity
    - status code: 200

## 6. Components required for testing
- REST API views.

## 7. Continuous integration
Continuous integration should be provided through [GitHub Actions](https://github.com/features/actions).

## 8. Technology stack
- Backend
    - language: Python
    - framework: Django and DRF(Django Rest Framework)
    - database: PostgreSQL
    - deployment method: Docker-compose