from getpass import getpass
import time
from tokenize import Token
from IPython.display import clear_output
from IPython.display import Image
from IPython.display import display
import base64
import requests
import json

url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"
endpoint_question = "/question"
endpoint_all_questions = "/question/all"
endpoint_post_question = "/question"

def get_all_questions():
    questions = requests.get(url+endpoint_all_questions)
    return questions.json()['questions']
questions = get_all_questions()
print(questions)


def edit_user(token, payload):
    payload_json_string = json.dumps(payload)
    headers={
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.put(
        url + endpoint_user,
        data=payload_json_string,
        headers=headers
    )
    return response.text

alex_edit_payload={
    "first_name":"Bill"
}

edit_user(al['token'], jims_edit_payload)
def random_question(self):
    while True:
            counter = 0
            answer = input(f"{questions[0]['question']} ")
            if answer.lower() == questions[0]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[1]['question']} ")
            if answer.lower() == questions[1]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[2]['question']} ")
            if answer.lower() == questions[2]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[3]['question']} ")
            if answer.lower() == questions[3]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[4]['question']} ")
            if answer.lower() == questions[4]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[5]['question']} ")
            if answer.lower() == questions[5]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[6]['question']} ")
            if answer.lower() == questions[6]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[7]['question']} ")
            if answer.lower() == questions[7]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[8]['question']} ")
            if answer.lower() == questions[8]['answer'].lower():
                counter += 1
                print(counter)
            answer = input(f"{questions[9]['question']} ")
            if answer.lower() == questions[9]['answer'].lower():
                counter += 1
                if counter == 10:
                    return f'You got: {counter} out of 10. Perfect Score!'
                if counter >= 7:
                    return f'You got: {counter} out of 10. You passed!'
                if counter < 7:
                    return f'You got: {counter} out of 10. Better luck next time.'
            else:
                if counter == 10:
                    return f'You got: {counter} out of 10. Perfect Score!'
                if counter >= 7:
                    return f'You got: {counter} out of 10. You passed!'
                if counter < 7:
                    return f'You got: {counter} out of 10. Better luck next time.'