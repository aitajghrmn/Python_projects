print("Calculate your Body Mass Index (BMI). \ " \
"Enter your weight in kilograms and height in meters. ")

weight=float(input("Enter your weight in kg :"))
height=float(input("Enter your height in m :"))
bmi=weight/(height*height)

print("Your BMI is : " , bmi)
