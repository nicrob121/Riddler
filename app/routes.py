from app import app
from flask import render_template, request
from app.models import model, formopener

score = 0

@app.route('/')
@app.route('/index')
def index():
    return render_template("Riddler.html")
@app.route("/reset")
def reset():
    global score
    score = 0
    return render_template("Riddler.html")
@app.route('/results', methods=["POST","GET"])
def results():
    global score
    if request.method == "GET":
        return "<h1>Please answer the riddle you cheater<h1>"
    else:
        userdata = formopener.dict_from(request.form)
        print(userdata)
        useranswer = userdata['useranswer']
        qid = int(userdata['qid'])
        message = model.riddle(qid, useranswer, 0)
        score = model.updateScore(message, score)
        
        return render_template('results.html', answer1 = useranswer, message = message, score = score)






# answer2 = answer2, answer3 = answer3, answer4 = answer4, answer5 = answer5, answer6 = answer6, answer7 = answer7, message = message