import pymysql  as sql

db = sql.connect(host='localhost',port=3306,user='bank_app',password='redhat',database='bank_app')

c = db.cursor()

f = open('bank_data.csv')
data = []
for line in f :
    d = line.split(',')
    d[2] = float(d[2][:-1])
    data.append(d)
    
f.close()
for var in data :
    name = var[0]
    password = var[1]
    bal = var[2]
    cmd = "insert into bank(user,password,bal) values('{}','{}',{})".format(name,password,bal)
    c.execute(cmd)
    
db.commit()
print("Added data to bank sucessfully")
c.close()
db.close()


