from project import main


def uz_pay():
    number = int(input("""Telefon raqamingizni kiriting: 
                +998 _ >>>"""))
    if len(str(number)) != 9:
        print("Xato. Son 7 xonalidan iborat bo'lishi kerak.")
        return uz_pay()
    elif number < 100000000:
        print("Xato. Son 7 xonalidan iborat bo'lishi kerak.")
        return uz_pay()
    else:
        print("Raqam muvvafaqiyatli kiritildi")
        return main()
