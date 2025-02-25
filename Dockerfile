# Use the official Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Install dependencies
COPY /recipes/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY recipes /app

# Expose the port the app will run on
EXPOSE 8000
