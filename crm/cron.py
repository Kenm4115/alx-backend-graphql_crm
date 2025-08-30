import datetime
import requests

LOG_FILE = "/tmp/crm_heartbeat_log.txt"
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql"

def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Try querying GraphQL hello field
    try:
        query = {"query": "{ hello }"}
        response = requests.post(GRAPHQL_ENDPOINT, json=query)
        if response.status_code == 200:
            data = response.json()
            hello_value = data.get("data", {}).get("hello", "")
            message += f" | GraphQL hello: {hello_value}"
        else:
            message += f" | GraphQL check failed (status {response.status_code})"
    except Exception as e:
        message += f" | GraphQL check error: {e}"

    # Append to log file
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
