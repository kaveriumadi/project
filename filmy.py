import sqlite3
from flask import Flask, request
from flask import jsonify

app = Flask(__name__)
app.config[""] = "sqlite3:///C:/Users\KAVU/eclipse-workspace/practice3/justpractice/filmy.db"


conn = sqlite3.connect('filmy.db')

def commit(conn):
    print('db_commit() ...')
    #import pdb
    #pdb.set_trace()
    conn.commit()
    
def init_db(conn):
    print('init_db() ...')
    cur = conn.cursor()
    return cur

def close_db(conn):
    print('close_db() ...')
    conn.close()
    
@app.route('/cur')   
def create_table(cur):
    print('create_table() ...')
    cur.execute("""DROP TABLE IF EXISTS Film""")
    cur.execute("""CREATE TABLE Film
            (name text, heroine text,year integer, hero text)""")
    
@app.route('/records', methods=['POST'])
def post_recs():
    print('post_recs() ...')
    
    payload = request.json
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()

    for i in payload:
        cur.execute("""INSERT INTO Film VALUES (?,?,?,?)""",
                    (i['year'], i['heroine'], i['name'], i['hero']))
 
    commit(conn) 
    return 'success'

@app.route('/fetch_alls', methods=['GET'])
def fetch_recs():
    print('fetch_recs() ...')
    #payload = request.json
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()
    #import pdb;pdb.set_trace()
    sql1 = 'SELECT * FROM Film' 
    cur.execute(sql1)
    recs = cur.fetchall()
    
    print(recs)
    
    return jsonify(recs) 

@app.route('/fetch_one/<int:year>', methods=['GET'])
def fetch_rec(year):
    print('fetch_recs() ...')
    #payload = request.json
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()
    #import pdb;pdb.set_trace()
     
    sql1 = f"SELECT * FROM Film where year={year}" 
    cur.execute(sql1)
    recs = cur.fetchall()
    
    print(recs)
    
    return jsonify(recs)

@app.route('/update_recs/<int:year>', methods=['PUT'])    
def update_rec(year):
    print("update records")
    
    payload = request.json
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()
    #import pdb;pdb.set_trace()
    for i in payload:
        #import pdb;pdb.set_trace()
        var = f"update Film set name=\'{i['name']}\', heroine=\'{i['heroine']}\', hero=\'{i['hero']}\' where year={i['year']}"
        cur.execute(var)
      
    print("updated")
    commit(conn) 
    return 'success'

@app.route('/recs_all', methods=['PUT'])    
def update_recs():
    print("update records")
    payload = request.json
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()
    
    for i in payload:
        var = f"update Film set name=\'{i['name']}\', heroine=\{i['heroine']}\, hero=\'{i['hero']}\' where year={i['year']}"
        cur.execute(var)
      
    print("updated")
    commit(conn) 
    return 'success'

@app.route('/rec/<int:year>', methods=['PUT'])    
def update_single_rec(year):
    payload = request.json
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()
    for i in payload:
        #import pdb;pdb.set_trace()
        var = f"UPDATE Film set heroine={i['heroine']}, hero=\'{i['hero']}\'where year={i['year']}"
        cur.execute(var)
    commit(conn)
    
    return 'success', 200


@app.route('/record/<int:year>', methods=['DELETE'])    
def delete_rec(year):
    print("delete records")
    conn = sqlite3.connect('filmy.db')
    cur = conn.cursor()

    sql = f'DELETE from  Film WHERE year={year}'
    cur.execute(sql)
    commit(conn) 
    return 'success'

    
    
if __name__ == '__main__':   
        app.run(debug=True)

