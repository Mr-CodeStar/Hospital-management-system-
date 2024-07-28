from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import csv
def delete_frame():
    for c_frame in main_frame.winfo_children():
        c_frame.destroy() 
##################################################################################################
def Home():
    delete_frame()
    home_frame=LabelFrame(main_frame,font=(30),bg="black")
    home_frame.place(x=1,y=1,height=945,width=1705)
    count1=0
    count2=0
    if os.path.exists("Doctor_Details.csv"):
        f=open("Doctor_Details.csv","r")
        creader=csv.reader(f)
        lst=[]
        for i in creader:
            lst.append(i)
        count1=len(lst)
        f.close()
        hlabel1=Label(home_frame,text="Total Number of Doctor's\n{}".format(count1),font=("Bold",40),bd=70,bg="blue",fg="white")
        hlabel1.place(x=5,y=5)
    if os.path.exists("Doctor_Details.csv"):
        f=open("Patient_Details.csv","r")
        creader=csv.reader(f)
        lst=[]
        for i in creader:
            lst.append(i)
        count2=len(lst)
        f.close()
        hlabel2=Label(home_frame,text="Total Number of Patient's\n{}".format(count2),font=("Bold",40),bd=70,bg="blue",fg="white")
        hlabel2.place(x=870,y=5)
    hlabel3=Label(home_frame,text="Welcome To DPD Hospital",font=("Bold",40),bd=70,bg="blue",fg="white")
    hlabel3.place(x=400,y=500)
