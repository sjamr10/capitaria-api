FROM python:3.8
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONPATH=/app
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt --no-cache-dir
COPY tests /app/tests
COPY app /app/app
