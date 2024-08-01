def bmi_calculator(w, h):
    BMI = w * 720 / (h**2)
    return BMI


def BMI():
    w = float(input("Enter person's weight in pounds: "))
    h = float(input("Enter person's height in inches: "))
    BMI = bmi_calculator(w, h)

    print(f"BMI: {round(BMI, 2)}")

    if BMI >= 19 and BMI <= 26:
        print("within healthy range")
    elif BMI > 26:
        print("below healthy range")
    else:
        print("above healthy range")


BMI()
