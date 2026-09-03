from flask import Flask
import random

number = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Guess the number!</p>"

@app.route("/<int:number_1>")
def bye_world(number_1):
    if number_1 < number:
        return "<p>Too low!</p>"
    elif number_1 == number:
        return "<p>GOOD JOB</p>"
    else:
        return "<p>Too high!</p>"
    
if __name__ == "__main__":
    app.run(port=5000)
