from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

currentWord = None
table = []

@app.route("/")
def home():
    return render_template("index.html")


# Receive text from HTML
@app.route("/submit", methods=["POST"])
def submit():
    global table, currentWord

    data = request.get_json()
    text = data.get("value", "")

    table = text.split()
    currentWord = None

    print("User entered:", text)

    return jsonify({
        "status": "success",
        "received": text,
        "message": "Input received successfully!"
    })


# Get the next word
@app.route("/next", methods=["GET"])
def next_word():
    global table, currentWord

    if len(table) > 0:
        currentWord = table.pop(0)

        return jsonify({
            "value": currentWord
        })

    return jsonify({
        "value": "00000000"
    })


if __name__ == "__main__":
    app.run(debug=True)

