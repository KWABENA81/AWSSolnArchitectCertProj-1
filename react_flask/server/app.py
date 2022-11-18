from os import environ

import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config.from_pyfile('config.py')
app.config.from_object('config.Config')


def get_db_connection():
    conn = psycopg2.connect(
        host='172.23.0.2',
        database='data_db',
        user='postgres',
        password='password')
    return conn


# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('postgresql://postgres:password@172.21.0.2/data_db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@172.21.0.2/data_db'
db = SQLAlchemy(app)


class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


def __init__(self, name, city, addr, pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', students=students)


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        if name == '':
            name = 'John Doe'
        city = request.form['city']
        if city == '':
            city = 'John City'
        addr = request.form['addr']
        if addr == '':
            addr = '2789 John Blvd'
        pin = request.form['pin']
        if pin == '':
            pin = '02145'

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO students (name, city, addr, pin)'
                    ' VALUES (%s, %s, %s, %s)',
                    (name.capitalize(), city.capitalize(), addr.capitalize(), pin.capitalize()))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')


if __name__ == '__main__':
    #   db.create_all()
    app.run(debug=True)
