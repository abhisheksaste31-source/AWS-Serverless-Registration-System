\# 🚀 AWS Serverless Registration System



A serverless user registration application built using \*\*Amazon S3, Amazon API Gateway, AWS Lambda, Amazon RDS for MySQL, and AWS IAM\*\*.



This project demonstrates a complete serverless registration workflow where users access a static registration website hosted on Amazon S3. Registration requests are sent through Amazon API Gateway to AWS Lambda, which processes the request and stores the registration data in an Amazon RDS MySQL database.



\---



\## 📌 Project Overview



This project demonstrates how a web application can be built using a serverless architecture on AWS.



The frontend is hosted as a static website on Amazon S3. When a user submits the registration form, the request is sent to an HTTP API created using Amazon API Gateway.



API Gateway invokes the AWS Lambda function, which processes the registration request and connects to Amazon RDS for MySQL.



The user registration information is then stored persistently in the `users` table inside the `regdb` database.



\### Project Flow



```text

User

&#x20; ↓

Amazon S3

&#x20; ↓

Amazon API Gateway

&#x20; ↓

AWS Lambda

&#x20; ↓

Amazon RDS MySQL

&#x20; ↓

regdb → users

```



\---



\# 🏗️ AWS Architecture



!\[AWS Serverless Registration Architecture](screenshots/01-architecture-diagram.png)



\### Architecture Flow



```text

&#x20;                   Internet User

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │    Amazon S3     │

&#x20;               │  Static Website  │

&#x20;               │    index.html    │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                   HTTPS / POST

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │  API Gateway     │

&#x20;               │   HTTP API       │

&#x20;               │ POST /register   │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │   AWS Lambda     │

&#x20;               │  Python Backend  │

&#x20;               │     regUser      │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                  MySQL Connection

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │   Amazon RDS     │

&#x20;               │      MySQL       │

&#x20;               │      regdb       │

&#x20;               └────────┬─────────┘

&#x20;                        │

&#x20;                        ▼

&#x20;               ┌──────────────────┐

&#x20;               │   users Table    │

&#x20;               │ id               │

&#x20;               │ name             │

&#x20;               │ email            │

&#x20;               │ password         │

&#x20;               └──────────────────┘

```



\---



\# ☁️ AWS Services Used



| AWS Service              | Purpose                               |

| ------------------------ | ------------------------------------- |

| \*\*Amazon S3\*\*            | Hosts the static frontend website     |

| \*\*Amazon API Gateway\*\*   | Provides the HTTP API endpoint        |

| \*\*AWS Lambda\*\*           | Executes backend registration logic   |

| \*\*Amazon RDS for MySQL\*\* | Stores registration data              |

| \*\*AWS IAM\*\*              | Provides Lambda execution permissions |

| \*\*Amazon CloudWatch\*\*    | Provides Lambda monitoring and logs   |



\---



\# 🔄 Application Workflow



The complete registration workflow is:



```text

1\. User opens the S3 hosted website

&#x20;               ↓

2\. Registration form is displayed

&#x20;               ↓

3\. User enters Name, Email and Password

&#x20;               ↓

4\. Frontend sends POST request

&#x20;               ↓

5\. API Gateway receives the request

&#x20;               ↓

6\. API Gateway invokes Lambda

&#x20;               ↓

7\. Lambda processes the request

&#x20;               ↓

8\. Lambda connects to RDS MySQL

&#x20;               ↓

9\. Data is inserted into users table

&#x20;               ↓

10\. Lambda returns success response

&#x20;               ↓

11\. User sees registration success

&#x20;               ↓

12\. Data is verified in MySQL

```



\---



\# 🗄️ Amazon RDS MySQL



Amazon RDS for MySQL is used as the persistent database layer of the application.



!\[Amazon RDS MySQL](screenshots/02-rds-mysql.png)



\### Database Configuration



```text

Database Engine : MySQL

Database Name   : regdb

Table           : users

```



\### Database Structure



```text

regdb

&#x20;│

&#x20;└── users

&#x20;     ├── id

&#x20;     ├── name

&#x20;     ├── email

&#x20;     └── password

```



\### Users Table



| Column     | Data Type    | Description   |

| ---------- | ------------ | ------------- |

| `id`       | INT          | Primary Key   |

| `name`     | VARCHAR(100) | User name     |

| `email`    | VARCHAR(100) | User email    |

| `password` | VARCHAR(100) | User password |



\### SQL Schema



The database schema is available in:



```text

database/schema.sql

```



Example:



```sql

USE regdb;



CREATE TABLE users (

&#x20;   id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   name VARCHAR(100),

&#x20;   email VARCHAR(100),

&#x20;   password VARCHAR(100)

);

```



\---



\# ⚡ AWS Lambda



AWS Lambda is used as the backend service for processing registration requests.



!\[AWS Lambda Function](screenshots/03-lambda-function.png)



\### Lambda Configuration



```text

Function Name : regUser

Runtime       : Python

Architecture  : x86\_64

```



\### Lambda Responsibilities



The Lambda function:



\* Receives requests from API Gateway

\* Handles CORS requests

