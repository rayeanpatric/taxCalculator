import tkinter as tk

# Create a function to calculate tax
def calculate_tax():
    # Get the values from the entry boxes
    standardDeduction = float(standardDeduction_entry.get())
    totalIncome = float(totalIncome_entry.get())
    hra = float(hra_entry.get())
    coOperation = int(coOperation_entry.get())
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

    # Calculate the taxable income
    # taxable_income = income - expenses - deductions - (dependents * 2000)

    # Calculate the tax
    # tax = taxable_income * (tax_rate / 100)

    # Update the tax label
    # tax_label.config(text=f"${tax:.2f}")

# Create the main window
root = tk.Tk()

# Set the window title
root.wm_title("Tax Calculator")

# Set the window size
root.wm_geometry("1920x1080+0+0")

# Create the Tax Calculator label
standardDeduction_label = tk.Label(root, text="Tax Calculator", font = ("Times New Roman", 16, "bold"), foreground="#060c1f")
standardDeduction_label.grid(row=0, column=0, padx=10, pady=10)

# Create the Standard Deduction label and entry box
standardDeduction_label = tk.Label(root, text="Standard Deduction: ")
standardDeduction_label.grid(row=1, column=0, padx=10, pady=10)
standardDeduction_entry = tk.Entry(root)
standardDeduction_entry.grid(row=1, column=2, padx=10, pady=10, columnspan=3)

# Create the Total Income label and entry box
totalIncome_label = tk.Label(root, text="Total Income: ")
totalIncome_label.grid(row=2, column=0, padx=10, pady=10)
totalIncome_entry = tk.Entry(root)
totalIncome_entry.grid(row=2, column=2, padx=10, pady=10, columnspan=3)

# Create the Housing Rent Allowance label and entry box
hra_label = tk.Label(root, text="Housing rent Allowance:")
hra_label.grid(row=3, column=0, padx=10, pady=10)
hra_entry = tk.Entry(root)
hra_entry.grid(row=3, column=2, padx=10, pady=10, columnspan=3)

# Create the Co-Operation label and entry box
coOperation_label = tk.Label(root, text="Co-Operation Amount :")
coOperation_label.grid(row=4, column=0, padx=10, pady=10)
coOperation_entry = tk.Entry(root)
coOperation_entry.grid(row=4, column=2, padx=10, pady=10, columnspan=3)

# Create the GPF label and entry box
gpf_label = tk.Label(root, text="GPF Amount:")
gpf_label.grid(row=5, column=0, padx=10, pady=10)
gpf_entry = tk.Entry(root)
gpf_entry.grid(row=5, column=2, padx=10, pady=10, columnspan=3)

# Create the Child Tution label and entry box
childTution_label = tk.Label(root, text="Child Tution Amount:")
childTution_label.grid(row=6, column=0, padx=10, pady=10)
childTution_entry = tk.Entry(root)
childTution_entry.grid(row=6, column=2, padx=10, pady=10, columnspan=3)

# Create the lic label and entry box
lic_label = tk.Label(root, text="lic Amount:")
lic_label.grid(row=7, column=0, padx=10, pady=10)
lic_entry = tk.Entry(root)
lic_entry.grid(row=7, column=2, padx=10, pady=10, columnspan=3)

# Create the Housing Loan Principle label and entry box
hlp_label = tk.Label(root, text="Housing Loan Principle Amount:")
hlp_label.grid(row=8, column=0, padx=10, pady=10)
hlp_entry = tk.Entry(root)
hlp_entry.grid(row=8, column=2, padx=10, pady=10, columnspan=3)

# Create the Section 80CCC label and entry box
section80CCC_label = tk.Label(root, text="Section 80CCC Amount:")
section80CCC_label.grid(row=9, column=0, padx=10, pady=10)
section80CCC_entry = tk.Entry(root)
section80CCC_entry.grid(row=9, column=2, padx=10, pady=10, columnspan=3)

# Create the Section 80CCD label and entry box
section80CCD_label = tk.Label(root, text="Section 80CCD Amount:")
section80CCD_label.grid(row=10, column=0, padx=10, pady=10)
section80CCD_entry = tk.Entry(root)
section80CCD_entry.grid(row=10, column=2, padx=10, pady=10, columnspan=3)

# Create the PM Relief label and entry box
pmRelief_label = tk.Label(root, text="PM Relief Amount:")
pmRelief_label.grid(row=11, column=0, padx=10, pady=10)
pmRelief_entry = tk.Entry(root)
pmRelief_entry.grid(row=11, column=2, padx=10, pady=10, columnspan=3)

# Create the CM Relief label and entry box
cmRelief_label = tk.Label(root, text="CM Relief Amount:")
cmRelief_label.grid(row=12, column=0, padx=10, pady=10)
cmRelief_entry = tk.Entry(root)
cmRelief_entry.grid(row=12, column=2, padx=10, pady=10, columnspan=3)

# Create the hli label and entry box
hli_label = tk.Label(root, text="Housing Loan Interest Amount:")
hli_label.grid(row=13, column=0, padx=10, pady=10)
hli_entry = tk.Entry(root)
hli_entry.grid(row=13, column=2, padx=10, pady=10, columnspan=3)

# Create the Medical Claim label and entry box
mediClaim_label = tk.Label(root, text="Medical Claim:")
mediClaim_label.grid(row=14, column=0, padx=10, pady=10)
mediClaim_entry = tk.Entry(root)
mediClaim_entry.grid(row=14, column=2, padx=10, pady=10, columnspan=3)

# Create the Child Exception label and entry box
childException_label = tk.Label(root, text="Child Exception Amount:")
childException_label.grid(row=15, column=0, padx=10, pady=10)
childException_entry = tk.Entry(root)
childException_entry.grid(row=15, column=2, padx=10, pady=10, columnspan=3)

# Create the Advance Tax label and entry box
advanceTax_label = tk.Label(root, text="Advance Tax Paid:")
advanceTax_label.grid(row=16, column=0, padx=10, pady=10)
advanceTax_entry = tk.Entry(root)
advanceTax_entry.grid(row=16, column=2, padx=10, pady=10, columnspan=3)

# Create the tax label
tax_label = tk.Label(root, text="")
tax_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_tax)
calculate_button.grid(row=17, column=0, columnspan=3, padx=10, pady=10)

# Run the main loop
root.mainloop()