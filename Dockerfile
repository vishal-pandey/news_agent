FROM python:3.11

# Set working directory
WORKDIR /app

# Install system dependencies
# RUN apt get update && apt get install -y

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port that ADK server runs on
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["adk", "web", "--allow_origins", "*", "--port", "8080", "--host", "0.0.0.0"]
