#  AWS Lambda REST API with GitHub Actions and CloudFormation

This project demonstrates how to build, deploy, and automate a **serverless REST API** using **AWS Lambda**, **API Gateway**, and **CloudFormation**.

---

## Description

This project was created as part of a ca lab assignment to deepen my understanding of **Lambda and RestAPI** using **AWS CloudFormation**.  
The goal was to deploy a RESTful API integrated with AWS Lambda and ensure efficient ilities were included such as security.

---

##  Live API Endpoint

**Invoke URL:**  
[https://xbc3flxofi.execute-api.us-east-1.amazonaws.com/Dev/hello](https://xbc3flxofi.execute-api.us-east-1.amazonaws.com/Dev/hello)


**Expected Response:**
```json
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"message\": \"Hello, Abbie!\"}"
}

Deletion of API & Lambda on aws console to avoid charges. Screenshots provided in both the github folder and Word document.
The live api has been deleted to avoid any charges on aws, it can be created at anytime using the templates provided.



