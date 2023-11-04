import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from customtkinter import CTkScrollbar

def add_widgets():
    
    standardDeduction_label = tk.Label(frame, text="Tax Calculator\n", font = ("Times New Roman", 18, "bold"), foreground="#6900EE")
    standardDeduction_label.grid(row=0, column=3, padx=10, pady=10, sticky = "")

    # Create the Standard Deduction label and entry box
    standardDeduction_label = tk.Label(frame, text="Standard Deduction: ", font = ("Calibri", 13, "normal"))
    standardDeduction_label.grid(row=1, column=2, padx=10, pady=10, sticky = "w")
    standardDeduction_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    standardDeduction_entry.grid(row=1, column=6, padx=10, pady=10, columnspan=3)

    # Create the Total Income label and entry box
    totalIncome_label = tk.Label(frame, text="Total Income: ", font = ("Calibri", 13, "normal"))
    totalIncome_label.grid(row=2, column=2, padx=10, pady=10, sticky = "w")
    totalIncome_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    totalIncome_entry.grid(row=2, column=6, padx=10, pady=10, columnspan=3)

    # Create the Housing Rent Allowance label and entry box
    hra_label = tk.Label(frame, text="Housing rent Allowance:", font = ("Calibri", 13, "normal"))
    hra_label.grid(row=3, column=2, padx=10, pady=10, sticky = "w")
    hra_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    hra_entry.grid(row=3, column=6, padx=10, pady=10, columnspan=3)

    # Create the Co-Operation label and entry box
    coOperation_label = tk.Label(frame, text="Co-Operation Amount :", font = ("Calibri", 13, "normal"))
    coOperation_label.grid(row=4, column=2, padx=10, pady=10, sticky = "w")
    coOperation_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    coOperation_entry.grid(row=4, column=6, padx=10, pady=10, columnspan=3)

    # Create the GPF label and entry box
    gpf_label = tk.Label(frame, text="GPF Amount:", font = ("Calibri", 13, "normal"))
    gpf_label.grid(row=5, column=2, padx=10, pady=10, sticky = "w")
    gpf_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    gpf_entry.grid(row=5, column=6, padx=10, pady=10, columnspan=3)

    # Create the Child Tution label and entry box
    childTution_label = tk.Label(frame, text="Child Tution Amount:", font = ("Calibri", 13, "normal"))
    childTution_label.grid(row=6, column=2, padx=10, pady=10, sticky = "w")
    childTution_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    childTution_entry.grid(row=6, column=6, padx=10, pady=10, columnspan=3)

    # Create the lic label and entry box
    lic_label = tk.Label(frame, text="LIC Amount:", font = ("Calibri", 13, "normal"))
    lic_label.grid(row=7, column=2, padx=10, pady=10, sticky = "w")
    lic_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    lic_entry.grid(row=7, column=6, padx=10, pady=10, columnspan=3)

    # Create the Housing Loan Principle label and entry box
    hlp_label = tk.Label(frame, text="Housing Loan Principle Amount:", font = ("Calibri", 13, "normal"))
    hlp_label.grid(row=8, column=2, padx=10, pady=10, sticky = "w")
    hlp_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    hlp_entry.grid(row=8, column=6, padx=10, pady=10, columnspan=3)

    # Create the Section 80CCC label and entry box
    section80CCC_label = tk.Label(frame, text="Section 80CCC Amount:", font = ("Calibri", 13, "normal"))
    section80CCC_label.grid(row=9, column=2, padx=10, pady=10, sticky = "w")
    section80CCC_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    section80CCC_entry.grid(row=9, column=6, padx=10, pady=10, columnspan=3)

    # Create the Section 80CCD label and entry box
    section80CCD_label = tk.Label(frame, text="Section 80CCD Amount:", font = ("Calibri", 13, "normal"))
    section80CCD_label.grid(row=10, column=2, padx=10, pady=10, sticky = "w")
    section80CCD_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    section80CCD_entry.grid(row=10, column=6, padx=10, pady=10, columnspan=3)

    # Create the PM Relief label and entry box
    pmRelief_label = tk.Label(frame, text="PM Relief Amount:", font = ("Calibri", 13, "normal"))
    pmRelief_label.grid(row=11, column=2, padx=10, pady=10, sticky = "w")
    pmRelief_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    pmRelief_entry.grid(row=11, column=6, padx=10, pady=10, columnspan=3)

    # Create the CM Relief label and entry box
    cmRelief_label = tk.Label(frame, text="CM Relief Amount:", font = ("Calibri", 13, "normal"))
    cmRelief_label.grid(row=12, column=2, padx=10, pady=10, sticky = "w")
    cmRelief_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    cmRelief_entry.grid(row=12, column=6, padx=10, pady=10, columnspan=3)

    # Create the hli label and entry box
    hli_label = tk.Label(frame, text="Housing Loan Interest Amount:", font = ("Calibri", 13, "normal" ))
    hli_label.grid(row=13, column=2, padx=10, pady=10, sticky = "w",)
    hli_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    hli_entry.grid(row=13, column=6, padx=10, pady=10, columnspan=3)

    # Create the Medical Claim label and entry box
    mediClaim_label = tk.Label(frame, text="Medical Claim:", font = ("Calibri", 13, "normal"))
    mediClaim_label.grid(row=14, column=2, padx=10, pady=10, sticky = "w")
    mediClaim_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    mediClaim_entry.grid(row=14, column=6, padx=10, pady=10, columnspan=3)

    # Create the Child Exception label and entry box
    childException_label = tk.Label(frame, text="Child Exception Amount:", font = ("Calibri", 13, "normal"))
    childException_label.grid(row=15, column=2, padx=10, pady=10, sticky = "w")
    childException_entry = tk.Entry(frame, border=1, font = ("Calibri", 12, "normal"), width=15, justify="left")
    childException_entry.grid(row=15, column=6, padx=10, pady=10, columnspan=3)

    # Create the Advance Tax label and entry box
    advanceTax_label = tk.Label(frame, text="Advance Tax Paid:\n\n", font = ("Calibri", 13, "normal"))
    advanceTax_label.grid(row=16, column=2, padx=10, pady=10, sticky = "w")
    advanceTax_entry = tk.Entry(frame, font = ("Calibri", 12, "normal"), width=15, justify="left")
    advanceTax_entry.grid(row=16, column=6, padx=10, pady=10, columnspan=3)

    # Create the tax label
    tax_label = tk.Label(frame, text="")
    tax_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    tax_label = tk.Label(frame, text="")
    tax_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10) 

    # Create the calculate button
    calculate_button = tk.Button(frame, text="Calculate", width=15, height=2)
    calculate_button.grid(row=17, column=3, columnspan=2, padx=10, pady=10)

root = ctk.CTk()

root.wm_title("Tax Calculator")
root.wm_geometry("600x600")
#root.wm_resizable(False, False)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

canvas = ctk.CTkCanvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = CTkScrollbar(root, command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

add_widgets()

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()