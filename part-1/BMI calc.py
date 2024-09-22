# BMI = weight in kg / (height in m)^2

weight = float(input("Enter weight in kg :- "))
height = float(input("Enter height in meters :- "))

bmi = weight / (height * height)
print ("BMI is :- ",bmi)
print(f'BMI is :- {bmi}')