age = int(input("Enter your age :- "))

if age>= 18:
    score = int(input("Enter your exam score :- "))
    if score>= 40:
        print("you meet both the age and score criterea, you are qualified")
    else:
        print("you meet both the age but do not the score criterea")
else:
    print("You do not meet the age criteria, plsease try when you are above 18 ")
