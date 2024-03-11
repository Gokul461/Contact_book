from tkinter import *
from tkinter import messagebox
import psycopg2
import tkinter.messagebox

def get_data(n,p,a,e):     
    sname  = n
    sphone = p
    saddress = a
    semail = e
    try: 
        conn = psycopg2.connect(dbname ="contact_book",user="postgres",password="gokul",host="localhost",port="5432")
        cur = conn.cursor()
        query = '''insert into book1(name,phone_no,address,email) values (%s,%s,%s,%s);'''
        cur.execute(query,(sname,sphone,saddress,semail))
        print("Successfully inserted!")
        conn.commit()
        conn.close()
        display_all()
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="The Fields must not be empty for insertion")

def del_data(n):
    sid= n
    try:
        conn = psycopg2.connect(dbname='contact_book',user='postgres',password='gokul',host='localhost',port='5432')
        cur = conn.cursor()
        query = '''delete from book1 where Id = (%s);'''
        cur.execute(query,(sid))
        print("Successfully deleted!")
        conn.commit()
        conn.close()    
        display_all()
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="Please provide Id of the contact")
def get_no(n):
    sname = n
    try:
        conn = psycopg2.connect(dbname ="contact_book",user="postgres",password="gokul",host="localhost",port="5432")
        cur = conn.cursor()
        query = '''select name,phone_no,address from book1 where Id = (%s);'''
        cur.execute(query,(sname))
        r = cur.fetchone()
        display(r)
        conn.commit()
        conn.close()
        display_all()
    except:
        tkinter.messagebox.showwarning(title="Warning!",message="Please provide Id fro searching")
def display(r):
    display_box = Listbox(frame,width=30,height=1)
    display_box.grid(row=8,column=1)
    display_box.insert(END,r)
    
def display_all():
    conn = psycopg2.connect(dbname ="contact_book",user="postgres",password="gokul",host="localhost",port="5432")
    cur = conn.cursor()
    query = '''select Id,name,phone_no from book1;'''
    cur.execute(query)
    r = cur.fetchall()
    display_box = Listbox(frame,width=30,height=5)
    display_box.grid(row=5,column=1)
    for i in r:
        display_box.insert(END,i)
    conn.commit()
    conn.close()

def edit(i):
    sid = i
    def change(i):
        conn = psycopg2.connect(dbname='contact_book',user='postgres',password='gokul',host='localhost',port='5432')
        cur = conn.cursor()
        n=entry_n.get(1.0,"end-1c")
        p=entry_p.get(1.0,"end-1c")
        a=entry_a.get(1.0,"end-1c")
        e=entry_e.get(1.0,"end-1c")

        query = '''update book1 set name = (%s),phone_no =(%s),address = (%s),email =(%s) where Id = (%s);'''
        cur.execute(query,(n,p,a,e,sid))   
        print("Successfully edited!")
        conn.commit()
        conn.close()
        root1.destroy()    
        display_all()
    if sid != " ":
        print(sid)
        root1 = Tk()
        root1.resizable(False,False)
        root1.title("Modifier")
        root1.config(bg='gray')
        f1 = Frame(root1)
        f1.pack(side=LEFT)
        root1.geometry("300x400")
        root.resizable(False,False)
        lab = Label(f1,text="Enter name",font=('Arial Black',10))
        lab.pack(pady=3)
        entry_n = Text(f1,width=30,height=1)
        entry_n.pack(pady=10)
        lab = Label(f1,text="Enter Phone number",font=('Arial Black',10))
        lab.pack(pady=3)
        entry_p = Text(f1,width=30,height=1)
        entry_p.pack(pady=10)
        lab = Label(f1,text="Enter Address",font=('Arial Black',10))
        lab.pack(pady=3)
        entry_a = Text(f1,width=30,height=1)
        entry_a.pack(pady=10)
        lab = Label(f1,text="Enter Email Id",font=('Arial Black',10))
        lab.pack(pady=3)
        entry_e = Text(f1,width=30,height=1)
        entry_e.pack(pady=10)
        save = Button(f1,text = "Save",bg='black',fg='white',command = lambda: change(sid))
        save.pack()
        root1.mainloop()

        
root = Tk()
root.title("Contact book")
canvas = Canvas(root,bg='gray10',width=900,height=900)
canvas.grid(row=0,column=0)
root.resizable(False,False)
frame = Frame(canvas,bg='gray10')
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)


label = Label(frame,text="Add data",pady=10,bg='gray10',fg='white',font=('times new roman',20))
label.grid(row = 0,column=1)

label = Label(frame,text="Name",pady=10,padx=5,bg='gray10',fg='white',font=('times new roman',15))
label.grid(row = 1,column=0)

label = Label(frame,text="Phone no",pady=10,padx=5,bg='gray10',fg='white',font=('times new roman',15))
label.grid(row = 2,column=0)

label = Label(frame,text="Email",pady=10,padx=5,bg='gray10',fg='white',font=('times new roman',15))
label.grid(row = 3,column=0)

label = Label(frame,text="Address",pady=10,padx=5,bg='gray10',fg='white',font=('times new roman',15))
label.grid(row = 4,column=0)

entry1 = Entry(frame)
entry1.grid(row=1,column=1)
entry2 = Entry(frame)
entry2.grid(row=2,column=1)
entry3 = Entry(frame)
entry3.grid(row=3,column=1)
entry4 = Entry(frame)
entry4.grid(row=4,column=1)

add= Button(frame,text="Add",width=5,height=1,command= lambda: get_data(entry1.get(),entry2.get(),entry3.get(),entry4.get()))
add.grid(row=4,column=2)

label = Label(frame,text="Search",pady=10,padx=5,bg='gray10',fg='white',font=('Times New Roman',20))
label.grid(row = 6,column=1)

label = Label(frame,text="Enter Id",pady=10,padx=5,bg='gray10',fg='white',font=('Times New Roman',15))
label.grid(row = 7,column=0)

entry = Entry(frame)
entry.grid(row=7,column=1)

display_box = Listbox(frame,width=30,height=5)
display_box.grid(row=5,column=1)

search= Button(frame,text="Search",width=5,height=1,command = lambda: get_no(entry.get()))
search.grid(row=7,column=2)

label = Label(frame,text="update/delete",pady=10,padx=5,bg='gray10',fg='white',font=('Times New Roman',20))
label.grid(row = 9,column=1)

label = Label(frame,text="Enter Id",pady=10,padx=5,bg='gray10',fg='white',font=('Times New Roman',15))
label.grid(row = 10,column=0)

entry5 = Entry(frame)
entry5.grid(row=10,column=1)

upda= Button(frame,text="Update",width=5,height=1,command =lambda: edit(entry5.get()))
upda.grid(row=10,column=2)

dle= Button(frame,text="Delete",width=5,height=1,command=lambda: del_data(entry5.get()))
dle.grid(row=13,column=1)
 
display_all()
root.mainloop()
