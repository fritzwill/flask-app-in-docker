from flask import Flask, render_template
# include request above if you want request methods
# include render_template above
# from werkzeug.contrib.fixers import ProxyFix
import psycopg2

app = Flask(__name__)
app.config['DEBUG'] = True # reload server on code change

# postgress (database) config
DB_USER = 'postgres'
DB_PASS = 'password'
DB_NAME = 'postgres'
DB_HOST = 'db'
#DB_PORT = '5432'

conn = psycopg2.connect("dbname='{}' user='{}' password='{}' host='{}'".format(DB_NAME, DB_USER, DB_PASS, DB_HOST))
cur = conn.cursor()

# Create table if not already made
cur.execute("CREATE TABLE IF NOT EXISTS users ("
	"id          INT PRIMARY KEY     NOT NULL, "
    "username    varchar(255)    NOT NULL, "
    "firstname   varchar(255)    NULL, " 
    "lastname    varchar(255)    NULL);")

# Routes
@app.route('/')
def index():
	return "Flask Dockerized"

##### REQUEST METHODS #####
# @app.route("/")
# def index():
# 	return "Method used: %s" % request.method

# @app.route(".bacon", methods=['GET', 'POST'])
# def bacon():
# 	if request.method == 'POST':
# 		return "You are using POST"
# 	else:
# 		return "Yodocker rmi $(docker images -a -q)u are probably using GET"

##### HTML TEMPLATES #####
@app.route('/<name>')
def profile(name):
	return render_template("profile.html", name=name)

##### PASSSING OBJECTS #####
# @app.route("/shopping")
# def shpping():
# 	food = ["Cheese", "Tuna", "Beef"]
# 	return render_template("shopping.html", food=food)

@app.route('/adduser')
def adduser():
	cur.execute("INSERT INTO users (id, username, firstname, lastname) VALUES (1, 'willfritz', 'Will', 'Fritz');")
	return "Added User"

@app.route('/users')
def users():
	cur.execute("SELECT * FROM users;")
	results = cur.fetchone()
	print type(results)
	return results

if __name__ == "__main__":
	app.run(host='0.0.0.0')
