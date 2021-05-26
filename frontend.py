from tkinter import *
from backend import Database

database=Database("books.db")               # creating an object & passing parameter db name

class Window(object):

    def __init__(self,window):

        self.window = window

        self.window.wm_title("BookStore")


        l1=Label(window,text="Title")       # Label Method to set label 
        l1.grid(row=0,column=0)

        l2=Label(window,text="Author")
        l2.grid(row=0,column=2)

        l3=Label(window,text="Year")
        l3.grid(row=1,column=0)

        l4=Label(window,text="ISBN")
        l4.grid(row=1,column=2)

        self.title_text=StringVar()                          # creating object with datatype
        self.e1=Entry(window,textvariable=self.title_text)   # Entry Method is use to take input # textvariable parameter takes input of special datatype
        self.e1.grid(row=0,column=1)

        self.author_text=StringVar()
        self.e2=Entry(window,textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e3=Entry(window,textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        self.list1=Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)

        sb1=Scrollbar(window)                            # Creating Scrollbar by using Scrollbar() method        
        sb1.grid(row=2,column=2,rowspan=6)

        #Appling scroll bar to our listbox
        self.list1.configure(yscrollcommand=sb1.set)     #Apply configure method to list1  #(yscrollcommand=sb1.set) = means that vertical scrollbar along the y-axis
        sb1.configure(command=self.list1.yview)          #Apply configure method to sb1    #(command=list1.yview) = means when you scroll the bar the vertical view of the list will change.

        # binding
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)     # tkinter library -> bind() is use to bind a function to a widget event. 

        b1=Button(window,text="View all", width=12,command=self.view_command)     # Creating Button # command parameter connects database functions to button
        b1.grid(row=2,column=3)

        b2=Button(window,text="Search entry", width=12,command=self.search_command)    # Commanad = is use to connect database with front end
        b2.grid(row=3,column=3)

        b3=Button(window,text="Add entry", width=12,command=self.add_command)     # we cannot put here insert() function directly so we have to make here that fuction and pass here that function i.e. insert_command or add_command
        b3.grid(row=4,column=3)

        b4=Button(window,text="Update selected", width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window,text="Delete selected", width=12,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window,text="Close", width=12,command=window.destroy)          # command=window.destroy --> will close the window
        b6.grid(row=7,column=3)

    def get_selected_row(self,event):                # used to click on row in listbox and that row should get selected and displayed in inputbox.
        index=self.list1.curselection()[0]           # id = index[0] in tuple
        self.selected_tuple=self.list1.get(index)    # From the listbox get the tuple with index x
        											 # selected_tuple will get whole row or tuple of the selected index i.e of that row which we click in listbox
        #selected_tuple should be filled in Entry box
        self.e1.delete(0,END)                        # DELETE previous values in entry box
        self.e1.insert(END,self.selected_tuple[1])   # title = index[1] in tuple
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])   # author = index[2] in tuple
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])
        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])

    def view_command(self):                          # this fuctions is used in button's command parameter
        self.list1.delete(0,END)                     # Delete all previous rows in list1 from (0,END) i.e index 0 to end
        for row in database.view():                  # we iterate through tuple  # database.view() is equivalent to print(view()) in backend.py
            self.list1.insert(END,row)               # we insert tuples in list or listbox  # insert(END,row) = new rows will put at the end of the list.

    def search_command(self):                       
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):    #title_text is text that user inputs in the entry wigets. .get()will output it(get it)
            self.list1.insert(END,row)               # will insert & display in listbox 

    def add_command(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))       # (END,The values that user enter in tuple () to get all values in one row)

    def delete_command(self):
        database.delete(self.selected_tuple[0])       # AS delete(id) we want id as parameter and that parameter is given to us by get_selected_row() function as index 1 or 2 or something as a id of selected row

    def update_command(self):                         # As update(id,title,author,year,isbn)
        database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())

window=Tk()
Window(window)
window.mainloop()
