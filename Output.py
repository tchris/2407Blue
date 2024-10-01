

import tkinter as tk
from tkinter import ttk

# Function for the Export button (placeholder for now)
def export_data():
    print("Exporting data...")

# Function for the Restart button (placeholder for now)
def restart_application():
    print("Restarting application...")

# Create the main window
root = tk.Tk()
root.title("Ballistics Output Page")

# Create a Frame
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Configure grid columns for equal width
for i in range(3):
    main_frame.grid_columnconfigure(i, weight=1)

# Create a Canvas for "Cool Guy Logo" 
logo_canvas = tk.Canvas(main_frame, width=400, height=50, bg="white", relief="solid")
logo_canvas.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")

# Draw diagonal lines from corner to corner (create an 'X')
logo_canvas.create_line(0, 0, 400, 50, fill="black")
logo_canvas.create_line(400, 0, 0, 50, fill="black")

# Create "Cool Guy Logo" text
logo_canvas.create_text(200, 25, text="Cool Guy Logo", font=("Arial", 14), fill="black")

# Create labels and input widgets for new output fields

# Come
come_label = tk.Label(main_frame, text="Come:")
come_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
come_entry = tk.Entry(main_frame)
come_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

come_unit_var = tk.StringVar()
come_unit_dropdown = ttk.Combobox(main_frame, textvariable=come_unit_var, values=["mil", "MOA"], state="readonly")
come_unit_dropdown.grid(row=1, column=2, sticky="ew", padx=10, pady=5)

# Wind Drift
wind_drift_label = tk.Label(main_frame, text="Wind Drift:")
wind_drift_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
wind_drift_entry = tk.Entry(main_frame)
wind_drift_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

wind_drift_unit_var = tk.StringVar()
wind_drift_unit_dropdown = ttk.Combobox(main_frame, textvariable=wind_drift_unit_var, values=["inches", "cm"], state="readonly")
wind_drift_unit_dropdown.grid(row=2, column=2, sticky="ew", padx=10, pady=5)

# Distance to Target
distance_to_target_label = tk.Label(main_frame, text="Distance to Target:")
distance_to_target_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
distance_to_target_entry = tk.Entry(main_frame)
distance_to_target_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

distance_to_target_unit_var = tk.StringVar()
distance_to_target_unit_dropdown = ttk.Combobox(main_frame, textvariable=distance_to_target_unit_var, values=["yards", "meters"], state="readonly")
distance_to_target_unit_dropdown.grid(row=3, column=2, sticky="ew", padx=10, pady=5)

# Velocity at Target
velocity_at_target_label = tk.Label(main_frame, text="Velocity at Target:")
velocity_at_target_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
velocity_at_target_entry = tk.Entry(main_frame)
velocity_at_target_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

velocity_at_target_unit_var = tk.StringVar()
velocity_at_target_unit_dropdown = ttk.Combobox(main_frame, textvariable=velocity_at_target_unit_var, values=["fps", "m/s"], state="readonly")
velocity_at_target_unit_dropdown.grid(row=4, column=2, sticky="ew", padx=10, pady=5)

# Energy on Target
energy_on_target_label = tk.Label(main_frame, text="Energy on Target:")
energy_on_target_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
energy_on_target_entry = tk.Entry(main_frame)
energy_on_target_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

energy_on_target_unit_var = tk.StringVar()
energy_on_target_unit_dropdown = ttk.Combobox(main_frame, textvariable=energy_on_target_unit_var, values=["Joules", "ft-lbs"], state="readonly")
energy_on_target_unit_dropdown.grid(row=5, column=2, sticky="ew", padx=10, pady=5)

# Create Export Button
export_button = tk.Button(main_frame, text="Export", command=export_data)
export_button.grid(row=6, column=0, pady=20, padx=10, sticky="w")  # Align button to the left

# Create Restart Button
restart_button = tk.Button(main_frame, text="Restart", command=restart_application)
restart_button.grid(row=6, column=2, pady=20, padx=10, sticky="e")  # Align button to the right

# Start the Tkinter event loop
root.mainloop()
