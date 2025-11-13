# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Set the working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_BREAK_SYSTEM_PACKAGES 1


# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .


EXPOSE 8000


# Run Uvicorn as the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]