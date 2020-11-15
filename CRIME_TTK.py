import tkinter as tk
from tkinter import *
import tkinter.messagebox
import sqlite3
import tkinter.ttk as ttk



#---------------------Main Window Code
main_window = Tk()
main_window.title("Crime Database Management System")

width = 1150
height = 650
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
main_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
main_window.resizable(0, 0)
main_window.config(bg="#36454F")
#bg_image_main=tk.PhotoImage(file="main_page.png")   
#tk.Label(master=main_window,image=bg_image_main).pack() 

#Title = tk.Frame(main_window, bd=1, relief=SOLID)
#Title.place(x=500,y=10)
lbl_display = Label(master=main_window, text="Crime Database Management", font=('arial', 20), fg="#000000")
#lbl_display.pack()
lbl_display.place(x=500,y=10)

logo_img=tk.PhotoImage(file="picture.png")
logo_label=tk.Label(master=main_window,
  image=logo_img)
logo_label.place(x=120,y=10)






#-----------------------Database Table Connections
conn_crime=sqlite3.connect('crime.db')
c_crime=conn_crime.cursor()
def create_crime_table():
        c_crime.execute("CREATE TABLE IF NOT EXISTS Crime(Crime_id TEXT PRIMARY KEY, Crime_name TEXT, Criminal_Name TEXT, Station_Name TEXT, Place TEXT)")
create_crime_table()

def create_station_table():
        c_crime.execute("CREATE TABLE IF NOT EXISTS station(station_id TEXT PRIMARY KEY, station_name TEXT, Place TEXT, Address TEXT, Phone TEXT)")
create_station_table()

def create_criminal_table():
        c_crime.execute("CREATE TABLE IF NOT EXISTS criminal(criminal_id TEXT PRIMARY KEY, criminal_name TEXT, crime_id TEXT, Place TEXT, Phone TEXT)")
create_criminal_table()
 
def create_victim_table():
        c_crime.execute("CREATE TABLE IF NOT EXISTS victim(victim_id TEXT PRIMARY KEY, victim_Name TEXT, Place TEXT, Crime_id TEXT, Phone TEXT)")
create_victim_table()

def create_complaint_table():
        c_crime.execute("CREATE TABLE IF NOT EXISTS complaint(complaint_id TEXT PRIMARY KEY, complaint TEXT, complainant TEXT, status TEXT, Phone TEXT)")
create_complaint_table()

def admin_table():
        c_crime.execute("CREATE TABLE IF NOT EXISTS admin(username TEXT PRIMARY KEY, password TEXT)")
admin_table()



#----------------------Front end
def crime_homepage():
    login_frame.destroy()
    global main_menu_frame
    main_menu_frame=tk.Frame(master=main_window,
    height=29,width=1000)
    main_menu_frame.place(x=350,y=570)
    global main_menu_widget
    main_menu_widget=[0 for i in range(7)]

    main_menu_widget[0]=tk.Button(master=main_menu_frame,text="CRIME",
    padx=2,pady=3,relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000",height=2,width=16,
    command=clicked_crimemenu)

    main_menu_widget[1]=tk.Button(master=main_menu_frame,text="STATION",
    padx=2,pady=3,relief="raised",bg="#8B0000",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=2,width=16,
    command=clicked_stationmenu)

    main_menu_widget[2]=tk.Button(master=main_menu_frame,text="CRIMINAL",
    padx=2,pady=3,relief="raised",bg="#8B0000",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=2,width=16,
    command=clicked_criminalmenu)

    main_menu_widget[3]=tk.Button(master=main_menu_frame,text="VICTIM",
    padx=2,pady=3,relief="raised",bg="#8B0000",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=2,width=16,
    command=clicked_victimmenu)
   
    main_menu_widget[4]=tk.Button(master=main_menu_frame,text="COMPLAINT",
    padx=2,pady=3,relief="raised",bg="#8B0000",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=2,width=16,
    command=clicked_complaintmenu)
   
    main_menu_widget[0].pack(side="left")
    main_menu_widget[1].pack(side="left")
    main_menu_widget[2].pack(side="left")
    main_menu_widget[3].pack(side="left")
    main_menu_widget[4].pack(side="left")
    '''main_menu_widget[5].pack(side="left")
    main_menu_widget[6].pack(side="left")'''
    global tree_frame
    tree_frame=tk.Frame(master=main_window,height=500,width=600)
    tree_frame.place(x=350,y=70)

    global tree_view,vert_scrollbar
    vert_scrollbar=ttk.Scrollbar(master=tree_frame,orient="vertical")
    tree_view=ttk.Treeview(
    master=tree_frame,
    selectmode="browse",
    height=23,
    show="headings",
    yscrollcommand=vert_scrollbar.set)
    vert_scrollbar.config(command=tree_view.yview)
    tree_view.pack(side="left")
    vert_scrollbar.pack(side="left",fill='y')

    tree_view["columns"]=('A','B','C','D','E','F')
    tree_view.column('A',minwidth=40,width=40,stretch=tk.NO)
    tree_view.column('B',minwidth=90,width=110,stretch=tk.NO)
    tree_view.column('C',minwidth=175,width=200,stretch=tk.NO)
    tree_view.column('D',minwidth=115,width=120,stretch=tk.NO)
    tree_view.column('E',minwidth=125,width=130,stretch=tk.NO)
    tree_view.column('F',minwidth=115,width=120,stretch=tk.NO)

    
