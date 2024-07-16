from flask import Flask, render_template, redirect, request
import random
from worksheet import Worksheet

app = Flask(__name__)


@app.route("/")
def timesTableForm():
    return render_template("timesTablesForm.html")

@app.route("/divisionForm")
def divisionForm():
    return render_template("divisionForm.html")


@app.route("/timesTablesWorksheet", methods=["post", "get"])
def timesTablesWorksheet():
    if request.method == "POST":
        # get worksheet title, instrs and num of questions
        title = request.form.get("title")
        qCount = int(request.form.get("questions"))
        instrs = request.form.get("instructions")

        # get numbers to multiply by
        selectedNums = request.form.getlist("times-tables")
        upTo = int(request.form.get("up-to"))
        

        # generate every possible question using the numbers given
        possibleQs = []
        for i in range(2, upTo +1):
            for j in selectedNums:
                possibleQs.append(f"{str(i)} x {j}")

        questions=[]
        # randomly pick questions until enough have been added
        while len(questions) < qCount:
            chosen = random.choice(possibleQs)
            possibleQs.remove(chosen)
            questions.append(chosen)

            # if all possible questions have been added, start adding duplicates
            if len(possibleQs) == 0:
                possibleQs = list(questions)

            
        return render_template("worksheet.html", ws=Worksheet(title, instrs, questions))
    return "get"


@app.route("/divisionWorksheet", methods=["post", "get"])
def divisionWorksheet():
    if request.method == "POST":
        # get worksheet title, instrs and num of questions
        title = request.form.get("title")
        qCount = int(request.form.get("questions"))
        instrs = request.form.get("instructions")

        # get divisors 
        selectedNums = request.form.getlist("times-tables")
        upTo = int(request.form.get("up-to"))
        

        # generate every possible question using the numbers given
        possibleQs = []
        for i in range(2, upTo +1):
            for j in selectedNums:
                possibleQs.append(f"{i*int(j)} / {j}")

        questions=[]
        # randomly pick questions until enough have been added
        while len(questions) < qCount:
            chosen = random.choice(possibleQs)
            possibleQs.remove(chosen)
            questions.append(chosen)

            # if all possible questions have been added, start adding duplicates
            if len(possibleQs) == 0:
                possibleQs = list(questions)

            
        return render_template("worksheet.html", ws=Worksheet(title, instrs, questions))
    return "get"





if __name__ == '__main__':
    app.run()