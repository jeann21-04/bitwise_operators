def display_result(op_name, result):
    print(f"\nResult of {op_name}:")
    print(f"Decimal: {result}")
    print(f"Binary : {bin(result)}\n")


def bitwise_menu():
    print("===== Bitwise Operations Menu =====")
    print("1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("4. NOT (~)")
    print("5. LEFT SHIFT (<<)")
    print("6. RIGHT SHIFT (>>)")
    print("7. Exit")


def main():
    while True:
        bitwise_menu()
        choice = input("Select an operation (1-7): ")

        if choice == '7':
            print("Exiting program. Goodbye!")
            break

        if choice in ['1', '2', '3', '5', '6']:
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))

        if choice == '1':  # AND
            result = a & b
            display_result(f"{a} & {b}", result)

        elif choice == '2':  # OR
            result = a | b
            display_result(f"{a} | {b}", result)

        elif choice == '3':  # XOR
            result = a ^ b
            display_result(f"{a} ^ {b}", result)

        elif choice == '4':  # NOT
            a = int(input("Enter an integer: "))
            result = ~a
            display_result(f"~{a}", result)

        elif choice == '5':  # LEFT SHIFT
            result = a << b
            display_result(f"{a} << {b}", result)

        elif choice == '6':  # RIGHT SHIFT
            result = a >> b
            display_result(f"{a} >> {b}", result)

        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    main()