#    global function_button_frame
#   function_button_frame=tk.Frame(master=main_window,height=300,width=270,bg="#000000")
#    function_button_frame.place(x=60,y=100)

    global add_button,delete_button,reset_button,deleteall_button
    global search_button,search_entry

    search_entry=tk.Entry(master=main_window,borderwidth=8,width=35,relief="flat")
    search_entry.insert(0,"Search crime")
    '''search_entry.bind("<FocusIn>",search_clicked)'''

    search_button=tk.Button(master=main_window,width=35,text="Search",bg="#000080",fg="#FFFFFF")

    reset_button=tk.Button(master=main_window,width=35,text="Reset",bg="#000080",fg="#FFFFFF")

    add_button=tk.Button(master=main_window,width=35, text="Add data",bg="#000080",fg="#FFFFFF")

    delete_button=tk.Button(master=main_window,width=35, text="Delete",bg="#000080",fg="#FFFFFF")

    deleteall_button=tk.Button(master=main_window,width=35, text="Delete All",bg="#000080",fg="#FFFFFF")


    search_entry.place(x=50,y=150)
    search_button.place(x=50,y=210)
    reset_button.place(x=50,y=270)
    add_button.place(x=50,y=330)
    delete_button.place(x=50,y=390)
    deleteall_button.place(x=50,y=450)

    global logout_button
    logout_button=tk.Button(master=main_window,width=20,text="LOGOUT",bg="#3A4141",fg="#FFFFFF")
    logout_button.place(x=1000,y=5)
    logout_button.config(command=clicked_logout)
   
    clicked_crimemenu()
   
   
