from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import random
from bd import *



app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'urlshort'

@app.route('/')
def index():
    return render_template('mainpage.html')


@app.route('/links')
def get():
    conn = mysql.connect()
    cursor = conn.cursor()
    linkss = getlinks(cursor)
    cursor.close()
    conn.close()
    return render_template('registrado.html', links=linkss)


@app.route('/registrar', methods=['POST'])
def inserir():
    if request.method == 'POST':
        link1= request.form.get('link1')
        link2 = random.randint(000000, 999999)
        conn =mysql.connect()
        cursor = conn.cursor()
        usuario(cursor, conn, link1, link2)
        conn.close()
        cursor.close()

        return redirect(url_for('get'))

    else:
        return render_template('mainpage.html')


if __name__ == '__main__':
    app.run(debug=True)