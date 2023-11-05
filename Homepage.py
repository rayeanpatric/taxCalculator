from customtkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import scrolledtext as st
from tkinter import messagebox
from customtkinter import CTkScrollbar
from tkinter import BOTH, ttk
import csv

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

    def calculateTax():
        # Get the values from the entry boxes
        standardDeduction = float(standardDeduction_entry.get())
        totalIncome = float(totalIncome_entry.get())
        hra = float(hra_entry.get())
        cooperation = float(cooperation_entry.get())
        gpf = float(gpf_entry.get())
        childTution = float(childTution_entry.get())
        lic  = float(lic_entry.get())
        hlp = float(hlp_entry.get())
        section80CCC = float(section80CCC_entry.get())
        section80CCD = float(section80CCD_entry.get())
        pmRelief = float(pmRelief_entry.get())
        cmRelief = float(cmRelief_entry.get())
        hli = float(hli_entry.get())
        mediClaim = float(mediClaim_entry.get())
        childException = float(childException_entry.get())
        advanceTax = float(advanceTax_entry.get())

        Section80C = gpf + childTution + lic + hlp
        StandardException = Section80C + section80CCC + section80CCD

        if StandardException >= 150000:
            StandardException = 150000

        if hli >= 200000:
            hli = 200000

        if mediClaim >= 25000:
            mediClaim = 25000

        if childException >= 75000:
            childException = 75000

        DeductedIncome = totalIncome - (standardDeduction + hra + cooperation + pmRelief + cmRelief + StandardException + hli + mediClaim + childException)
        print(DeductedIncome)
        global final_tax

        root = CTk()

        root.wm_geometry(f"400x270")
        root.wm_iconbitmap("icon.ico")
        root.wm_title("Final Tax")
        root.wm_resizable(False, False)

        canvas = tk.Canvas(root)
        canvas.pack(fill=BOTH)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')
        ttk.Label(frame, text="\n\tFinal Amount", font=("san serif", 12, "bold"), foreground="purple", anchor='center').pack()

        if DeductedIncome <= 250000:
                final_tax = 0
                ttk.Label(frame, text=f"\n\tYour taxable amt.: Rs. {final_tax}\n", font=("san serif", 12, "normal"), anchor='center').pack()

        elif 250000 < DeductedIncome < 500001:
            ti7 = DeductedIncome - 250000
            ti8 = 0.05 * ti7
            final_tax = (ti8) + ((ti8) * 0.04)
            ttk.Label(frame, text=f"\n\tYour taxable amt.: Rs. {int(round(final_tax, 1))}\n", font=("san serif", 12, "normal"), anchor='center').pack()

        elif 500000 < DeductedIncome < 1000001:
                      ti7 = DeductedIncome - 250000
                      if ti7 > 250000:
                          ti8 = ti7 - 250000
                          ti9 = ti8 + 12500
                          if ti8 > 250000:
                              ti9 = ti8 - 250000
                              tx1 = 0.2 * ti9
                              final_tax = ((ti9 + tx1) + ((ti9 + tx1) * 0.04))


                              ttk.Label(frame, text=f"\nYour taxable amt.: Rs. {int(round(final_tax, 1))}", font=("san serif", 12, "normal"), anchor='center').pack()

                          else:
                              final_tax = ti9 + ((ti9) * 0.04)
                              ttk.Label(frame,
                                 text=f"\nYour taxable amt.: Rs. {int(round(final_tax, 1))}",
                                 font=("san serif", 12, "normal"), anchor='center').pack()


        else:

            ti7 = DeductedIncome - 1000000
            ti8 = (ti7 * 0.3)
            ti9 = (ti8 + 112500) * 0.04
            final_tax = (ti8 + ti9 + 112500)
            ttk.Label(frame, text=f"\n\tYour taxable amt.: Rs. {int(round(final_tax, 1))}\n", font=("san serif", 12, "normal"), anchor='center').pack()

        ft = final_tax - float(advanceTax)
        Positive_ft = -1 * ft

        if ft < 0:
            ttk.Label(frame, text=f"\n\tThe amt. to be returned to you: Rs.{int(round(Positive_ft, 1))}", font=("san serif", 12, "normal"), anchor='center').pack()
        elif ft == 0:
            ttk.Label(frame, text="\n\tThe amt. to be paid by you: Rs. 0", font=("san serif", 12, "normal"), anchor='center').pack()
        else:
            ttk.Label(frame, text=f"\n\tThe amt to be paid by you: Rs. {int(round(ft, 1))}", font=("san serif", 12, "normal"), anchor='center').pack()

        field_names = ['Col1', 'Col2', 'Col3', 'Col4', 'Col5', 'Col6', 'Col7','Col8', 'Col9', 'Col10',  'Col11', 'Col12', 'Col13',  'Col14', 'Col15', 'Col16', 'Col17']
          
        dict = {'Col1': standardDeduction,
                  'Col2': totalIncome,
                  'Col3': hra,
                  'Col4': cooperation,
                  'Col5': gpf,
                  'Col6': childTution,
                  'Col7': lic,
                  'Col8': hlp,
                  'Col9': section80CCC,
                  'Col10': section80CCD,
                  'Col11': pmRelief,
                  'Col12': cmRelief,
                  'Col13': hli,
                  'Col14': mediClaim,
                  'Col15': childException,
                  'Col16': advanceTax,
                  'Col17': ft}
        
        with open('History.csv', 'a', newline='', encoding='utf8') as f:
            writer = csv.DictWriter(f, field_names)
            writer.writerow(dict)

        root.mainloop()

    def add_widgets():

        global standardDeduction_entry
        global totalIncome_entry
        global hra_entry
        global cooperation_entry 
        global gpf_entry
        global childTution_entry
        global lic_entry
        global hlp_entry
        global section80CCC_entry
        global section80CCD_entry
        global pmRelief_entry
        global cmRelief_entry
        global hli_entry
        global mediClaim_entry
        global childException_entry
        global advanceTax_entry

        standardDeduction_label = ttk.Label(frame, text="Tax Calculator\n", font = ("Times New Roman", 18, "bold"), foreground="#6900EE")
        standardDeduction_label.grid(row=0, column=3, padx=10, pady=10, sticky = "")

        # Create the Standard Deduction label and entry box
        standardDeduction_label = ttk.Label(frame, text="Standard Deduction: ", font = ("Calibri", 13, "normal"))
        standardDeduction_label.grid(row=1, column=2, padx=10, pady=10, sticky = "w")
        standardDeduction_entry = ttk.Entry(frame, font = ("Calibri", 12, "normal"), width=18, justify="left")
        standardDeduction_entry.grid(row=1, column=6, padx=10, pady=10, columnspan=3)

        # Create the Total Income label and entry box
        totalIncome_label = ttk.Label(frame, text="Total Income: ", font = ("Calibri", 13, "normal"))
        totalIncome_label.grid(row=2, column=2, padx=10, pady=10, sticky = "w")
        totalIncome_entry = ttk.Entry(frame, font = ("Calibri", 12, "normal"), width=18, justify="left")
        totalIncome_entry.grid(row=2, column=6, padx=10, pady=10, columnspan=3)

        # Create the Housing Rent Allowance label and entry box
        hra_label = ttk.Label(frame, text="Housing rent Allowance:", font = ("Calibri", 13, "normal"))
        hra_label.grid(row=3, column=2, padx=10, pady=10, sticky = "w")
        hra_entry = ttk.Entry(frame, font = ("Calibri", 12, "normal"), width=18, justify="left")
        hra_entry.grid(row=3, column=6, padx=10, pady=10, columnspan=3)

        # Create the Co-Operation label and entry box
        cooperation_label = ttk.Label(frame, text="Co-Operation Amount :", font = ("Calibri", 13, "normal"))
        cooperation_label.grid(row=4, column=2, padx=10, pady=10, sticky = "w")
        cooperation_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        cooperation_entry.grid(row=4, column=6, padx=10, pady=10, columnspan=3)

        # Create the GPF label and entry box
        gpf_label = ttk.Label(frame, text="GPF Amount:", font = ("Calibri", 13, "normal"))
        gpf_label.grid(row=5, column=2, padx=10, pady=10, sticky = "w")
        gpf_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        gpf_entry.grid(row=5, column=6, padx=10, pady=10, columnspan=3)

        # Create the Child Tution label and entry box
        childTution_label = ttk.Label(frame, text="Child Tution Amount:", font = ("Calibri", 13, "normal"))
        childTution_label.grid(row=6, column=2, padx=10, pady=10, sticky = "w")
        childTution_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        childTution_entry.grid(row=6, column=6, padx=10, pady=10, columnspan=3)

        # Create the lic label and entry box
        lic_label = ttk.Label(frame, text="LIC Amount:", font = ("Calibri", 13, "normal"))
        lic_label.grid(row=7, column=2, padx=10, pady=10, sticky = "w")
        lic_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        lic_entry.grid(row=7, column=6, padx=10, pady=10, columnspan=3)

        # Create the Housing Loan Principle label and entry box
        hlp_label = ttk.Label(frame, text="Housing Loan Principle Amount:", font = ("Calibri", 13, "normal"))
        hlp_label.grid(row=8, column=2, padx=10, pady=10, sticky = "w")
        hlp_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        hlp_entry.grid(row=8, column=6, padx=10, pady=10, columnspan=3)

        # Create the Section 80CCC label and entry box
        section80CCC_label = ttk.Label(frame, text="Section 80CCC Amount:", font = ("Calibri", 13, "normal"))
        section80CCC_label.grid(row=9, column=2, padx=10, pady=10, sticky = "w")
        section80CCC_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        section80CCC_entry.grid(row=9, column=6, padx=10, pady=10, columnspan=3)

        # Create the Section 80CCD label and entry box
        section80CCD_label = ttk.Label(frame, text="Section 80CCD Amount:", font = ("Calibri", 13, "normal"))
        section80CCD_label.grid(row=10, column=2, padx=10, pady=10, sticky = "w")
        section80CCD_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        section80CCD_entry.grid(row=10, column=6, padx=10, pady=10, columnspan=3)

        # Create the PM Relief label and entry box
        pmRelief_label = ttk.Label(frame, text="PM Relief Amount:", font = ("Calibri", 13, "normal"))
        pmRelief_label.grid(row=11, column=2, padx=10, pady=10, sticky = "w")
        pmRelief_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        pmRelief_entry.grid(row=11, column=6, padx=10, pady=10, columnspan=3)

        # Create the CM Relief label and entry box
        cmRelief_label = ttk.Label(frame, text="CM Relief Amount:", font = ("Calibri", 13, "normal"))
        cmRelief_label.grid(row=12, column=2, padx=10, pady=10, sticky = "w")
        cmRelief_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        cmRelief_entry.grid(row=12, column=6, padx=10, pady=10, columnspan=3)

        # Create the hli label and entry box
        hli_label = ttk.Label(frame, text="Housing Loan Interest Amount:", font = ("Calibri", 13, "normal" ))
        hli_label.grid(row=13, column=2, padx=10, pady=10, sticky = "w",)
        hli_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        hli_entry.grid(row=13, column=6, padx=10, pady=10, columnspan=3)

        # Create the Medical Claim label and entry box
        mediClaim_label = ttk.Label(frame, text="Medical Claim:", font = ("Calibri", 13, "normal"))
        mediClaim_label.grid(row=14, column=2, padx=10, pady=10, sticky = "w")
        mediClaim_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        mediClaim_entry.grid(row=14, column=6, padx=10, pady=10, columnspan=3)

        # Create the Child Exception label and entry box
        childException_label = ttk.Label(frame, text="Child Exception Amount:", font = ("Calibri", 13, "normal"))
        childException_label.grid(row=15, column=2, padx=10, pady=10, sticky = "w")
        childException_entry = ttk.Entry(frame,  font = ("Calibri", 12, "normal"), width=18, justify="left")
        childException_entry.grid(row=15, column=6, padx=10, pady=10, columnspan=3)

        # Create the Advance Tax label and entry box
        advanceTax_label = ttk.Label(frame, text="Advance Tax Paid:", font = ("Calibri", 13, "normal"))
        advanceTax_label.grid(row=16, column=2, padx=10, pady=10, sticky = "w")
        advanceTax_entry = ttk.Entry(frame, font = ("Calibri", 12, "normal"), width=18, justify="left")
        advanceTax_entry.grid(row=16, column=6, padx=10, pady=10, columnspan=3)

        # Create the tax label
        space = ttk.Label(frame, text="\t")
        space.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        space = ttk.Label(frame, text="")
        space.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        space = ttk.Label(frame, text="\n\n\n\n\n")
        space.grid(row=17, column=0, columnspan=8, padx=10, pady=10)

        # Create the calculate button
        calculate_button = tk.Button(frame, text="Calculate", width=12, height=1, background="#6900EE", foreground="white", font = ("Calibri", 15, "bold"), bd=1, command=calculateTax)
        calculate_button.grid(row=17, column=3, columnspan=2, padx=10, pady=10)

    # Create the root window
    root = CTk()

    # Set the root window attributes
    root.wm_title("Tax Calculator")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    # Calculate the center of the screen
    x = int(width / 2)
    y = int(height / 2)

    root.wm_geometry(f"800x750")
    root.wm_resizable(False, False)
    root.iconbitmap("icon.ico")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    canvas = tk.Canvas(root)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Create the scrollbar
    scrollbar = CTkScrollbar(root, command=canvas.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    add_widgets()

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()
    

def about():
    About = tk.Tk()
    About.iconbitmap('icon.ico')
    About.wm_title("About")
    About.wm_geometry("648x500+650+250")
    About.wm_resizable(False, False)
    
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
    documentation.wm_resizable(False, False)
    
    # Create a ScrolledText widget
    text = st.ScrolledText(documentation, font=("Times New Roman", 15))
    text.pack(fill=tk.BOTH, expand=True)

    text.insert(tk.INSERT, """
    \t\t\t     Documentation                

""")
    
    documentation.mainloop()

def closeWindow():
    message_box = messagebox.askquestion("Exit", "Do you want to exit?")
    if message_box == "yes":
        root.destroy()
    else:
        pass

#defing Buttons
button = tk.Button(root, text="Tax Calculator", background="#FFE5B4", border=0, borderwidth=0 ,width=50, height=3, font=("Calibri", 15, "bold"), command=taxCal)
button.place(x=300, y=270)

button = tk.Button(root, text="About", background="#FFE5B4", border=0, width=50, borderwidth=0 ,height=3, font=("Calibri", 15, "bold"), command=about)
button.place(x=300, y=390)

button = tk.Button(root, text="Documentation", background="#FFE5B4", border=0, borderwidth=0 ,width=50, height=3, font=("Calibri", 15, "bold"), command=documentation)
button.place(x=300, y=510)

button = tk.Button(root, text="Exit", background="#FFE5B4", width=50, border=0, borderwidth=0 ,height=3, font=("Calibri", 15, "bold"), command=closeWindow)
button.place(x=300, y=630)

root.mainloop()