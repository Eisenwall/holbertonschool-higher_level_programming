#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# тут будем хранить пользователей
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/status")
def status():
    return "OK"

@app.route("/data")
def get_data():
    # просто вернуть имена пользователей
    names = list(users.keys())
    return jsonify(names)

@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    uname = data.get("username")
    if not uname:
        return jsonify({"error": "Username is required"}), 400

    users[uname] = {
        "username": uname,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[uname]
    }), 201

if __name__ == "__main__":
    app.run()
