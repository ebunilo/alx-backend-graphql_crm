import datetime
from alx_backend_graphql.schema import schema


def log_crm_heartbeat():
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{timestamp} CRM is alive\n"
    
    with open("/tmp/crm_heartbeat_log.txt", "a") as f:
        f.write(message)
    
    # Optionally, query the GraphQL hello field to verify the endpoint is responsive
    try:
        result = schema.execute("{ hello }")
        if result.errors:
            # Log error if needed
            error_message = f"{timestamp} GraphQL query failed: {result.errors}\n"
            with open("/tmp/crm_heartbeat_log.txt", "a") as f:
                f.write(error_message)
        else:
            # Endpoint is responsive
            pass
    except Exception as e:
        error_message = f"{timestamp} Error querying GraphQL: {str(e)}\n"
        with open("/tmp/crm_heartbeat_log.txt", "a") as f:
            f.write(error_message)