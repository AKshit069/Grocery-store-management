from flask import Flask, jsonify, request
from products_dao import get_sql_connection
import products_dao
import uom_dao
import json
import orders_dao

app = Flask(__name__)

@app.route('/getProducts', methods=['GET'])
def get_products():
    print("get_products() was called")  # Debugging statement
    try:
        connection = products_dao.get_sql_connection()
        products = products_dao.get_all_products(connection)
        response = jsonify(products)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/getUOM', methods=['GET'])
def get_uom():
    print("get_uom() was called")  # Debugging statement
    try:
        connection = products_dao.get_sql_connection()
        response = uom_dao.get_uoms(connection)
        print(response)
        response = jsonify(response)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    try:
        request_payload = json.loads(request.form['data'])  # Load JSON payload from form data
        connection = products_dao.get_sql_connection()  # Ensure the connection is established
        product_id = products_dao.insert_new_product(connection, request_payload)
        response = jsonify({
            'product_id': product_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    try:
        connection = products_dao.get_sql_connection()  # Ensure the SQL connection is established
        product_id = request.form['product_id']  # Get the product_id from the request
        return_id = products_dao.delete_product(connection, product_id)
        response = jsonify({
            'product_id': return_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    try:       
        request_payload = json.loads(request.form['data'])      
        connection = products_dao.get_sql_connection()        
        order_id = orders_dao.insert_order(connection, request_payload)       
        response = jsonify({
            'order_id': order_id
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        
        return jsonify({"error": str(e)}), 500

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    try:  
        connection = products_dao.get_sql_connection()   
        orders = orders_dao.get_all_orders(connection)

        response = jsonify(orders)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        # Return error message in case of any issues
        return jsonify({"error": str(e)}), 500







if __name__ == "__main__":
    print("Starting Python Flask Server for Grocery Store Management System")
    app.run(port=5000, debug=True)
