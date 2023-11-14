import tkinter as tk
from tkinter import ttk
import database  # Assuming you have a database module with a function named showall


class RealEstateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real State Application")
        self.root.state("zoomed")

        self.create_treeview()
        self.create_search_widgets()

    def create_treeview(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Client", "Government", "Area", "Employee ID", "Address","Issue"),
                                  show="headings")

        # Define column names and set their headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Client", text="Client")
        self.tree.heading("Government", text="Government")
        self.tree.heading("Area", text="Area")
        self.tree.heading("Employee ID", text="Employee ID")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Issue", text="Address")


        # Set column widths
        self.tree.column("ID", width=50)
        self.tree.column("Client", width=100)
        self.tree.column("Government", width=100)
        self.tree.column("Area", width=100)
        self.tree.column("Employee ID", width=100)
        self.tree.column("Address", width=150)
        self.tree.column("Issue", width=150)


        rows = database.showall()

        # Insert data into the treeview dynamically
        for row in rows:
            self.tree.insert("", "end", values=row)

        self.tree.pack()

    def create_search_widgets(self):
        label_search = tk.Label(self.root, text="Enter Search Term:")
        label_search.pack(pady=10)

        self.entry_search = tk.Entry(self.root)
        self.entry_search.pack(pady=10)

        button_search = tk.Button(self.root, text="Search", command=self.search_data)
        button_search.pack(pady=10)

    def search_data(self):
        search_term = self.entry_search.get()
        # Use the search term to query the database or perform other actions
        data = database.getdata(search_term)
        if data == 0:
            label_search = tk.Label(self.root, text="Not Found")
            label_search.pack(pady=10)
            return

        self.create_entry_widgets(data)

    def create_entry_widgets(self, data):
        labels = ["Client Price:", "Government Price:", "Area Price:", "Address:", "Issue:"]
        entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(self.root, text=label_text)
            label.pack(side=tk.LEFT, padx=5)
            
            entry = tk.Entry(self.root) if i < 3 else tk.Text(self.root, width=50, height=5)
            entry.pack(side=tk.LEFT, padx=5)
            entries.append(entry)
            if i == 3:
                entry.insert(tk.END, data[5])
            elif(i == 4):
                entry.insert(tk.END, data[6])

    # You can use entries list to access the values later if needed



if __name__ == "__main__":
    root = tk.Tk()
    app = RealEstateApp(root)
    root.mainloop()
