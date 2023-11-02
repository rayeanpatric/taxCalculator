from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext as st

root = CTk()

# Set window title, icon and size
root.wm_title("Tax Calculator")
root.iconbitmap("icon.ico")
root.wm_geometry("1920x1080+0+0")
root.wm_resizable(True, False)

# Load and resize background image
img = Image.open("background.png")
img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

# Set the background image
root.configure(background='black')
root.attributes('-transparentcolor', 'black')
root.geometry("%dx%d+0+0" % (img.width(), img.height()))
canvas = CTkCanvas(root, width=img.width(), height=img.height(), highlightthickness=0)
canvas.pack()
canvas.create_image(0, 0, image=img, anchor='nw')

# Defining Functions

def taxCal():
    #Creating a Tax Calculator window
    tax = tk.Tk()
    tax.iconbitmap('icon.ico')
    tax.wm_title('Tax Calculator')
    tax.wm_geometry("1920x1080+0+0")
    tax.wm_resizable(0, 0)

    #Defining Widgets
    

def about():
    About = tk.Tk()
    About.iconbitmap('icon.ico')
    About.wm_title("About")
    About.wm_geometry("648x500+650+250")
    About.wm_resizable(0, 0)
    
    # Create a ScrolledText widge   t
    text = st.ScrolledText(About, font=("Times New Roman", 15))
    text.pack(fill=tk.BOTH, expand=True)
    
    # Insert text into the ScrolledText widget
    text.insert(tk.INSERT, """
    \t\t\t           About
    
     To use Pytax calculator you need to open the program and when opened a 
     screen appears with few options namely:
                
     a) Tax calculator : This button can be pressed to calculate your tax amount.
    
     b) About : This is the section which you are in right now. this section helps 
                you with the flow of instructions to run the program and calculate tax
    
     c) documentation : This is basically a section which contains information of 
                developers who developed it.
                    
     How to use the application ?
                
      The following has to be inputted by the user : 
    
      1) By default the standard index is fixed as 50,000 rupees and the users 
         can alter it if needed.
                
      2) The users have to input their gross salary,housing rent
         allowance,tax on employment.
                
      3) 3 sections based on laws. users are eligible to calculate tax and get
         a partial deduction in their tax based on these sections namely :
    
             a) Section 80C (GPF, Child tuition fee, LIC amount, HBA principal)
             b) Section 80CCC
             c) Section 80CCD
                
      4) PM and CM relief fund:(users can enter the amount that they are 
         willing to donate to CM and PM relief fund).
                
      5) Housing Loan Interest, Medical Claims, Special Child Exceptions is 
         to be finally entered and click on the Calculate button for the 
         calculation.
                
     For feedback Pls visit codeshack.wix.com/pytax
                
                    \t\t             Copyright © 2023
                
                """)
    
    About.mainloop()

def documentation():

    #create a root window
    documentation = tk.Tk()
    documentation.iconbitmap('icon.ico')
    documentation.wm_title("Documentation")
    documentation.wm_geometry("648x500+650+250")
    documentation.wm_resizable(0, 0)
    
    # Create a ScrolledText widget
    text = st.ScrolledText(documentation, font=("Times New Roman", 15))
    text.pack(fill=tk.BOTH, expand=True)

    text.insert(tk.INSERT, """
    \t\t\t     Documentation                

""")
    
    documentation.mainloop()

def closeWindow():
    message_box = tk.messagebox.askquestion("Exit", "Do you want to exit?")
    if message_box == "yes":
        root.destroy()
    else:
        pass

#defing Buttons
button = tk.Button(root, text="Tax Calculator", background="#FFE5B4", border=None, borderwidth=0 ,width=50, height=3, font=("Calibri", 15, "bold"))
button.place(x=300, y=270)

button = tk.Button(root, text="About", background="#FFE5B4", border=None, width=50, borderwidth=0 ,height=3, font=("Calibri", 15, "bold"), command=about)
button.place(x=300, y=390)

button = tk.Button(root, text="Documentation", background="#FFE5B4", border=None, borderwidth=0 ,width=50, height=3, font=("Calibri", 15, "bold"), command=documentation)
button.place(x=300, y=510)

button = tk.Button(root, text="Exit", background="#FFE5B4", width=50, border=None, borderwidth=0 ,height=3, font=("Calibri", 15, "bold"), command=closeWindow)
button.place(x=300, y=630)

root.mainloop()