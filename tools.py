# from openai import OpenAI
from pathlib import Path
import json 

# client = OpenAI()

# 1. Define a list of callable tools for the model
tools = [
    {
        "type" : "function",
        "name" : "list_files",
        "description" : "List the files in the given directory.",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "path" : {
                    "type" : "string",
                    "description" : "A path to the desired directory where the files are.",
                },
            },
            "required" : ["path"],
            "additionalProperties" : False # tells the models not to invent extra arguments
        },
        "strict" : True, # it makes the model follow the schema exactly
    }
]

def list_files(path: str) -> list[str]:
    p = Path(path)
    return [x.name for x in p.iterdir() if x.is_file()]


if __name__ == "__main__":

    file_path = Path(".")
    print(list_files(file_path))
