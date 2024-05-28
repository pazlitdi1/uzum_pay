from classes import Buyurtmalar, PaymentStatus, Kartalarim, Category, Person, Store, Maxsulotlar
from manage import Check
import state
import kiyimlar, mayshiy_texnika


def buyurtmalar_table():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>>>""")
    if services == "1":
        print(Buyurtmalar.select())
        back = input("""
            0. Back
                >>>>""")
        if back == "0":
            return main()
        else:
            print("Error")
            return buyurtmalar_table()

    elif services == "2":
        name = input("Name: ")
        country = Buyurtmalar(name)
        print(country.insert())
        return buyurtmalar_table()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data:")
        new_data = input("New data:")
        print(Buyurtmalar.update(column, new_data, old_data, "country"))
        return buyurtmalar_table()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Buyurtmalar.delete(column, data, "country"))
        return buyurtmalar_table()

    else:
        print("Error please !!!")
        return buyurtmalar_table()


def payment_status_table():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>>>""")
    if services == "1":
        print(PaymentStatus.select())
        back = input("""
            0. Back
                >>>>""")
        if back == "0":
            return main()
        else:
            print("Error")
            return payment_status_table()

    elif services == "2":
        name = input("Name: ")
        payment_status = PaymentStatus(name)
        print(payment_status.insert())
        return payment_status_table()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data:")
        new_data = input("New data:")
        print(PaymentStatus.update(column, new_data, old_data, "payment_status"))
        return payment_status_table()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(PaymentStatus.delete(column, data, "payment_status"))
        return payment_status_table()

    else:
        print("Error please !!!")
        return payment_status_table()


