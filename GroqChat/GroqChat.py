import os
import sys

from groq import Groq

client = Groq(
    api_key=sys.argv[2],
)
# Argumento 1: Texto del usuario
# Argumento 2: apikey
# Argumento 3: modeloIA
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "responde en espanol " + sys.argv[1],
        }
    ],
    model=sys.argv[3],
)

print(chat_completion.choices[0].message.content)
