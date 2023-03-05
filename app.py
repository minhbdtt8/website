from flask import Flask, render_template, request, session, redirect
import sqlite3
from sqlite3 import Error
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "dn493f983h45983g845h94gh583"
DB_NAME = "identifier.sqlite"


def create_connection(db_file):
    """create a connection to the sqlite db"""
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)

    return None


@app.route('/')
def render_base_page():
        con = create_connection(DB_NAME)
        query = "SELECT id, cat_name FROM categories ORDER BY cat_name ASC"
        cur = con.cursor()  # You need this line next
        cur.execute(query)  # this line actually executes the query
        categories_list = cur.fetchall()  # puts the results into a list usable in python

        return render_template('home.html', categories=categories_list)

@app.route('/addword', methods=['GET', 'POST'])
def render_addword():
    if request.method == 'POST':
        print(request.form)
        Maori = request.form.get('Maori')
        English = request.form.get('English')
        Category = request.form.get('Category')
        Definition = request.form.get('Definition')
        level = request.form.get('level')

        con = create_connection(DB_NAME)
        query = "INSERT INTO vocab(ID, Maori, English, Category, Definition, level, image) VALUES(NULL,?,?,?,?,?,?)"
        cur = con.cursor()  # You need this line next

        cur.execute(query, (Maori, English, Category, Definition, level,))  # this line actually executes the query
        con.commit()
        con.close()
    return render_template('addword.html')

@app.route('/Spa', methods=['GET', 'POST'])
def render_Spa():
    return render_template('Spa.html')

@app.route('/kidschool', methods=['GET', 'POST'])
def render_kidschool():
    return render_template('kidschool.html')

@app.route('/Mapschool', methods=['GET', 'POST'])
def render_Mapschool():
    return render_template('Mapschool.html')

@app.route('/exptworker', methods=['GET', 'POST'])
def render_exptworker():
    return render_template('exptworker.html')

@app.route('/changeStore', methods=['GET', 'POST'])
def render_changeStore():

    return render_template('changeStore.html')

@app.route('/BarOrPub', methods=['GET', 'POST'])
def render_BarOrPub():

    return render_template('BarOrPub.html')





app.run(host='0.0.0.0', debug=True)