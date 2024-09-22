def save_user_data():
    name = input("Enter name :- ")
    email = input("Enter email :- ")
    contect = input("Enter content")

    user_data = f" Name:{name}\n Email:{email}\n Content:{contect}"
    with open('user_data.txt','a') as file:
        file.write(user_data)

save_user_data()

def read_user_data():
    with open("user_data.txt",'r') as file:
        print(file.read())

read_user_data()