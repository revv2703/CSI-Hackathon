from flask import Flask, render_template, request
import database
import mysql.connector as cn
import time
# from tabulate import tabulate
import os
app = Flask(__name__)


# INSERT INTO table_listnames (name, address, tele)
# SELECT * FROM (SELECT 'Rupert', 'Somewhere', '022') AS tmp
# WHERE NOT EXISTS (
#     SELECT name FROM table_listnames WHERE name = 'Rupert'
# ) LIMIT 1;

@app.route('/', methods =["GET", "POST"])
def ai():
    user_name="root"
    user_pass="root"
    con=cn.connect(host="localhost",user=user_name,password=user_pass)
    cur=con.cursor()
    if con.is_connected():
        print('Connection established ')
    cur.execute("use truedatabase")
    input_user = request.args.get("input")
    print(input_user)
    # SELECT * FROM trueinfo WHERE (NewsTitle LIKE '%DelhiTransport%')
    tmp_com = f"SELECT * FROM trueinfo WHERE (NewsTitle LIKE '%{input_user}%')"
    cur.execute(tmp_com)
    rec = cur.fetchall()
    if len(rec)==1:
        temp_ret = "True"
    elif len(rec)>1:
        temp_ret = "Prolly True"
    else:
        temp_ret = "False"
    print(temp_ret)
    return render_template("index.html")


app.run(debug=True)

# print(input)

# Writing APIs with python flask and using SQLAlchemy to make database models and fetch data