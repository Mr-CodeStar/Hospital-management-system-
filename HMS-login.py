from tkinter import*
from tkinter import messagebox
import os
import csv
########################################################################################################
def login():
    username = entry1.get()
    password = entry2.get()
    if  username == ''and password =='':
        messagebox.showerror('login','blanks are not allowed')
        root.destroy()
    else:
        if os.path.exists("Login.csv"):
            f=open("Login.csv","r")
            creader=csv.reader(f)
            user_name_value=[]
            password_value=[]
            for row in creader:
                user_name_value.append(row[0])
                password_value.append(row[1])
            if username in user_name_value and password in password_value:
                messagebox.showinfo('login','LOGIN IS SUCCESSFUL')
                root.destroy()
                import HMS
            else:
                messagebox.showerror('login','incorrect username and password')
                root.destroy()
        else:
            messagebox.showinfo('login','Please First Create an Account')
            root.destroy()
#########################################################################################################
def register():
    root.destroy()
    top=Tk()
    top.configure(bg='black')
    top.geometry("700x400")
    Label1=Label(top,text='Enter Your Details',bg="black",fg='white',font=("areal",25))
    Label1.place(x=200,y=10)
    Label2=Label(top,text="UserName :",font=("areal",20),bg="black",fg='white',)
    Label2.place(x=110,y=120)
    Label3=Label(top,text="Password :",font=("areal",20),bg="black",fg='white',)
    Label3.place(x=110,y=200)
    entry3=Entry(top,font=("areal",20))
    entry3.place(x=280,y=120)
    entry4=Entry(top,font=("areal",20))
    entry4.place(x=280,y=200)
    def register_complet():
        UserName=entry3.get()
        password=entry4.get()
        if UserName == '' and password =='':
            messagebox.showerror('REGISTER','blank are not allowed ')
        else:
            messagebox.showinfo('REGISTER','register is complet successfully ')
            if os.path.exists("Login.csv")==False:
                f=open("Login.csv","w")
                cwriter=csv.writer(f)
                cwriter.writerow([UserName,password])
                f.close()
                top.destroy()
                import HMS
            else:
                f=open("Login.csv","a")
                cwriter=csv.writer(f)
                cwriter.writerow([UserName,password])
                f.close()
                top.destroy()
                import HMS
    button3=Button(top,text="register complete",bg='Green',fg='white',font=("areal",17),bd=6,command=register_complet)
    button3.place(x=250,y=300)
#####################################################################################################
root=Tk()
root.configure(bg='black')
root.geometry("600x500")
Label1=Label(root,text='login page',bg="black",fg='white',font=("areal",25))
Label1.place(x=200,y=10)
Label2=Label(root,text="UserName :",font=("areal",20),bg="black",fg='white',)
Label2.place(x=30,y=120)
Label3=Label(root,text="password :",font=("areal",20),bg="black",fg='white',)
Label3.place(x=30,y=200)
entry1=Entry(root,font=("areal",20))
entry1.place(x=200,y=120)
entry2=Entry(root,font=("areal",20))
entry2.place(x=200,y=200)
button1=Button(root,text='login',bg='blue4',fg='white',font=("areal",17),bd=5,command=login)
button1.place(x=380,y=350)
button2=Button(root,text="register:",font=("areal",20),bg="blue4",fg='white',bd=5,command=register)
button2.place(x=90,y=350)
root.mainloop()
