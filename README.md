# Job Board API
A service that contains CRUD operations for interacting with job listings.

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
- [Keycloak Setup](#keycloak-setup)
  - [Configuring Client Credentials in Keycloak](#configuring-client-credentials-in-keycloak)
  - [Hardcode Claims Within A Client](#hardcode-claims-within-a-client)
- [Testing](#testing)



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
The `env_template` file contains default variables to store your datbase credentials and other sensitive data. Create a `.env` file in your project and copy the environment variables from the template and store them into the new config file. Ensure the file is reference in `.gitignore`.
  - For the `POSTGRES_DATABASE_URL` environment variable, you may run into issues connecting to the database. If so, ensure that the host name in the url string points to the postgresql container. Ex: `postgresql://[user]:[password]@[container name]/[database]`

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
# Keycloak Setup
Once you start the application and navigate to the Swagger UI to test the APTI endpoints, there is a lock icon next to the endpoint you want to test. When you click on the icon, you are required to implement your client id and secret to sucessfully send a request. Otherwise, a "401 unauthorized" is returned from the service. Keycloak is configured to submit secured between requests, utilizing the authorization and OAuth2 strategy. You must configure client credentials in Keycloak to submit API request in Swagger UI.

## Configuring Client Credentials in Keycloak
Log into the Keycloak admin console with the admin credentials configured in your `env` file.

Once logged into the portal, you are navigated to the master realm by default. You will need to create a new realm, so you can use the credentials and generated tokens to make secured requests against the API.

### Creating a Client
  - Navigate to **Manage Realms** -> **Create Realm** and name the realm of your choosing.
  - Once the realm is created, click on the newly created realm in the list and navigate to the **Clients** tab.
  - Click on the **Create Client** button. This is where you can configure client credentials for your service.
  - Provide a **Client ID** for your client `(Ex: job-board-api-client)`. Add a name and description *(optional)*.
  - Within the capability config, toggle the **Client configuration** option to on. This will enable the Credentials tab in the Keycloak config and the authentication step in the Swagger UI to enter client credentials.
  - Within the login settings, add `http://localhost:5000/*` and `http://localhost:5000/docs/oauth2-redirect` in the **Valid indirect URIs** section and add `http://localhost:5000` in the **Web origin**.
  - Click save.
### Adding Client Credentials
  - Once you've successfully created a client for your application, you should be navigated to the to the settings. If not, navigate to **Clients** in the side bar and selected the client you just created. You should be able to see the Credentials tab where you can fetch the generated client secret.
    - **Note:** If you don't see the Credentials tab, you may forgot to toggle the **Client configuration** option to on. Scroll down to the **Capability config** section and check if the option is toggled on. Once enabled, you should see the Credentials tab displayed.
  - Copy the client secret and store it in your env file including your client id.
  - *(A more secure approach when sending requests through the browser)* Using client secrets acceptable when making secured API requests through Postman, Curl, or integrating with Azure Key Vault and HashiCorp Vault where secrets are abstracted away from plain site. Referencing the client secret when submitting requests from the Swagger UI may not be the best alternative since the secret is normally stored in the browser. To disable using a client secret within the auth flow, click on **Clients**, click on the client id associated with the application, and within the client details, scroll down and toggle the **Client configuration** option to off. This will allow you to authenticate without entering your client secret. You should be able to gain access to the endpoints by entering your client id and leaving the client secret field blank.
### Adding a User
  - We need to add a user in order to authenticate a request.
  - Navigate to the **Users** link in the side bar click the **Add User** button to a add a user.
  - Provide the user a username and click save.
  - Once you successfully create a user, navigate to the **Credentials** tab and set a password for the user. The credentials are used to authenticate a user before submitting a request.
  - If you would like to add a user with admin access, you can do so by assigning the user the admin role by navigating to **Role Mappings** -> **Realm Roles**. If the admin role is not displayed within the list of realm roles, go to **Realm roles** -> **Create role** to add the role. Name the role `admin` and provide a description. Create a user and assign the user the `admin` role. Confirm the role was assigned successfully to the user by logging into the user and submitting a request to one API endpoints that require admin access.
### Applying the your credentials in the Swagger UI
  - Navigate to [Swagger](#http://localhost:5000/docs#). Click the `Authorized` button and enter the client id and client secret you stored in the env file.
  - Once you successfully submit your client crendentials, you may be navigated to the Keycloak admin login page to enter user credentials for the first time.
  - Once you've successfully submit the user credentials created in the previous step, you should be able to hit one of API endpoints with no issues. 

## Hardcode Claims Within A Client
After authenticating and submitting a request, you may run into a `Invalid token: Invalid audience` being returned in the response. If you run into this error, go into the developer tools to grab the auth token *(Ex: **Inspect** -> **Network** -> name of the endpoint -> **Headers** -> copy the token under the Authorization header)*.

Navigate to [JWT Debugger](#https://www.jwt.io/) and paste your generated token into the text area to encode and validate the JWT. Head over to the right of the page under the "Decoded Payload" section and look for the `aud` field. You may notice that the field contained the `account` within the payload. This is the default value that is populated whenever a token is generated. We can modify claims in Keycloak to include claims that are associated with our client to address the error.
  - Log into the Keycloak admin console.
  - Go to **Client** and click on the name of your client.
  - Within the client details, navigate to the **Client Scopes** tab and click on the client scope that has "dedicated" appended to the name.
  - Within dedicated scopes, click **Add Mapper** -> **By Configuration**.
  - Scroll down and select **Hardcoded Claim**
  - Provide a name for the mapper.
  - Type in `aud` for the **Token Claim Name**.
  - Store the **Claim Value** the same as your client id.
  - Save your changes.

Submit another request using one of the API endpoints in Swagger and verify you can return a successful response. Follow the same steps earlier in the wiki for validating your JWT and confirm that the `aud` field contains the appropriate values. When you examine the decoded payload on the right of the page, the field should contain an array of claims including the claim value that was created in Keycloak.

# Testing
Enter `pytest` in the terminal to run the unit and integration tests.

