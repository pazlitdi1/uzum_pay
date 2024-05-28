import psycopg2 as psql


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database='real_project',
            user='postgres',
            password='Mansur777',
            host='localhost',
            port=5432,
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ['create', 'delete', 'update', 'insert', 'alter']
        db.commit()
        if query_type in data:
            if query_type == "create":
                return f"created successfully"
            return f"{query_type} query successfully"
        else:
            return cursor.fetchall()


class Check:
    @staticmethod
    def login_check(person, password):
        query = f"SELECT * FROM person WHERE person = '{person}' and password = '{password}'"
        data = Database.connect(query, "select")
        if len(data) >= 1:
            return True

        else:
            return False


def add_column():
    # query_1 = "ALTER TABLE customers ADD COLUMN username VARCHAR(20)"
    # query_2 = "ALTER TABLE customers ADD COLUMN password VARCHAR(20)"
    # Database.connect(query_1, "alter")
    # Database.connect(query_2, "alter")

    query = f"""
            INSERT INTO customers(first_name, last_name, username, password, birth_date) 
            VALUES('Farzona', 'Shamsiyeva', 'ferzii', 'ferzina', '2008-07-02')"""
    return Database.connect(query, "insert")

# if __name__ == "__main__":
#     print(add_column())


if __name__ == '__main__':
    add_column()
