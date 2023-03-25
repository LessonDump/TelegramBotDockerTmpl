# Простой шаблон Telegram-бота на основе docker-compose

## Требования:

- docker
- docker-compose

Бот пишет логи в директорию `logs` в корне проекта. Директория синхронизирована с контейнером.

---

Создать и запустить контейнер:

```bash
$ export BOT_TOKEN=<BOT_TOKEN>  # Токен бота
$ docker-compose up -d
```

Остановить запущенный контейнер:

```bash
$ docker-compose stop
```

Запустить остановленный контейнер:

```bash
$ docker-compose start
```

Остановить и удалить контейнер и сеть:

```bash
$ docker-compose down
```

Удалить образ:

```bash
$ docker rmi telegram_bot_docker_tmpl
```

Очистить логи:

```bash
$ rm -rf logs/*
```
