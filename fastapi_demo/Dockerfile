FROM python:3.10-slim


ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN pip install "poetry==1.7.1"

WORKDIR /app


# requirements.txt -> pip freeze 를 카피하는게 깔끔
COPY pyproject.toml poetry.lock* ./ 
RUN poetry install --no-root

COPY . .

# 7. FastAPI 앱 실행
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


