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
    },

    {
        "type" : "function",
        "name" : "read_file",
        "description" : "Read the content of given file.",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "path" : {
                    "type" : "string",
                    "description" : "Will read a file and show its content"
                },
            },
            "required" : ["path"],
            "additionalProperties" : False
        },
        "strict" : True,
    }
]

def list_files(path: str) -> list[str]:
    try:
        p = Path(path)
        files = [x.name for x in p.iterdir() if x.is_file()]
    except FileNotFoundError:
        return f"Error: directory not found: {path}"
    except NotADirectoryError:
        return f"Error: not a directory: {path}"

    if not files:
        return f"No files found in {path}"
    return "\n".join(sorted(files))
    

    


