# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY product_api.py .

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "product_api.py"]