# Тестовое задание (Открытые Бизнес Технологии)

## Пример работы setup.py:


Сборка пакета
```python setup.py sdist --formats=gztar --dist-dir  ./```

Создание вирт. окружения:

```virtualenv venv```

```source venv/bin/activate```

Установка всех зависимостей:

```pip install -r requirements.txt```

Установка пакета: ```python setup.py install```

Запуск приложения:

```python venv/lib/python3.9/site-packages/m3_project-1.0.0-py3.9.egg/m3_project/manage.py makemigrations```

```python venv/lib/python3.9/site-packages/m3_project-1.0.0-py3.9.egg/m3_project/manage.py migrate```

```python venv/lib/python3.9/site-packages/m3_project-1.0.0-py3.9.egg/m3_project/manage.py runserver 0.0.0.0:8000```