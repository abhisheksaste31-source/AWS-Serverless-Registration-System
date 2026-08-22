# AWS Serverless Registration System

## 📌 Project Overview

The **AWS Serverless Registration System** is a cloud-based web application that allows users to submit their registration details through a web interface. The application uses AWS serverless services to process, store, and manage registration data without requiring a traditional backend server.

The project demonstrates how AWS services can be integrated to build a scalable, highly available, and cost-effective serverless application.

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │      User        │
                    │   Web Browser    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Amazon S3     │
                    │ Static Website   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   API Gateway    │
                    │   REST API       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  AWS Lambda      │
                    │ Backend Logic    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Amazon         │
                    │   DynamoDB       │
                    │ Registration DB  │
                    └──────────────────┘
```

---

## ☁️ AWS Services Used

| AWS Service        | Purpose                            |
| ------------------ | ---------------------------------- |
| Amazon S3          | Hosts the static frontend          |
| Amazon API Gateway | Provides REST API endpoints        |
| AWS Lambda         | Executes backend application logic |
| Amazon DynamoDB    | Stores registration information    |
| AWS IAM            | Manages permissions and access     |
| Amazon CloudWatch  | Monitoring and Lambda logs         |

---

## ✨ Features

* User registration form
* Serverless backend
* REST API integration
* Registration data stored in DynamoDB
* Static frontend hosting using Amazon S3
* No EC2 server required
* Automatic Lambda scaling
* IAM-based access control
* CloudWatch logging and monitoring
* Highly scalable architecture
* Pay-per-use serverless model

---

## 📁 Project Structure

```text
AWS-Serverless-Registration-System/
│
├── README.md
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda/
│   └── registration-function.py
│
└── screenshots/
    ├── s3-bucket.png
    ├── api-gateway.png
    ├── lambda.png
    ├── dynamodb.png
    └── application.png
```

---

# 🚀 Deployment Steps

## 1. Create DynamoDB Table

Open the AWS Management Console and navigate to **Amazon DynamoDB**.

Create a table with:

```text
Table Name:
Registrations
```

Create the required partition key according to the Lambda application's configuration.

Example:

```text
Primary Key:
id
```

Use a suitable data type such as:

```text
String
```

---

## 2. Create Lambda Function

Go to:

```text
AWS Console
→ Lambda
→ Create function
```

Select:

```text
Author from scratch
```

Example configuration:

```text
Function name:
registration-function
```

Choose the appropriate runtime for the Lambda code.

The Lambda function receives registration data from API Gateway and stores it in DynamoDB.

---

## 3. Lambda Backend Logic

The Lambda function performs the following operations:

```text
Receive API Request
        ↓
Read Registration Data
        ↓
Validate Input
        ↓
Generate Registration ID
        ↓
Store Data in DynamoDB
        ↓
Return API Response
```

Example registration information:

```text
Name
Email
Mobile
```

---

## 4. Configure IAM Permissions

The Lambda execution role requires permission to access DynamoDB.

Required permission example:

```text
dynamodb:PutItem
dynamodb:GetItem
dynamodb:Scan
```

The permissions should be granted only to the resources required by the application.

---

## 5. Create API Gateway

Open:

```text
AWS Console
→ API Gateway
→ Create API
```

Create an API and configure a route such as:

```text
POST /register
```

Connect the route to:

```text
AWS Lambda
→ registration-function
```

---

## 6. Configure CORS

Enable CORS for the API so that the frontend hosted on Amazon S3 can communicate with API Gateway.

Example:

```text
Allowed Origins:
*

Allowed Methods:
POST
OPTIONS
```

For production environments, replace `*` with the actual website origin.

---

## 7. Deploy API

Create a deployment stage such as:

```text
prod
```

After deployment, API Gateway provides an invoke URL similar to:

```text
https://xxxxxxxxxx.execute-api.ap-south-1.amazonaws.com/prod
```

Use the correct API URL in the frontend JavaScript file.

---

# 🌐 Frontend Configuration

The frontend contains:

```text
index.html
style.css
script.js
```

The JavaScript sends registration data to API Gateway.

Example flow:

```text
HTML Form
    ↓
JavaScript
    ↓
API Gateway
    ↓
Lambda
    ↓
