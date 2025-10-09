#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "supersecretkey"  # обычно прячут, но тут просто пример
jwt = JWTManager(app)

# пользователи
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- BASIC AUTH ---
@auth.verify_password
def verify_pw(u, p):
    if u in users and check_password_hash(users[u]["password"], p):
        return users[u]
    return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

# --- JWT LOGIN ---
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 401

    uname = data["username"]
    pwd = data["password"]

    if uname not in users or not check_password_hash(users[uname]["password"], pwd):
        return jsonify({"error": "Invalid username or password"}), 401

    token = create_access_token(identity={"username": uname, "role": users[uname]["role"]})
    return jsonify({"access_token": token}), 200

# --- JWT PROTECTED ROUTE ---
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# --- ADMIN ONLY ROUTE ---
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if not current_user or current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# --- JWT ERROR HANDLERS ---
@jwt.unauthorized_loader
def unauthorized_error(e):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_error(e):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == "__main__":
    app.run()
