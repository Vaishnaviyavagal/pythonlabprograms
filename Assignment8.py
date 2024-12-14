#Demonstration of CRUD operations using sqlite3
import sqlite3
con=sqlite3.connect("student.db")
while(1):
    print("1.Create\n2.Insert\n3.Delete\n4.Display\n5.Exit")
    ch=int(input("Enter your choice : "))
    if(ch==1):
        sql="create table stud(rno integer primary key, name text, cgpa real)"
        con.execute(sql)
        print("Table created successfully")
    elif(ch==2):
        print("Enter the details of student : ")
        r = int(input("Enter the Roll Number : "))
        nm = input("Enter the name : ")
        cg = float(input("Enter the CGPA : "))
        con.execute("insert into stud (rno, name, cgpa) values (?, ?, ?)",(r, nm, cg))
        con.commit()
        print("Record Inserted successfully")
    elif(ch==3):
        r=int(input("Enter the roll number to be deleted : "))
        con.execute("delete from stud where rno = ?",(r,))
        con.commit()
        print("Record deleted successfully")
    elif(ch==4):
        cc=con.cursor()
        sql="SELECT * FROM stud"
        cc.execute(sql)
        rs=cc.fetchall()
        for my_row in rs:
            print(my_row)
    elif(ch==5):
        con.close()
        exit()
    else:
        print("Invalid choice")
