from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/yourmom")
def secondhome():
    return "Mommy energy"

@app.route("/<daddyenergy>") # /milk -> daddyenergy = milk
def milk(daddyenergy): # daddyenergy = milk
    return render_template('base.html', word=daddyenergy) # word = daddyenegry = milk
    

if __name__ == "__main__":
    app.run(debug = True)