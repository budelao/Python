import json
import os
import pymysql

def lambda_handler(event, context):
    db_host = os.environ.get("DB_HOST", "host.docker.internal")

    try:
        connection = pymysql.connect(
            host=db_host,
            port=int(os.environ.get("DB_PORT", "3306")),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "root"),
            database=os.environ.get("DB_NAME", "sistema")
        )
    except pymysql.MySQLError as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

    try:
        with connection.cursor() as cursor:

            sql = "SELECT * FROM tb_estados"

            cursor.execute(sql)

            results = cursor.fetchall()

            estados = []

            for row in results:
                estados.append({
                    "id": row[0],
                    "nome": row[1],
                    "sigla": row[2]
                })

        return {
            "statusCode": 200,
            "body": json.dumps(estados)
        }

    finally:
        connection.close()