def Doctor():
    delete_frame()
    doctor_frame=LabelFrame(main_frame,font=(30),bg="black")
    doctor_frame.place(x=1,y=1,height=945,width=1705)
    table=ttk.Treeview(doctor_frame,columns=("Specialization","Name","Sex","Consultancy Fees","Contact No.","Email","Address"),show="headings")
    table.heading("Specialization",text="Specialization")
    table.heading("Name",text="Name")
    table.heading("Sex",text="Sex")
    table.heading("Consultancy Fees",text="Consultancy Fees")
    table.heading("Contact No.",text="Contact No.")
    table.heading("Email",text="Email")
    table.heading("Address",text="Address")
    table.place(x=135,y=700)
    def clicker(event):
        Clear()
        cursor_row=table.focus()
        content=table.item(cursor_row)
        row=content["values"]
        specivalue.set(row[0])
        dentry2.insert(0,row[1])
        sexvalue.set(row[2])
        dentry4.insert(0,row[3])
        dentry5.insert(0,row[4])
        dentry6.insert(0,row[5])
        dentry7.insert(0,row[6])
    table.bind("<Double-1>",clicker)
    adddoc=LabelFrame(doctor_frame,text="Add Doctor",font=(30),fg="white",bg="black")
    adddoc.place(x=40,y=40,height=600,width=700)
    if os.path.exists("Doctor_Details.csv")==False:
        f=open("Doctor_Details.csv","w")
        f.close()
    ############################### Functions ################################################
    def Add():
        lst=[specivalue.get(),dentry2.get(),sexvalue.get(),dentry4.get(),dentry5.get(),dentry6.get(),dentry7.get()]
        f=open("Doctor_Details.csv","a",newline="")
        cwriter=csv.writer(f)
        cwriter.writerow(lst)
        f.close()
        for item in table.get_children():
            table.delete(item)
        treeview()
        Clear()
    def treeview():
        f=open("Doctor_Details.csv","r")
        creader=csv.reader(f)
        for rec in creader:
            table.insert(parent="",index=0,value=rec)
        f.close()
    treeview()
    def Update():
        val=dentry5.get()
        f=open("Doctor_Details.csv","r")
        creader=csv.reader(f)
        lst=[]
        for i in creader:
            lst.append(i)
        lst1=[]
        for i in lst:
            if val not in i:
                lst1.append(i)
        f.close()
        g=open("Doctor_Details.csv","w")
        cwriter=csv.writer(g)
        cwriter.writerows(lst1)
        g.close()
        for item in table.get_children():
            table.delete(item)
        treeview()
        Add()
    def Delete():
        val=dentry5.get()
        f=open("Doctor_Details.csv","r")
        creader=csv.reader(f)
        lst=[]
        for i in creader:
            lst.append(i)
        lst1=[]
        for i in lst:
            if val not in i:
                lst1.append(i)
        f.close()
        g=open("Doctor_Details.csv","w")
        cwriter=csv.writer(g)
        cwriter.writerows(lst1)
        g.close()
        for item in table.get_children():
            table.delete(item)
        treeview()
        Clear()
    def Search():
        f=open("Doctor_Details.csv","r")
        val=dentry8.get()
        creader=csv.reader(f)
        for i in creader:
            if i[4]==val:
                val=i
        f.close()
        Clear()
        specivalue.set(val[0])
        dentry2.insert(0,val[1])
        sexvalue.set(val[2])
        dentry4.insert(0,val[3])
        dentry5.insert(0,val[4])
        dentry6.insert(0,val[5])
        dentry7.insert(0,val[6])
    def Clear():
        specivalue.set("")
        sexvalue.set("")
        for widget in adddoc.winfo_children():
            if isinstance(widget,Entry):
                widget.delete(0,"end")
        for widget in doctor_frame.winfo_children():
            if isinstance(widget,Entry):
                widget.delete(0,"end")
    ############################### Labels ###################################################
    dlabel1=Label(adddoc,text="Specialization :",font=("Bold",20),bg="black",fg="white")
    dlabel1.place(x=10,y=10)
    dlabel2=Label(adddoc,text="Name :",font=("Bold",20),bg="black",fg="white")
    dlabel2.place(x=10,y=70)
    dlabel3=Label(adddoc,text="Sex :",font=("Bold",20),bg="black",fg="white")
    dlabel3.place(x=10,y=140)
    dlabel4=Label(adddoc,text="Consultancy Fees :",font=("Bold",20),bg="black",fg="white")
    dlabel4.place(x=10,y=200)
    dlabel5=Label(adddoc,text="Contact No. :",font=("Bold",20),bg="black",fg="white")
    dlabel5.place(x=10,y=270)
    dlabel6=Label(adddoc,text="Email :",font=("Bold",20),bg="black",fg="white")
    dlabel6.place(x=10,y=340)
    dlabel7=Label(adddoc,text="Address :",font=("Bold",20),bg="black",fg="white")
    dlabel7.place(x=10,y=400)
    ############################### Entrys ####################################################
    specialization=["Dentist","Orthopedic","Physician","Gynaecologist","Gastroenterogist","Eye Specialist","E.N.T","Neurologist"]
    specivalue=StringVar()
    dentry1=OptionMenu(adddoc,specivalue,*specialization)
    dentry1.place(x=250,y=10,height=30,width=300)
    dentry2=Entry(adddoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    dentry2.place(x=140,y=70)
    sexvalue=StringVar()
    sex=["Male","Female","Others"]
    dentry3=OptionMenu(adddoc,sexvalue,*sex)
    dentry3.place(x=100,y=140,height=30,width=300)
    dentry4=Entry(adddoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    dentry4.place(x=300,y=200)
    dentry5=Entry(adddoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    dentry5.place(x=230,y=270)
    dentry6=Entry(adddoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    dentry6.place(x=140,y=340)
    dentry7=Entry(adddoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    dentry7.place(x=170,y=400)
    ############################### Buttons ###################################################
    dbutton1=Button(adddoc,text="ADD",command=Add,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    dbutton1.place(x=40,y=500)
    dbutton2=Button(adddoc,text="UPDATE",command=Update,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    dbutton2.place(x=160,y=500)
    dbutton3=Button(adddoc,text="CLEAR",command=Clear,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    dbutton3.place(x=340,y=500)
    dbutton4=Button(adddoc,text="DELETE",command=Delete,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    dbutton4.place(x=490,y=500)
#####################################################################################################
    dlabel8=Label(doctor_frame,text="Search a Doctor :",font=("Bold",50),bg="black",fg="white")
    dlabel8.place(x=800,y=300)
    dentry8=Entry(doctor_frame,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    dentry8.place(x=1000,y=404)
    dbutton5=Button(doctor_frame,text="SEARCH",command=Search,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    dbutton5.place(x=805,y=400)
def Patient():
    delete_frame()
    patient_frame=LabelFrame(main_frame,font=(30),bg="black")
    patient_frame.place(x=1,y=1,height=945,width=1705)
    if os.path.exists("Patient_Details.csv")==False:
        f=open("Patient_Details.csv","w")
        f.close()
    table=ttk.Treeview(patient_frame,columns=("Name","Age","Sex","D.O.B","Contact No.","Email","Address","Admition Date","Symtoms"),show="headings")
    table.heading("Name",text="Name")
    table.heading("Age",text="Age")
    table.heading("Sex",text="Sex")
    table.heading("D.O.B",text="D.O.B")
    table.heading("Contact No.",text="Contact No.")
    table.heading("Email",text="Email")
    table.heading("Address",text="Address")
    table.heading("Admition Date",text="Admition Date")
    table.heading("Symtoms",text="Symtoms")
    table.place(x=6,y=600,width=1700)
    scrollbar=Scrollbar(patient_frame,orient="horizontal",command=table.xview)
    scrollbar.place(x=550,y=850,width=600,height=20)
    table.configure(yscrollcommand=scrollbar.set)
    addpoc=LabelFrame(patient_frame,text="Add Patient",font=(30),fg="White",bg="black")
    addpoc.place(x=1,y=0,width=1700,height=600)
    def clicker(event):
        Clear()
        cursor_row=table.focus()
        content=table.item(cursor_row)
        row=content["values"]
        pentry1.insert(0,row[0])
        pentry2.insert(0,row[1])
        sexvalue.set(row[2])
        pentry4.insert(0,row[3])
        pentry5.insert(0,row[4])
        pentry6.insert(0,row[5])
        pentry7.insert(0,row[6])
        pentry8.insert(0,row[7])
        pentry9.insert(tk.END,row[8])
    table.bind("<Double-1>",clicker)
    ################################### Patient Lables ###########################################
    plabel1=Label(addpoc,text="Name :",font=("Bold",20),bg="black",fg="white")
    plabel1.place(x=1,y=10)
    plabel2=Label(addpoc,text="Age :",font=("Bold",20),bg="black",fg="white")
    plabel2.place(x=1,y=70)
    plabel3=Label(addpoc,text="Sex :",font=("Bold",20),bg="black",fg="white")
    plabel3.place(x=1,y=140)
    plabel4=Label(addpoc,text="D.O.B :",font=("Bold",20),bg="black",fg="white")
    plabel4.place(x=1,y=200)
    plabel5=Label(addpoc,text="Contact No. :",font=("Bold",20),bg="black",fg="white")
    plabel5.place(x=1,y=270)
    plabel6=Label(addpoc,text="Email :",font=("Bold",20),bg="black",fg="white")
    plabel6.place(x=1,y=340)
    plabel7=Label(addpoc,text="Address :",font=("Bold",20),bg="black",fg="white")
    plabel7.place(x=1,y=400)
    plabel8=Label(addpoc,text="Admition Date :",font=("Bold",20),bg="black",fg="white")
    plabel8.place(x=1,y=470)
    plabel9=Label(addpoc,text="Symtoms :",font=("Bold",20),bg="black",fg="white")
    plabel9.place(x=600,y=10)
    ############################### Patient Entrys ####################################################
    pentry1=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry1.place(x=130,y=10)
    pentry2=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry2.place(x=110,y=70)
    sexvalue=StringVar()
    sex=["Male","Female","Others"]
    pentry3=OptionMenu(addpoc,sexvalue,*sex)
    pentry3.place(x=110,y=140,height=30,width=300)
    pentry4=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry4.place(x=130,y=200)
    pentry5=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry5.place(x=200,y=270)
    pentry6=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry6.place(x=140,y=340)
    pentry7=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry7.place(x=170,y=400)
    pentry8=Entry(addpoc,font=("Bold",20),bg="white",bd=2,relief=SUNKEN)
    pentry8.place(x=230,y=470)
    pentry9=Text(addpoc,width=70)
    pentry9.place(x=770,y=10)
############################### Functions ########################################################
    def Add():
        lst=[pentry1.get(),pentry2.get(),sexvalue.get(),pentry4.get(),pentry5.get(),pentry6.get(),pentry7.get(),pentry8.get(),pentry9.get("1.0",tk.END)]
        f=open("Patient_Details.csv","a",newline="")
        cwriter=csv.writer(f)
        cwriter.writerow(lst)
        f.close()
        for item in table.get_children():
            table.delete(item)
        treeview()
        Clear()
    def treeview():
        f=open("Patient_Details.csv","r")
        creader=csv.reader(f)
        for rec in creader:
            table.insert(parent="",index=0,value=rec)
        f.close()
    treeview()
    def Update():
        val=pentry5.get()
        f=open("Patient_Details.csv","r")
        creader=csv.reader(f)
        lst=[]
        for i in creader:
            lst.append(i)
        lst1=[]
        for i in lst:
            if val not in i:
                lst1.append(i)
        f.close()
        g=open("Patient_Details.csv","w")
        cwriter=csv.writer(g)
        cwriter.writerows(lst1)
        g.close()
        for item in table.get_children():
            table.delete(item)
        treeview()
        Add()
    def Clear():
        sexvalue.set("")
        for widget in addpoc.winfo_children():
            if isinstance(widget,Entry):
                widget.delete(0,"end")
        pentry9.delete("1.0",tk.END)
    def Delete():
        val=pentry5.get()
        f=open("Patient_Details.csv","r")
        creader=csv.reader(f)
        lst=[]
        for i in creader:
            lst.append(i)
        lst1=[]
        for i in lst:
            if val not in i:
                lst1.append(i)
        f.close()
        g=open("Patient_Details.csv","w")
        cwriter=csv.writer(g)
        cwriter.writerows(lst1)
        g.close()
        for item in table.get_children():
            table.delete(item)
        treeview()
        Clear()
    def Search():
        f=open("Patient_Details.csv","r")
        val=pentry5.get()
        creader=csv.reader(f)
        for i in creader:
            if i[4]==val:
                val=i
        f.close()
        Clear()
        pentry1.insert(0,val[0])
        pentry2.insert(0,val[1])
        sexvalue.set(val[2])
        pentry4.insert(0,val[3])
        pentry5.insert(0,val[4])
        pentry6.insert(0,val[5])
        pentry7.insert(0,val[6])
        pentry8.insert(0,val[7])
        pentry9.insert(tk.END,val[8])
    ############################### Buttons ######################################################
    pbutton1=Button(addpoc,text="ADD",command=Add,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    pbutton1.place(x=1500,y=10)
    pbutton2=Button(addpoc,text="UPDATE",command=Update,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    pbutton2.place(x=1500,y=100)
    pbutton3=Button(addpoc,text="CLEAR",command=Clear,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    pbutton3.place(x=1500,y=190)
    pbutton4=Button(addpoc,text="DELETE",command=Delete,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    pbutton4.place(x=1500,y=280)
    pbutton5=Button(addpoc,text="SEARCH",command=Search,font=("Bold",20),bd=3,bg="Blue",fg="White",activebackground="Blue",activeforeground="White",relief=RAISED)
    pbutton5.place(x=1500,y=370)
##################################################################################################
root=Tk()
root.title("Hospital Managment System")
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry("{0}x{1}".format(screen_width,screen_height))
root.configure(bg="Black")
frame1=LabelFrame(root,font=(30),bg="blue",relief=RAISED)
frame1.place(x=0,y=6,height=50,width=screen_width)
l1=Label(frame1,text="DPD Hospital Admin Control",font=("Bold",25),bg="blue",fg="white")
l1.place(x=210,y=1)
menu=Label(frame1,text="Menu",font=("Bold",20),bg="blue",fg="white")
menu.place(x=60,y=3,height=38,width=89)
################### Main Window Frames ##############################################
frame2=LabelFrame(root,font=(30),bg="Black")
frame2.place(x=1,y=60,height=200,width=200)
frame3=LabelFrame(root,font=(30),bg="Black")
frame3.place(x=1,y=260,height=200,width=200)
frame4=LabelFrame(root,font=(30),bg="Black")
frame4.place(x=1,y=460,height=200,width=200)
frame5=LabelFrame(root,font=(30),bg="Black")
frame5.place(x=1,y=660,height=200,width=200)
frame6=LabelFrame(root,font=(30),bg="Black")
frame6.place(x=1,y=860,height=150,width=200)
main_frame=LabelFrame(root,font=(30),bg="black",)
main_frame.place(x=205,y=60,height=950,width=1710)
################### Main Window Buttons ##############################################
Button1=Button(frame2,text="Home",command=Home,bg="Orange",fg="white",activebackground="#256ECD",activeforeground="white",bd=6,font=("Bold",40),padx=10,pady=59)
Button1.place(x=1,y=1)
Button2=Button(frame3,text="Doctor",command=Doctor,bg="purple",fg="white",activebackground="#256ECD",activeforeground="white",bd=6,font=("Bold",39),padx=2,pady=60)
Button2.place(x=1,y=1)
Button3=Button(frame4,text="Patient",command=Patient,bg="red",fg="white",activebackground="#256ECD",activeforeground="white",bd=6,font=("Bold",37),padx=3,pady=60)
Button3.place(x=1,y=1)
Button4=Button(frame5,text="Exit",command=root.destroy,bg="green",fg="white",activebackground="#256ECD",activeforeground="white",bd=6,font=("Bold",37),padx=43,pady=60)
Button4.place(x=1,y=1)
l1=Label(frame6,text="DPD",font=("Bold",25),bg="blue",fg="white")
l1.place(x=0,y=0,height=145,width=195)
root.mainloop()