import tkinter as tk
import database

def on_close():
    root.destroy()

def clear_inputs():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete("1.0", tk.END)
    entry5.delete("1.0", tk.END)

def get_inputs():
    try:
        client_demand = float(entry1.get())
        gov_price = float(entry2.get())
        area_price = float(entry3.get())
        address = entry4.get("1.0", "end-1c")
        issue = entry5.get("1.0", "end-1c")
        print(client_demand, gov_price, area_price, address, issue)
        database.uploadetail(1, client_demand, gov_price, area_price, address,issue)
        clear_inputs()
    except ValueError:
        er = tk.Label(root, text=("Invalid input. Please enter numeric values."), fg="#ff0000")
        er.grid(row=8, column=1, pady=5, padx=5)  # Adjusted row to 8

def on_checkbox_click():
    if var.get():
        entry4.config(state="normal")
        entry5.config(state="normal")
        label.config(text="Checkbox is checked")
    else:
        entry4.config(state="disabled")
        entry5.config(state="disabled")
        label.config(text="Checkbox is unchecked")

root = tk.Tk()
root.title("Real Estate Application")
root.state('zoomed')

root.protocol("WM_DELETE_WINDOW", on_close)

heading = tk.Label(root, text="Welcome Employee", font=("Arial", 24))
heading.grid(row=0, column=0, columnspan=2, pady=10)

# Input fields and labels using grid
label1 = tk.Label(root, text="Client Price:")
label1.grid(row=1, column=0, sticky='e', pady=5, padx=5)  # Adjusted pady and padx
entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, pady=5, padx=5)  # Adjusted pady and padx

label2 = tk.Label(root, text="Government Price:")
label2.grid(row=2, column=0, sticky='e', pady=5, padx=5)  # Adjusted pady and padx
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, pady=5, padx=5)  # Adjusted pady and padx

label3 = tk.Label(root, text="Area Price:")
label3.grid(row=3, column=0, sticky='e', pady=5, padx=5)  # Adjusted pady and padx
entry3 = tk.Entry(root)
entry3.grid(row=3, column=1, pady=5, padx=5)  # Adjusted pady and padx

label4 = tk.Label(root, text="Address:")
label4.grid(row=4, column=0, sticky='e', pady=5, padx=5)  # Adjusted pady and padx
entry4 = tk.Text(root, width=50, height=5)
entry4.grid(row=4, column=1, pady=10, padx=5)  # Adjusted pady and padx

label5 = tk.Label(root, text="Issue:")
label5.grid(row=5, column=0, sticky='e', pady=5, padx=5)  # Adjusted pady and padx
entry5 = tk.Text(root, width=50, height=5, state="disabled")
entry5.grid(row=5, column=1, pady=10, padx=5)  # Adjusted pady and padx

var = tk.IntVar()

# Create the checkbox
checkbox = tk.Checkbutton(root, text="Enable Issue", variable=var, command=on_checkbox_click)
checkbox.grid(row=6, column=0, columnspan=2, pady=5, padx=5)  # Adjusted pady and padx

# Create a label to display the checkbox state
label = tk.Label(root, text="Checkbox is unchecked")
label.grid(row=7, column=0, columnspan=2, pady=10)

# Submit and Clear Buttons
submit_button = tk.Button(root, text="Submit", command=get_inputs)
submit_button.grid(row=8, column=0, pady=5, padx=5)  # Adjusted row to 8, column to 0, and added pady and padx

clear_button = tk.Button(root, text="Clear", command=clear_inputs)
clear_button.grid(row=8, column=1, pady=5, padx=5)  # Adjusted row to 8, column to 0, and added pady and padx

root.mainloop()
