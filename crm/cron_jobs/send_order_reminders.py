#!/usr/bin/env python3
import datetime
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

LOG_FILE = "/tmp/order_reminders_log.txt"
GRAPHQL_ENDPOINT = "http://localhost:8000/graphql"

def main():
    # GraphQL transport setup
    transport = RequestsHTTPTransport(
        url=GRAPHQL_ENDPOINT,
        verify=True,
        retries=3,
    )
    client = Client(transport=transport, fetch_schema_from_transport=True)

    # Calculate date 7 days ago
    seven_days_ago = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()

    # GraphQL query
    query = gql("""
        query($date: Date!) {
            allOrders(filter: { orderDateGte: $date }) {
                edges {
                    node {
                        id
                        orderDate
                        customer {
                            email
                        }
                    }
                }
            }
        }
    """)

    params = {"date": seven_days_ago}

    try:
        result = client.execute(query, variable_values=params)
        orders = result.get("allOrders", {}).get("edges", [])

        with open(LOG_FILE, "a") as log:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for edge in orders:
                node = edge["node"]
                order_id = node["id"]
                email = node["customer"]["email"]
                log.write(f"{timestamp} - Reminder for Order {order_id}, Customer: {email}\n")

        print("Order reminders processed!")

    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"{datetime.datetime.now()} - ERROR: {e}\n")
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
