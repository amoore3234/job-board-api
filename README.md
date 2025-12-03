# Job Board API
An API that contains CRUD operations for interacting with job listings.

# Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequistes)
- [Installation](#installation)
  - [Python Virtual Environment](#python-virtual-environment)
- [Getting Started](#getting-started)
  - [Spinning Up The Job Board API Container](#spinning-up-the-job-board-api-container)
    - [Running The Application](#running-the-application)
    - [Running Queries Against The Prostgres Container](#running-queries-against-the-postgres-container)
  - [Running The Server Locally](#running-the-server-locally)
- [Making Requests Against The CRUD Endpoints](#making-requests-against-the-crud-endpoints)
- [Configuring Keycloak](#configuring-keycloak)
- [Testing](#testing)
- [Dev Links](#dev-links)

# Introduction
This project uses a web scraping mechanism to fetch job listings from external job board sites. The project is containerized using Docker and Docker Compose for easy deployment.

# Features
- **Job Board API:** An API built with with Python 3.14+.
- **Beautiful Soup:** A library for parsing HTML and XML documents. The application utilizes the library to extract data from websites.
- **Keycloak Inegration:** The application utilizes Keycloak's features for implementing client credentials for secured requests between clients.
- **Playwright:** A library used to perform web scraping functionality.

# Prerequistes
- [Python 3.14](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)
- **For Windows (WSL):**
  - [WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)
  - [Ubuntu](https://documentation.ubuntu.com/wsl/latest/howto/install-ubuntu-wsl2/)
    - **Note:** If there is an issue starting the docker engine, you may need to add the user to the docker group. you can run this command:
      - `sudo usermod -aG docker $USER`

# Installation
## Python Virtual Environment
  - **Linux/WSL**
    - Open your WSL terminal and navigate to your project's directory.
    - Install the python virtual environment (if it doesn't exist).
      - `apt install python3.12-venv`
    - Create the virtual environment
      - `python3 -m venv my_env`
    - Activate the virtural environment
      - `source my_env/bin/activate`
    - Since the virtual environment is now activated, install the required packages for your environment.
      - `pip3 install package_name` or `pip3 install -r requirements`
    - Deactivate the virtual environment when finished.
      - `deactivate`
  - **Windows(PowerShell):**
    - Open your Powershell terminal and navigate to your project's directory.
    - Install the python virtual environment (if it doesn't exist). Enter `python` in the terminal and a window should appear providing instructions to install python on your machine.
      - `python`
    - Create the virtual environment
      - `python -m venv my_env`
    - Activate the virtural environment
      - `.\my_env\Scripts\Activate.ps1`
    - Since the virtual environment is now activated, install the required packages for your environment.
      - `pip install package_name` or `pip install -r requirements`
    - Deactivate the virtual environment when finished.
      - `deactivate`
  - **Mac:**
    - Navigate to your project's directory.
    - Create the virtual environment. Change "my_env" to your desired environment name.
      - `python3 -m venv my_env`
    - Activate the virtual environment.
      - `source my_env/bin/activate`
    - Since the virtual environment is now activated, install the required packages for your environment.
      - `pip install package_name` or `pip install -r requirements`
    - Deactivate the environment when finished
      - `deactivate`

# Getting Started

## Spinning up the Job Board API Container
The `env_template` file contains default variables to store your datbase credentials and other sensitive data. Create a `.env` file in your project and copy the environment variables from the template and store them into the new config file. Ensure the file is referenced in `.gitignore`.
  - For the `POSTGRES_DATABASE_URL` environment variable, you may run into issues connecting to the database. If so, ensure that the host name in the url string points to the postgresql container. Ex: `postgresql+asyncpg://[user]:[password]@[container name]/[database]`
      - **Note:** Explicitly including the library name, `asyncpg` into the url allows the service to save job board data to the database asynchronously. Without it, an error would occur and data is not stored in the database.

### Running the Application
  - Start and build the application with the required docker command
    - `docker compose --env-file .env -f docker/docker-compose.yml up --build -d`

### Running Queries Against the Postgres Container
1. Once you spin up the application, if you need to run queries against the database, you can use the command below to access bash
    - `docker exec -it <container_name_or_id> /bin/bash`
2. Once you are able to interact with the container, you can run queries against the db. Run the command below to access the db by entering your postgres user name and datbase name.
    - `psql -U your_username -d your_database_name`

## Running the Server Locally
If you want to run the server locally to send API requests, you can use the command below and replace "main" with the name of your file that you want to run. In this application, the file we will want to run is app.py since the file contains the endpoints we want to retrieve data. Ex: app:app.
    - `uvicorn main:app --reload`

## Making Requests Against the CRUD endpoints
Once you start the container, you can navigate to [Swagger](#http://localhost:5000/docs#) to interact with the CRUD endpoints.

Here is a sample payload you can use to create a job posting.
```
{
  "job_title": "Frontend Software Engineer",
  "job_url": "https://example.com/jobs/1",
  "company_logo": "https://example.com/logo.png",
  "company_address": "13423 Newport Blvd, Newport Beach, USA",
  "company_salary": "$100,000",
  "company_metadata": [
    "Java",
    "JavaScript",
    "React"
  ],
  "date_posted": "2025-08-15"
}
```
# Configuring Keycloak
When running the Keycloak instance, additional configurations are required to setup Oauth credentials properly in Keycloak and send protected requests to the endpoints. You can follow the instructions in the [Keycloak wiki](https://github.com/amoore3234/Project-Wiki/blob/main/Guide/Keycloak.md#keycloak-setup) to configure the client credentials in Keycloak.

# Testing
Enter `pytest` in the terminal to run the unit and integration tests.

# Dev Links
- [Job Board FastAPI Docs](http://localhost:5000/docs#/)
- [Job Board API Keycloak Admin](http://localhost:8081/)

