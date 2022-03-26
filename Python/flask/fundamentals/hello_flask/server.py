from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/hi/<string:name>')
def hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:input>')
def repeat(num, input):
    return f"{input * num}"

@app.route('/<path:path>')
def error(path):
    return f"Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)