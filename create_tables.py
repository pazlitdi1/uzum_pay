from manage import Database


def create_table_pr():
    buyurtmalar = f"""
        CREATE TABLE buyurtmalar(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        create_date TIMESTAMP DEFAULT now());"""

    payment_status = f"""
            CREATE TABLE payment_status(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            create_date TIMESTAMP DEFAULT now());"""

    kartalarim = f"""
            CREATE TABLE kartalarim(
            id SERIAL PRIMARY KEY,
            kartalarim_name VARCHAR(50),
            karta_amal_qilish_muddati VARCHAR(5),   
            create_date TIMESTAMP DEFAULT now())"""

    category = f"""
           CREATE TABLE category(
           id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           create_date TIMESTAMP DEFAULT now());"""

    person = f"""
              CREATE TABLE person(
              id SERIAL PRIMARY KEY,
              first_name VARCHAR(50),
              last_name VARCHAR(50),
              person VARCHAR(50),
              password integer,
              birth_date DATE,
              buyurtmalar INT REFERENCES buyurtmalar(id),
              kartalarim INT REFERENCES kartalarim(id),
              create_date TIMESTAMP DEFAULT now());"""

    store = f"""
             CREATE TABLE store(
             id SERIAL PRIMARY KEY,
             name VARCHAR(50),
             create_date TIMESTAMP DEFAULT now());"""

    maxsulotlar = f"""
           CREATE TABLE maxsulotlar(
           id SERIAL PRIMARY KEY,
           name VARCHAR(100),
           description TEXT,
           price NUMERIC,
           count INTEGER,
           serial_number INTEGER,
           start_date DATE,
           end_date DATE,
           store_id INT REFERENCES store(id),
           category_id INT REFERENCES category(id),
           create_date TIMESTAMP DEFAULT now());"""

    data = {
        "buyurtmalar": buyurtmalar,
        "payment_status": payment_status,
        "kartalarim": kartalarim,
        "category": category,
        "person": person,
        "store": store,
        "maxsulotlar": maxsulotlar

    }
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table_pr()








