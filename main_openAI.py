# API Keys: https://platform.openai.com/settings/organization/api-keys
# Billing: https://platform.openai.com/settings/organization/billing/overview

from openai import OpenAI

openai_client = OpenAI(api_key="OPENAI_API_KEY")

prompt = "Give me a very short recipe for a cake please."

dictionary = {
    "role": "user", 
    "content": prompt
    }

response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[dictionary]
)

answer = response.choices[0].message.content

print(f"\n{answer}\n")
