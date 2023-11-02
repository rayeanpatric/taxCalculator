import tkinter as tk

# Create a function to calculate tax
def calculate_tax():
    # Get the values from the entry boxes
    income = float(income_entry.get())
    expenses = float(expenses_entry.get())
    deductions = float(deductions_entry.get())
    dependents = int(dependents_entry.get())
    tax_rate = float(tax_rate_entry.get())

    # Calculate the taxable income
    taxable_income = income - expenses - deductions - (dependents * 2000)

    # Calculate the tax
    tax = taxable_income * (tax_rate / 100)

    # Update the tax label
    tax_label.config(text=f"${tax:.2f}")

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Tax Calculator")

# Set the window size
root.geometry("800x600")

# Create the income label and entry box
income_label = tk.Label(root, text="Income:")
income_label.grid(row=0, column=0, padx=10, pady=10)
income_entry = tk.Entry(root)
income_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the expenses label and entry box
expenses_label = tk.Label(root, text="Expenses:")
expenses_label.grid(row=1, column=0, padx=10, pady=10)
expenses_entry = tk.Entry(root)
expenses_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the deductions label and entry box
deductions_label = tk.Label(root, text="Deductions:")
deductions_label.grid(row=2, column=0, padx=10, pady=10)
deductions_entry = tk.Entry(root)
deductions_entry.grid(row=2, column=1, padx=10, pady=10)

# Create the dependents label and entry box
dependents_label = tk.Label(root, text="Dependents:")
dependents_label.grid(row=3, column=0, padx=10, pady=10)
dependents_entry = tk.Entry(root)
dependents_entry.grid(row=3, column=1, padx=10, pady=10)

# Create the tax rate label and entry box
tax_rate_label = tk.Label(root, text="Tax Rate:")
tax_rate_label.grid(row=4, column=0, padx=10, pady=10)
tax_rate_entry = tk.Entry(root)
tax_rate_entry.grid(row=4, column=1, padx=10, pady=10)

# Create the tax label
tax_label = tk.Label(root, text="")
tax_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_tax)
calculate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
