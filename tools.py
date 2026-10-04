from openai import OpenAI
import json 

client = OpenAI()

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
            "required" : ["path"]
        },
    }
]