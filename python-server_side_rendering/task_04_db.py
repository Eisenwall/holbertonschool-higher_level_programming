#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import os
import sqlite3

app = Flask(__name__)

# --- File Readers ---
def read_json_file(filepath):
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def read_csv_file(filepath):
    products = []
    if not os.path.exists(filepath):
        return products
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
            except ValueError:
                continue
            products.append(row)
    return products

# --- SQLite Reader ---
def read_sqlite_db(db_path):
    if not os.path.exists(db_path):
        return []
    products = []
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except sqlite3.Error:
        return []
    return products

# --- Flask Route ---
@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products_list = []
    error_msg = None

    if source not in ['json', 'csv', 'sql']:
        error_msg = "Wrong source"
        return render_template('product_display.html', error=error_msg)

    if source == 'json':
        products_list = read_json_file('products.json')
    elif source == 'csv':
        products_list = read_csv_file('products.csv')
    else:
        products_list = read_sqlite_db('products.db')

    # Filter by ID if provided
    if id_param:
        try:
            id_val = int(id_param)
            filtered = [p for p in products_list if p.get('id') == id_val]
            if not filtered:
                error_msg = "Product not found"
                products_list = []
            else:
                products_list = filtered
        except ValueError:
            error_msg = "Invalid id"
            products_list = []

    return render_template('product_display.html', products=products_list, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