DynamoDB
```

Update the API endpoint in:

```text
script.js
```

Example:

```javascript
const API_URL = "YOUR_API_GATEWAY_URL";
```

Replace the placeholder with the deployed API Gateway URL.

---

# 🪣 Amazon S3 Static Website Hosting

Create an S3 bucket for the frontend.

Example:

```text
aws-serverless-registration-website
```

Upload:

```text
index.html
style.css
script.js
```

Configure the bucket for static website hosting if using the S3 website endpoint.

For a production deployment, CloudFront can be placed in front of S3 to provide HTTPS and improved global delivery.

---

# 🔄 Application Flow

```text
1. User opens website
          ↓
2. Website loads from Amazon S3
          ↓
3. User enters registration details
          ↓
4. JavaScript sends POST request
          ↓
5. API Gateway receives request
          ↓
6. API Gateway invokes Lambda
          ↓
7. Lambda validates the data
          ↓
8. Lambda stores registration in DynamoDB
          ↓
9. DynamoDB returns success
          ↓
10. Lambda sends response
          ↓
11. API Gateway returns response
          ↓
12. User sees registration success message
```

---

# 🔐 Security

The project uses AWS IAM to control access between AWS services.

Recommended security practices:

* Follow least-privilege IAM permissions
* Enable HTTPS for production
* Restrict API Gateway CORS origins
* Do not expose AWS access keys in frontend code
* Enable CloudWatch logging
* Validate user input in Lambda
* Use appropriate DynamoDB permissions

---

# 📊 Monitoring

AWS CloudWatch can be used to monitor Lambda execution.

Useful metrics include:

```text
Invocations
Errors
Duration
Throttles
Concurrent Executions
```

Lambda logs can be viewed through:

```text
AWS Lambda
→ Monitor
→ View CloudWatch logs
```

---

# 🧪 Testing

Test the complete application using the following flow:

```text
Open Website
      ↓
Enter Name
      ↓
Enter Email
      ↓
Enter Mobile
      ↓
Click Register
      ↓
Check Success Message
      ↓
Open DynamoDB
      ↓
Verify Registration Record
```

---

# 🛠️ Technologies Used

### Frontend

```text
HTML5
CSS3
JavaScript
```

### Backend

```text
AWS Lambda
API Gateway
```

### Database

```text
Amazon DynamoDB
```

### Cloud

```text
Amazon S3
AWS IAM
Amazon CloudWatch
```

---

# 💡 Key Learning Outcomes

Through this project, I learned:

* How to build serverless applications on AWS
* How Amazon S3 hosts static websites
* How API Gateway exposes REST APIs
* How Lambda executes backend logic
* How DynamoDB stores application data
* How IAM controls AWS resource access
* How CloudWatch monitors serverless applications
* How multiple AWS services communicate with each other
* How to design scalable cloud architectures

---

# 📸 Project Screenshots

Add your project screenshots inside the `screenshots` folder.

Recommended screenshots:

```text
screenshots/
│
├── s3-bucket.png
├── api-gateway.png
├── lambda-function.png
├── dynamodb-table.png
├── iam-role.png
├── cloudwatch.png
└── application.png
```

Then add them to this README using:

```markdown
## 📸 Screenshots

### Application

![Application](screenshots/application.png)

### Amazon S3

![S3](screenshots/s3-bucket.png)

### API Gateway

![API Gateway](screenshots/api-gateway.png)

### AWS Lambda

![Lambda](screenshots/lambda-function.png)

### DynamoDB

![DynamoDB](screenshots/dynamodb-table.png)

### CloudWatch

![CloudWatch](screenshots/cloudwatch.png)
```

---

# 🎯 Final Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  Amazon S3       │
                  │ Static Frontend  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  API Gateway    │
                  │   REST API      │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  AWS Lambda     │
                  │ Backend Logic   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Amazon DynamoDB │
                  │ Registration DB │
                  └─────────────────┘

          IAM → Access Control
          CloudWatch → Monitoring & Logs
```

---

# 👨‍💻 Project Author

**Abhishek Saste**

Cloud & DevOps Enthusiast

---

## ⭐ Conclusion

The **AWS Serverless Registration System** demonstrates a complete serverless application architecture using AWS managed services. By using S3, API Gateway, Lambda, and DynamoDB, the application can handle user registrations without managing traditional servers such as EC2.

This project provides practical experience with **AWS Serverless Architecture, API Integration, Database Management, IAM Security, and Cloud Monitoring**.
