from curses.ascii import isdigit
from getpass import getpass
from multiprocessing.sharedctypes import Value
import time
from tokenize import Token
from IPython.display import clear_output
from IPython.display import Image
from IPython.display import display
import random
import base64
import requests

url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"
endpoint_question = "/question"
endpoint_all_questions = "/question/all"
endpoint_post_question = "/question"

#def get_question():
    #question = requests.get(url+endpoint_question)
    #return question.json()['questions']
#question = get_question()
#print(question)
def login_user(user_name, password):
    auth_string = user_name + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    return user_data.json()
#login_user('alexanderacollins@gmail.com', '123')
al=login_user('alexanderacollins@gmail.com','123')
#al['token']


def get_all_questions():
    questions = requests.get(url+endpoint_all_questions)
    return questions.json()['questions']
questions = get_all_questions()
#print(get_all_questions())

def lam():
    return len(questions)
#print(lam())

import json

def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text
    
alexs_payload={
    "email":"alexander@gmail.com",
    "first_name":"Alex",
    "last_name":"Collins",
    "password":"123"
}

#register_user(alexs_payload) 

def login_user(user_name, password):
    auth_string = user_name + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    return user_data.json()
#login_user('alexanderacollins@gmail.com', '123')
al=login_user('alexanderacollins@gmail.com','123')
#al['token']

