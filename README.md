# 🚀 AWS Serverless Registration System

A serverless user registration application built using **Amazon S3, Amazon API Gateway, AWS Lambda, Amazon RDS for MySQL, AWS IAM, and Amazon CloudWatch**.

This project demonstrates a complete serverless registration workflow where users access a static registration website hosted on Amazon S3. Registration requests are sent through Amazon API Gateway to AWS Lambda, which processes the request and stores registration data in an Amazon RDS MySQL database.

---

## 📌 Project Overview

This project demonstrates how a web application can be built using a serverless architecture on AWS.

The frontend is hosted as a static website on **Amazon S3**.

When a user submits the registration form:

```text
User
  ↓
Amazon S3
  ↓
Amazon API Gateway
  ↓
AWS Lambda
  ↓
Amazon RDS MySQL
  ↓
regdb → users
🏗️ AWS Architecture

Architecture Flow
                   Internet User
                         │
                         ▼
                ┌──────────────────┐
                │    Amazon S3     │
                │  Static Website  │
                │    index.html    │
                └────────┬─────────┘
                         │
                    HTTPS / POST
                         │
                         ▼
                ┌──────────────────┐
                │  API Gateway     │
                │   HTTP API       │
                │ POST /register   │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   AWS Lambda     │
                │  Python Backend  │
                │     regUser      │
                └────────┬─────────┘
                         │
                   MySQL Connection
                         │
                         ▼
                ┌──────────────────┐
                │   Amazon RDS     │
                │      MySQL       │
                │      regdb       │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   users Table    │
                │------------------│
                │ id               │
                │ name             │
                │ email            │
                │ password         │
                └──────────────────┘
☁️ AWS Services Used
AWS Service	Purpose
Amazon S3	Hosts the static frontend website
Amazon API Gateway	Provides the HTTP API endpoint
AWS Lambda	Executes backend registration logic
Amazon RDS for MySQL	Stores registration data
AWS IAM	Provides Lambda execution permissions
Amazon CloudWatch	Provides Lambda monitoring and logs
🔄 Application Workflow
1. User opens the S3 hosted website
                ↓
2. Registration form is displayed
                ↓
3. User enters Name, Email and Password
                ↓
4. Frontend sends POST request
                ↓
5. API Gateway receives the request
                ↓
6. API Gateway invokes Lambda
                ↓
7. Lambda processes the request
                ↓
8. Lambda connects to RDS MySQL
                ↓
9. Data is inserted into users table
                ↓
10. Lambda returns success response
                ↓
11. User sees registration success
                ↓
12. Data is verified in MySQL
🗄️ Amazon RDS MySQL

Amazon RDS for MySQL is used as the persistent database layer.

Database Configuration
Database Engine : MySQL
Database Name   : regdb
Table           : users
Database Structure
regdb
 │
 └── users
      ├── id
      ├── name
      ├── email
      └── password
Users Table
Column	Data Type	Description
id	INT	Primary Key
name	VARCHAR(100)	User name
email	VARCHAR(100)	User email
password	VARCHAR(100)	User password
⚡ AWS Lambda

AWS Lambda is used as the backend service for processing registration requests.

Lambda Configuration
Function Name : regUser
Runtime       : Python
Architecture  : x86_64
Lambda Responsibilities
Receives requests from API Gateway
Handles CORS requests
Reads JSON request data
Connects to RDS MySQL
Inserts user registration data
Commits the database transaction
Returns a success or error response
Lambda Source Code
lambda/lambda_function.py
🔐 Lambda Environment Variables

Database connection details are configured using Lambda environment variables.

DB_HOST
DB_USER
DB_PASSWORD
DB_NAME

⚠️ Never commit database passwords, API keys, AWS credentials, or other secrets to GitHub.

🌐 Amazon API Gateway

Amazon API Gateway provides the HTTP endpoint used by the frontend.

API Configuration
API Type       : HTTP API
API Name       : regapi
Route          : POST /register
Integration    : AWS Lambda
Lambda         : regUser
Stage          : regstage
API Request Flow
Frontend
   │
   │ POST /register
   ▼
API Gateway
   │
   ▼
AWS Lambda
   │
   ▼
Amazon RDS MySQL
🌍 CORS Configuration

CORS is configured to allow the S3-hosted frontend to communicate with API Gateway.

Example:

Access-Control-Allow-Origin  : *
Access-Control-Allow-Headers : content-type
Access-Control-Allow-Methods : POST, OPTIONS

🔐 For production applications, replace * with the specific frontend origin.

🪣 Amazon S3 Static Website

Amazon S3 is used to host the static frontend.

Frontend Structure
frontend/
└── index.html

The frontend communicates with API Gateway using JavaScript.

🖥️ Registration Page

The application provides a simple registration interface.

Registration Fields
Name
Email
Password

Example request:

{
    "name": "John",
    "email": "john@example.com",
    "password": "example-password"
}
✅ Registration Success

After successful registration, Lambda returns a success response.

Example:

{
    "message": "User registered successfully"
}
🗃️ Database Verification

After registration, the data can be verified in the RDS MySQL database.

Run:

USE regdb;

SELECT * FROM users;

The newly registered user should appear in the users table.

🧪 Testing

The application was tested using the complete end-to-end workflow.

Test Flow
S3 Website
   ↓
Registration Form
   ↓
API Gateway
   ↓
AWS Lambda
   ↓
RDS MySQL
   ↓
users Table
Test Results
✅ S3 website loads successfully
✅ Registration form works
✅ API Gateway receives POST request
✅ Lambda processes the request
✅ Lambda connects to RDS MySQL
✅ User data is inserted into database
✅ Success response is returned
✅ Database data can be verified using SQL
🔒 Security

Basic AWS security practices:

Database credentials are configured through Lambda environment variables.
AWS credentials are not stored in source code.
Sensitive files should be excluded using .gitignore.
CORS is configured for frontend communication.
Lambda uses an IAM execution role.
RDS access should be controlled using Security Groups.
Private keys such as .pem files should never be uploaded to GitHub.
Production Recommendation

For production:

Passwords should be securely hashed.
AWS Secrets Manager should be considered for database credentials.
CORS should be restricted to trusted origins.
RDS should preferably remain private.
HTTPS should be used for application communication.
📦 Lambda Dependencies

requirements.txt:

mysql-connector-python

Install:

pip install mysql-connector-python -t .
🚀 Deployment Steps
Step 1 — Create RDS MySQL

Create an Amazon RDS MySQL instance.

Create/use:

regdb

Create the table:

USE regdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(100)
);
Step 2 — Create IAM Role

Create an IAM role for Lambda and attach the required Lambda permissions.

Example:

Role Name: reg-role
Step 3 — Prepare Lambda Package

Install the MySQL connector:

pip install mysql-connector-python -t .

Package the Lambda code and dependencies into a ZIP file.

Step 4 — Create Lambda Function
Function Name : regUser
Runtime       : Python
Architecture  : x86_64

Upload the Lambda deployment package.

Step 5 — Configure Environment Variables
DB_HOST
DB_USER
DB_PASSWORD
DB_NAME
Step 6 — Create API Gateway

Create an HTTP API:

API Name: regapi

Create route:

POST /register

Connect it to:

AWS Lambda → regUser

Create stage:

regstage

Configure CORS.

Step 7 — Configure Frontend

Update the API Gateway endpoint in:

frontend/index.html

Example:

const API_URL =
"https://YOUR_API_ID.execute-api.ap-south-1.amazonaws.com/regstage/register";
Step 8 — Create S3 Static Website

Create an S3 bucket and upload:

index.html

Enable static website hosting.

Step 9 — Test Application

Open the S3 website URL and enter:

Name
Email
Password

Click:

Register

Expected flow:

S3
 ↓
API Gateway
 ↓
Lambda
 ↓
RDS MySQL
Step 10 — Verify Database

Connect to RDS MySQL:

USE regdb;

SELECT * FROM users;
📁 Project Structure
AWS-Serverless-Registration-System/
│
├── frontend/
│   └── index.html
│
├── lambda/
│   ├── lambda_function.py
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
├── .gitignore
│
└── README.md
📸 Project Screenshots
1. AWS Architecture

2. Amazon RDS MySQL

3. AWS Lambda

4. Amazon API Gateway

5. Amazon S3 Static Website

6. Registration Page

7. Registration Success & Database Verification

🧰 Technologies Used
Frontend
HTML
CSS
JavaScript
Backend
Python
AWS Lambda
Database
Amazon RDS
MySQL
AWS Services
Amazon S3
Amazon API Gateway
AWS Lambda
Amazon RDS for MySQL
AWS IAM
Amazon CloudWatch
Version Control
Git
GitHub
🎯 Key Learning Outcomes
Building serverless applications on AWS
Hosting static websites using Amazon S3
Creating HTTP APIs using API Gateway
Developing backend logic using AWS Lambda
Connecting Lambda with Amazon RDS MySQL
Configuring IAM roles and permissions
Configuring CORS
Working with Lambda environment variables
Deploying Python dependencies to Lambda
Testing an end-to-end AWS application
Managing AWS projects using Git and GitHub
⭐ Project Highlights
Serverless Architecture
        +
Amazon S3
        +
API Gateway
        +
AWS Lambda
        +
Amazon RDS MySQL
        +
IAM
        +
CloudWatch
        =
Complete Serverless Registration System
👨‍💻 Author

Abhishek Saste

Cloud & DevOps Enthusiast

GitHub:

https://github.com/abhisheksaste31-source

📄 License

This project is created for educational and demonstration purposes.
