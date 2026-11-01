# API Keys: https://platform.openai.com/settings/organization/api-keys
# Billing: https://platform.openai.com/settings/organization/billing/overview

import json

from openai import OpenAI

openai_client = OpenAI(api_key="YOUR_API_KEY_HERE")

prompt = "Describe an Apple in Json format with the following keys: name, color, taste, and origin."

dictionary = {
    "role": "user", 
    "content": prompt
    }

response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[dictionary],
    response_format={"type": "json_object"}
)

answer = response.choices[0].message.content

jsonresponse = json.loads(answer)

print(f"\n{jsonresponse["name"]}\n")
