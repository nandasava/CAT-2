from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "obituary_platform"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        date_of_death = request.form['date_of_death']
        content = request.form['content']
        author = request.form['author']

        cur = mysql.connection.cursor()
        query = """
            INSERT INTO obituaries (name, date_of_birth, date_of_death, content, author) 
            VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(query, (name, date_of_birth, date_of_death, content, author))
        mysql.connection.commit()
        cur.close()

        return ('obituaries_list','successfully submitted')  # Redirect to obituaries list
    return render_template('obituary_form.html')

@app.route('/obituaries_list')
def obituaries_list():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM obituaries"
    cur.execute(query)
    obituaries = cur.fetchall()
    cur.close()
    results=["#"]
    return render_template('obituaries_list.html', obituaries=obituaries, results=results)

if __name__ == '__main__':
    app.run(debug=True)
