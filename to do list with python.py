#---------------------------importing the required modules---------------------------------#
from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do_list')
        self.root.geometry('720x500+300+150')
        
         
        #----------------------------------FILE IMAGES------------------------------------#

        #-------------------------------creaating a delete icon------------------------------------#
        self.delete_icon = PhotoImage(file='delete-image.png')

        #---------------------------------- adding an icon for the app---------------------------------#
        self.icon = PhotoImage(file='android-chrome-38x38.png')
        self.root.iconphoto(True,self.icon)
        #--------------------------------------labelling the app--------------------------------#
        self.label = Label(self.root, text='To-Do-List-App',
             font = 'arial, 25 bold', width=10, bd=5, bg='grey', fg='light blue')

        self.label.pack(side='top', fill='both')

        self.label2 = Label(self.root, text='Input Task below',
             font = 'arial, 10 italic bold', width=22, height=1, bd='5', bg='grey', fg='black')
        self.label2.place(x=30, y=170)

        self.label2 = Label(self.root, text='Tasks',
             font = 'arial, 20 bold', width=10, bd=5, bg='grey', fg='light blue')
        self.label2.place(x=400, y=60)
       
        self.main_frame = Frame(self.root ,bg='black')
        self.main_frame.place()

        #-----------------------------creating the a list box to display the list of tasks------------------------#
        self.main_text = Listbox(self.root, height=14, bd=2.5,bg='#32405b',fg='white', width=50, font= 'arial, 11  italic bold')
        self.main_text.place(x=300, y=120)

        #-------------------------------creating a textbox fot the user to enter tasks--------------------------------#
        self.textbox = Text(self.root, bd=5,height= 10 ,width= 25, font= 'arial, 10 bold' ,bg='#32405b', fg='royal blue')
        self.textbox.see(1.0)
        self.textbox.place(x=30, y= 200)


        #----------------------add task functionality-------------------------------------#
        
        def add():
            content = self.textbox.get(1.0,END)
            self.main_text.insert(END,content)
            with open('to-do-list-data-storage.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close() 
            self.textbox.delete(1.0,END)

        #-----------------creating functionality for the edit button------------------------------------#

        def edit():
            text_to_edit_index = self.main_text.curselection() 
            text_to_edit = self.main_text.get(text_to_edit_index)
            if text_to_edit is not None:
                self.textbox.insert(index= 1.0, chars=text_to_edit)
            else:
                pass
            
        #---------------enabling the script to open the data storage to delete data
            with open('to-do-list-data-storage.txt', 'r+') as f:
                edit_lines = f.readlines( )
                f.seek(0)
                for text in edit_lines:
                    item = str(text)
                    if item == text_to_edit:
                        f.reconfigure
                        'll'
                        f.write()
                        
        #----------------------adding functionality for the delete button---------------------------------------------#
        def delete():  
            delete = self.main_text.curselection() 
            look = self.main_text.get(delete)
            with open('to-do-list-data-storage.txt', 'r+') as f:
                new_f = f.readlines( )
                print(new_f)
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete)
        #---------------enabling the script to open the data storage to delete data
        with open('to-do-list-data-storage.txt') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close
        #-----------------------creating the buttons -----------------------------------#
        self.button = Button(self.root, text="Add task", font="serif, 10 bold italic",
             width=21, bd=5, bg= 'grey', fg= 'light blue',  command=add)
        self.button.place(x=30, y=55)

        self.button2 = Button(self.root, text="Edit task", font="serif, 10 bold italic",
             width=21, borderwidth=5, bg='grey', fg= 'light blue', command=edit)
        self.button2.place(x=30, y=92)


        self.button3 = Button(self.root, image=self.delete_icon, command=delete, borderwidth=0 )
        self.button3.place(x=470, y=390, )

def main() :
    root = Tk()
    ui = Todo(root)
    root.mainloop()
    

if __name__ == "__main__":
    main()