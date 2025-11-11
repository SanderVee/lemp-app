from flask import Flask, render_template, url_for
import os
from dotenv import load_dotenv
load_dotenv()
import mysql.connector

app = Flask(__name__, template_folder="Linux-sivu")

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password=os.getenv("DB_PASSWORD")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    time = cursor.fetchone()[0]
    conn.close()

    return render_template("index.html", time=time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