\* Reads JSON request data

\* Connects to RDS MySQL

\* Inserts user registration data

\* Commits the database transaction

\* Returns a success or error response



\### Lambda Source Code



```text

lambda/lambda\_function.py

```



\---



\# 🔐 Lambda Environment Variables



Database connection details are configured using Lambda environment variables.



```text

DB\_HOST

DB\_USER

DB\_PASSWORD

DB\_NAME

```



Example:



```text

DB\_HOST     = RDS Endpoint

DB\_USER     = admin

DB\_PASSWORD = \*\*\*\*\*\*\*\*

DB\_NAME     = regdb

```



> ⚠️ Database passwords and secret values should never be committed to GitHub.



\---



\# 🌐 Amazon API Gateway



Amazon API Gateway provides the HTTP endpoint used by the frontend.



!\[Amazon API Gateway](screenshots/04-api-gateway.png)



\### API Configuration



```text

API Type       : HTTP API

API Name       : regapi

Route          : POST /register

Integration    : AWS Lambda

Lambda         : regUser

Stage          : regstage

```



\### API Request Flow



```text

Frontend

&#x20;  │

&#x20;  │ POST /register

&#x20;  ▼

API Gateway

&#x20;  │

&#x20;  ▼

AWS Lambda

&#x20;  │

&#x20;  ▼

Amazon RDS MySQL

```



\---



\# 🌍 CORS Configuration



CORS is configured to allow the S3-hosted frontend to communicate with API Gateway.



Example configuration:



```text

Access-Control-Allow-Origin  : \*

Access-Control-Allow-Headers : content-type

Access-Control-Allow-Methods : POST, OPTIONS

```



This allows the browser-based frontend to send registration requests to the API.



\---



\# 🪣 Amazon S3 Static Website



Amazon S3 is used to host the static frontend of the application.



!\[Amazon S3 Static Website](screenshots/05-s3-static-website.png)



\### Frontend



```text

frontend/

└── index.html

```



The S3 bucket hosts the static registration page.



The frontend communicates with API Gateway using JavaScript.



Example:



```javascript

const API\_URL = "YOUR\_API\_GATEWAY\_URL";

```



The actual API Gateway endpoint is configured after creating the API.



\---



\# 🖥️ Registration Page



The application provides a simple registration interface.



!\[Registration Page](screenshots/06-registration-page.png)



\### Registration Fields



```text

Name

Email

Password

```



When the user clicks the \*\*Register\*\* button, JavaScript sends the data to the API Gateway endpoint.



Example request:



```json

{

&#x20;   "name": "John",

&#x20;   "email": "john@example.com",

&#x20;   "password": "example-password"

}

```



\---



\# ✅ Registration Success



After successful registration, Lambda returns a success response.



Example:



```json

{

&#x20;   "message": "User registered successfully"

}

```



The success response is displayed on the frontend.



\---



\# 🗃️ Database Verification



After registration, the data can be verified in the RDS MySQL database.



!\[Registration Success and Database Verification](screenshots/07-registration-success-database.png)



Run:



```sql

USE regdb;



SELECT \* FROM users;

```



The newly registered user should appear in the `users` table.



\---



\# 🧪 Testing



The application was tested using the complete end-to-end workflow.



\### Test Flow



```text

S3 Website

&#x20;   ↓

Registration Form

&#x20;   ↓

API Gateway

&#x20;   ↓

AWS Lambda

&#x20;   ↓

RDS MySQL

&#x20;   ↓

users Table

```



\### Test Results



\* ✅ S3 website loads successfully

\* ✅ Registration form works

\* ✅ API Gateway receives POST request

\* ✅ Lambda processes the request

\* ✅ Lambda connects to RDS MySQL

\* ✅ User data is inserted into database

\* ✅ Success response is returned

\* ✅ Database data can be verified using SQL



\---



\# 🔒 Security



The project follows basic AWS security practices.



\### Security Practices



\* Database credentials are stored in Lambda environment variables.

\* AWS credentials are not stored in source code.

\* Sensitive files are excluded using `.gitignore`.

\* CORS is configured for frontend communication.

\* Lambda uses an IAM execution role.

\* RDS access should be controlled using Security Groups.

\* Private keys such as `.pem` files should not be uploaded to GitHub.



\### Production Recommendation



For a production authentication system, passwords should be securely hashed instead of storing plain-text passwords.



\---



\# 📦 Lambda Dependencies



The Lambda function uses the MySQL Connector for Python.



`requirements.txt`:



```text

mysql-connector-python

```



The dependency is packaged with the Lambda deployment package before uploading the function.



\---



\# 🚀 Deployment Steps



\## Step 1 — Create RDS MySQL



Create an Amazon RDS MySQL instance.



Create/use the database:



```text

regdb

```



Create the table:



```sql

USE regdb;



CREATE TABLE users (

&#x20;   id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   name VARCHAR(100),

&#x20;   email VARCHAR(100),

&#x20;   password VARCHAR(100)

);

```



\---



\## Step 2 — Create IAM Role



Create an IAM role for Lambda.



Example:



```text

Role Name: reg-role

```



