while True:
    print("\n===Simple Calculator ni maci===\n")
    print("1.Addition")
    print("2.Multiplication")
    print("3.Subtraction")
    print("4.Division")
    print("5.exit")

    choice = input("Choose(1-5)")

    if choice == "5":
        print("Calculator Closed.")
        break

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("First Number: "))
        num2 = float(input("Second Number: "))

        if choice == "1":
            answer = num1 + num2
        elif choice == "2":
            answer = num1 * num2
        elif choice == "3":
            answer = num1 - num2
        else:
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            answer = num1 / num2

        print("Answer:", answer)
    else:
        print("Invalid choice.")