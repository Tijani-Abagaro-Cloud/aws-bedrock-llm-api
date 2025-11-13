#Exposes a simple chat-style LLM API

#Expects JSON: { "prompt": "..." }

#Calls AWS Bedrock (Claude 3 by default)

#Returns { "prompt": "...", "response": "..." }

import json
import os
import boto3

# Use region + model from environment, with sensible defaults
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
MODEL_ID = os.environ.get("MODEL_ID", "anthropic.claude-3-haiku-20240307")

bedrock = boto3.client("bedrock-runtime", region_name=AWS_REGION)


def handler(event, context):
    """
    Lambda entrypoint for an LLM-powered API.

    Expected event (API Gateway HTTP API proxy):
    {
      "body": "{\"prompt\": \"Explain AWS Bedrock in simple terms\"}"
    }
    """

    try:
        body_str = event.get("body") or "{}"
        body = json.loads(body_str)
        user_prompt = body.get("prompt") or "Say hello from AWS Bedrock."

        # Build Claude-style message format
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 256,
            "temperature": 0.2,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_prompt}
                    ],
                }
            ],
        }

        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(payload),
        )

        response_body = json.loads(response["body"].read())
        # Claude 3 returns content as a list of blocks
        answer = response_body["content"][0]["text"]

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps(
                {
                    "model_id": MODEL_ID,
                    "prompt": user_prompt,
                    "response": answer,
                }
            ),
        }

    except Exception as e:
        # Simple error logging + safe client response
        print(f"Error invoking Bedrock: {e}")

        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(
                {
                    "error": "Failed to generate response",
                    "details": str(e),
                }
            ),
        }