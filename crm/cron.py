import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/crm_heartbeat_log.txt"
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql"


def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive"

    # Set up gql client
    try:
        transport = RequestsHTTPTransport(
            url=GRAPHQL_ENDPOINT,
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Query hello field
        query = gql("{ hello }")
        response = client.execute(query)

        hello_value = response.get("hello", "")
        message += f" | GraphQL hello: {hello_value}"

    except Exception as e:
        message += f" | GraphQL check error: {e}"

    # Append to log file
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")


LOG_FILE = "/tmp/low_stock_updates_log.txt"
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql"


def update_low_stock():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

    try:
        # GraphQL transport
        transport = RequestsHTTPTransport(
            url=GRAPHQL_ENDPOINT,
            verify=True,
            retries=3,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        # Mutation query
        mutation = gql("""
        mutation {
          updateLowStockProducts {
            success
            message
            updatedProducts {
              id
              name
              stock
            }
          }
        }
        """)

        response = client.execute(mutation)
        data = response.get("updateLowStockProducts", {})

        message = f"{timestamp} | {data.get('message', 'No response')}"
        updated_products = data.get("updatedProducts", [])

        for product in updated_products:
            message += f"\n - {product['name']}: {product['stock']} units"

    except Exception as e:
        message = f"{timestamp} | Error: {e}"

    # Write log
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
