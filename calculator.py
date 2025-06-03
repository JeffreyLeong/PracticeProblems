# calculator.py
# A simple app doing mathmatical calculations
# by: Jeffrey Leong

def menu():
    print("Please select from the following: ")
    print("\t1. Add")
    print("\t2. Subtract")
    print("\t3. Multiply")
    print("\t4. Divide")
    print("\t5. Quit")

def adding(first_num, second_num):
    addition_value = first_num + second_num
    return addition_value

def subtracting(first_num, second_num):
    subtraction_value = first_num - second_num
    return subtraction_value

def multiplying(first_num, second_num):
    multiplication_value = first_num * second_num
    return multiplication_value

def dividing(first_num, second_num):
    division_value = first_num / second_num
    return division_value

def main():
   
    print("A simple calculator app\n")
    while True:
        menu()
        try:
            menu_selection = int(input("\nType the number for the operation that you wish to do: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
       
        if menu_selection == 5:
            print("\nHave a nice day")
            break
        elif menu_selection in [1, 2, 3, 4]:
            try:
                first_number = float(input("\nEnter a number: "))
                second_number = float(input("Enter a second number: "))
            except ValueError:
                print("Invalid number input. Please try again.")
                continue
           
            if menu_selection == 1:
                add_value = adding(first_number, second_number)
                print(f"Your numbers add to {add_value:.2f}")
            elif menu_selection == 2:
                sub_value = subtracting(first_number, second_number)
                print(f"Your numbers subtract to {sub_value:.2f}")
            elif menu_selection == 3:
                mul_value = multiplying(first_number, second_number)
                print(f"Your numbers multiply to {mul_value:.2f}")
            elif menu_selection == 4:
                div_value = dividing(first_number, second_number)
                print(f"Your number divides to {div_value:.2f}")
            elif menu_selection == 5:
                print("\nHave a nice day")
        else:
            print("Invalid selection. Please enter a number between 1 - 5.")
       
        again = input("Do you want to keep going? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

main()