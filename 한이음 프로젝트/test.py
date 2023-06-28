from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    data_list = [
        {'celsius': 25, 'fahrenheit': 77, 'humidity': 60},
        {'celsius': 28, 'fahrenheit': 82.4, 'humidity': 65},
        {'celsius': 30, 'fahrenheit': 86, 'humidity': 70}
    ]
    return render_template('index.html', data_list=jsonify(data_list))

if __name__ == '__main__':
    app.run(debug=True)