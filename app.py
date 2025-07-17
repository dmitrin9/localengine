from flask import Flask, render_template
import search as searchRanking

app = Flask(__name__)

@app.route("/search/<terms>")
def search(terms):
    splittedTerms = terms.split("+")
    print("TERMS ", splittedTerms)
    rank = searchRanking.search(splittedTerms)
    print(rank)
    return render_template("results.html", terms=splittedTerms, rank=rank)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
