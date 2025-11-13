# aws-bedrock-llm-api

A serverless **LLM API** built on **AWS Bedrock**, **Lambda**, **API Gateway**, and **CDK (Python)**.

The goal of this project is to demonstrate a real-world **GenAI microservice** pattern on AWS that can be shared on GitHub, LinkedIn, and YouTube.

---

##  Architecture

```text
Client (Web / Postman / Curl)
        │
        ▼
API Gateway (HTTP API)
        │
        ▼
AWS Lambda (Python)
        │
        ▼
AWS Bedrock (Claude 3 / LLM)

📁 Project Structure
aws-bedrock-llm-api/
│
├── lambda/
│   └── handler.py          # Lambda code that calls AWS Bedrock
│
├── cdk/
│   ├── app.py              # CDK app entry
│   ├── llm_api_stack.py    # CDK stack (API Gateway + Lambda + IAM)
│   ├── requirements.txt    # CDK Python dependencies
│   └── cdk.json
│
├── .gitignore
└── README.md

## Deploy with CDK (Python)

From the cdk/ folder:

pip install -r requirements.txt

# One-time per account/region
cdk bootstrap aws://YOUR-AWS-ACCOUNT-ID/us-east-1

# Deploy the stack
cdk deploy


After deployment, CDK will print the HTTP API endpoint URL.

## Example Request
curl -X POST "https://your-api-id.execute-api.us-east-1.amazonaws.com/chat" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain AWS Bedrock in simple terms."}'

## What This Demonstrates

AWS CDK (Python) for Infrastructure as Code

Serverless architecture (API Gateway + Lambda)

Calling AWS Bedrock (Claude 3) from Lambda

Clean LLM microservice pattern