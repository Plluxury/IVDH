# Используем официальный образ Python 3.11.2
FROM python:3.11.2

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в контейнер в директорию /app
COPY requirements.txt /app/

# Устанавливаем зависимости, указанные в requirements.txt
RUN pip install -r requirements.txt

# Копируем остальной код приложения в контейнер в директорию /app
COPY . /app/