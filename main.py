from flask import Flask
from flask import render_template
from flask import request,redirect
from init import get_jobs

app = Flask("Job Scapper")


@app.route("/")
def home():
    
    return render_template("index.html")



@app.route("/report")
def report():
     ## www.google.com/reqort ?~~~ADW  =>> query arguments
    word = request.args.get("word")
    if word:
       word = word.lower()
       jobs = get_jobs(word)
       print(jobs)
    else:
        return redirect("/")

    return render_template("report.html", searchBy = word)



app.run(host = "0.0.0.0")