# Use an official base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (optional)
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file(s)
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . .

COPY docker-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN chmod -R 777 /app

ENTRYPOINT ["/entrypoint.sh"]
