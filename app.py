from flask import Flask, render_template, request, url_for, redirect
import base64
import search as searchRanking

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search = request.form.get("search")
        byte = search.encode("utf-8")
        encoded = base64.b64encode(byte)
        url_endpoint = url_for("search", terms=encoded.decode("utf-8"))
        return redirect(url_endpoint)

    return render_template("index.html")

@app.route("/search/<terms>")
def search(terms):
    termsEncode = base64.b64decode(terms.encode("utf-8"))
    splittedTerms = termsEncode.decode("utf-8").split(" ")
    rank = searchRanking.search(splittedTerms)
    return render_template("results.html", terms=splittedTerms, rank=rank)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
