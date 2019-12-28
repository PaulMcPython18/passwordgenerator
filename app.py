from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/random')
def random():
    return render_template('random.html')
@app.route('/', methods = ["POST"])
def predict():
    import random
    length_input = request.form['namequery']
    available_chars = "qwertyiopsDfghjklzxcvbnmQWERTYUIOPASdFGHuJKLZXaCVBNM!@#$%^&*()"
    for char in available_chars:
        if char in length_input:
            return render_template('random.html', message='* Please input a number * ')
    length_input = int(request.form['namequery'])
    if length_input >= 70:
        return render_template('random.html', message='* Please input a number that is less than 70 * ')
    available_chars = "qwertyiopsDfghjklzxcvbnmQWERTYUIOPASdFGHuJKLZXaCVBNM1234567890!@#$%&!@#$%&!@#$%&$#@!&^%$)(*&*()(*&^%$#{}{}"
    output = ""
    for i in range(length_input):
        output += random.choice(available_chars)
    print(output)
    return render_template('result.html', pwd=output)
@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(debug=True)
