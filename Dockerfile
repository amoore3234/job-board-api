# Use an official Ubuntu base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /api

# Update package lists and install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install the virtual environment package
RUN apt-get update && apt-get install -y python3.12-venv

# Install Uvicorn
RUN apt install -y uvicorn

# Create virtual environment
RUN python3 -m venv /opt/.venv

# Activate virtual environment
ENV PATH="/opt/.venv/bin:$PATH"

# Copy the rest of your application code
COPY ./ /api

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port your application listens on
EXPOSE 5000 5432

# Define the command to run your application
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]