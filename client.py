from openai import OpenAI

# Replace with your actual OpenAI API key
client = OpenAI(api_key="")

# Call the OpenAI Chat Completion endpoint
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
        {"role": "user", "content": "What is coding?"}
    ]
)

# Print the assistant's reply
print("Jarvis:", response.choices[0].message.content)

