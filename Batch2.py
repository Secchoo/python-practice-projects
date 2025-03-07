def prog01():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The smaller number is: {min(num1, num2)}")

def prog02():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Not Equal") if num1 != num2 else print("Equal")

def prog03():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The difference is: {num1 - num2}")

def prog04():
    num1 = float(input("Enter dividend: "))
    num2 = float(input("Enter divisor: "))
    if num2 != 0:
        print(f"The quotient is: {int(num1 / num2)}")
    else:
        print("Error: Division by zero!")

def prog05():
    num1 = float(input("Enter dividend: "))
    num2 = float(input("Enter divisor: "))
    if num2 != 0:
        print(f"The remainder is: {num1 % num2}")
    else:
        print("Error: Division by zero!")

def prog06():
    first_num = float(input("Enter first number: "))
    total = first_num
    for i in range(9):
        num = float(input(f"Enter number {i+2}: "))
        total -= num
    print(f"The result is: {total}")

def prog07():
    even_count = 0
    for i in range(10):
        num = int(input(f"Enter number {i+1}: "))
        if num % 2 == 0:
            even_count += 1
    print(f"Number of even numbers: {even_count}")

def prog08():
    i = 0
    while i <= 100:
        if i % 2 != 0:
            print(i, end=' ')
        i += 1
    print()

def prog09():
    i = 0
    while i <= 100:
        if i % 10 != 0 and i % 10 != 5:
            print(i, end=' ')
        i += 1
    print()

def prog10():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    start = min(num1, num2)
    end = max(num1, num2)
    for i in range(int(start) + 1, int(end)):
        print(i, end=' ')
    print()

def main():
    while True:
        print("\n=== Number Processing Programs ===")
        print("1. Find smaller number")
        print("2. Check if numbers are not equal")
        print("3. Calculate difference")
        print("4. Calculate quotient (integer)")
        print("5. Calculate remainder")
        print("6. Subtract remaining numbers")
        print("7. Count even numbers")
        print("8. Print odd numbers 0-100")
        print("9. Print numbers not ending in 0 or 5")
        print("10. Print numbers between two numbers")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-10): ")
        
        if choice == '0':
            print("Goodbye!")
            break
        elif choice == '1':
            prog01()
        elif choice == '2':
            prog02()
        elif choice == '3':
            prog03()
        elif choice == '4':
            prog04()
        elif choice == '5':
            prog05()
        elif choice == '6':
            prog06()
        elif choice == '7':
            prog07()
        elif choice == '8':
            prog08()
        elif choice == '9':
            prog09()
        elif choice == '10':
            prog10()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()