from flask import Flask, render_template
app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return render_template('index.html')

@app.route('/play')
def play():
    return render_template('index1.html')

@app.route('/play/<int:num>')
def level2(num):
    return render_template('index2.html', num = num)

@app.route('/play/<int:num>/<string:color>')
def level3(num, color):
    return render_template('index3.html', num = num, color = color)

@app.route('/<path:path>')
def error(path):
    return "Error! No path found, try again!"

if __name__ == "__main__":
    app.run(debug=True)