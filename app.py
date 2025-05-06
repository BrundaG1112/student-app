from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    usn = request.form.get('usn')
    return jsonify({"status": "success", "name": name, "usn": usn})

if __name__ == '__main__':
    app.run(debug=True)

