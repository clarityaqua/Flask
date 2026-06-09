# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r") as f:
        return json.load(f)

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    jobs = load_jobs()
    keyword = request.args.get("keyword")
    results = []
    for job in jobs:
        if keyword.lower() in job["title"].lower():
            results.append(job)
    return render_template("search.html", results=results, keyword=keyword)

# /YOUR CODE


# BLUEPRINT | DONT EDIT

import os

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

# /BLUEPRINT