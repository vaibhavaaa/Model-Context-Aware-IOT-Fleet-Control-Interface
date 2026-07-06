import json

def lambda_handler(event, context):
    print("EVENT:", event)

    token = event["headers"].get("authorization")

    # Hardcoded secret token (you keep this private)
    VALID_TOKEN = "kljlkjoimnlknaslkkjlk "

    if token == VALID_TOKEN:
        return { "isAuthorized": True }

    return { "isAuthorized": False }


