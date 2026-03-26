# MCP_CORE_CONCEPT
these tell about how does an the mcp came into picture due to that json format

see here we use the json format for each of them 

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


in the above one we see an the json format for an the insert select update delete 
so, if we want to do the operation for the n number of them then we want to add the json format n times also 

To omit these only the Anthropic brought an the standard mcp concept i means a standard json format by using a single json we can operate n number of operation


