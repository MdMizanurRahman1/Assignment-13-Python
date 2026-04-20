from flask import Flask

app = Flask(__name__)

# Function to check prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Endpoint of the route
@app.route('/prime_number/<number>')
def check_prime(number):
    try:
        num = int(number)
        result = is_prime(num)

        response = {
            "Number": num,
            "isPrime": result
        }

        return response

    except ValueError:
        return {
            "message": "Invalid input",
            "status": 400
        }


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)