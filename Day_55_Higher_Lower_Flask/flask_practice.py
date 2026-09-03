from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_world():
    return "<p>Bye World!</p>"\
    "<p> UWU </p>"\
    "<img src = https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjRicDNsNGs0Njl6eG54MHB4OWRhNndoN2w3Mnk0NWF3c3cxNnplcyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/OuQmhmAAdJFLi/giphy.webp>"

@app.route("/username/<name>")
def greet(name):
    return f"<p>Hello, {name}!</p>"
    
if __name__ == "__main__":
    app.run(port=5000)
