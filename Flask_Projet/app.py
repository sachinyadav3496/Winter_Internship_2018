from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('one.html')
    #return "Welcome First Web Page Powered by Flask Frame Work <a href='/data'>Data</a>"

@app.route('/data')
def data():

    page = """ 
    <!Doctype html>
    <html>
    <body>
    <h1>YOu are at data page</h1>
    <a href='/'>Home</a>
    </body>
    </html>"""
    
    return page
if __name__ == "__main__" : 

    app.run(host='localhost',port=80,debug=True)
