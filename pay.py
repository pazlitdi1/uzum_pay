import project


def humo_uz():
    print("Humo")
    money = input("Iltimos summani kiriting: ")
    if money.isalnum():
        print("To'lov qabul qilindi")
        return project.main()
    else:
        print("Kechirasiz xatolik yuz berdi !!!")
        return humo_uz()


def uz_card():
    print("UZcard")
    money = input("Iltimos summani kiriting: ")
    if money.isalnum():
        print("To'lov qabul qilindi")
        return project.main()
    else:
        print("Kechirasiz xatolik yuz berdi !!!")
        return uz_card()


def visa_card():
    print("VISA")
    money = input("Iltimos summani kiriting: ")
    if money.isalnum():
        print("To'lov qabul qilindi")
        return project.main()
    else:
        print("Kechirasiz xatolik yuz berdi !!!")
        return visa_card()


def master_card():
    print("Mastercard")
    money = input("Iltimos summani kiriting: ")
    if money.isalnum():
        print("To'lov qabul qilindi")
        return project.main()
    else:
        print("Kechirasiz xatolik yuz berdi !!! ")
        return master_card()
