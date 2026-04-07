print("Convert temperatures between Celsius and Fahranheit. ")

print("Do you want to convert from Celsius to Fahrenheit or Fahrenheit to Celsius?" \
      "1.Celcius to Fahranheit " \
      "2.Fahranheit to Celcius")

number=int(input("Enter the temperature you want to convert: "))

choice=int(input("Enter your choice: "))
if choice == 1:
        print(9/5 * number + 32)
if choice == 2:
        print((number - 32) * 5/9)
else:    print("Invalid choice!")
