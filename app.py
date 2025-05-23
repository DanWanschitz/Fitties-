from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/activity")
def activity():
    return render_template("activity.html")

@app.route("/research")
def research():
    return render_template("research.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/gamepage")
def gamepage():
    return render_template("gamepage.html")

@app.route("/memorymaze")
def memory_maze():
    return render_template("memorymaze.html")

@app.route("/memorygame")
def memory_game():
    return render_template("memorygame.html")

@app.context_processor
def inject_request():
    return dict(request=request)
if __name__ == "__main__":
    app.run(debug=True)
