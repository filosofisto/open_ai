import openai
import os
import sys
import time

start_time = time.time()

times = []

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    stream=True,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful teacher."
        },
        {
            "role": "user",
            "content": "Are there other measures than time complexity for an algorithm?",
        },
        {
            "role": "assistant",
            "content": "Yes, there are other measures besides time complexity for an algorithm, "
                       "such as space complexity.",
        },
        {
            "role": "user",
            "content": "What is it?"
        },
    ],
)

chunks = []

for chunk in response:
    delta = chunk['choices'][0]['delta']
    times.append(time.time() - start_time)

    # Last will be empty
    if 'content' in delta:
        sys.stdout.write(delta['content'])

    chunks.append(chunk)

print(f"\n\nFull response received {times[-1]:.2f} seconds after request")
# print(response["choices"][0]["message"]["content"])
