import json
import mysql.connector
import os


def lambda_handler(event, context):

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
    }

    try:

        # Handle CORS preflight request
        if event.get("requestContext", {}).get("http", {}).get("method") == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": headers,
                "body": json.dumps("CORS OK")
            }

        # Read request body
        body = json.loads(event["body"])

        # Connect to RDS MySQL
        connection = mysql.connector.connect(
            host=os.environ["DB_HOST"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_NAME"]
        )

        cursor = connection.cursor()

        # Insert user data
        query = """
        INSERT INTO users(name, email, password)
        VALUES(%s, %s, %s)
        """

        values = (
            body["name"],
            body["email"],
            body["password"]
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({
                "message": "User registered successfully"
            })
        }

    except Exception as e:

        print(str(e))

        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({
                "error": str(e)
            })
        }