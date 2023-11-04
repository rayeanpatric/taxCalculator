import tkinter as tk
from tkinter import ttk

def add_widgets():
    
    standardDeduction_label = tk.Label(frame, text="Tax Calculator\n", font = ("Times New Roman", 16, "bold"), foreground="#060c1f")
    standardDeduction_label.grid(row=0, column=3, padx=10, pady=10, sticky = "n")

    # Create the Standard Deduction label and entry box
    standardDeduction_label = tk.Label(frame, text="Standard Deduction: ")
    standardDeduction_label.grid(row=1, column=2, padx=10, pady=10, sticky = "w")
    standardDeduction_entry = tk.Entry(frame)
    standardDeduction_entry.grid(row=1, column=6, padx=10, pady=10, columnspan=3)

    # Create the Total Income label and entry box
    totalIncome_label = tk.Label(frame, text="Total Income: ")
    totalIncome_label.grid(row=2, column=2, padx=10, pady=10, sticky = "w")
    totalIncome_entry = tk.Entry(frame)
    totalIncome_entry.grid(row=2, column=6, padx=10, pady=10, columnspan=3)

    # Create the Housing Rent Allowance label and entry box
    hra_label = tk.Label(frame, text="Housing rent Allowance:")
    hra_label.grid(row=3, column=2, padx=10, pady=10, sticky = "w")
    hra_entry = tk.Entry(frame)
    hra_entry.grid(row=3, column=6, padx=10, pady=10, columnspan=3)

    # Create the Co-Operation label and entry box
    coOperation_label = tk.Label(frame, text="Co-Operation Amount :")
    coOperation_label.grid(row=4, column=2, padx=10, pady=10, sticky = "w")
    coOperation_entry = tk.Entry(frame)
    coOperation_entry.grid(row=4, column=6, padx=10, pady=10, columnspan=3)

    # Create the GPF label and entry box
    gpf_label = tk.Label(frame, text="GPF Amount:")
    gpf_label.grid(row=5, column=2, padx=10, pady=10, sticky = "w")
    gpf_entry = tk.Entry(frame)
    gpf_entry.grid(row=5, column=6, padx=10, pady=10, columnspan=3)

    # Create the Child Tution label and entry box
    childTution_label = tk.Label(frame, text="Child Tution Amount:")
    childTution_label.grid(row=6, column=2, padx=10, pady=10, sticky = "w")
    childTution_entry = tk.Entry(frame)
    childTution_entry.grid(row=6, column=6, padx=10, pady=10, columnspan=3)

    # Create the lic label and entry box
    lic_label = tk.Label(frame, text="lic Amount:")
    lic_label.grid(row=7, column=2, padx=10, pady=10, sticky = "w")
    lic_entry = tk.Entry(frame)
    lic_entry.grid(row=7, column=6, padx=10, pady=10, columnspan=3)

    # Create the Housing Loan Principle label and entry box
    hlp_label = tk.Label(frame, text="Housing Loan Principle Amount:")
    hlp_label.grid(row=8, column=2, padx=10, pady=10, sticky = "w")
    hlp_entry = tk.Entry(frame)
    hlp_entry.grid(row=8, column=6, padx=10, pady=10, columnspan=3)

    # Create the Section 80CCC label and entry box
    section80CCC_label = tk.Label(frame, text="Section 80CCC Amount:")
    section80CCC_label.grid(row=9, column=2, padx=10, pady=10, sticky = "w")
    section80CCC_entry = tk.Entry(frame)
    section80CCC_entry.grid(row=9, column=6, padx=10, pady=10, columnspan=3)

    # Create the Section 80CCD label and entry box
    section80CCD_label = tk.Label(frame, text="Section 80CCD Amount:")
    section80CCD_label.grid(row=10, column=2, padx=10, pady=10, sticky = "w")
    section80CCD_entry = tk.Entry(frame)
    section80CCD_entry.grid(row=10, column=6, padx=10, pady=10, columnspan=3)

    # Create the PM Relief label and entry box
    pmRelief_label = tk.Label(frame, text="PM Relief Amount:")
    pmRelief_label.grid(row=11, column=2, padx=10, pady=10, sticky = "w")
    pmRelief_entry = tk.Entry(frame)
    pmRelief_entry.grid(row=11, column=6, padx=10, pady=10, columnspan=3)

    # Create the CM Relief label and entry box
    cmRelief_label = tk.Label(frame, text="CM Relief Amount:")
    cmRelief_label.grid(row=12, column=2, padx=10, pady=10, sticky = "w")
    cmRelief_entry = tk.Entry(frame)
    cmRelief_entry.grid(row=12, column=6, padx=10, pady=10, columnspan=3)

    # Create the hli label and entry box
    hli_label = tk.Label(frame, text="Housing Loan Interest Amount:")
    hli_label.grid(row=13, column=2, padx=10, pady=10, sticky = "w")
    hli_entry = tk.Entry(frame)
    hli_entry.grid(row=13, column=6, padx=10, pady=10, columnspan=3)

    # Create the Medical Claim label and entry box
    mediClaim_label = tk.Label(frame, text="Medical Claim:")
    mediClaim_label.grid(row=14, column=2, padx=10, pady=10, sticky = "w")
    mediClaim_entry = tk.Entry(frame)
    mediClaim_entry.grid(row=14, column=6, padx=10, pady=10, columnspan=3)

    # Create the Child Exception label and entry box
    childException_label = tk.Label(frame, text="Child Exception Amount:")
    childException_label.grid(row=15, column=2, padx=10, pady=10, sticky = "w")
    childException_entry = tk.Entry(frame)
    childException_entry.grid(row=15, column=6, padx=10, pady=10, columnspan=3)

    # Create the Advance Tax label and entry box
    advanceTax_label = tk.Label(frame, text="Advance Tax Paid:\n\n")
    advanceTax_label.grid(row=16, column=2, padx=10, pady=10, sticky = "w")
    advanceTax_entry = tk.Entry(frame)
    advanceTax_entry.grid(row=16, column=6, padx=10, pady=10, columnspan=3)

    # Create the tax label
    tax_label = tk.Label(frame, text="")
    tax_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Create the calculate button
    calculate_button = tk.Button(frame, text="Calculate")
    calculate_button.grid(row=17, column=3, columnspan=2, padx=10, pady=10)

root = tk.Tk()
root.wm_title("Tax Calculator")
root.geometry("600x500")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

canvas = tk.Canvas(root)
canvas.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

add_widgets()

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()