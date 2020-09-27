
restart = ('y')

while restart == 'y':
    print("Welcome, Create any Triangle pattern of your choice \n")
    n = int(input("Enter the number of rows : "))
    print("\nChoose Your Pattern Shape")
    print("\nPress 1 for Left Triangle patterns")
    print("Press 2 for Right Triangle patterns")
    print("Press 3 for Downward Left Triangle patterns")
    print("Press 4 for Downward Right Triangle patterns")

    option = int(input("Enter Your Choice : "))

    if option == 1:
        print("\nChoose Your Pattern Type")
        print("\nPress 1 for Star")
        print("Press 2 for Number")
        print("Press 3 for Alphabet")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            print("\nLeft Triangle Star Pattern")
            for i in range(0, n):
                for j in range(0, i + 1):
                    print("*", end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice == 2:
            print("\nLeft Triangle Number Pattern")
            x = 0
            for i in range(0, n):
                x += 1
                for j in range(0, i + 1):
                    print(x, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice == 3:
            print("\nLeft Triangle Alphabet Pattern")
            x = 65
            for i in range(0, n):
                ch = chr(x)
                x += 1
                for j in range(0, i + 1):
                    print(ch, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        else:
            print("Invalid Option \n")
            restart = ('y')

    elif option == 2:
        print("\nChoose Your Pattern Type")
        print("\nPress 1 for Star")
        print("Press 2 for Number")
        print("Press 3 for Alphabet")

        choice_2 = int(input("Enter your choice : "))

        if choice_2 == 1:
            print("\nRight Triangle Star Pattern")
            k = 2 * n - 2
            for i in range(0, n):
                for j in range(0, k):
                    print(end=" ")
                k = k - 2
                for j in range(0, i + 1):
                    print("*", end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice_2 == 2:
            print("\nRight Triangle Number Pattern")
            k = 2 * n - 2
            x = 0
            for i in range(0, n):
                x += 1
                for j in range(0, k):
                    print(end=" ")
                k = k - 2
                for j in range(0, i + 1):
                    print(x, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice_2 == 3:
            print("\nRight Triangle Alphabet Pattern")
            k = 2 * n - 2
            x = 65
            for i in range(0, n):
                ch = chr(x)
                x += 1
                for j in range(0, k):
                    print(end=" ")
                k = k - 2
                for j in range(0, i + 1):
                    print(ch, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        else:
            print("Invalid Option \n")
            restart = ('y')

    elif option == 3:
        print("\nChoose Your Pattern Type")
        print("\nPress 1 for Star")
        print("Press 2 for Number")
        print("Press 3 for Alphabet")

        choice_3 = int(input("Enter your choice : "))

        if choice_3 == 1:
            print("\nLeft Triangle Star Inverted Pattern")
            for i in range(n-1, -1, -1):
                for j in range(0, i + 1):
                    print("*", end=" ")
                print("\r")

            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice_3 == 2:
            print("\nLeft Triangle Number Inverted Pattern")
            x = 0
            for i in range(n-1, -1, -1):
                x += 1
                for j in range(0, i + 1):
                    print(x, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice_3 == 3:
            print("\nLeft Triangle Alphabet Inverted Pattern")
            x = 65
            for i in range(n-1, -1, -1):

                ch = chr(x)
                x += 1
                for j in range(0, i + 1):
                    print(ch, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        else:
            print("Invalid Option \n")
            restart = ('y')

    elif option == 4:
        print("\nChoose Your Pattern Type")
        print("\nPress 1 for Star")
        print("Press 2 for Number")
        print("Press 3 for Alphabet")

        choice_4 = int(input("Enter your choice : "))

        if choice_4 == 1:
            print("\nRight Triangle Star Inverted Pattern")
            k = 2 * n - 2
            for i in range(n-1, -1, -1):
                for j in range(k, 0, -1):
                    print(end=" ")
                k = k + 2
                for j in range(0, i + 1):
                    print("*", end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice_4 == 2:
            print("\nRight Triangle Number Inverted Pattern")
            k = 2 * n - 2
            x = 0
            for i in range(n-1, -1, -1):
                x += 1
                for j in range(k, 0, -1):
                    print(end=" ")
                k = k + 2
                for j in range(0, i + 1):
                    print(x, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        elif choice_4 == 3:
            print("\nRight Triangle Alphabet Inverted Pattern")
            k = 2 * n - 2
            x = 65
            for i in range(n-1, -1, -1):
                ch = chr(x)
                x += 1
                for j in range(k, 0, -1):
                    print(end=" ")
                k = k + 2
                for j in range(0, i + 1):
                    print(ch, end=" ")
                print("\r")
            restart = input("\nPress y to restart : ").lower()
            print("\n")
            if restart != 'y':
                print("Thank you!!!")
                break

        else:
            print("Invalid Option \n")
            restart = ('y')

    else:
        print("Invalid Option \n")
        restart = ('y')