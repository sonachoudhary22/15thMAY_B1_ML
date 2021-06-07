import tkinter as tk
import sqlite3
db = sqlite3.connect('mydb_1.sqlite')
print(db)
app = tk.Tk()
app.title('Basic Calculator')
app.geometry('300x400')

val = tk.Variable(app)
db1=tk.Variable(app)
display = tk.Label(app,width=30, height=4, bg='#fff', textvariable=val);
display.pack()

count = 0
calculated = False

def calculate():
    global count
    global calculated
    global db
    calculated = True
    count += 1
    expression = val.get()
    result = float(eval(expression))
    db.execute('insert into calc_history (id, expression, result) values ({},"{}",{})'.format(count,expression,result))
    db.commit()    
    val.set(str(eval(expression)))    

def typing(v):
    global calculated
    val.set(val.get()+v)

def clear():
    val.set('')

def read_data():
    global db
##    db = sqlite3.connect('mydb.sqlite')
    print("Connected to SQLite")
    r=db.execute('''SELECT *from calc_history''')
    print(r)
    result = r.fetchall();
    print("Total rows are:  ", len(result))
    print("Printing each row")
    for row in result:
            print("Id: ", row[0])
            print("Expression: ", row[1])
            print("Result: ", row[2])
            print("\n")
##    db.close()

#read_data()

tk.Button(app,text='7',width=4, height = 2,command=lambda:typing('7')).place(x=50,y=100)
tk.Button(app,text='8',width=4, height = 2,command=lambda:typing('8')).place(x=100,y=100)
tk.Button(app,text='9',width=4, height = 2,command=lambda:typing('9')).place(x=150,y=100)
tk.Button(app,text='+',width=4, height = 2,command=lambda:typing('+')).place(x=200,y=100)
tk.Button(app,text='4',width=4, height = 2,command=lambda:typing('4')).place(x=50,y=150)
tk.Button(app,text='5',width=4, height = 2,command=lambda:typing('5')).place(x=100,y=150)
tk.Button(app,text='6',width=4, height = 2,command=lambda:typing('6')).place(x=150,y=150)
tk.Button(app,text='-',width=4, height = 2,command=lambda:typing('-')).place(x=200,y=150)
tk.Button(app,text='1',width=4, height = 2,command=lambda:typing('1')).place(x=50,y=200)
tk.Button(app,text='2',width=4, height = 2,command=lambda:typing('2')).place(x=100,y=200)
tk.Button(app,text='3',width=4, height = 2,command=lambda:typing('3')).place(x=150,y=200)
tk.Button(app,text='x',width=4, height = 2,command=lambda:typing('*')).place(x=200,y=200)
tk.Button(app,text='CE',width=4, height = 2,command=clear).place(x=50,y=250)
tk.Button(app,text='0',width=4, height = 2,command=lambda:typing('0')).place(x=100,y=250)
tk.Button(app,text='=',width=4, height = 2,command=calculate).place(x=150,y=250)
tk.Button(app,text='/',width=4, height = 2,command=lambda:typing('/')).place(x=200,y=250)  
tk.Button(app,text='His',width=6, height = 2,command=read_data).place(x=120,y=300)


app.mainloop()
