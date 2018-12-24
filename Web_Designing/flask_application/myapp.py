from flask import Flask,render_template,request 
import pymysql as sql 

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hi')
@app.route('/hi/<string:name>')
def hi(name=None):
    return render_template('hello.html',name=name)

@app.route('/login',methods=['GET','POST'])
def login():
	db = sql.connect(host='localhost',port=3306,user='root',password='',database='grras')
	c = db.cursor()
	name = request.form['username']
	password = request.form['password']
	cmd = "select * from user where name='{}' and password='{}'".format(name,password)
	c.execute(cmd)
	data = c.fetchone()

	if data : 
		info = {
			'Name' : data[0],
			'First Name' :data[2],
			'Last Name' : data[3],
			'Email'  : data[4],
			'Phone Number' : data[5],
			}
		return render_template('data.html',info=info)
	else :
		return f"""<h1 style='color:red'>Erorr!! Invalid User or Password</h1>
		<a href='/'>Home</a>""" 

if __name__ == "__main__" : 

    app.run(host='localhost',port=80,debug=True)
