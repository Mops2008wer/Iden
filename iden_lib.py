from ram import _read
from ram import _mov
from ram import _read_metadata
from ram import _mov_metadata
from core import ___app
from bootsys import oprinit, returnsystem
import os
from tkinter import *
from tkinter import messagebox

def rap_run(metadata, appcom):
    if(appcom[0] == "exit_app"):
        returnsystem()
    if(appcom[0] == "print_ui"):
        def button1():
            window.destroy()
        def exit():
            window.destroy()
            returnsystem()
        window = Tk()
        window.title("RaidenProgect")  
        if appcom[4] == "default":
            window.geometry('250x250')
            window.columnconfigure(0, minsize=250)
            frame_top = LabelFrame(text="")
            frame_top.pack(padx=100, pady=30)
            lbl = Label(window, text=_read_metadata(metadata, appcom[1]), font=("Arial Bold", 17))
            lbl.pack()
            btn = Button(window, text=_read_metadata(metadata, appcom[2]), command=button1, font=("Arial Bold", 13))
            btn.pack()
            if appcom[3] != "false":
                btn = Button(window, text=_read_metadata(metadata, appcom[3]), command=exit, font=("Arial Bold", 10))
                btn.pack()
        if appcom[4] == "yae":
            window.geometry('300x250')
            window.columnconfigure(0, minsize=125)
            logo = PhotoImage(file = _read_metadata(metadata, appcom[5]))
            label = Label(window, image = logo)
            label.img_ref = logo
            label.place(x = 25, y = 75, width = 150)
            lbl = Label(window, text=_read_metadata(metadata, appcom[1]), font=("Arial Bold", 17))
            lbl.place(x = 25, y = 25, width = 100)
            btn = Button(window, text=_read_metadata(metadata, appcom[2]), command=button1, font=("Arial Bold", 13))
            btn.place(x = 160, y = 165, width = 110)
            if appcom[3] != "false":
                btn = Button(window, text=_read_metadata(metadata, appcom[3]), command=exit, font=("Arial Bold", 10))
                btn.place(x = 170, y = 200, width = 100)
        window.mainloop()
    if(appcom[0] == "print_ui_2"):
        def button1():
            window.destroy()
        def exit():
            window.destroy()
            returnsystem()
        window = Tk()
        window.title("IdenProgect")  
        if appcom[5] == "default":
            window.geometry('250x250')
            window.columnconfigure(0, minsize=250)
            frame_top = LabelFrame(text="")
            frame_top.pack(padx=100, pady=25)
            lbl = Label(window, text=_read_metadata(metadata, appcom[1]), font=("Arial Bold", 17))
            lbl.pack()
            lbl = Label(window, text=_read_metadata(metadata, appcom[2]), font=("Arial Bold", 15))
            lbl.pack()
            btn = Button(window, text=_read_metadata(metadata, appcom[3]), command=button1, font=("Arial Bold", 13))
            btn.pack()
            if appcom[4] != "false":
                btn = Button(window, text=_read_metadata(metadata, appcom[4]), command=exit, font=("Arial Bold", 10))
                btn.pack()
        if appcom[5] == "yae":
            window.geometry('300x250')
            window.columnconfigure(0, minsize=125)
            logo = PhotoImage(file = _read_metadata(metadata, appcom[6]))
            label = Label(window, image = logo)
            label.img_ref = logo
            label.place(x = 25, y = 75, width = 150)
            lbl = Label(window, text=_read_metadata(metadata, appcom[1]), font=("Arial Bold", 14))
            lbl.place(x = 25, y = 25, width = 170)
            lbl = Label(window, text=_read_metadata(metadata, appcom[2]), font=("Arial Bold", 12))
            lbl.place(x = 0, y = 50, width = 200)
            btn = Button(window, text=_read_metadata(metadata, appcom[3]), command=button1, font=("Arial Bold", 13))
            btn.place(x = 160, y = 165, width = 110)
            if appcom[4] != "false":
                btn = Button(window, text=_read_metadata(metadata, appcom[4]), command=exit, font=("Arial Bold", 10))
                btn.place(x = 170, y = 200, width = 100)
        window.mainloop()
    if(appcom[0] == "input_ui"):
        def button1():
            window.destroy()
            _mov_metadata(metadata, message.get(), appcom[3])
        window = Tk()
        window.title("IdenProgect")
        if appcom[4] == "default":
            window.geometry('250x250')
            window.columnconfigure(0, minsize=250)
            frame_top = LabelFrame(text="")
            frame_top.pack(padx=100, pady=30)
            message = StringVar()
            lbl = Label(window, text=_read_metadata(metadata, appcom[1]), font=("Arial Bold", 17))
            lbl.pack()
            message_entry = Entry(textvariable=message)
            message_entry.pack()
            btn = Button(window, text=_read_metadata(metadata, appcom[2]), command=button1, font=("Arial Bold", 13))
            btn.pack()
        if appcom[4] == "yae":
            window.geometry('300x250')
            window.columnconfigure(0, minsize=125)
            message = StringVar()
            logo = PhotoImage(file = _read_metadata(metadata, appcom[6]))
            label = Label(window, image = logo)
            label.img_ref = logo
            label.place(x = 25, y = 75, width = 150)
            lbl = Label(window, text=_read_metadata(metadata, appcom[1]), font=("Arial Bold", 14))
            lbl.place(x = 25, y = 25, width = 170)
            message_entry = Entry(textvariable=message)
            message_entry.place(x = 0, y = 50, width = 200)
            btn = Button(window, text=_read_metadata(metadata, appcom[2]), command=button1, font=("Arial Bold", 13))
            btn.place(x = 160, y = 165, width = 110)
            if appcom[5] != "false":
                btn = Button(window, text=_read_metadata(metadata, appcom[4]), command=exit, font=("Arial Bold", 10))
                btn.place(x = 170, y = 200, width = 100)
        window.mainloop()
    if(appcom[0] == "os_ui"):
        os_ui()

