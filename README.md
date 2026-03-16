## TMS SIROCCO

## STACK:
# backend
    - python
    - FastAPI
    - PostgreSQL
    - SQLAlchemy
    - Pydantic
    - Uvicorn
# frontend
    - Next.js
    - TypeScript

# uvicorn
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs

# alembic
alembic revision --autogenerate -m "описание изменения"
alembic upgrade head

alembic current
alembic history

# db
psql -U postgres -d tms_db          - вход в БД
SELECT id, name FROM companies;     - посмотреть id компании
DROP TABLE employees;               - удалить таблицу
\q                                  - выход

# git
git add .
git commit -m "fead: add Alembic and initial database migration"
git log --oneline

git rm -r --cached venv

feat — новая функциональность
fix — исправление ошибки
refactor — изменение кода без изменения функциональности
docs — изменения документации
chore — технические изменения

## BACKEND STRUCTURE
    - models (Описывают таблицы базы данных)
    - schemas (Проверяют и описывают выходные и выходные данные) create, update, read
    - routers (Принимает запросы извне)
    - servises (Сожержат бизнес-логику)
    - database db (Подключение к БД, сессии, base)
    - repositories (Прямые операции с БД)
    - core (Общие настройки проекта)

## MODELS
    company:
    vehicle:
    city:
    location:
    employee:
    driver:
    document:

                MODELS      SCHEMAS        routers
company             x
company_role        x
company_account     x
employee            x
driver              x
vehicle             x           x           x
city                x           x           x
location            x           x           x
document            x                      