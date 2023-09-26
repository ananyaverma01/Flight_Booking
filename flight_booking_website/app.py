import mysql.connector
from flask import Flask,render_template,request

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="flight_db"
)
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        source = request.form.get("from")
        destination= request.form.get("to")
        travellers= request.form.get("passengers")
        date=request.form.get("date")

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM flight_details WHERE source = '"+source+"' AND destination = '"+destination+"'")
        
        myresult = list(mycursor.fetchall())

        for x in range(len(myresult)):
          myresult[x]=list(myresult[x])
          myresult[x][3]=str( myresult[x][3])

        print(source,destination,travellers,date)
        return render_template("index.html", key=True,data=myresult)
    return render_template("index.html", key=False)

if __name__ == "__main__":
    app.run(debug=True)