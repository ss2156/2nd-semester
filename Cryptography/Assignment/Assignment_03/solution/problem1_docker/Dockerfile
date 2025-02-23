# Use an official Python base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy required files
COPY problem_1.py string.txt /app/

# Install required dependencies
RUN pip install pycryptodome

# Expose the port
EXPOSE 5000

# Run the server
CMD ["python", "problem_1.py"]
