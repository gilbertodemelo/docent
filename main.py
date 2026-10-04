import json
from dotenv import load_dotenv
from openai import OpenAI
from tools import list_files, read_file, tools

load_dotenv()
client = OpenAI()

input_list = [
    {"role": "user", "content": "List the files in the current directory, then read tools.py and summarize it."}
]

MAX_ROUNDS = 10

for _ in range(MAX_ROUNDS):
    response = client.responses.create(
        model="gpt-5-nano",
        tools=tools,
        input=input_list,
    )

    # Keep everything the model returned (including reasoning items)
    input_list += response.output

    tool_calls = [item for item in response.output if item.type == "function_call"]

    # No tool calls means the model is done
    if not tool_calls:
        break

    for item in tool_calls:
        args = json.loads(item.arguments)

        if item.name == "list_files":
            result = list_files(args["path"])
        elif item.name == "read_file":
            result = read_file(args["path"])
        else:
            result = f"Error: unknown tool {item.name}"

        input_list.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result,
            }
        )

print(response.output_text)