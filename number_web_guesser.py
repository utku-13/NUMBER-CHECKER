from flask import Flask
from random import randint

app = Flask(__name__)
HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
#below is perfeclty working h1 adder.

# def h1_adder(fn):
#     def wrapper():
#         return "<h1>" f"{fn()}" "</h1>"  
#     return wrapper

CREATED_NUM = randint(1,10)

@app.route("/")
def hello_to_game():
    return  '<h1 style="text-align:center">Welcome To The Game!!</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" align="middle" widht=500>'

@app.route(f"/number/<int:number>")
def check_number(number):
    if number == CREATED_NUM:
        return f'<h1>It is Correct</h1>' \
                f'<img src="{CORRECT}">'
    elif number > CREATED_NUM:
        return f'<h1>It is High</h1>' \
                f'<img src="{HIGH}">'
    else :
        return f'<h1>It is Low</h1>' \
                f'<img src="{LOW}">'


if __name__ =="__main__":
    app.run(debug=True)

#Perfectly working number guesser!!