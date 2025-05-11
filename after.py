import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        
        # Simple Interest formula: SI = (P * R * T) / 100
        interest = (principal * rate * time) / 100
        result_label.config(text=f"Simple Interest: {interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Interest Calculator")

# Labels and Entry fields
tk.Label(root, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=5)
principal_entry = tk.Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Rate of Interest (%):").grid(row=1, column=0, padx=10, pady=5)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Time (Years):").grid(row=2, column=0, padx=10, pady=5)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Simple Interest: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
