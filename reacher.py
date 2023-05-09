import psycopg2
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

DB_HOST = "softwarec.cwmrd99bpx4t.us-east-1.rds.amazonaws.com"
DB_NAME = "Group2"
DB_USER = "postgres"
DB_PASS = "null"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()

@app.route('/')
@cross_origin()
def index():
    #response.headers.add('Access-Control-Allow-Origin', '*')
    data = request.get_json()
    fname = data['fname']
    lname = data['lname']
    number = data['number']
    error = check_number(fname, lname, number)  # call your check_number function
    if error:
        return jsonify({'error': error})
    else:
        # do something with the data (e.g. save to a database)
        return jsonify({'success': 1})
    

def check_number(fname, lname, number):
    try:
        cur.execute("INSERT INTO ClientData (FirstName, LastName, SpecialNumber) VALUES (%s, %s, %s)",
                    (fname, lname, number))
        conn.commit()
        return None
    except Exception as e:
        print("Error: ", e)
        conn.rollback()
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
