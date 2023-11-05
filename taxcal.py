import tkinter as tk
from tkinter import BOTH, ttk
import customtkinter as ctk
from customtkinter import CTkScrollbar

# Create a function to calculate tax
def calculateTax():
    # Get the values from the entry boxes
    standardDeduction = float(standardDeduction_entry.get())
    totalIncome = float(totalIncome_entry.get())
    hra = float(hra_entry.get())
    cooperation = int(cooperation_entry.get())
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

    root = ctk.CTk()
    
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

    elif DeductedIncome <= 750000: 
        final_tax = (((DeductedIncome - 500000 * 10) / 100)+ 12500 + ((((DeductedIncome - 500000 * 10) / 100)+ 12500) * 0.04))
        ttk.Label(frame, text=f"\nYour taxable amt.: Rs. {int(round(final_tax, 1))}", font=("san serif", 12, "normal"), anchor='center').pack()
                      
    elif DeductedIncome <= 1000000: 
        final_tax = (((DeductedIncome - 750000 * 15) / 100)+ 37500 + ((((DeductedIncome - 750000 * 15) / 100)+ 37500) * 0.04))
        ttk.Label(frame, text=f"\nYour taxable amt.: Rs. {int(round(final_tax, 1))}", font=("san serif", 12, "normal"), anchor='center').pack()

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
root = ctk.CTk()

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
