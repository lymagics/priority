# Installation instructions for development
To successfully install project locally follow this steps:
1. Create and fill in .env with examples from .env.example file.
2. Run docker-compose:
```
    docker-compose -f development.yml up -d
```
3. Apply database migrations:
```
    docker-compose -f development.yml exec web python manage.py migrate
```
4. Run tests to ensure everything works fine:
```
    docker-compose -f development.yml exec web python manage.py test
```