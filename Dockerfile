FROM python:3.11.2-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ~/TelegramBotDockerTmpl

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY app ./app

CMD ["python", "-m", "app"]

# -------------------------------
# Build an image from a Dockerfile:
# $ docker build -t telegram_bot_docker_tmpl .
# -------------------------------
# Create and run a new container from an image:
# $ docker run -d --name TelegramBotDockerTmpl --env "TMPL_BOT_TOKEN=<TMPL_BOT_TOKEN>" telegram_bot_docker_tmpl
# -------------------------------
# Stop running container:
# $ docker stop TelegramBotDockerTmpl
# -------------------------------
# Start stopped container:
# $ docker start TelegramBotDockerTmpl
# -------------------------------
# Remove container:
# $ docker rm TelegramBotDockerTmpl
# -------------------------------
# Remove image:
# $ docker rmi telegram_bot_docker_tmpl
# -------------------------------
# Execute a command in a running container:
# $ docker exec -it TelegramBotDockerTmpl bash
