# SI = P * N * R / 100

principal = int(input("Enter the amount borrowed :- "))
years = float(input("Enter the period in years :- "))
rate = float(input("Enter rate of interest :- "))


interest = principal*years*rate/100
print('Simple intrest clculated is '+ str(interest))


print("--------------------------------------------")

# Simple Interest Calculation
principal = int(input("Enter the amount borrowed: "))
years = float(input("Enter the period in years: "))
rate = float(input("Enter rate of interest: "))

interest = principal * years * rate / 100

# Using f-string for better readability
print(f'Simple interest on the principal amount of ${principal} for a period of {years} years at a rate of {rate}% is ${interest}')
