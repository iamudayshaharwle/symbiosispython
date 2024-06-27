

question_prompt = [
    "what is my name?\n(a) bruce\n(b) uday\n(c) tom\n\n",
    "what is my age?\n(a) 23\n(b) 25\n(c) 20\n\n",
    "where i live?\n(a) india\n(b) us\n(c) japan\n\n",
    'what i like?\n(a) movies\n(b) football\n(c) nothing\n\n'
]

class Question:
    def __init__(self,prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions =[
    Question(question_prompt[0],'b'),
    Question(question_prompt[1],'c'),
    Question(question_prompt[2],'a'),
     Question(question_prompt[3],'a'),
]

def test(questions):
    score =0 
    for x in questions:
        answer = input(x.prompt)
        if answer == x.answer:
            score += 1
    print(f'your score is {score}/{len(questions)}')   
    

test(questions)