def kartalarim_table():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
            >>>>""")
    if services == "1":
        print(Kartalarim.select())
        back = input("""
            0. Back
                >>>>""")
        if back == "0":
            return kartalarim_table()
        else:
            print("Error")
            return kartalarim_table()

    elif services == "2":
        name = input("Name: ")
        karta_amal_qilish_muddati = input("Karta amal qilish muddattini kiriting: ")
        print(Kartalarim.insert(name, karta_amal_qilish_muddati))
        return kartalarim_table()


def category_tables():
    services = input("""
            1. Select
            2. Insert
            3. Update
            4. Delete
                >>>>""")
    if services == "1":
        print(Store.select())
        back = input("""
                0. Back
                    >>>>""")
        if back == "0":
            return main()
        else:
            print("Error")
            return store_table()

    elif services == "2":
        name = input("Name: ")
        store = Store(name,)
        print(store.insert())
        return store_table()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data:")
        new_data = input("New data:")
        print(Category.update(column, new_data, old_data, "category"))
        return category_tables()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Category.delete(column, data, "category"))
        return category_tables()

    else:
        print("Error please !!!")
        return category_tables()


def person_table():
    services = input("""
                1. Select
                2. Insert
                3. Update
                4. Delete
                    >>>>""")
    if services == "1":
        print(Person.select())
        back = input("""
                    0. Back
                        >>>>""")
        if back == "0":
            return main()
        else:
            print("Error")
            return person_table()

    elif services == "2":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        birth_date = input("Birth date: ")
        address_id = input("Address ID: ")
        person = Person(first_name, last_name, birth_date, address_id)
        print(person.insert())
        return person_table()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data:")
        new_data = input("New data:")
        print(Person.update(column, new_data, old_data, "customers"))
        return person_table()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Person.delete(column, data, "customers"))
        return person_table()


def store_table():
    services = input("""
                1. Select
                2. Insert
                3. Update
                4. Delete
                    >>>>""")
    if services == "1":
        print(Store.select())
        back = input("""
                    0. Back
                        >>>>""")
        if back == "0":
            return store_table()
        else:
            print("Error")
            return store_table()

    elif services == "2":
        name = input("Name: ")
        store = Store(name)
        print(store.insert())
        return store_table()

    elif services == "3":
        column = input("Column name: ")
        old_data = input("Old data:")
        new_data = input("New data:")
        print(Store.update(column, new_data, old_data, " store"))
        return store_table()

    elif services == "4":
        column = input("Column name: ")
        data = input("Data: ")
        print(Store.delete(column, data, " store"))
        return store_table()

    else:
        print("Error please !!!")
        return store_table()


def maxsulotlar_table():
    services = input("""
            1.Select
            2.Insert
            3.Update
            4.Delete
                >>>>""")

    if services == "1":
        print(Maxsulotlar.select())
        back = input("""
                0. Back
                    >>>> """)
        if back == "0":
            return main()

    elif services == "2":
        name = input("Product name: ")
        description = input("Product description: ")
        price = float(input("Product price: "))
        count = int(input("Product count: "))
        serial_number = input("Product serial number: ")
        start_date = input("Product start date (YYYY-MM-DD): ")
        end_date = input("Product end date (YYYY-MM-DD): ")
        store_id = int(input("Store ID: "))
        category_id = int(input("Category ID: "))
        product = Maxsulotlar(name, description, price, count, serial_number, start_date, end_date, store_id, category_id)
        print(product.insert())

        return maxsulotlar_table()

    elif services == "3":
        old_name = input("Old product name: ")
        new_name = input("New product name: ")
        new_description = input("New product description: ")
        new_price = float(input("New product price: "))
        new_count = int(input("New product count: "))
        new_serial_number = input("New product serial number: ")
        new_start_date = input("New product start date (YYYY-MM-DD): ")
        new_end_date = input("New product end date (YYYY-MM-DD): ")
        new_store_id = int(input("New store ID: "))
        new_category_id = int(input("New category ID: "))
        product = Maxsulotlar(old_name, None, None, None, None, None, None, None, None)
        print(product.update(new_name, new_description, new_price, new_count, new_serial_number, new_start_date,
                             new_end_date, new_store_id, new_category_id))
        return maxsulotlar_table()

    elif services == "4":
        name = input("Product name: ")
        product = Maxsulotlar(name, None, None, None, None, None, None, None, None)
        print(product.delete())
        return maxsulotlar_table()

    else:
        print("Invalid input")
        return maxsulotlar_table()


def toplamlar():
    print("O'zingizga yoqgan to'plamni tanlang")
    print("Iltimos")
    tovar = input("""
    1. Kiyimlar 
    2. Mayshiy texnika
    3. Bolalar uchun kiyimlar
    4. Kitoblar
    5. Sport uchun maxsulotlar
    6. Aksesuarlar
            >>>>""")

    if tovar == "1":
        kiyimlar.brend()

    elif tovar == "2":
        mayshiy_texnika.mayshiy_brend()

    elif tovar == "3":
        pass

    elif tovar == "4":
        pass

    elif tovar == "5":
        pass

    elif tovar == "6":
        pass

    else:
        print("Kechirasiz xatolik yuz berdi !!!")
        print("Qayta urunib koring")
        return toplamlar()


def main():
    tables = input("""
    1. Buyurtmalar 
    2. Payment Status 
    3. Kartalarim 
    4. Category
    5. Person 
    6. Store 
    7. Maxsulotlar
    8.To'lov qilish
                >>>>""")
    if tables == "1":
        return buyurtmalar_table()

    elif tables == "2":
        return payment_status_table()

    elif tables == "3":
        return kartalarim_table()

    elif tables == "4":
        return category_tables()

    elif tables == "5":
        return person_table()

    elif tables == "6":
        return store_table()

    elif tables == "7":
        return maxsulotlar_table()

    elif tables == "8":
        toplamlar()

    else:
        print("Kechirasiz xatolik yuz berdi !!! ")
        print("ILtimos qayta urunib ko'ring ")
        return main()


def login():
    username = input("Username: ")
    password = input("Password: ")
    if Check.login_check(username, password):
        return main()
    else:
        print(" Kechirasiz username yoki password noto'g'ri")
        return login()


def register():
    print("Korzinka sahifaga otish uchun malumotlarni kiriting !!!")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    person = input("Username: ")
    password_1 = input("Password: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        print("Passwordlar mos kelmadi!")
        password_1 = input("Password: ")
        password_2 = input("Reply Password: ")

    new_person = Person(first_name, last_name, person, password_1)
    print(new_person.insert())
    return state.countries()


def intro():
    print("<<<<Korzinka>>>>")
    user = input(""""
    1. Login
    2. Register 
            >>>""")
    if user == "1":
        login()

    elif user == "2":
        register()

    else:
        print("Kechirasiz xatolik yuz berdi !!!")
        return intro()


if __name__ == "__main__":
    intro()