Attach the required Lambda permissions.



\---



\## Step 3 — Prepare Lambda Package



Install the MySQL connector:



```bash

pip install mysql-connector-python -t .

```



Package the Lambda code and dependencies into a ZIP file.



\---



\## Step 4 — Create Lambda Function



Create a Lambda function:



```text

Function Name : regUser

Runtime       : Python

Architecture  : x86\_64

```



Upload the Lambda deployment package.



\---



\## Step 5 — Configure Environment Variables



Configure:



```text

DB\_HOST

DB\_USER

DB\_PASSWORD

DB\_NAME

```



Example:



```text

DB\_HOST     = your-rds-endpoint

DB\_USER     = admin

DB\_PASSWORD = your-password

DB\_NAME     = regdb

```



\---



\## Step 6 — Create API Gateway



Create an HTTP API:



```text

API Name: regapi

```



Create the route:



```text

POST /register

```



Configure the Lambda integration:



```text

API Gateway

&#x20;     ↓

AWS Lambda

&#x20;     ↓

regUser

```



Create the stage:



```text

regstage

```



Configure CORS.



\---



\## Step 7 — Configure Frontend



Update the API Gateway endpoint in:



```text

frontend/index.html

```



Example:



```javascript

const API\_URL = "https://YOUR\_API\_ID.execute-api.ap-south-1.amazonaws.com/regstage/register";

```



\---



\## Step 8 — Create S3 Static Website



Create an S3 bucket.



Upload:



```text

index.html

```



Enable static website hosting.



The S3 website becomes the public frontend of the application.



\---



\## Step 9 — Test Application



Open the S3 website URL.



Enter:



```text

Name

Email

Password

```



Click:



```text

Register

```



The request should follow:



```text

S3

&#x20;↓

API Gateway

&#x20;↓

Lambda

&#x20;↓

RDS MySQL

```



\---



\## Step 10 — Verify Database



Connect to the RDS MySQL database and run:



```sql

USE regdb;



SELECT \* FROM users;

```



Verify that the registered user is present.



\---



\# 📁 Project Structure



```text

AWS-Serverless-Registration-System/

│

├── frontend/

│   └── index.html

│

├── lambda/

│   ├── lambda\_function.py

│   └── requirements.txt

│

├── database/

│   └── schema.sql

│

├── screenshots/

│   ├── 01-architecture-diagram.png

│   ├── 02-rds-mysql.png

│   ├── 03-lambda-function.png

│   ├── 04-api-gateway.png

│   ├── 05-s3-static-website.png

│   ├── 06-registration-page.png

│   └── 07-registration-success-database.png

│

├── README.md

└── .gitignore

```



\---



\# 🎯 Key Features



\* ✅ Serverless AWS architecture

\* ✅ Amazon S3 static website hosting

\* ✅ Amazon API Gateway HTTP API

\* ✅ AWS Lambda Python backend

\* ✅ Amazon RDS MySQL database

\* ✅ CORS configuration

\* ✅ IAM Lambda execution role

\* ✅ Environment-based database configuration

\* ✅ Persistent user registration

\* ✅ End-to-end AWS integration

\* ✅ GitHub-ready project structure



\---



\# 📚 Technologies Used



```text

Frontend        : HTML, CSS, JavaScript

Backend         : Python

API             : Amazon API Gateway

Compute         : AWS Lambda

Database        : Amazon RDS MySQL

Storage         : Amazon S3

Security        : AWS IAM

Monitoring      : Amazon CloudWatch

Version Control : Git \& GitHub

```



\---



\# 💡 Learning Outcomes



Through this project, I gained practical hands-on experience with:



\* AWS serverless architecture

\* Amazon S3

\* Static website hosting

\* Amazon API Gateway

\* HTTP APIs

\* AWS Lambda

\* Python Lambda functions

\* Amazon RDS for MySQL

\* MySQL database integration

\* IAM roles and permissions

\* CORS configuration

\* Environment variables

\* AWS cloud application deployment

\* Git and GitHub



\---



\# 📸 Project Screenshots



\## 🏗️ AWS Architecture



!\[AWS Architecture](screenshots/01-architecture-diagram.png)



\## 🗄️ Amazon RDS MySQL



!\[Amazon RDS](screenshots/02-rds-mysql.png)



\## ⚡ AWS Lambda



!\[AWS Lambda](screenshots/03-lambda-function.png)



\## 🌐 API Gateway



!\[API Gateway](screenshots/04-api-gateway.png)



\## 🪣 Amazon S3 Static Website



!\[Amazon S3](screenshots/05-s3-static-website.png)



\## 🖥️ Registration Page



!\[Registration Page](screenshots/06-registration-page.png)



\## ✅ Registration Success \& Database Verification



!\[Registration Success](screenshots/07-registration-success-database.png)



\---



\# 👨‍💻 Author



\*\*Abhishek Saste\*\*



Cloud \& DevOps Enthusiast



GitHub: \[abhisheksaste31-source](https://github.com/abhisheksaste31-source)



\---



\# ⭐ Project



If you find this project useful, consider giving this repository a ⭐ star.



