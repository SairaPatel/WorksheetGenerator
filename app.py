from flask import Flask, render_template, redirect, request
import random
from worksheet import Worksheet

app = Flask(__name__)


@app.route("/")
def timesTableForm():
    return render_template("index.html")

@app.route("/worksheet", methods=["post", "get"])
def worksheet():
    if request.method == "POST":
        # get worksheet title and num of questions
        title = request.form.get("title")
        qCount = int(request.form.get("questions"))

        # get numbers to multiply by
        selectedNums = request.form.getlist("times-tables")
        upTo = int(request.form.get("up-to"))
        
       
        # number of possible unique questions
        max = (5-1) * len(selectedNums)
        

        # generate questions randomly until done or until every possible unique question has been added
        questions = []

        while len(questions) < max and len(questions) < qCount:
            num1 = random.randint(2, upTo)
            num2 = int(random.choice(selectedNums))

            if num1 < num2:
                question = f"{num1} x {num2}"
            else:
                question = f"{num2} x {num1}"

            if question not in questions:
                questions.append(question)

        # if still not done (but every possible q has been added), fill in with duplicate questions
        while len(questions) < qCount:
            questions.append(random.choice(questions))

            
        return render_template("worksheet.html", ws=Worksheet(title, "", questions))
    return "get"

if __name__ == '__main__':
    app.run()