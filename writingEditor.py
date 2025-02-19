#Skeleton. Non-functional as of 2/19/2025
# Text Editor Specifically for writing Disjointed Pieces and other things

    # https://tkdocs.com/tutorial/fonts.html
    # https://tkdocs.com/tutorial/text.html
    # https://tkinterpython.top/menustoolbars/
    # https://www.pythontutorial.net/tkinter/tkinter-menubutton/
    # https://pythontutorial.net/tkinter/tkinter-menu/
    # https://www.pythontutorial.net/tkinter/tkinter-optionmenu/
    # https://www.pythontutorial.net/tkinter/tkinter-notebook/

#all the imports
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

#main window
main = Tk()
main.geometry('800x600')
main.title('Bad Writing')

menubar= Menu(main, tearoff=0)
main.configure(menu=menubar)


#Creating the Notebook
notebook = ttk.Notebook(main, height=550, width=750, padding = '3 3 3 3')
notebook.grid(row=1, column=0, pady=10, padx = 10,  sticky=(N,W,S,E))


## /* Need the Grid Equivalent of expand = true!*/

#FUNCTIONS

#Creating a Sections. Can be the ScrolledText directly b/c it extends frame
section2 = ScrolledText(notebook, relheight=.90, relwidth=.8, padx=5, pady=5, wrap="word")
notebook.add(section1, text = 'name')


# MENU BAR -> https://tkinterpython.top/menustoolbars/
    
    #Requires an image pack. Should be able to access native image guide
    #FILE

    #UNDO Menu help -> https://tkdocs.com/tutorial/text.html
    
    #MORE SECTIONS
    
# TOOLBAR
        #Need to figure out how to access native icons so that I'm not double dipping
            # Required functions:
                # to store all icons into a searchable array
                # Create a new secgion and add to notebook
            # Create a library?
                # for a built-in 
                    # tool bar
                    # menu bar
                    # individual pieces as well
            
toolbar = Frame(main, bd=1, relief=RAISED)
    
    #Font, color, bold,  word count
Button(toolbar, image= ___ or text= '', relief = FLAT/RAISED, command = ___)
Button.grid(---)
        
        #Set the color as a mini frame? With the highlight and text color as the bg colors w/a function?
