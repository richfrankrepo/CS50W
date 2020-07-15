while True:
    try:
        n = int(input("number: "))
    except ValueError:
        print("You twat, you didn't enter a number!")
        continue
    else:
        if n>0:
            print("n is positive")
        elif n<0:
            print("n is negative")
        else:
            print("n is equal to zero")
        break
    