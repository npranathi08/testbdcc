from flask import *
from flask_mysqldb import MySQL
import pandas


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'people'

mysql = MySQL(app)


@app.route('/')
def Home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM people")
    fetchdata = cur.fetchall()
    cur.close()

    return render_template('home.html',data = fetchdata)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        data = pd.DataFrame(data)
        return render_template('data.html', data=data.to_html(header=False, index=False))



if __name__ == "__main__":
    app.run(debug=True)
