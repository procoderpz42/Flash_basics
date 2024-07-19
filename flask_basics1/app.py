from flask import Flask, render_template
import random


app = Flask(__name__)

my_college = "ASRJC"
rival_college = "ACJC"
secret_text = "I am the impostor!!"
secret_nums = [1, 2, 3, 4, 999887766554332134271935, 15923864819389492]
secret_info = {"name": "franstin", "age": "17"}

@app.route("/")
@app.route("/main")
def home():
    return "<h1>Hello World!!</h1>"


@app.route("/comp")
@app.route("/computing")
def computing():
    return "<p>What is computing?</p>"

@app.route("/about")
def about():
    return return_template("about.html", my_college = my_college, rival_college=rival_college)


@app.route("/secret")
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template("secret.html", lucky_num=lucky_num, secret_text=secret_text, secret_info=secret_info)
    
if __name__ == "__main__":
    app.run(debug=True, port=1234)
