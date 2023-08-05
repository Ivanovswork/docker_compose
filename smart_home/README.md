Инструкция
-

Для запуска dj-приложения необходимо выполнить следущие команды поочердно

```base
cd drf/
```

```base
docker build . --tag=doc2
```

```base
docker run -d doc2
```

```base
cd smart_home/
```

```base
python manage.py migrate
```

```base
python manage.py runserver
```
