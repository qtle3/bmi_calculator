def bmi_calculator(w, h):
    # Calculate BMI
    BMI = w * 703 / (h**2)
    return BMI


def BMI():
    # Get user input
    w = float(input("Enter person's weight in pounds: "))
    h = float(input("Enter person's height in inches: "))
    BMI = bmi_calculator(w, h)

    # Print BMI
    print(f"BMI: {round(BMI, 2)}")

    # Determine if BMI is within healthy range
    if BMI >= 19 and BMI <= 26:
        print("within healthy range")
    elif BMI < 26:
        print("below healthy range")
    else:
        print("above healthy range")


BMI()