def os_ui():
	metadata = "explorer.metadata"
	def button3():
		_mov_metadata("iden.metadata", "false", 5)
		exit(0)
	def button2():
		window.destroy()
		_mov_metadata("iden.metadata", "false", 5)
		_mov_metadata(metadata, app_name.get(), app_id.get())
		returnsystem()
	def button1():
		window.destroy()
		_mov_metadata("iden.metadata", "true", 5)
		_mov_metadata("iden.metadata", _read_metadata(metadata, app_id.get()), 1)
	window = Tk()
	window.title("IdenProgect")  
	window.geometry('750x580')
	appname = 1

	for i in range(35):
		c = (i)//7
		r = (i)-(c*7)
		print(c, r)
		appname = _read_metadata(metadata, i)
		btn = Button(window, text=(appname + " (" + str(i) + ")"), font=("Arial Bold", 10), width=12, height=6, command=button1)
		btn.grid(column=r, row=c)

	btn = Button(window, text="App add", command=button2, width=9, font=("Arial Bold", 15))
	btn.grid(column=0, row=6)
	btn = Button(window, text="App start", command=button1, width=9, font=("Arial Bold", 15))
	btn.grid(column=1, row=6)
	app_name = StringVar()
	app_id = StringVar()
	app_name_entry = Entry(width=17, textvariable=app_name)
	app_name_entry.grid(column=3, row=6)
	app_id_entry = Entry(width=17, textvariable=app_id)
	app_id_entry.grid(column=2, row=6)
	btn = Button(window, text="Exit", command=button3, width=9, font=("Arial Bold", 15))
	btn.grid(column=4, row=6)
	btn = Button(window, text=("""Iden Nodes
""" + _read_metadata("iden.metadata", 4)), command=button3, width=9, font=("Arial Bold", 8))
	btn.grid(column=6, row=6)
	window.mainloop()