def post_question(token, payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.post(
        url + endpoint_post_question,
        data = payload_json_string,
        headers = headers
    )
    return response.text

alexs_payload={
    "question":"What is the capital of Jalisco?",
    "answer":"Guadalajara."
}
#post_question(al['token'], alexs_payload)



def delete_question(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    
    response = requests.delete(
        url+endpoint_question+'/''15',
        headers=headers
    )
    return response.text
#print(delete_question(al['token']))

def random_question():
    box = []
    max_questions = len(questions) - 1
    random_num = random.randrange(0, max_questions)
    rand_question = [questions[random_num]['question'], questions[random_num]['answer']]
    box.append(rand_question[-1])
    return box
#print(random_question())


def get_choices(questions, rand_question):
    max_questions = len(questions) - 1
    choices = []
    i = 0
    while i < 3:
        random_num = random.randrange(0, max_questions)
        question = questions[random_num]['question']
        if question == rand_question['question']:
            continue
        else:
            choices.append(question)
            i = i + 1

    return choices

#question = random_question()

from getpass import getpass
import time
import random
from IPython.display import clear_output
from IPython.display import Image
from IPython.display import display

def login(email):
    clear_output()
    password=getpass("Password: ")
    user = login_user(email, password) 
    return user

def register():
    clear_output()
    print("Registration:")
    email = input("Email: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    password = getpass("Password: ")
    
    user_dict={
        "email":email,
        "first_name":first_name,
        "last_name":last_name,
        "password":password
    }
    return register_user(user_dict)

class QuizBowl():
    def __init__(self):
        self.score = 0
        self.counter = 0
        self.question_dict = {}
        self.id = []

    def random_question(self):
            
       
            while self.counter < 10:
           
                max_questions = len(questions) - 1
                random_num = random.randrange(0, max_questions)
                rand_question = {questions[random_num]['question']:questions[random_num]['answer']}
                for key, value in rand_question.items():
                    answer = input(f'{key} ')
                    if answer.lower() == value.lower():
                        self.score += 1
                        self.counter += 1
                        print(f'nice job! answer was {value}', self.counter)
                    if answer.lower() != value.lower():
                        self.counter += 1
                        print(f'sorry! answer was {value}', self.counter)
                    if self.counter >= 10:
                        break
            if self.score == 10:
                print(f'Your score was {self.score}. You rock!')
                time.sleep(2)
                return
            if self.score >= 7:
                print(f'Your score was {self.score}. You passed!')
                time.sleep(2)
                return
            elif self.score < 7:
                print(f'Your score was {self.score}. Better Luck Next Time')
                time.sleep(2)
                return

    def get_post_question(self, token):
        payload_json_string = json.dumps(self.question_dict)
        headers = {
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token
        }
        response = requests.post(
            url + endpoint_post_question,
            data = payload_json_string,
            headers = headers
        )
        return response.text

    def get_edit_question(self, token):
        payload_json_string = json.dumps(self.question_dict)
        headers={
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token
        }
        response = requests.put(
            url + endpoint_question +'/'f'{self.id.pop()}',
            data=payload_json_string,
            headers=headers
        )
        return response.text

    def get_delete_question(self, token):
        headers = {
            'Authorization':"Bearer " + token
        }
        
        response = requests.delete(
            url+endpoint_question+'/'f'{self.id.pop()}',
            headers=headers
        )
        return response.text

    def get_my_questions(self, token):
        headers = {
            'Content-Type':'application/json',
            'Authorization':'Bearer ' + token
        }
        response = requests.get(
            url + endpoint_question,
            headers = headers
        )
        return response.text
    

def main():
    quiz = QuizBowl()
    
    while True:
        print("Want to Enter Quiz Bowl?")
        email = input("Type your email to login or Type `register` to Register ")
        if email == 'register':
            success_register = register()
            if success_register:
                print("You have successfully registered")
                continue
        if email == 'alexanderacollins@gmail.com':
            answer = input('''If you are who you say you are...
            what was the name of you first companion? ''')
            if answer.lower() == "jax":
                print("Welcome My King!")
            else:
                print("Be Gone Demon!")
            time.sleep(1)
            while True:
                print("""
Welcome to Quiz Bowl!

You Can:
1. Take Quiz
2. Create Question
3. Edit Question
4. Delete Question
5. View Questions
6. Quit      
""")            
                prompt = input("Enter Choice Here: ")
                if prompt == "1":
                    print(quiz.random_question())
                if prompt == "2":
                    question = input("What is your question? ")
                    ans = input("What is your answer? ")
                    quiz.question_dict["question"] = question
                    quiz.question_dict["answer"] = ans
                    prompt = input(f"Are you sure you would like to submit {quiz.question_dict}?")
                    if prompt[0].lower() == "y":
                        print(quiz.get_post_question(al['token']))
                    else:
                        pass
                if prompt == "3":
                    print(quiz.get_my_questions(al['token']))
                    id_num = input("What is the id number of the question you would like to edit? ")
                    quiz.id.append(id_num)
                    question = input("New Question: ")
                    ans = input("New Answer: ")
                    quiz.question_dict["question"] = question
                    quiz.question_dict["answer"] = ans
                    prompt = input(f"Are you sure you would like to submit this edit: {quiz.question_dict}? ")
                    if prompt[0].lower() == "y":
                        print(quiz.get_edit_question(al['token']))
                    else:
                        pass

                if prompt == "4":
                    print(quiz.get_my_questions(al['token']))
                    id_num = input("What is the id number of the question you would like to delete? ")
                    quiz.id.append(id_num)
                    prompt = input(f"Are you sure you would like to delete question number {quiz.id}? ")
                    if prompt[0].lower() == "y":
                        print(quiz.get_delete_question(al['token']))
                    else:
                        pass
                if prompt == "5":
                    print(quiz.get_my_questions(al['token']))
                    time.sleep(2)
                if prompt == "6":
                    print("Thanks for playing!")
                    return
                

        elif email.lower() == "quit":
            print("Goodbye")
            break
        else:
            try:
                login(email)
            except:
                print("Invalid Username/Password combo")
                time.sleep(2)
                continue
        while True:
            print("""
Welcome to Quiz Bowl!

You Can:
1. Take Quiz
2. Quit      
""")
            prompt = input("Enter Choice Here: ")
            if prompt == "1":
                print(quiz.random_question())
            if prompt == "2":
                print("Thanks for playing!")
                return
                
main()
                    

















