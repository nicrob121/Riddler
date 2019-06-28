



def riddle(qid, useranswer, score):
   
    riddles = [
        {"riddle": "When does Christmas come before Thanksgiving?", "answer":"in the dictionary"},
        {"riddle": "What word in the dictionary is spelled incorrectly?", "answer":"incorrectly"},
        {"riddle": "What is brown and sticky?", "answer": "a stick"},
        {"riddle": "I'm tall when I'm young, and I'm short when I'm old. What am I?", "answer":"a candle"},
        {"riddle": "What occurs once in a minute, twice in a moment, but never in a thousand years?", "answer":"the letter m"},
        {"riddle": "You can old it without using your hands or arms. What is it?", "answer":"your breath"},
        {"riddle": "What building has the most stories?", "answer":"a library"},
        {"riddle": "In what month do people sleep the least?", "answer":"february"},
        {"riddle": "What has a head and a tail but no body?", "answer":"a coin"},
        {"riddle": "What tastes better than it smells?", "answer":"your tongue"},
        {"riddle": "What belongs to you, but others use it more than you?", "answer":"your name"},
        {"riddle": "What stays the same no matter how many letters you take away?", "answer":"a mailman"},
        {"riddle": "What has four legs, but can't walk?", "anwswer": "a table"},
        {"riddle": "What is seen in the middle of March and April that can't be seen at the beginning or end of either month?", "anwser": "the letter r"},
        {"riddle": "What English word has three consecutive double letters?", "answer": "bookkeeper"}
    ]

    if useranswer == riddles[qid]["answer"]:
        score = score + 1
        return "Correct! It's " + riddles[qid]["answer"] + "."
        
    else:
        return "Incorrect. It's " + riddles[qid]["answer"] + ". Now you can use it on your friends."

def updateScore(msg, score):
    if msg[0] == "C":
        return score + 1
    else:
        return score






# def ansriddle2(answer):
#     if answer == 'incorrectly':
#         image = "static/images/smile.jpg"
#         return "Correct."
#     else:
#         return "You're wrong"

# def ansriddle3(answer):
#     if answer == 'a stick':
#         image = "static/images/smile.jpg"
#         return "Correct."
#     else:
#         return "You're wrong"
        
    
        
        