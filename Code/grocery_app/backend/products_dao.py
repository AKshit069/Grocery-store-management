import pymysql
import os

def get_sql_connection():
    try:
        user = os.environ.get('DB_USER', 'root')
        password = os.environ.get('DB_PASSWORD', 'Akshit_123')
        host = os.environ.get('DB_HOST', '127.0.0.1')
        database = os.environ.get('DB_DATABASE', 'gs')
        port = int(os.environ.get('DB_PORT', 3306))

        cnx = pymysql.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            port=port
        )
        return cnx
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def get_all_products(connection):
    connection = get_sql_connection()  # Use the global connection
    cursor = connection.cursor()

    query = ("SELECT products.product_id, products.name, products.uom_id,products.price_per_unit, uom.uom_name FROM products inner join uom on uom.uom_id =products.uom_id")
    cursor.execute(query)

    response = []
    for row in cursor:
        print(row)  # Print each row to verify what you are getting

        (product_id, name, uom_id, price_per_unit, uom_name) = row  # Ensure these match the table schema

        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name':uom_name
            # If uom_name is not a column in your table, remove this line
        })

    cursor.close()  # Close the cursor
    connection.close()  # Close the connection
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()

    query = "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid 

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid
 

if __name__ == '__main__':    
    connection = get_sql_connection()  # This should be outside of the function
    print(delete_product(connection, 35))


