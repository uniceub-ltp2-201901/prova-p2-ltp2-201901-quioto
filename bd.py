def db(mysql):

    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

def getlinks(cursor):

    cursor.execute('select link1, link2 from urlshort.urlbatata1')


    links = cursor.fetchall()


    return links


def usuario(cursor, conn, link1, link2):
    cursor.execute(f'insert into urlshort.urlbatata1 (link1, link2) values("{link1}", "{link2}")')
    conn.commit()