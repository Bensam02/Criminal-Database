import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

main_window = Tk()
main_window.title("Crime Database Management System")

width = 1024
height = 520
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
main_window.geometry("%dx%d+%d+%d" % (width, height, x, y))
main_window.resizable(0, 0)
main_window.config(bg="#000000")

Title = Frame(main_window, bd=1, relief=SOLID)
Title.place(x=375,y=10)
lbl_display = Label(Title, text="Crime Database Management", font=('arial', 15))
lbl_display.pack()



def crime_homepage():
    main_menu_frame=tk.Frame(master=main_window,
    height=29,width=1000)
    main_menu_frame.place(x=20,y=45)
    global main_menu_widget
    main_menu_widget=[0 for i in range(7)]

    main_menu_widget[0]=tk.Button(master=main_menu_frame,text="CRIME",
    padx=2,pady=3,relief="sunken",bg="#FFFFFF",activebackground="#FFFFFF",
    foreground="#000000",activeforeground="#000000",height=1,width=12)
    ''', command=clicked_productmenu'''

    main_menu_widget[1]=tk.Button(master=main_menu_frame,text="STATION",
    padx=2,pady=3,relief="raised",bg="#979797",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=1,width=12)
    ''', command=clicked_customermenu'''

    main_menu_widget[2]=tk.Button(master=main_menu_frame,text="Criminal",
    padx=2,pady=3,relief="raised",bg="#979797",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=1,width=12)
    ''', command=clicked_salespersonmenu'''

    main_menu_widget[3]=tk.Button(master=main_menu_frame,text="Victim",
    padx=2,pady=3,relief="raised",bg="#979797",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=1,width=12)
    ''', command=clicked_suppliermenu'''

    main_menu_widget[4]=tk.Button(master=main_menu_frame,text="E",
    padx=2,pady=3,relief="raised",bg="#979797",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=1,width=12)
    ''', command=clicked_stockmenu'''

    main_menu_widget[5]=tk.Button(master=main_menu_frame,text="F",
    padx=2,pady=3,relief="raised",bg="#979797",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=1,width=12)
    ''', command=clicked_purchasementmenu'''

    main_menu_widget[6]=tk.Button(master=main_menu_frame,text="G",
    padx=2,pady=3,relief="raised",bg="#979797",activebackground="#35A5F6",
    foreground="#FFFFFF",activeforeground="#FFFFFF",height=1,width=12)
    ''', command=clicked_paymentmenu'''

    main_menu_widget[0].pack(side="left")
    main_menu_widget[1].pack(side="left")
    main_menu_widget[2].pack(side="left")
    main_menu_widget[3].pack(side="left")
    main_menu_widget[4].pack(side="left")
    main_menu_widget[5].pack(side="left")
    main_menu_widget[6].pack(side="left")

    global tree_frame
    tree_frame=tk.Frame(master=main_window,height=500,width=600)
    tree_frame.place(x=20,y=80)

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
    tree_view.column('B',minwidth=90,width=90,stretch=tk.NO)
    tree_view.column('C',minwidth=200,width=200,stretch=tk.NO)
    tree_view.column('D',minwidth=105,width=105,stretch=tk.NO)
    tree_view.column('E',minwidth=120,width=120,stretch=tk.NO)
    tree_view.column('F',minwidth=110,width=110,stretch=tk.NO)

    global add_button,delete_button,reset_button,deleteall_button
    global search_button,search_entry

    search_entry=tk.Entry(master=main_window,borderwidth=8,width=34,relief="flat")
    search_entry.insert(0,"Search crime")
    '''search_entry.bind("<FocusIn>",search_clicked)'''

    search_button=ttk.Button(master=main_window,width=35,text="Search")

    reset_button=ttk.Button(master=main_window,width=35,text="Reset")

    add_button=ttk.Button(master=main_window,width=35, text="Add data")

    delete_button=ttk.Button(master=main_window,width=35, text="Delete")

    deleteall_button=ttk.Button(master=main_window,width=35, text="Delete All")


    search_entry.place(x=742,y=15)
    search_button.place(x=742,y=70)
    reset_button.place(x=742,y=115)
    add_button.place(x=742,y=160)
    delete_button.place(x=742,y=205)
    deleteall_button.place(x=742,y=250)

crime_homepage()    
    
main_window.mainloop()
