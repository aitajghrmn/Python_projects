def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError("Invalid operation")


while True:
    print('''1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit''')

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Goodbye!")
        break

    elif choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                result = calculator(a, b, "add")
            elif choice == '2':
                result = calculator(a, b, "subtract")
            elif choice == '3':
                result = calculator(a, b, "multiply")
            elif choice == '4':
                result = calculator(a, b, "divide")

            print(f"Result: {result}")

        except ValueError:
            print("Please enter a valid number.")

        except ZeroDivisionError as e:
            print(e)

        except Exception as e:
            print(f"Unexpected error: {e}")

    else:
        print("Invalid choice. Please choose between 1 and 5.")
