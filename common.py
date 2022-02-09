commands = {
    "register": "register",
    "deregister": "deregister",
    "message": "msg"
}

codes = {
    "INCOMPLETE_COMMAND_PARAMETERS": 201,
    "COMMAND_UNKNOWN": 301,
    "COMMAND_ACCEPTED": 401,
    "USER_NOT_REGISTERED": 501,
    "USER_ALREADY_EXISTS": 502
}

code_definitions = {
    201: "Command parameters incomplete",
    301: "Command unknown",
    401: "Command accepted",
    501: "User not registered",
    502: "User account exists"
}
