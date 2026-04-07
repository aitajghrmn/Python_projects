'''This app helps the user to calculate two numbers.'''

print("What do you want to do? " \
"1. + " \
"2. - " \
"3. * " \
"4./")

choice=int(input("Enter your choice: "))

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

if choice == 1:
    print("The sum is: ", a+b)
elif choice == 2:
    print("The difference is: ", a-b)
elif choice == 3:
    print("The product is: ", a*b)
elif choice == 4:
    print("The quotient is: ", a/b)
else:
    print("Invalid choice!")

    
