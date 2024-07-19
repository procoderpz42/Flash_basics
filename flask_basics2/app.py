from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

valid_animal = ["chickens", "ducks", "pandas"]
@app.route("/<animal>")
def animal_info(animal):
    if animal in valid_animal:
        return render_template(f"{animal}.html")
    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, port=12345)
