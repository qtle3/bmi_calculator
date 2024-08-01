def BMI():
    w = float(input("Enter person's weight in pounds: "))
    h = float(input("Enter person's height in inches: "))
    BMI = w * 720 / (h**2)

    if BMI >= 19 and BMI <= 26:
        print(round(BMI, 2))
        print("within healthy range")
    elif BMI > 26:
        print(round(BMI, 2))
        print("below healthy range")
    else:
        print(round(BMI, 2))
        print("above healthy range")


BMI()
