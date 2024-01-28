# fastapi-password-generator
REST API using FastAPI that enables users to request new passwords based on specified criteria.


## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Run the FastAPI Server](#1-run-the-fastapi-server)
  - [Generate Password](#2-generate-password)
    - [Request](#request)
    - [Parameters](#parameters)
    - [Response](#response)
    - [Sending a POST Request](#sending-a-post-request)
  - [Running Test for Generate Password Endpoint](#3-running-test-for-generate-password-endpoint)
    - [How to Run the Tests](#how-to-run-the-tests)
  - [My Resume API](#4-my-resume-api)
    - [Access Details](#access-details)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/KartikeyaMalimath/fastapi-password-generator.git
    cd fastapi-password-generator
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Run the FastAPI Server

- Start the FastAPI server by running the following command in your terminal:

    ```bash
    uvicorn main:app --reload
    ```

### 2. Generate Password

#### Request
- **Endpoint** `/generate-password`
- **Method:** `POST`
- **Body:**

  ```json
  {
    "length": 12,
    "exclude_uppercase": false,
    "exclude_lowercase": false,
    "exclude_numbers": false,
    "exclude_special_characters": false,
    "exclude_characters": "'/;:",
    "custom_characters": "@_",
    "passphrase": "FIDO_Tech"
  }
  ```
  In this JSON input, all parameters are optional except for **length**, which is required.

#### Parameters

- **length** (`int`): The length of the password to generate.
- **exclude_uppercase** Optional(`bool`):  `true` to exclude uppercase characters in the password.
- **exclude_lowercase** Optional(`bool`): Pass `true` to exclude lowercase characters in the password.
- **exclude_numbers** Optional(`bool`): Pass `true` to exclude numbers in the password.
- **exclude_special_characters** Optional(`bool`): Pass `true` to exclude all special characters in the password.
- **exclude_characters** Optional(`str`): Pass characters to be excluded in the password.
- **custom_characters** Optional(`str`): Pass custom characters to include at least one custom character in the password.
- **passphrase** Optional(`str`): Pass a passphrase to be used as seed to generate the password.

#### Response

- **Body:**

    ```json
    {
        "password": "GeneratedPassword123"
    }
    ```

#### Sending a POST Request

Use a tool like curl or Postman to send a POST request to the `/generate-password` endpoint with the required parameters. Alternatively, you can use the provided Swagger UI on [http://localhost:8000/docs](http://localhost:8000/docs) to submit requests interactively.

- Example curl Command

    ```bash
    curl --header "Content-Type: application/json" --request POST --data "{"""length""": 12, """exclude_uppercase""": false, """exclude_lowercase""": false, """exclude_numbers""": false, """exclude_special_characters""": false, """exclude_characters""": """/;:""", """custom_characters""": """@_""", """passphrase""": """FIDO_Tech"""}" http://localhost:8000/generate-password    
  ```

### 3. Running Test for Generate Password Endpoint

#### How to Run the Tests
Ensure your FastAPI application is running.
Open a terminal and navigate to the directory containing your pytest file.

- Run the following command:
    ```bash
    pytest --verbose tests/
    ```
  
### 4. My Resume API

Explore my Resume through this API. Retrieve information about my education, skills, work experience, publications, and projects.

#### Access Details
- **Endpoint:** `/` 
- **Method**: `GET`
- Example Request:
    ```bash
    curl -X GET "http://localhost:8000/"  
    ```



