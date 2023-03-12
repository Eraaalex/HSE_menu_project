FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=eralex
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=project_db

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]