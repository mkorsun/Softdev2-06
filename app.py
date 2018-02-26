from flask import request, Flask, render_template
from assgn5 import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/results', methods=['GET'])
def results():
    type = request.args.get("search")
    data = ""
    text = request.args.get("text")
    if type == "name":
        data = find(text)
    elif type == "ID":
        data = findid(text)
    elif type == "evo":
        data = findevo(text)
    return render_template("results.html", data = data)

if __name__ == "__main__":
	app.debug = True
app.run()
