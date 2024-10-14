# fastapi-chat

Чат на FastAPI

## Стек
* `python 3.12`
* `FastAPI`
* `SQLAlchemy`
* `sqlite`
* `websocket`

### Работа с зависимостями
* Устанавливаем `pip-compile`
```bash
pip install pip-tools
```
* Добавляем новую зависимость в список `project.dependencies` в `pyproject.toml`
* Генерируем обновленный `requirements.txt`
```bash
pip-compile -o requirements.txt pyproject.toml
```
* Устанавливаем зависимости
```bash
pip install -r requirements.txt
```


## Конфигурация:
* Переменные окружения берутся из файла `.environment`

## Запуск:
* Локально: `uvicorn app.main:app --reload`

## Документация:
* swagger: `{base_url}/docs`
* openapi (json): `{base_url}/openapi.json`

## Линтеры:

### pre-commit

1. Запустить скрипт:

   ```shell
   pre-commit run -a
   ```
