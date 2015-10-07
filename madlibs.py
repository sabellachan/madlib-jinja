from random import choice, sample

from flask import Flask, render_template, request




# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page. <a href='/hello'>Hello</a>"

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/game', methods=["POST"])
def show_game_form():
    game_response = request.form.get("game")
    name = request.form.get("name")
    if game_response == "no":
        return render_template("goodbye.html", person=name)
    else:
        return render_template("game.html")        

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliments = sample(set(AWESOMENESS), 3)
    print type(compliments)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route('/madlib')
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    adverb = request.args.get("adverb")
    smell = request.args.get("smell")
    taste = request.args.get("taste")

    madlib_options = ["madlib.html", "madlib1.html", "madlib2.html"]
    madlib = choice(madlib_options)

    return render_template(madlib, color=color, noun=noun, person=person, 
        adjective=adjective, adverb=adverb, smell=smell, taste=taste)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
