# MCP_CORE_CONCEPT


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


In the above example, we are defining separate JSON objects for select, insert, update, and delete operations.

If we want to support many operations, we must keep adding more JSON definitions again and again. This makes the system harder to maintain and less scalable.

To solve this problem, Anthropic introduced the MCP (Model Context Protocol) concept. MCP provides a standard structure where a single JSON-based interface can handle multiple operations dynamically instead of defining a new JSON block every time.

This reduces duplication and makes the integration more flexible and easier to manage.


