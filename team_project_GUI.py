# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 13:01:43 2024

@author: Josh
"""

import tkinter as tk
from tkinter import ttk
from unitconversions import convert_and_run, error, error_section
from ammolist import lst
from Output import OutputPage

# Function to store text from all text boxes and dropdowns
def store_text():
    weapon_name = weapon_name_entry.get()
    ammunition = ammunition_var.get()
    shooting_direction = shooting_direction_entry.get()
    humidity = humidity_entry.get()
    wind_direction = wind_direction_var.get()
    wind_speed = wind_speed_entry.get()
    wind_speed_unit = wind_speed_unit_var.get()
    altitude = altitude_entry.get()
    altitude_unit = altitude_unit_var.get()
    temperature = temperature_entry.get()
    temperature_unit = temperature_unit_var.get()
    zero_range = zero_range_entry.get()
    zero_range_unit = zero_range_unit_var.get()
    distance = distance_entry.get()
    distance_unit = distance_unit_var.get()

    output = (
        weapon_name,
        ammunition,
        shooting_direction,
        humidity,
        wind_direction,
        wind_speed,
        wind_speed_unit,
        altitude,
        altitude_unit,
        temperature,
        temperature_unit,
        zero_range,
        zero_range_unit,
        distance,
        distance_unit
    )
    
    
    try:
        export_file_name, Output_DropMils, Output_WindageMils, Output_distancetoTargetft, Output_VelocityatTargetfts, Output_EnergyatTargetlbsft = convert_and_run(weapon_name, ammunition, shooting_direction, humidity, wind_direction, wind_speed, wind_speed_unit, altitude, altitude_unit, temperature, temperature_unit, zero_range, zero_range_unit, distance, distance_unit)
        DropMils = Output_DropMils
        WindageMils = Output_WindageMils
        OutputPage(export_file_name, Output_DropMils, Output_WindageMils, Output_distancetoTargetft, Output_VelocityatTargetfts, Output_EnergyatTargetlbsft, weapon_name, ammunition, shooting_direction, humidity, wind_direction, wind_speed, wind_speed_unit, altitude, altitude_unit, temperature, temperature_unit, zero_range, zero_range_unit, distance, distance_unit, DropMils, WindageMils)
    except TypeError:
        errors = error()
        print(errors) #replace with output
    
    
def search(event):
    value = event.widget.get()
    if value == '':
        ammunition_dropdown['values'] = lst
    else:
        data = []
        for item in lst:
            if value.lower() in item.lower():
                data.append(item)
            ammunition_dropdown['values'] = data


# Create the main window
root = tk.Tk()
root.title("Ballistics Calculator")

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

# Create labels and input widgets in grid format

# Weapon Name
weapon_name_label = tk.Label(main_frame, text="Weapon Name:")
weapon_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
weapon_name_entry = tk.Entry(main_frame)
weapon_name_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

#ammo dropdown

ammunition_label = tk.Label(main_frame, text="Ammunition:")
ammunition_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
ammunition_var = tk.StringVar()
ammunition_dropdown = ttk.Combobox(main_frame, textvariable=ammunition_var, values=lst)
ammunition_dropdown.set('Search')
ammunition_dropdown.bind('<KeyRelease>', search)  # Make sure to use '<KeyRelease>' with angle brackets

# Use grid for the dropdown
ammunition_dropdown.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)


# Shooting Direction
shooting_direction_label = tk.Label(main_frame, text="Shooting Direction:")
shooting_direction_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
shooting_direction_entry = tk.Entry(main_frame)
shooting_direction_entry.grid(row=3, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Humidity
humidity_label = tk.Label(main_frame, text="Humidity:")
humidity_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
humidity_entry = tk.Entry(main_frame)
humidity_entry.grid(row=4, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Wind Direction (Dropdown)
wind_direction_label = tk.Label(main_frame, text="Wind Direction:")
wind_direction_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
wind_direction_var = tk.StringVar()
wind_direction_dropdown = ttk.Combobox(main_frame, textvariable=wind_direction_var, values=["North", "East", "South", "West"], state="readonly")
wind_direction_dropdown.grid(row=5, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

# Wind Speed [1] [2]
wind_speed_label = tk.Label(main_frame, text="Wind Speed:")
wind_speed_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
wind_speed_entry = tk.Entry(main_frame)
wind_speed_entry.grid(row=6, column=1, sticky="ew", padx=10, pady=5)

wind_speed_unit_var = tk.StringVar()
wind_speed_unit_dropdown = ttk.Combobox(main_frame, textvariable=wind_speed_unit_var, values=["mph", "km/h"], state="readonly")
wind_speed_unit_dropdown.grid(row=6, column=2, sticky="ew", padx=10, pady=5)

# Altitude
altitude_label = tk.Label(main_frame, text="Altitude:")
altitude_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
altitude_entry = tk.Entry(main_frame)
altitude_entry.grid(row=7, column=1, sticky="ew", padx=10, pady=5)

altitude_unit_var = tk.StringVar()
altitude_unit_dropdown = ttk.Combobox(main_frame, textvariable=altitude_unit_var, values=["meters", "feet"], state="readonly")
altitude_unit_dropdown.grid(row=7, column=2, sticky="ew", padx=10, pady=5)

# Temperature
temperature_label = tk.Label(main_frame, text="Temperature:")
temperature_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)
temperature_entry = tk.Entry(main_frame)
temperature_entry.grid(row=8, column=1, sticky="ew", padx=10, pady=5)

temperature_unit_var = tk.StringVar()
temperature_unit_dropdown = ttk.Combobox(main_frame, textvariable=temperature_unit_var, values=["Celsius", "Fahrenheit"], state="readonly")
temperature_unit_dropdown.grid(row=8, column=2, sticky="ew", padx=10, pady=5)

# Zero Range
zero_range_label = tk.Label(main_frame, text="Zero Range:")
zero_range_label.grid(row=9, column=0, sticky="w", padx=10, pady=5)
zero_range_entry = tk.Entry(main_frame)
zero_range_entry.grid(row=9, column=1, sticky="ew", padx=10, pady=5)

zero_range_unit_var = tk.StringVar()
zero_range_unit_dropdown = ttk.Combobox(main_frame, textvariable=zero_range_unit_var, values=["meters", "yards"], state="readonly")
zero_range_unit_dropdown.grid(row=9, column=2, sticky="ew", padx=10, pady=5)

# Distance
distance_label = tk.Label(main_frame, text="Distance:")
distance_label.grid(row=10, column=0, sticky="w", padx=10, pady=5)
distance_entry = tk.Entry(main_frame)
distance_entry.grid(row=10, column=1, sticky="ew", padx=10, pady=5)

distance_unit_var = tk.StringVar()
distance_unit_dropdown = ttk.Combobox(main_frame, textvariable=distance_unit_var, values=["meters", "yards"], state="readonly")
distance_unit_dropdown.grid(row=10, column=2, sticky="ew", padx=10, pady=5)

# Submit Button
submit_button = tk.Button(main_frame, text="Submit", command=store_text)
submit_button.grid(row=11, column=2, pady=20, padx=10, sticky="e")  # Align button with the last column (Distance [2])

# Start the Tkinter event loop
root.mainloop()
