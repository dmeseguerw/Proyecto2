## Create docker image:
    # $ docker build --tag proyecto2:latest .

## Run tests:
    # $ docker run -p 80:80 proyecto2:latest


# Base image
FROM python:3


# Basic information
LABEL maintainers = "daniel.meseguer@ucr.ac.cr,esteban.valverde_h@ucr.ac.cr"
LABEL version="1.0"
LABEL description = "Proyect 2: Docker Image for Veterinary Web Application"

# Define working directory
WORKDIR /usr/src/vet_app

# Install django
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY Veterinary .
COPY README.md .

# Expose port 80
EXPOSE 8000

# Run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]

