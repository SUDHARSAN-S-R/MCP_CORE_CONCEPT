import os

from groq import Groq

from tool_executor import execute_query

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("Set GROQ_API_KEY in your environment before running this script.")

client = Groq(api_key=API_KEY)
MODEL_NAME = "llama-3.3-70b-versatile"

tools = [
    {
        "type": "function",
        "function": {
            "name": "select",
            "description": "This function is used to perform select query",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "insert",
            "description": "This function is used to perform insert query",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "update",
            "description": "This function is used to perform update query",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "delete",
            "description": "This function is used to perform delete query",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    }
]


def chat(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            tools=tools,
            tool_choice="auto",
        )
    except Exception as exc:
        message = str(exc)
        if "404" in message or "not found" in message.lower():
            print(
                f"Model not found: {MODEL_NAME}. "
                "Use a supported Groq model, for example llama-3.3-70b-versatile."
            )
            return
        if "429" in message or "rate limit" in message.lower():
            print(
                "Groq quota or rate limit exceeded (429). "
                "Check your Groq plan/usage and retry after a short wait."
            )
            return
        if "401" in message or "unauthorized" in message.lower():
            print(
                "Invalid Groq API key (401). "
                "Check your API key and try again."
            )
            return
        raise

    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            result = execute_query(name)

            print("tool", name)
            print("result", result)
    else:
        print("response", message.content)


if __name__ == "__main__":
    chat("insert")