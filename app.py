from flask import Flask, render_template, redirect, request
import random
from worksheet import Worksheet
from question import Question

app = Flask(__name__)


@app.route("/")
def timesTableForm():
    return render_template("timesTablesForm.html")

@app.route("/division")
def divisionForm():
    return render_template("divisionForm.html")

@app.route("/indices")
def indicesForm():
    return render_template("indicesForm.html")

@app.route("/formulae")
def formulaeForm():
    return render_template("formulaeForm.html")


@app.route("/timesTablesWorksheet", methods=["post", "get"])
def timesTablesWorksheet():
    if request.method == "POST":
        # get worksheet title, instrs and num of questions
        title = request.form.get("title")
        qCount = int(request.form.get("questions"))
        instrs = request.form.get("instructions")

        # get numbers to multiply by
        selectedNums = request.form.getlist("multiplicands")
        upTo = int(request.form.get("up-to"))
        

        # generate every possible question using the numbers given
        possibleQs = []
        for i in range(2, upTo +1):
            for j in selectedNums:
                possibleQs.append(Question(i, "x", j ))
                #f"{str(i)} x {j}"

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
        selectedNums = request.form.getlist("divisors")
        upTo = int(request.form.get("up-to"))
        

        # generate every possible question using the numbers given
        possibleQs = []
        for i in range(2, upTo +1):
            for j in selectedNums:
                possibleQs.append(Question(i*int(j), "/", j))
                #f"{i*int(j)} / {j}"

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



@app.route("/indicesWorksheet", methods=["post", "get"])
def indicesWorksheet():
    if request.method == "POST":
        # get worksheet title, instrs and num of questions
        title = request.form.get("title")
        qCount = int(request.form.get("questions"))
        instrs = request.form.get("instructions")

        # get indices and bases 
        selectedNums = request.form.getlist("bases")
        upTo = int(request.form.get("up-to"))
        
        # get fractional
        indicesType = request.form.getlist("indices-type")

        # generate every possible question using the numbers given
        possibleQs = []
        
        for j in selectedNums:
            for i in range(2, upTo +1):

                # add question
                possibleQs.append(Question(j, "^", i))

                # add negative index question
                if "negative" in indicesType:
                    possibleQs.append(Question(j, "^", -1*i))

                # add reciprocal index question
                if "reciprocal" in indicesType:
                    possibleQs.append(Question(int(j)**i, "^", f"1/{i}"))

            # add zero index question
            if "zero" in indicesType:
                possibleQs.append(Question(j, "^", 0))



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


@app.route("/formulaeWorksheet", methods=["post", "get"])
def formulaeWorksheet():
    if request.method == "POST":
        # get worksheet title and instrs
        title = request.form.get("title")
        instrs = request.form.get("instructions")

        # get topics
        topics = request.form.getlist("topics")

        # get foundation
        higher = len(request.form.getlist("foundation")) == 0

        
        # generate all questions for selected topics
        possibleQs = []

        if "areas" in topics:
            possibleQs.append(Question("Area of a rectangle", "", ""))
            possibleQs.append(Question("Area of a triangle", "", ""))
            possibleQs.append(Question("Area of a paralellogram", "", ""))
            possibleQs.append(Question("Area of a trapezium", "", ""))
            possibleQs.append(Question("Area of a circle", "", ""))
            possibleQs.append(Question("Circumference of a circle", "", ""))
        if "volumes" in topics:
            possibleQs.append(Question("Volume of a prism", "", ""))
            possibleQs.append(Question("Volume of a cylinder", "", ""))
            
            if higher:
                possibleQs.append(Question("Volume of a pyramid", "", ""))
        if "pythag" in topics:
            possibleQs.append(Question("Pythagoras' theorem", "", ""))
            possibleQs.append(Question("SOHCAHTOA", "", ""))
        
        for x in [0, 30, 45, 60, 90]:
            if "sin-vals" in topics:
                possibleQs.append(Question(f"Exact value of sin({x})", "", ""))
            if "cos-vals" in topics:
                possibleQs.append(Question(f"Exact value of cos({x})", "", ""))            
            if "tan-vals" in topics:
                possibleQs.append(Question(f"Exact value of tan({x})", "", ""))
            
            
        if "sine-cosine" in topics and higher:
            possibleQs.append(Question("Sine rule", "", ""))
            possibleQs.append(Question("Cosine rule", "", ""))
            possibleQs.append(Question("Area of a triangle (using trigonometry)", "", ""))

        if "quadratic" in topics and higher:
            possibleQs.append(Question("Quadratic formula", "", ""))

        
        # randomise question if necessary
        if len(request.form.getlist("randomise")) == 0:
            questions = possibleQs
        else:
            qCount= len(possibleQs)
            questions=[]
            # randomly pick questions until enough all questions have been added/reordered
            while len(questions) < qCount:
                chosen = random.choice(possibleQs)
                possibleQs.remove(chosen)
                questions.append(chosen)


        return render_template("worksheet.html", ws=Worksheet(title, instrs, questions))
    return "get"



if __name__ == '__main__':
    app.run()