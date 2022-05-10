from tkinter import * 

#Enviroment setup as window for root
root = Tk()
root.title("Translator")

#Functions
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
 

#Structute of GUI
label1 = Label(root,text = "Translation starts here")
but_list  = Button(root, text = "Languages", padx = 20, pady = 20, command = openNewWindow)
label2 = Label(root,text = "You said:")
entry = Entry(root, width = 50, borderwidth = 5)

#Grid in the system
label1.grid(row = 0, column = 0)
but_list.grid(row = 1, column = 0)
entry.grid(row = 2, column = 0)



#Packing it on the screen
#my.pack()
#my1.pack()


#The loop
root.mainloop()
