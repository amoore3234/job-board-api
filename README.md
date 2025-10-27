# Job Board API
A service that contains CRUD operations for interacting with job listings.

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)

# Introduction
This project uses a web scraping mechanism to fetch job listings from external job board sites. The project is containerized using Docker and Docker Compose for easy deployment.

# Features
- **Job Board API:** An API built with with Python 3.14+.
- **Beautiful Soup:** A library for parsing HTML and XML documents. The application utilizes the library to extract data from websites.
- **Keycloak Inegration:** The application utilizes Keycloak's features for implementing client credentials for secured requests between clients.

# Prerequistes
- [Python 3.14](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)
- **For Windows:**
  - [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
  - [Ubuntu](https://documentation.ubuntu.com/wsl/latest/howto/install-ubuntu-wsl2/)
    - **Note:** If there is an issue starting the docker engine, you may need to add the user to the docker group. you can run this command:
      - `sudo usermod -aG docker $USER`

# Installation
1. Python Virtual Environment
  - **Windows:**
    - Open your WSL terminal and navigate to your project's directory.
    - Install the python virtual environment (if it doesn't exist).
      - `apt install python3.12-venv`
    - Create the virtual environment
      - `python3 -m venv .venv`
    - Activate the virtural environment
      - `source .venv/bin/activate`
    - Deactivate the virtual environment when finished.
      - `deactivate`
  - **Mac:**
    - Navigate to your project's directory.
    - Create the virtual environment. Change "my_env" to your desired environment name.
      - `python3 -m venv my_env`
    - Activate the virtual environment.
      - `source my_env/bin/activate`
    - Since the virtual environment is now activated, install the required packages for your environment.
      - `pip install package_name`
    - Deactivate the environment when finished
      - `deactivate`

# Getting Started
1. Running the application
  - Start and build the application with the required docker command
    - `docker compose -f docker/docker-compose.yml up --build`
2. Running the server locally
  - If you want to run the server locally to send API requests, you can use the command below and replace "main" with the name of your file that you want to run.
    - `uvicorn main:app --reload`
3. Making queries against postgres container
  - Once you spin up the application, if you need to run queries against the database, you can use the command below to access bash
    - `docker exec -it <container_name_or_id> /bin/bash `

