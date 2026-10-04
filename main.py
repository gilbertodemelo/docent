from openai import OpenAI
import json
from dotenv import load_dotenv
from tools import read_file, list_files, tools

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

print(response.output_text)