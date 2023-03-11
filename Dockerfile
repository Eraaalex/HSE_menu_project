# Use the official Python image as the base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variables for the database connection
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=eralex
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=project_db

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]