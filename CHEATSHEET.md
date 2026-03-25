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

git status
git add .
git commit -m "fead: add Alembic and initial database migration"
    fead — новая функциональность
    fix — исправление ошибки
    refactor — изменение кода без изменения функциональности
    docs — изменения документации
    chore — технические изменения
git push

git branch
git checkout -b new-branch

git restore .
git reset --hard

git log --oneline
git diff