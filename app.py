from flask import Flask, render_template, request, jsonify
from brute_force import brute_force

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/simulate", methods=["POST"])
def simulate():

    data = request.get_json()

    password = data["password"]

    result = brute_force(password)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)