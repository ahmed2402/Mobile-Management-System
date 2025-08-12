from flask import Blueprint, request, jsonify
import mysql.connector
from config import DB_CONFIG

sales_bp = Blueprint('sales', __name__)

# Helper function to get DB connection
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# GET all sales
@sales_bp.route("/", methods=["GET"])
def get_sales():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT s.sale_id, i.name AS item_name, s.quantity, s.sale_price, 
                   s.profit, s.payment_method, s.sale_date
            FROM sales s
            JOIN items i ON s.item_id = i.item_id
            ORDER BY s.sale_date DESC;
        """
        cursor.execute(query)
        sales = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(sales), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST - Add a new sale
@sales_bp.route("/", methods=["POST"])
def add_sale():
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO sales (item_id, quantity, sale_price, profit, payment_method, sale_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data["item_id"],
            data["quantity"],
            data["sale_price"],
            data["profit"],  # calculated from frontend
            data["payment_method"],
            data["sale_date"]
        ))

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Sale added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE - Remove a sale
@sales_bp.route("/<int:sale_id>", methods=["DELETE"])
def delete_sale(sale_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sales WHERE sale_id = %s", (sale_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Sale deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT - Update a sale
@sales_bp.route("/<int:sale_id>", methods=["PUT"])
def update_sale(sale_id):
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            UPDATE sales
            SET item_id = %s,
                quantity = %s,
                sale_price = %s,
                profit = %s,
                payment_method = %s,
                sale_date = %s
            WHERE sale_id = %s
        """
        cursor.execute(query, (
            data["item_id"],
            data["quantity"],
            data["sale_price"],
            data["profit"],  # still coming from frontend
            data["payment_method"],
            data["sale_date"],
            sale_id
        ))

        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Sale updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

