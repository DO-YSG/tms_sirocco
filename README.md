# SIROCCO
TMS, Digital CEO, AI agents

# STACK
# backend
python
FastAPI
PostgreSQL
SQLAlchemy
Pydantic
Uvicorn
# frontend
Next.js + TypeScript
shadcn/ui
TanStack Query
TanStack Table
Zustand№

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
# убрал файлы из индекса
git rm -r --cached .

fead — новая функциональность
fix — исправление ошибки
refactor — изменение кода без изменения функциональности
docs — изменения документации
chore — технические изменения