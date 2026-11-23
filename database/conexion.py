import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Samuel_123$",          # <-- cambia por tu contraseña de MySQL
    "database": "tinajones_db",
    "use_pure": True,
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
