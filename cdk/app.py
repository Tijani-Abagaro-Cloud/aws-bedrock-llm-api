#!/usr/bin/env python3
import aws_cdk as cdk
from llm_api_stack import LlmApiStack

app = cdk.App()
LlmApiStack(app, "LlmApiStack")
app.synth()
