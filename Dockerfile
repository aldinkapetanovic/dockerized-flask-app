# Use an official Python runtime as a parent image
FROM python:slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY app.py /app/

# Expose port 80
# EXPOSE 80

# Start Gunicorn
CMD gunicorn -b 0.0.0.0:8000 app:app
