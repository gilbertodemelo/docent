from openai import OpenAI
import json
from dotenv import load_dotenv
from tools import list_files, tools

load_dotenv()
client = OpenAI()

user_input = "Please list all the file in the current directory"


input_list = [
    {
        "role" : "user",
        "content" : user_input
    }
]

# Prompt the model with tools defines
response = client.responses.create(
    model="gpt-5-nano",
    tools=tools,
    input = input_list,
)

# keep everything the model returned (including reasoning times)
input_list += response.output


# Run each tool call the model asked for
for item in response.output:
    if item.type == "function" and item.name == "list_files":
        args = json.loads(item.arguments)
        result = list_files(args["path"])
        input_list.append(
            {
                "type" : "functional_call_output",
                "call_id" : item.call_id,
                "output" : result,
            }
        )

# 2nd call: the model reads the tool result and answers
response = client.responses.create(
    model="gpt-5-nano",
    tools=tools,
    input=input_list
)


print(response.output_text)