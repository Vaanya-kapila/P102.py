import os

def main():
    print("Hi there! I have designed an all in one calculator which does functions like-")
    print("1. Convert decimal number to BINARY, OCTAL and HEXADECIMAL")
    print("'2' to do Addition .'3' to do Subtraction .'4' to Multiply .'5' to Divide .")

    choice = int(input("Enter your choice: "))

    if(choice == 1):
        print("Ok so going on with program number 1.")
        num = int(input("Enter the desired number which you want to convert: "))
        print("The decimal value of", num, "is:")
        print(bin(num), "in binary.")
        print(oct(num), "in octal.")
        print(hex(num), "in hexadecimal.")

    elif choice==2:
        num1   =   int(input("Enter The First Number - "))
        num2   =   int(input("Enter The Second Number - "))

        Add = float(num1 + num2)
        

        print("The Sum is ", Add)

    elif choice==3:
        num1   =   int(input("Enter The First Number - "))
        num2   =   int(input("Enter The Second Number - "))

        Subtract = float(num1 - num2)
        

        print("The Difference is ", Subtract)
    
    elif choice==4:
        num1   =   int(input("Enter The First Number - "))
        num2   =   int(input("Enter The Second Number - "))

        Multiply = float(num1 * num2)
        

        print("The Product is ", Multiply)
    
    elif choice==5:
        num1   =   int(input("Enter The First Number - "))
        num2   =   int(input("Enter The Second Number - "))

        Divide = float(num1 / num2)
        

        print("The Quotient is ", Divide)

    else:
        print("Please enter a valid number ")   

main()