def clicked_crimemenu():
 
    active_menu=[0 for i in range(5)]
    active_menu[0]=1
    main_menu_widget[0].config(relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000")
    for i in range(5):
        if i!=0:
            main_menu_widget[i].config(relief="raised",bg="#8B0000",activebackground="#35A5F6",
            foreground="#FFFFFF",activeforeground="#FFFFFF")


    tree_view.heading('A',text="Sl No",anchor=tk.W)
    tree_view.heading('B',text="Crime_id",anchor=tk.W)
    tree_view.heading('C',text="Crime",anchor=tk.W)
    tree_view.heading('D',text="Criminal Name",anchor=tk.W)
    tree_view.heading('E',text="Station Name",anchor=tk.W)
    tree_view.heading('F',text="Place",anchor=tk.W)
   
    tree_view.delete(*tree_view.get_children())
    con = sqlite3.connect("crime.db")
    cur = con.cursor()
    query = "select Crime_id,Crime_name,Criminal_Name,Station_Name,Place from Crime"
    cur.execute(query)
    res = cur.fetchall()
    j=1
    for i in res:
        i=list(i)
        i[0]=str(i[0])
        i=tuple(i)
        tree_view.insert(parent="",index="end",values=((j,)+i))
        j+=1
    cur.close()
    con.close()
   
    search_entry.delete(0,"end")
    search_entry.config(fg="#888888")
    search_entry.insert(0,"Search Crime")
    search_button.focus()
    search_button.config(command=search_crime)


    reset_button.config(command=clicked_crimemenu)
    add_button.config(text="Add a new Crime",command=clicked_addcrime)
    delete_button.config(text="Delete a Crime",command=delete_crime_clicked)
    deleteall_button.config(text="Delete all Crimes",command=clicked_addcrime)


def clicked_stationmenu():
    global first_click_search
    first_click_search=True

    active_menu=[0 for i in range(5)]
    active_menu[1]=1
    main_menu_widget[1].config(relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000")
    for i in range(5):
        if i!=1:
            main_menu_widget[i].config(relief="raised",bg="#8B0000",activebackground="#35A5F6",
            foreground="#FFFFFF",activeforeground="#FFFFFF")

    tree_view.heading('A',text="Sl No",anchor=tk.W)
    tree_view.heading('B',text="StationID",anchor=tk.W)
    tree_view.heading('C',text="Name",anchor=tk.W)
    tree_view.heading('D',text="Place",anchor=tk.W)
    tree_view.heading('E',text="Address",anchor=tk.W)
    tree_view.heading('F',text="Phone",anchor=tk.W)
   
    tree_view.delete(*tree_view.get_children())
    con = sqlite3.connect("crime.db")
    cur = con.cursor()
    query = "select * from station"
    cur.execute(query)
    res = cur.fetchall()
    j=1
    for i in res:
        i=list(i)
        i[0]=str(i[0])
        i=tuple(i)
        tree_view.insert(parent="",index="end",values=((j,)+i))
        j+=1
    cur.close()
    con.close()
   
    search_entry.delete(0,"end")
    search_entry.config(fg="#888888")
    search_entry.insert(0,"Search Station")
    search_button.focus()
    search_button.config(command=search_station)


    reset_button.config(command=clicked_stationmenu)
    add_button.config(text="Add a new Station",command=clicked_addstation)
    delete_button.config(text="Delete a Station",command=delete_station_clicked)
    deleteall_button.config(text="Delete all Stations",command=clicked_addstation)

   
def clicked_criminalmenu():
    global first_click_search
    first_click_search=True

    active_menu=[0 for i in range(5)]
    active_menu[2]=1
    main_menu_widget[2].config(relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000")
    for i in range(5):
        if i!=2:
          main_menu_widget[i].config(relief="raised",bg="#8B0000",activebackground="#35A5F6",
          foreground="#FFFFFF",activeforeground="#FFFFFF")

    tree_view.heading('A',text="Sl No",anchor=tk.W)
    tree_view.heading('B',text="Criminal ID",anchor=tk.W)
    tree_view.heading('C',text="Name",anchor=tk.W)
    tree_view.heading('D',text="Crime ID",anchor=tk.W)
    tree_view.heading('E',text="Place",anchor=tk.W)
    tree_view.heading('F',text="Phone",anchor=tk.W)
   
    tree_view.delete(*tree_view.get_children())
    con = sqlite3.connect("crime.db")
    cur = con.cursor()
    query = "select * from criminal"
    cur.execute(query)
    res = cur.fetchall()
    j=1
    for i in res:
        i=list(i)
        i[0]=str(i[0])
        i=tuple(i)
        tree_view.insert(parent="",index="end",values=((j,)+i))
        j+=1
    cur.close()
    con.close()
   
    search_entry.delete(0,"end")
    search_entry.config(fg="#888888")
    search_entry.insert(0,"Search Criminal")
    search_button.focus()
    search_button.config(command=search_criminal)


    reset_button.config(command=clicked_criminalmenu)
    add_button.config(text="Add a new Criminal",command=clicked_addcriminal)
    delete_button.config(text="Delete a Criminal",command=delete_criminal_clicked)
    deleteall_button.config(text="Delete all Criminals",command=clicked_addcriminal)


def clicked_victimmenu():
    global first_click_search
    first_click_search=True

    active_menu=[0 for i in range(5)]
    active_menu[3]=1
    main_menu_widget[3].config(relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000")
    for i in range(5):
        if i!=3:
            main_menu_widget[i].config(relief="raised",bg="#8B0000",activebackground="#35A5F6",
            foreground="#FFFFFF",activeforeground="#FFFFFF")

    tree_view.heading('A',text="Sl No",anchor=tk.W)
    tree_view.heading('B',text="Victim ID",anchor=tk.W)
    tree_view.heading('C',text="Name",anchor=tk.W)
    tree_view.heading('D',text="Place",anchor=tk.W)
    tree_view.heading('E',text="Crime ID",anchor=tk.W)
    tree_view.heading('F',text="Phone",anchor=tk.W)
   
    tree_view.delete(*tree_view.get_children())
    con = sqlite3.connect("crime.db")
    cur = con.cursor()
    query = "select * from victim"
    cur.execute(query)
    res = cur.fetchall()
    j=1
    for i in res:
        i=list(i)
        i[0]=str(i[0])
        i=tuple(i)
        tree_view.insert(parent="",index="end",values=((j,)+i))
        j+=1
    cur.close()
    con.close()
   
    search_entry.delete(0,"end")
    search_entry.config(fg="#888888")
    search_entry.insert(0,"Search Victim")
    search_button.focus()
    search_button.config(command=search_victim)


    reset_button.config(command=clicked_victimmenu)
    add_button.config(text="Add a new Victim",command=clicked_addvictim)
    delete_button.config(text="Delete a Victim",command=delete_victim_clicked)
    deleteall_button.config(text="Delete all Victims",command=clicked_addvictim)
   

def clicked_complaintmenu():
    global first_click_search
    first_click_search=True

    active_menu=[0 for i in range(5)]
    active_menu[4]=1
    main_menu_widget[4].config(relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000")
    for i in range(5):
        if i!=4:
            main_menu_widget[i].config(relief="raised",bg="#8B0000",activebackground="#35A5F6",
            foreground="#FFFFFF",activeforeground="#FFFFFF")

    tree_view.heading('A',text="Sl No",anchor=tk.W)
    tree_view.heading('B',text="Complaint ID",anchor=tk.W)
    tree_view.heading('C',text="Complaint",anchor=tk.W)
    tree_view.heading('D',text="Complainant",anchor=tk.W)
    tree_view.heading('E',text="Status",anchor=tk.W)
    tree_view.heading('F',text="Phone",anchor=tk.W)
   
    tree_view.delete(*tree_view.get_children())
    con = sqlite3.connect("crime.db")
    cur = con.cursor()
    query = "select * from complaint"
    cur.execute(query)
    res = cur.fetchall()
    j=1
    for i in res:
        i=list(i)
        i[0]=str(i[0])
        i=tuple(i)
        tree_view.insert(parent="",index="end",values=((j,)+i))
        j+=1
    cur.close()
    con.close()
   
    search_entry.delete(0,"end")
    search_entry.config(fg="#888888")
    search_entry.insert(0,"Search Complaint")
    search_button.focus()
    search_button.config(command=search_complaint)


    reset_button.config(command=clicked_complaintmenu)
    add_button.config(text="Add a new Complaint",command=clicked_addcomplaint)
    delete_button.config(text="Delete a Complaint",command=delete_complaint_clicked)
    deleteall_button.config(text="Delete all Complaints",command=clicked_addcomplaint)
   
   
   
def clicked_addcrime():

    global addwindow,centry0,centry1,centry2,centry3,centry4
    addwindow=tk.Toplevel()
    canvas=tk.Canvas(master=addwindow,width=500,height=65)
    canvas.place(x=0,y=0)
    canvas.create_rectangle(0,0,500,85,fill="#FFA500")
    addwindow.config(bg="#000000")
    addwindow.geometry("500x400")
    addwindow.title("New Crime")
    clabelh=tk.Label(master=addwindow,text="NEW CRIME DETAILS",bg="#FFA500",fg="#000000",width=30,font=("bold",15))
    clabelh.place(x=85,y=20)
    details_frame=tk.Frame(master=addwindow,width=400,height=300,bg="#000000")
    details_frame.place(x=100,y=75)  
   
   
    clabel0=tk.Label(master=details_frame,text="Crime ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    clabel1=tk.Label(master=details_frame,text="Crime",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel1.grid(row=1,column=1,pady=10,sticky="W")
    centry1 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry1.grid(row=1,column=2,pady=10,ipady=2,ipadx=2)
    clabel2 = tk.Label(master=details_frame, text="Criminal Name",bg="#000000",anchor="w",fg="#FFFFFF",width=10,font=("bold", 10))
    clabel2.grid(row=2,column=1,pady=10,sticky="W")
    centry2 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry2.grid(row=2,column=2,pady=10,ipady=2)
    clabel3 = tk.Label(master=details_frame, text="Station",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel3.grid(row=3,column=1,pady=10,sticky="W")
    centry3 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry3.grid(row=3,column=2,pady=10,ipady=2,ipadx=2)
    clabel4 = tk.Label(master=details_frame, text="Place",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel4.grid(row=4,column=1,pady=10,sticky="W")
    centry4 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry4.grid(row=4,column=2,pady=10,ipady=2,ipadx=2)
    centry0.focus()

    ttk.Button(master=addwindow, text="   ADD CRIME   ", command=validatecrime).place(x=200,y=340)

    addwindow.resizable(False,False)
    addwindow.mainloop()
   

def validatecrime():

    if centry0.get()=="":
        response=messagebox.showerror(title="Error",message="Crime ID is mandatory!")
        centry0.focus()
        return

    add_crime()
  #  centry0.get(), centry1.get(), centry2.get(), centry3.get(), centry4.get()
   
def add_crime():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
  #  Crime_id, Crime_name, Criminal_Name, Station_Name, Place
    Crime_id = centry0.get()
    Crime_name = centry1.get()
    Criminal_Name = centry2.get()
    Station_Name = centry3.get()
    Place = centry4.get()
    c_crime.execute("INSERT INTO Crime VALUES (?,?,?,?,?)", (Crime_id, Crime_name, Criminal_Name, Station_Name, Place))
    conn_crime.commit()
    conn_crime.close()
    return
   
   
def clicked_addstation():

    global addwindow,centry0,centry1,centry2,centry3,centry4
    addwindow=tk.Toplevel()
    canvas=tk.Canvas(master=addwindow,width=500,height=65)
    canvas.place(x=0,y=0)
    canvas.create_rectangle(0,0,500,85,fill="#654321")
    addwindow.config(bg="#000000")
    addwindow.geometry("500x400")
    addwindow.title("New Station")
    clabelh=tk.Label(master=addwindow,text="NEW STATION DETAILS",bg="#654321",fg="#FFFFFF",width=30,font=("bold",15))
    clabelh.place(x=85,y=20)
    details_frame=tk.Frame(master=addwindow,width=400,height=300,bg="#000000")
    details_frame.place(x=85,y=75)

   
    clabel0=tk.Label(master=details_frame,text="Station ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    clabel1=tk.Label(master=details_frame,text="Station Name",bg="#000000",anchor="w",fg="#FFFFFF",width=10,font=("bold",10))
    clabel1.grid(row=1,column=1,pady=10,sticky="W")
    centry1 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry1.grid(row=1,column=2,pady=10,ipady=2,ipadx=2)
    clabel2 = tk.Label(master=details_frame, text="Place",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel2.grid(row=2,column=1,pady=10,sticky="W")
    centry2 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry2.grid(row=2,column=2,pady=10,ipady=2)
    clabel3 = tk.Label(master=details_frame, text="Address",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel3.grid(row=3,column=1,pady=10,sticky="W")
    centry3 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry3.grid(row=3,column=2,pady=10,ipady=2,ipadx=2)
    clabel4 = tk.Label(master=details_frame, text="Phone",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel4.grid(row=4,column=1,pady=10,sticky="W")
    centry4 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry4.grid(row=4,column=2,pady=10,ipady=2,ipadx=2)
    centry0.focus()

    ttk.Button(master=addwindow, text="   ADD STATION   ",command=validatestation).place(x=200,y=340)

    addwindow.resizable(False,False)
    addwindow.mainloop()


def validatestation():

    if centry0.get()=="":
        response=messagebox.showerror(title="Error",message="Please add station")
        centry0.focus()
        return

    add_station()

   
def add_station():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    Station_id = centry0.get()
    Station_name = centry1.get()
    Place = centry2.get()
    Address = centry3.get()
    Phone = centry4.get()
    c_crime.execute("INSERT INTO station VALUES (?,?,?,?,?)", (Station_id, Station_name, Place, Address, Phone))
    conn_crime.commit()
    conn_crime.close()
    return



def clicked_addcriminal():

    global addwindow,centry0,centry1,centry2,centry3,centry4
    addwindow=tk.Toplevel()
    canvas=tk.Canvas(master=addwindow,width=500,height=65)
    canvas.place(x=0,y=0)
    canvas.create_rectangle(0,0,500,85,fill="#FF6347")
    addwindow.config(bg="#000000")
    addwindow.geometry("500x400")
    addwindow.title("New Criminal")
    clabelh=tk.Label(master=addwindow,text="NEW CRIMINAL DETAILS",bg="#FF6347",fg="#000000",width=30,font=("bold",15))
    clabelh.place(x=85,y=20)
    details_frame=tk.Frame(master=addwindow,width=400,height=300,bg="#000000")
    details_frame.place(x=100,y=75)  
   
   
    clabel0=tk.Label(master=details_frame,text="Criminal ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    clabel1=tk.Label(master=details_frame,text="Name",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel1.grid(row=1,column=1,pady=10,sticky="W")
    centry1 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry1.grid(row=1,column=2,pady=10,ipady=2,ipadx=2)
    clabel2 = tk.Label(master=details_frame, text="Place",bg="#000000",anchor="w",fg="#FFFFFF",width=10,font=("bold", 10))
    clabel2.grid(row=2,column=1,pady=10,sticky="W")
    centry2 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry2.grid(row=2,column=2,pady=10,ipady=2)
    clabel3 = tk.Label(master=details_frame, text="Crime ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel3.grid(row=3,column=1,pady=10,sticky="W")
    centry3 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry3.grid(row=3,column=2,pady=10,ipady=2,ipadx=2)
    clabel4 = tk.Label(master=details_frame, text="Phone",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel4.grid(row=4,column=1,pady=10,sticky="W")
    centry4 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry4.grid(row=4,column=2,pady=10,ipady=2,ipadx=2)
    centry0.focus()

    ttk.Button(master=addwindow, text="   ADD CRIMINAL   ", command=validatecriminal).place(x=200,y=340)

    addwindow.resizable(False,False)
    addwindow.mainloop()
   

def validatecriminal():

    if centry0.get()=="":
        response=messagebox.showerror(title="Error",message="Criminal ID is mandatory!")
        centry0.focus()
        return

    add_criminal()
   
def add_criminal():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    criminal_id = centry0.get()
    criminal_name = centry1.get()
    crime_id = centry2.get()
    Place = centry3.get()
    Phone = centry4.get()
    c_crime.execute("INSERT INTO criminal VALUES (?,?,?,?,?)", (criminal_id, criminal_name, crime_id, Place, Phone))
    conn_crime.commit()
    conn_crime.close()
    return
   
   
   
def clicked_addvictim():

    global addwindow,centry0,centry1,centry2,centry3,centry4
    addwindow=tk.Toplevel()
    canvas=tk.Canvas(master=addwindow,width=500,height=65)
    canvas.place(x=0,y=0)
    canvas.create_rectangle(0,0,500,85,fill="#FF8C00")
    addwindow.config(bg="#000000")
    addwindow.geometry("500x400")
    addwindow.title("New Victim")
    clabelh=tk.Label(master=addwindow,text="NEW VICTIM DETAILS",bg="#FF8C00",fg="#000000",width=30,font=("bold",15))
    clabelh.place(x=85,y=20)
    details_frame=tk.Frame(master=addwindow,width=400,height=300,bg="#000000")
    details_frame.place(x=100,y=75)  
   
   
    clabel0=tk.Label(master=details_frame,text="Victim ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    clabel1=tk.Label(master=details_frame,text="Name",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel1.grid(row=1,column=1,pady=10,sticky="W")
    centry1 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry1.grid(row=1,column=2,pady=10,ipady=2,ipadx=2)
    clabel2 = tk.Label(master=details_frame, text="Place",bg="#000000",anchor="w",fg="#FFFFFF",width=10,font=("bold", 10))
    clabel2.grid(row=2,column=1,pady=10,sticky="W")
    centry2 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry2.grid(row=2,column=2,pady=10,ipady=2)
    clabel3 = tk.Label(master=details_frame, text="Crime ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel3.grid(row=3,column=1,pady=10,sticky="W")
    centry3 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry3.grid(row=3,column=2,pady=10,ipady=2,ipadx=2)
    clabel4 = tk.Label(master=details_frame, text="Phone",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel4.grid(row=4,column=1,pady=10,sticky="W")
    centry4 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry4.grid(row=4,column=2,pady=10,ipady=2,ipadx=2)
    centry0.focus()

    ttk.Button(master=addwindow, text="   ADD VICTIM   ", command=validatevictim).place(x=200,y=340)

    addwindow.resizable(False,False)
    addwindow.mainloop()
   

def validatevictim():

    if centry0.get()=="":
        response=messagebox.showerror(title="Error",message="Victim ID is mandatory!")
        centry0.focus()
        return

    add_victim()
   
def add_victim():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    victim_id = centry0.get()
    victim_name = centry1.get()
    Place = centry2.get()
    Crime_id = centry3.get()
    Phone = centry4.get()
    c_crime.execute("INSERT INTO victim VALUES (?,?,?,?,?)", (victim_id, victim_name,Place, Crime_id, Phone))
    conn_crime.commit()
    conn_crime.close()
    return
 
   
def clicked_addcomplaint():

    global addwindow,centry0,centry1,centry2,centry3,centry4
    addwindow=tk.Toplevel()
    canvas=tk.Canvas(master=addwindow,width=500,height=65)
    canvas.place(x=0,y=0)
    canvas.create_rectangle(0,0,500,85,fill="#FF8C00")
    addwindow.config(bg="#000000")
    addwindow.geometry("500x400")
    addwindow.title("New Victim")
    clabelh=tk.Label(master=addwindow,text="NEW COMPLAINT DETAILS",bg="#FF8C00",fg="#000000",width=30,font=("bold",15))
    clabelh.place(x=85,y=20)
    details_frame=tk.Frame(master=addwindow,width=400,height=300,bg="#000000")
    details_frame.place(x=100,y=75)  
   
   
    clabel0=tk.Label(master=details_frame,text="Complaint ID",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    clabel1=tk.Label(master=details_frame,text="Complaint",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold",10))
    clabel1.grid(row=1,column=1,pady=10,sticky="W")
    centry1 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry1.grid(row=1,column=2,pady=10,ipady=2,ipadx=2)
    clabel2 = tk.Label(master=details_frame, text="Complainant",bg="#000000",anchor="w",fg="#FFFFFF",width=10,font=("bold", 10))
    clabel2.grid(row=2,column=1,pady=10,sticky="W")
    centry2 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry2.grid(row=2,column=2,pady=10,ipady=2)
    clabel3 = tk.Label(master=details_frame, text="Status",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel3.grid(row=3,column=1,pady=10,sticky="W")
    centry3 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry3.grid(row=3,column=2,pady=10,ipady=2,ipadx=2)
    clabel4 = tk.Label(master=details_frame, text="Phone",bg="#000000",anchor="w",fg="#FFFFFF",width=8,font=("bold", 10))
    clabel4.grid(row=4,column=1,pady=10,sticky="W")
    centry4 = tk.Entry(master=details_frame,width=35,bd=4,relief="flat")
    centry4.grid(row=4,column=2,pady=10,ipady=2,ipadx=2)
    centry0.focus()

    ttk.Button(master=addwindow, text="   ADD COMPLAINT   ", command=validatecomplaint).place(x=200,y=340)

    addwindow.resizable(False,False)
    addwindow.mainloop()
   

def validatecomplaint():

    if centry0.get()=="":
        response=messagebox.showerror(title="Error",message="Complaint ID is mandatory!")
        centry0.focus()
        return

    add_complaint()
   
def add_complaint():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    complaint_id = centry0.get()
    complaint = centry1.get()
    complainant = centry2.get()
    status = centry3.get()
    Phone = centry4.get()
    c_crime.execute("INSERT INTO complaint VALUES (?,?,?,?,?)", (complaint_id, complaint,complainant, status, Phone))
    conn_crime.commit()
    conn_crime.close()
    return
 
   

def search_crime():
    search_text=search_entry.get()
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    if search_text not in ["","Search Crime"]:
        query="SELECT * FROM Crime WHERE crime_name LIKE '%s'"%("%"+str(search_text)+"%")
        tree_view.delete(*tree_view.get_children())
        c_crime.execute(query)
        res=c_crime.fetchall()
        j=1
        for i in res:
            i=list(i)
            i[0]=str(i[0])
            i=tuple(i)
            tree_view.insert(
                parent="",
                index="end",
                values=((j,)+i))
            j+=1
    c_crime.close()
    conn_crime.close()
   
def search_station():
    search_text=search_entry.get()
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    if search_text not in ["","Search Station"]:
        query="SELECT * FROM station WHERE station_name LIKE '%s'"%("%"+str(search_text)+"%")
        tree_view.delete(*tree_view.get_children())
        c_crime.execute(query)
        res=c_crime.fetchall()
        j=1
        for i in res:
            i=list(i)
            i[0]=str(i[0])
            i=tuple(i)
            tree_view.insert(
                parent="",
                index="end",
                values=((j,)+i))
            j+=1
    c_crime.close()
    conn_crime.close()
   
def search_criminal():
    search_text=search_entry.get()
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    if search_text not in ["","Search Criminal"]:
        query="SELECT * FROM criminal WHERE criminal_name LIKE '%s'"%("%"+str(search_text)+"%")
        tree_view.delete(*tree_view.get_children())
        c_crime.execute(query)
        res=c_crime.fetchall()
        j=1
        for i in res:
            i=list(i)
            i[0]=str(i[0])
            i=tuple(i)
            tree_view.insert(
                parent="",
                index="end",
                values=((j,)+i))
            j+=1
    c_crime.close()
    conn_crime.close()
   
def search_victim():
    search_text=search_entry.get()
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    if search_text not in ["","Search Victim"]:
        query="SELECT * FROM victim WHERE victim_Name LIKE '%s'"%("%"+str(search_text)+"%")
        tree_view.delete(*tree_view.get_children())
        c_crime.execute(query)
        res=c_crime.fetchall()
        j=1
        for i in res:
            i=list(i)
            i[0]=str(i[0])
            i=tuple(i)
            tree_view.insert(
                parent="",
                index="end",
                values=((j,)+i))
            j+=1
    c_crime.close()
    conn_crime.close()

def search_complaint():
    search_text=search_entry.get()
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    if search_text not in ["","Search Complaint"]:
        query="SELECT * FROM complaint WHERE complaint LIKE '%s'"%("%"+str(search_text)+"%")
        tree_view.delete(*tree_view.get_children())
        c_crime.execute(query)
        res=c_crime.fetchall()
        j=1
        for i in res:
            i=list(i)
            i[0]=str(i[0])
            i=tuple(i)
            tree_view.insert(
                parent="",
                index="end",
                values=((j,)+i))
            j+=1
    c_crime.close()
    conn_crime.close()


def delete_crime_clicked():
    global centry0
    addwindow=tk.Toplevel()
    addwindow.config(bg="#000000")
    addwindow.geometry("500x100")
    addwindow.title("Delete Crime")
    clabel0=tk.Label(master=addwindow,text="Enter Crime ID",bg="#000000",anchor="w",fg="#FFFFFF",width=15,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    global crimeid
    ttk.Button(master=addwindow, text="   DELETE CRIME   ", command=delete_crime).place(x=200,y=60)
   
def delete_crime():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    crimeid = centry0.get()
    c_crime.execute("DELETE  FROM Crime WHERE Crime_id=?", (crimeid,))
    conn_crime.commit()
    conn_crime.close()

def delete_station_clicked():
    global centry0
    addwindow=tk.Toplevel()
    addwindow.config(bg="#000000")
    addwindow.geometry("500x100")
    addwindow.title("Delete Station")
    clabel0=tk.Label(master=addwindow,text="Enter Station ID",bg="#000000",anchor="w",fg="#FFFFFF",width=15,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    global stationid
    ttk.Button(master=addwindow, text="   DELETE STATION   ", command=delete_station).place(x=200,y=60)
   
def delete_station():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    stationid = centry0.get()
    c_crime.execute("DELETE  FROM station WHERE station_id=?", (stationid,))
    conn_crime.commit()
    conn_crime.close()

def delete_criminal_clicked():
    global centry0
    addwindow=tk.Toplevel()
    addwindow.config(bg="#000000")
    addwindow.geometry("500x100")
    addwindow.title("Delete Criminal")
    clabel0=tk.Label(master=addwindow,text="Enter Criminal ID",bg="#000000",anchor="w",fg="#FFFFFF",width=15,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    global criminalid
    ttk.Button(master=addwindow, text="   DELETE CRIMINAL   ", command=delete_criminal).place(x=200,y=60)
   
def delete_criminal():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    criminalid = centry0.get()
    c_crime.execute("DELETE  FROM criminal WHERE criminal_id=?", (criminalid,))
    conn_crime.commit()
    conn_crime.close()

def delete_victim_clicked():
    global centry0
    addwindow=tk.Toplevel()
    addwindow.config(bg="#000000")
    addwindow.geometry("500x100")
    addwindow.title("Delete Victim")
    clabel0=tk.Label(master=addwindow,text="Enter Victim ID",bg="#000000",anchor="w",fg="#FFFFFF",width=15,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    global victimid
    ttk.Button(master=addwindow, text="   DELETE VICTIM   ", command=delete_victim).place(x=200,y=60)
   
def delete_victim():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    victimid = centry0.get()
    c_crime.execute("DELETE  FROM victim WHERE victim_id=?", (victimid,))
    conn_crime.commit()
    conn_crime.close()
   
def delete_complaint_clicked():
    global centry0
    addwindow=tk.Toplevel()
    addwindow.config(bg="#000000")
    addwindow.geometry("500x100")
    addwindow.title("Delete Complaint")
    clabel0=tk.Label(master=addwindow,text="Enter Complaint ID",bg="#000000",anchor="w",fg="#FFFFFF",width=15,font=("bold",10))
    clabel0.grid(row=0,column=1,pady=10,sticky="W")
    centry0 = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
    centry0.grid(row=0,column=2,pady=10,ipady=2,ipadx=2)
    global complaintid
    ttk.Button(master=addwindow, text="   DELETE COMPLAINT  ", command=delete_complaint).place(x=200,y=60)
   
def delete_complaint():
    conn_crime=sqlite3.connect('crime.db')
    c_crime=conn_crime.cursor()
    complaintid = centry0.get()
    c_crime.execute("DELETE  FROM complaint WHERE complaint_id=?", (complaintid,))
    conn_crime.commit()
    conn_crime.close()
   




def new_user():
	global addwindow
	global user_entry, pass_entry
	addwindow=tk.Toplevel()
	addwindow.config(bg="#ADDADC")
	addwindow.geometry("500x400")
	addwindow.title("Add User")
	user_login_img=tk.PhotoImage(file="logo.png")
	user_login_label=tk.Label(master=addwindow, image=user_login_img)
	user_login_label.place(x=190,y=70)
	title_label = tk.Label(master=addwindow,text="New User Registration",bg="#6E8687",anchor="w",fg="#FFFFFF",width=17,font=("bold",25))
	title_label.place(x=90,y=10)
	user_label = tk.Label(master=addwindow,text="Username: ",bg="#ADDADC",anchor="w",fg="#FFFFFF",width=10,font=("bold",15))
	user_label.place(x=60,y=190)
	user_entry = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
	user_entry.place(x=180,y=190)
	pass_label = tk.Label(master=addwindow,text="Password: ",bg="#ADDADC",anchor="w",fg="#FFFFFF",width=10,font=("bold",15))
	pass_label.place(x=60,y=240)
	pass_entry = tk.Entry(master=addwindow,width=35,bd=4,relief="flat")
	pass_entry.place(x=180,y=240)
	pass_entry.config(show="*")
	create_account_button=tk.Button(master=addwindow,width=30,text="Create Account",bg="#555555",fg="#FFFFFF")
	create_account_button.place(x=120,y=300)
	create_account_button.config(command=create_new_user)


def create_new_user():
	conn_crime=sqlite3.connect('crime.db')
	c_crime=conn_crime.cursor()
	user=user_entry.get()
	pass1=pass_entry.get()
	c_crime.execute("SELECT * FROM admin WHERE username = ? and password = ?",(user,pass1))
	result=c_crime.fetchall()
	if result:
		tk.messagebox.showerror(title="Error", message="Username Taken!")
	else:
		c_crime.execute("INSERT INTO admin VALUES (?,?)", (user, pass1))
		addwindow.destroy()
		tk.messagebox.showerror(title="New Uer", message="Registration Successful")
	conn_crime.commit()
	conn_crime.close()
	return

def clicked_logout():
	tree_frame.destroy()
	main_menu_frame.destroy()
	logout_button.destroy()
	search_entry.destroy()
	search_button.destroy()
	reset_button.destroy()
	add_button.destroy()
	delete_button.destroy()
	deleteall_button.destroy()
	login_page()


	
def login_page():
	global login_frame
	global user_entry, pass_entry
	login_frame=tk.Frame(master=main_window,height=300,width=500, bg="#6E8687")
	login_frame.place(x=300,y=200)
	login_label=tk.Label(master=login_frame,text="LOGIN",bg="#2AD2D2",anchor="center",fg="#FFFFFF",width=6,font=("bold",18))
	login_label.place(x=210,y=10)
	user_label = tk.Label(master=login_frame,text="Username: ",bg="#2AD2D2",anchor="center",fg="#FFFFFF",width=10,font=("bold",15))
	user_label.place(x=80,y=70)
	user_entry = tk.Entry(master=login_frame,width=35,bd=4,relief="flat")
	user_entry.place(x=210,y=70)
	pass_label = tk.Label(master=login_frame,text="Password: ",bg="#2AD2D2",anchor="center",fg="#FFFFFF",width=10,font=("bold",15))
	pass_label.place(x=80,y=130)
	pass_entry = tk.Entry(master=login_frame,width=35,bd=4,relief="flat")
	pass_entry.place(x=210,y=130)
	pass_entry.config(show="*")
	login_button=tk.Button(master=login_frame,width=20,text="Login",bg="#555555",fg="#FFFFFF")
	login_button.place(x=170,y=200)
	login_button.config(command=validate_login)
	create_account_label = tk.Label(master=login_frame,text="Don't have an account?",bg="#6E8687", anchor="w",fg="#000000",width=20,font=("underline",8))
	create_account_label.place(x=140,y=230)
	create_account_button=tk.Button(master=login_frame,width=30,text="Create an Account",bg="#555555",fg="#FFFFFF")
	create_account_button.place(x=140,y=250)
	create_account_button.config(command=new_user)

def validate_login():
	conn_crime=sqlite3.connect('crime.db')
	c_crime=conn_crime.cursor()
	user=user_entry.get()
	pass1=pass_entry.get()
	#find_user = ('SELECT * FROM admin WHERE username = ? and password = ?')
	c_crime.execute("SELECT * FROM admin WHERE username = ? and password = ?",(user,pass1))
	result=c_crime.fetchall()
	if result:
		crime_homepage()
	else:
		tk.messagebox.showerror(title="Error", message="INVALID CREDENTIALS!")
	conn_crime.commit()
	conn_crime.close()
	return

	
login_page()





   
#crime_homepage()    
   
main_window.mainloop()

