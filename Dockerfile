# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary dependencies
RUN pip install -r requirements.txt

# Make port 5000 available for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "main.py"]
