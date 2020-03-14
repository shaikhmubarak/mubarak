import mysql.connector as mysql
conn=mysql.connect(user="root",password="scott",host='127.0.01')
c=conn.curser()
c.execute("use python")
c.execute("select * from employees")
rows=c.fetchall()
empid = rows[1][10]
print(emp.id)
c.execute("update employees set ename='stu' where eno="+str(empid))
emp_id=input("enter employees id to delete")
c.execute("delete from employees where eno="+str(emp_Id))
comm.commit
c.execute("select * from employees ")
print(c.fetchall())

conn.close()
