#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

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

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    products_list = []
    error_msg = None

    if source not in ['json', 'csv']:
        error_msg = "Wrong source"
        return render_template('product_display.html', error=error_msg)

    if source == 'json':
        products_list = read_json_file('products.json')
    else:
        products_list = read_csv_file('products.csv')

    # Filter by id if provided
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
