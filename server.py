from flask import Flask
import random

number = random.randint(0,9)
print(number)

app = Flask(__name__)

@app.route("/")
def guess_a_number():
    return '<h1>Guesss a number between 0 and 9!</h1>' \
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'


@app.route(f"/<int:guess>")
def guess_number(guess):
    if guess < number:
        return '<h1>Too low!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > number:
        return '<h1>Too High!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>You found me!</h1>' \
               '<img src="https://media3.giphy.com/media/13ByqbM0hgfN7y/giphy.gif?cid=ecf05e47jb8z50ctfwcia7ljqmefaf0tvfnwuc73ubdunjjv&rid=giphy.gif&ct=g">'
# for n in range(0,9):
#     if n < number

if __name__ == "__main__":
    app.run(debug=True)