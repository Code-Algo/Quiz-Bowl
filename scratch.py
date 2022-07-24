from getpass import getpass
import time
from IPython.display import clear_output
from IPython.display import Image
from IPython.display import display

import requests

url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"


def get_books():
    books = requests.get(url+endpoint_book)
    return books.json()['books']
books = get_books()
books


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

def display_book_short(book):
    print(f"{book['id']} \t| {book['title'][:50].ljust(50)} | \t{book['subject']}")

def display_book_long(book):
    cover = Image(url=book['img'])
    display(cover)
    print(f'''
Title:\t {book['title']}
Author: {book['author']}
Pages:\t {book['pages']}
Subject: {book['subject']}
Summary: {book['summary']}
''')
    

    
class ReadingList():
    def __init__(self):
        self.reading_list=[]
        
    def add_book(self, book):
        if book not in self.reading_list:
            self.reading_list.append(book)
    
    def remove_book(self, book):
        self.reading_list.remove(book)
    
    def empty(self):
        self.reading_list=[]
    
    def show_book_list(self):
        clear_output()
        if not self.reading_list:
            print("Your reading list is empty")
        for book in self.reading_list:
            print(f'''
{"="*50}            
\n
Title:\t {book['title']}
Book ID: {book['id']}
Author:\t {book['author']}
Subject: {book['subject']}
Summary: {book['summary']}
\n
{"="*50}            
\n
''')
    
    def show_small_book_list(self):
        if not self.reading_list:
            print("Your reading list is empty")
        else:
            for book in self.reading_list:
                display_book_short(book)

def browse_books(books, reading_list, subject=None):
    while True:
        clear_output()
        print(f'''
Welcome to the Book Browser
You are viewing {subject if subject else 'all'} books
[ID] \t| {"[TITLE]".ljust(50)} | [SUBJECT]
        ''')
        if subject:
            books=get_book_by_category(books, subject)
        for book in books:
            display_book_short(book)

        selection = input("Select you book by ID [BACK to back out]")
        if selection.lower()=='back':
            return
        elif selection.isnumeric() and int(selection) in map(lambda book: book['id'], books):
            selection=int(selection)
            while True:
                print(f'''
You Selected: {list(filter(lambda book: book['id'] == selection, books))[0]['title']}
1. Add Book To Reading List
2. View More Information
3. Go Back
4. Go To Main Menu
''')
                action = input("Action: ")
                if action =="1":
                    reading_list.add_book(list(filter(lambda book: book['id']==selection, books))[0])
                    print("As you wish")
                    time.sleep(1)
                    break
                elif action =="2":
                    clear_output()
                    display_book_long(list(filter(lambda book: book['id']==selection, books))[0])
                    input("Press Enter To Continue")
                elif action=="3":
                    break
                elif action=="4":
                    return
                    
        else:
            print("Invalid ID")
            time.sleep(2)
            continue
    

def main():
    reading_list = ReadingList()
    books = get_books()
    
    while True:
        clear_output()
        print("Welcome to the Bookstore")
        email = input("Type your email to login or Type `register` to Register ")
        if email == 'register':
            success_register=register()
            if success_register:
                print("You have successfully registered")
                continue
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
        # First Scene of our app (above)
        while True:
            clear_output()
            print("""
Welcome to the Repository            
You can:            
1. Browse All Books
2. Browse Book by Category
3. View Reading List
4. Remove Book From Reading List
5. Quit     
""")
            command = input("Select your Fate: ")
            if command == "1":
                browse_books(books, reading_list)
            elif command == "2":
                while True:
                    print(" | ".join(get_category_list(books)))
                    cat = input("Category: ").title()
                    if cat in get_category_list(books):
                        browse_books(books, reading_list, cat)
                        break
                    print("Invalid Category")
                    time.sleep(2)
                    continue
            elif command == "3":
                reading_list.show_book_list()
                input("Press Enter To Return")
                continue
            elif command == "4":
                while True:
                    clear_output()
                    reading_list.show_small_book_list()
                    garbage = input("What book ID would you like to remove? [BACK to back out]")
                    if garbage.lower() == "back":
                        break
                    elif garbage.isnumeric() and int(garbage) in map(lambda book: book['id'], reading_list.reading_list):
                        reading_list.remove_book(list(filter(lambda book: book['id']==int(garbage), reading_list.reading_list))[0])
                        print(f'{garbage} has been removed')
                        time.sleep(2)
                        break
                    else:
                        print(f'{garbage} is not in your collection')
                        time.sleep(2)
                        break
                continue   
                    
            elif command == "5":
                print("Goodbye")
                break
            else:
                print("Invalid Selection")
                time.sleep(2)
                continue
        break
            

print(main())