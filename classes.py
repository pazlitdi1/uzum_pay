from manage import Database


class Buyurtmalar:
    table_name = "buyurtmalar"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {Buyurtmalar.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
        INSERT INTO buyurtmalar(name)  VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"

        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        if column == "id":
            query = f"DELETE FROM {table} WHERE {column} = {data}"
            return Database.connect(query, "delete")


class PaymentStatus:
    table_name = "payment_status"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {PaymentStatus.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
           INSERT INTO payment_status(name)  VALUES('{self.name}')
           """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"

        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}' "

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        if column == "id":
            query = f"DELETE FROM {table} WHERE {column} = {data}"
            return Database.connect(query, "delete")


class Kartalarim(Buyurtmalar):
    table_name = "kartalarim"

    def __init__(self, name, karta_amal_qilish_muddati):
        Buyurtmalar.__init__(self, name)
        self.srok = karta_amal_qilish_muddati

    @staticmethod
    def select():
        query = f"SELECT * FROM {Kartalarim.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    @staticmethod
    def insert(name, karta_amal_qilish_muddati):
        query = f"""
           INSERT INTO kartalarim_name(name, karta_amal_qilish_muddati)  VALUES('{name}', '{karta_amal_qilish_muddati}')
           """
        return Database.connect(query, "insert")


class Category(Buyurtmalar):
    table_name = "category"
    def __init__(self, name):
        Buyurtmalar.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Category.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
                       INSERT INTO category(name) 
                       VALUES('{self.name}')
                   """
        return Database.connect(query, "insert")


class Person(Buyurtmalar):
    table_name = "person"

    def __init__(self, first_name, last_name, person, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.person = person
        # self.birth_date = birth_date

    @staticmethod
    def select():
        query = f"SELECT * FROM {Person.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
                INSERT INTO person(first_name, last_name, person, password) 
                VALUES('{self.first_name}', '{self.last_name}', '{self.person}', '{self.password}')
            """
        return Database.connect(query, "insert")

    @staticmethod
    def personal_data(person, password):
        query = f"SELECT * FROM {Person.table_name} WHERE person = '{person}' and password = '{password}'"
        return Database.connect(query, "select")


class Store(PaymentStatus):
    table_name = "store"

    @staticmethod
    def select():
        query = f"SELECT * FROM {Store.table_name} ORDER BY id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
                   INSERT INTO store(name)  VALUES('{self.name}')
                   """
        return Database.connect(query, "insert")


class Maxsulotlar(Buyurtmalar):
    table_name = "maxsulotlar"

    def __init__(self, name, description, price, count, serial_number, start_date, end_date, store_id, category_id):
        Buyurtmalar.__init__(self, name)
        self.description = description
        self.price = price
        self.count = count
        self.serial_number = serial_number
        self.start_date = start_date
        self.end_date = end_date
        self.store_id = store_id
        self.category_id = category_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {Maxsulotlar.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
                        INSERT INTO maxsulotlar(name, description, price, count, serial_number, start_date, end_date, store_id, category_id) 
                        VALUES('{self.name}', '{self.description}', {self.price}, {self.count}, {self.serial_number}, '{self.start_date}', '{self.end_date}', {self.store_id}, {self.category_id})
                    """
        return Database.connect(query, "insert")