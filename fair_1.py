#pip install PyMySQL
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
#import tkinter as tk

#connection Later
def connection():
    conn=mysql.connect(host="localhost",user="root",password="Pass@1234",port="3306",database="student_db")
    return conn
def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    for array in read():
        my_tree.insert (parent='', index=' end', iid=array, text="", values=(array), tag="orow")
        
    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0,columnspan=5, rowspan=11, padx=10, pady=20)

#gui
root = Tk()
root.title("Student Registration System")
root. geometry("1080x720")
my_tree = ttk.Treeview (root)


#functions Later
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

#gui
label=Label(root, text="Student Registration System (CRUD MATRIX)", font= ('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)


studidLabel = Label(root, text="Student ID", font=("Arial",15))
fnLabel = Label(root, text="Full Name", font=("Arial",15))
addLabel = Label(root, text="Address", font=("Arial",15))
pnLabel = Label(root, text="Phone Number", font=("Arial",15))
depLabel = Label(root, text="Department", font=("Arial",15))


studidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
fnLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
addLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
pnLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
depLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)


studidEntry=Entry (root, width=55, bd=5, font=('Arial', 15))
fnEntry=Entry (root, width=55, bd=5, font=('Arial', 15))
addEntry=Entry(root, width=55, bd=5, font=('Arial',15))
pnEntry=Entry (root, width=55, bd=5, font=('Arial', 15))
depEntry=Entry (root, width=55, bd=5, font=(' Arial', 15))


studidEntry.grid (row=3, column=1, columnspan=4, padx=5, pady=0)
fnEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
addEntry.grid (row=5, column=1, columnspan=4, padx=5, pady=0)
pnEntry.grid (row=6, column=1, columnspan=4, padx=5, pady=0)
depEntry.grid (row=7, column=1, columnspan=4, padx=5, pady=0)


#command later
addBtn=Button(
    root, text= "Add", padx=65, pady=25, width=10, bd=5, font=('Arial',15), bg="#84F894"
)
updateBtn=Button(
    root, text= "Update", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84F894"
)
deleteBtn=Button(
    root, text= "Delete", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84F894"
)
searchBtn=Button(
    root,text= "Search", padx=65, pady=25, width=10, bd=5, font=('Arial', 15), bg="#84F894"
)
resetBtn=Button(
    root, text="Reset", padx=65, pady=25,width=10, bd=5, font=('Arial', 15), bg="#84F894"
)
selectBtn=Button(
    root, text="Select", padx=65, pady=25,width=10, bd=5, font=('Arial', 15), bg="#84F894"
)

addBtn.grid (row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid (row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid (row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid (row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid (row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid (row=13, column=5, columnspan=1, rowspan=2)


style=ttk. Style()
style.configure("Treeview.Heading", font=('Arial Bold',15))
my_tree['columns']=("StudentID", "FullName", "Address", "Phonenumber", "Department")

my_tree.column ("#0", width=0, stretch=NO)
my_tree.column("StudentID", anchor=W, width=170)
my_tree.column("FullName", anchor=W, width=150)
my_tree.column ("Address", anchor=W, width=150)
my_tree.column("Phonenumber", anchor=W, width=165)
my_tree.column("Department", anchor=W, width=150)

my_tree.heading("StudentID", text="StudentID", anchor=W)
my_tree.heading("FullName", text="FullName", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)
my_tree.heading ("Phonenumber", text="Phonenumber", anchor=W)
my_tree.heading("Department", text="Department", anchor=W)

refreshTable()

root.mainloop()



























