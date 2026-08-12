import psycopg2

from flask import Flask, render_template, redirect

app = Flask(__name__)


def db_conn():
    conn = psycopg2.connect(
        database="startup_db",
        host="localhost",
        port="5432",
        user="postgres",
        password="Ford6000$$$...",
    )
    return conn


@app.route('/')
def index():
    conn=db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM courses''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html',data=data)