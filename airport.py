from flask import Flask
import mysql.connector

app = Flask(__name__)

# Database connection
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="health_game",
    user="mizan",
    password="mizan2217",
    autocommit=True
)

# Endpoint of the route
@app.route('/airport/<icao>')
def get_airport(icao):
    cursor = connection.cursor()

    # SQL query
    sql = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))

    result = cursor.fetchone()

    if result:
        response = {
            "ICAO": icao,
            "Name": result[0],
            "Location": result[1]
        }
        return response
    else:
        return {
            "message": "Airport not found",
            "status": 404
        }


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)