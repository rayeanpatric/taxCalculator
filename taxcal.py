import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import CTkScrollbar

# Create a function to calculate tax
def calculate_tax(standardDeduction_entry, totalIncome_entry, hra_entry, cooperation_entry, 
                  gpf_entry, childTution_entry, lic_entry, hlp_entry, section80CCC_entry, 
                  section80CCD_entry, pmRelief_entry, cmRelief_entry, hli_entry, 
                  mediClaim_entry, childException_entry, advanceTax_entry):
    
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

def add_widgets():
    
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
    calculate_button = tk.Button(frame, text="Calculate", width=12, height=1, background="#6900EE", foreground="white", font = ("Calibri", 15, "bold"), bd=1)
    calculate_button.grid(row=17, column=3, columnspan=2, padx=10, pady=10)

# Create the root window
root = ctk.CTk()

# Set the root window attributes
root.wm_title("Tax Calculator")
root.wm_geometry("800x750")
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
