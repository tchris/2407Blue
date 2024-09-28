import tkinter as tk
from tkinter import ttk

def update_combobox(event):
    # Store the current cursor position and typed value
    current_value = combobox.get()
    cursor_position = combobox.index(tk.INSERT)

    # Filter the options based on the typed value
    matching_options = [item for item in options if current_value.lower() in item.lower()]
    combobox['values'] = matching_options

    # Open the dropdown to show matching options
    combobox.event_generate('<Down>')

    # Restore the focus and cursor position
    combobox.icursor(cursor_position)
    combobox.focus()

# Create the main window
root = tk.Tk()
root.title("Searchable Dropdown")

# Define options for the combobox
options = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape']

# Create a Combobox
combobox = ttk.Combobox(root)
combobox['values'] = options
combobox.pack(padx=10, pady=10)

# Bind the combobox to the update function
combobox.bind('<KeyRelease>', update_combobox)

# Run the application
root.mainloop()
