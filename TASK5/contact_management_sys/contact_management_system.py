import tkinter as tk
from tkinter import messagebox
import json
import os

# Define the file path for storing contacts
contacts_file = 'contacts.json'

# Function to load contacts from the JSON file
def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as file:
            return json.load(file)
    return []

# Function to save contacts to the JSON file
def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact():
    store_name = store_name_var.get()
    phone_number = phone_number_var.get()
    email = email_var.get()
    address = address_var.get()

    if store_name and phone_number:
        contacts.append({
            'store_name': store_name,
            'phone_number': phone_number,
            'email': email,
            'address': address
        })
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_form()
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Store name and phone number are required.")

# Function to clear the form fields
def clear_form():
    store_name_var.set("")
    phone_number_var.set("")
    email_var.set("")
    address_var.set("")

# Function to view all contacts
def view_contacts():
    contacts_listbox.delete(0, tk.END)
    for i, contact in enumerate(contacts, start=1):
        contacts_listbox.insert(tk.END, f"{i}. {contact['store_name']} - {contact['phone_number']}")

# Function to search contacts by name or phone number
def search_contacts():
    query = search_var.get().lower()
    contacts_listbox.delete(0, tk.END)
    results = [contact for contact in contacts if query in contact['store_name'].lower() or query in contact['phone_number']]
    for i, contact in enumerate(results, start=1):
        contacts_listbox.insert(tk.END, f"{i}. {contact['store_name']} - {contact['phone_number']}")

# Function to select a contact from the list
def select_contact(event):
    try:
        index = contacts_listbox.curselection()[0]
        selected_contact = contacts[index]
        store_name_var.set(selected_contact['store_name'])
        phone_number_var.set(selected_contact['phone_number'])
        email_var.set(selected_contact['email'])
        address_var.set(selected_contact['address'])
    except IndexError:
        pass

# Function to update a contact
def update_contact():
    try:
        index = contacts_listbox.curselection()[0]
        contacts[index]['store_name'] = store_name_var.get()
        contacts[index]['phone_number'] = phone_number_var.get()
        contacts[index]['email'] = email_var.get()
        contacts[index]['address'] = address_var.get()
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_form()
        view_contacts()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")

# Function to delete a contact
def delete_contact():
    try:
        index = contacts_listbox.curselection()[0]
        contacts.pop(index)
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        clear_form()
        view_contacts()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

# Main window setup
root = tk.Tk()
root.title("Contact Management System")

contacts = load_contacts()

# Variables for form fields
store_name_var = tk.StringVar()
phone_number_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

# Form fields
tk.Label(root, text="Store Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=store_name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=phone_number_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=email_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=address_var).grid(row=3, column=1, padx=10, pady=5)

# Buttons for adding, updating, and deleting contacts
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=5)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=1, padx=10, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=2, padx=10, pady=5)

# Search bar
tk.Label(root, text="Search").grid(row=5, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=search_var).grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Search", command=search_contacts).grid(row=5, column=2, padx=10, pady=5)

# Listbox to display contacts
contacts_listbox = tk.Listbox(root, width=50, height=15)
contacts_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=5)
contacts_listbox.bind('<<ListboxSelect>>', select_contact)

# Initially display all contacts
view_contacts()

# Run the main loop
root.mainloop()

