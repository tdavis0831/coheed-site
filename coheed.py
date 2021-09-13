from flask import Flask, render_template
app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")



@app.route("/band-info")
def biography():
    return render_template("band.html")




if __name__=="__main__":
    app.run()