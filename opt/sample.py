import openai

openai.api_key = "独自のAPIキー"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "こんにちは"}
    ]
)
print(response["choices"][0]["message"]["content"]) 



