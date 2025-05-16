from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

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

@app.context_processor
def inject_request():
    return dict(request=request)
if __name__ == "__main__":
    app.run(debug=True)