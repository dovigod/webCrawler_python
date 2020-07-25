from flask import Flask
from flask import render_template
from flask import request,redirect,send_file
from init import get_jobs
from exporter import save_to_file

app = Flask("Job Scapper")
##페이지당 스크래핑 될때마다 표기위해
fakedb ={}


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
       
       fromDB = fakedb.get(word)

       if fromDB:
           jobs =fromDB
       else:
            fakedb[word] = jobs
      
    else:
        return redirect("/")

    return render_template("report.html", searchBy = word , result_numb = len(jobs), jobs = jobs)

@app.route("/export")

def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = get_jobs(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")

    except:
        return redirect("/")


app.run(host = "0.0.0.0")