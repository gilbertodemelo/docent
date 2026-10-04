from pathlib import Path

tools = [
    {
        "type": "function",
        "name": "list_files",
        "description": "List the files in the given directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "A path to the desired directory where the files are.",
                },
            },
            "required": ["path"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "read_file",
        "description": "Read the content of the given file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Path to the file to read.",
                },
            },
            "required": ["path"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]


def list_files(path: str) -> str:
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


def read_file(path: str) -> str:
    try:
        return Path(path).read_text()
    except FileNotFoundError:
        return f"Error: file not found: {path}"
    except IsADirectoryError:
        return f"Error: not a file: {path}"
    except (PermissionError, UnicodeDecodeError) as e:
        return f"Error: cannot read {path}: {e}"


if __name__ == "__main__":
    print(list_files("."))
    print(read_file("./tools.py"))
    print(read_file("nope.txt"))
    print(read_file("."))