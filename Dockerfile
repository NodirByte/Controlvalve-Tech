# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set environment variables to ensure Python runs in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# First copy only the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

# Now copy the rest of your application code
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application
CMD ["python", "website/manage.py", "runserver", "0.0.0.0:8000"]
