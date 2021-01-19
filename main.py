from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)

#app.secret_key = 'hello'
@app.route("/")
def home():
    return render_template('home.html', name="", name2='')


@app.route('/name', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form = request.form
    #    session["user"] = user
        Var1 = form['N1']
        return render_template('/home.html', name=Var1)

@app.route('/user')
def user():
    if "user" in session:
        user = session["user"]
        bob1 = user
        return render_template('/home.html', name=bob1)
    else:
        return redirect(url_for('name'))




if __name__ == "__main__":
    app.run(port='5000')