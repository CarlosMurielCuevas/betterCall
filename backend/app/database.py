import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="mi_bd",
        user="tu_usuario",
        password="tu_contraseña"
    )
    return conn
