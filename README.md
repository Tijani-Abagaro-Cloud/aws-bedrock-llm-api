
# aws-bedrock-llm-api

A **serverless LLM API** built on **AWS Bedrock**, **Lambda**, and **API Gateway**.

This project demonstrates how to expose a **Bedrock-powered Large Language Model (LLM)** as a simple HTTPS API — a common pattern for real-world GenAI applications.

It is designed as a **portfolio / demo project** for:
- GitHub
- LinkedIn
- Technical interviews
- YouTube walkthroughs

---

##  High-Level Architecture

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


API Gateway exposes a public HTTPS endpoint

Lambda receives requests, validates input, calls Bedrock

Bedrock generates the LLM response (e.g., Claude 3 Haiku)

Response is returned as clean JSON

## Project Structure
aws-bedrock-llm-api/
│
├── lambda/
│   └── handler.py       # Lambda function calling AWS Bedrock
│
├── requirements.txt     # Python dependencies (for local use)
├── .gitignore
└── README.md

## Lambda: LLM API Contract

Request (JSON body):

{
  "prompt": "Explain AWS Bedrock in simple terms"
}


Response (JSON):

{
  "model_id": "anthropic.claude-3-haiku-20240307",
  "prompt": "Explain AWS Bedrock in simple terms",
  "response": "AWS Bedrock is a fully managed service that lets you..."
}

🛠️ Local Setup (for exploration)

Note: Real invocation of Bedrock requires:

AWS credentials with bedrock:InvokeModel

Bedrock enabled in your account/region

Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # Linux / macOS
# or
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


You can then import and test the handler locally using a sample event.

## Example API Call (once wired to API Gateway)
curl -X POST "https://your-api-id.execute-api.your-region.amazonaws.com/prod/chat" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Give me 3 ideas for an AWS Bedrock demo project."}'

## Why This Project Matters

This repo demonstrates:

Practical LLM integration using AWS Bedrock

Serverless pattern with AWS Lambda + API Gateway

Clean Python implementation of an LLM-backed microservice

Real-world GenAI architecture suitable for:

Solution Architect interviews

Senior/Principal Cloud roles

Freelance / consulting portfolios


👤 Author

Tijani A. Abagaro
Principal AWS Solutions Architect | Cloud & GenAI Architect

GitHub: Tijani-Abagaro-Cloud