# Use a slim Python image for a smaller footprint
FROM python:3.13-slim AS builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies required for building Python packages (e.g., PostgreSQL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Collect static files (ensure STATIC_ROOT is configured in settings)
RUN python manage.py collectstatic --noinput

# Create a non-root user and switch to it for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# Expose the port Gunicorn will listen on
EXPOSE 8000

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "-c", "gunicorn.conf.py", "config.wsgi:application"]