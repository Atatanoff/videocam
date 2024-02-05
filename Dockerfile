FROM python:3
# Определяем переменные среды
# Чтобы python не создавал файлы .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Чтобы видеть выходные данные приложения в реальном времени
ENV PYTHONUNBUFFERED=1
# Устанавливаем рабочую директорию
WORKDIR /opt/videocam
# Копируем в рабочую директорию файл зависимостей
COPY . /opt/videocam

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y && mkdir -p --mode=777 /data/cam
# Обновляем pip, устанавливаем зависимости
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python3", "new2.py"]

