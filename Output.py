import tkinter as tk
from tkinter import ttk
from exportFunction import create_pdf
import sys

def OutputPage(export_file_name, Output_DropMils, Output_WindageMils, 
               Output_distancetoTargetft, Output_VelocityatTargetfts, 
               Output_EnergyatTargetlbsft, weapon_name, ammunition, 
               shooting_direction, humidity, wind_direction, 
               wind_speed, wind_speed_unit, altitude, altitude_unit, 
               temperature, temperature_unit, zero_range, zero_range_unit, 
               distance, distance_unit):
    
    def come(event):
        comevalue = event.widget.get()
        if comevalue == 'MILs':
            come_entry.delete('1.0', 'end')
            come_entry.insert('end', f'{Output_DropMils}')
        else:
            Output_DropMOA = round(Output_DropMils / 3.43775, 1)
            come_entry.delete('1.0', 'end')
            come_entry.insert('end', f'{Output_DropMOA}')
    
    def wind(event):
        windvalue = event.widget.get()
        if windvalue == 'MILs':
            wind_drift_entry.delete('1.0', 'end')
            wind_drift_entry.insert('end', f'{Output_WindageMils}')
        else:
            Output_WindageMOA = round(Output_WindageMils / 3.43775, 1)
            wind_drift_entry.delete('1.0', 'end')
            wind_drift_entry.insert('end', f'{Output_WindageMOA}')
    
    def target(event):
        targetvalue = event.widget.get()
        if targetvalue == 'ft':
            distance_to_target_entry.delete('1.0', 'end')
            distance_to_target_entry.insert('end', f'{round(Output_distancetoTargetft, 1)}')
        else:
            distance_to_target_entry.delete('1.0', 'end')
            distance_to_target_entry.insert('end', f'{round(Output_distancetoTargetft * 0.3048, 1)}')

    def velocity(event):
        velocityvalue = event.widget.get()
        if velocityvalue == 'fps':
            velocity_at_target_entry.delete('1.0', 'end')
            velocity_at_target_entry.insert('end', f'{round(Output_VelocityatTargetfts, 1)}')
        else:
            velocity_at_target_entry.delete('1.0', 'end')
            velocity_at_target_entry.insert('end', f'{round(Output_VelocityatTargetfts * 0.3048, 1)}')

    def energy(event):
        energyvalue = event.widget.get()
        if energyvalue == 'ft-lbs':
            energy_on_target_entry.delete('1.0', 'end')
            energy_on_target_entry.insert('end', f'{round(Output_EnergyatTargetlbsft, 1)}')
        else:
            energy_on_target_entry.delete('1.0', 'end')
            energy_on_target_entry.insert('end', f'{round(Output_EnergyatTargetlbsft * 1.35582, 1)}')

    def export():
        create_pdf(weapon_name, ammunition, shooting_direction, humidity, 
                   wind_direction, wind_speed, wind_speed_unit, altitude, 
                   altitude_unit, temperature, temperature_unit, zero_range, 
                   zero_range_unit, distance, distance_unit, Output_DropMils, 
                   Output_WindageMils)

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
    come_label = tk.Label(main_frame, text="Come up:")
    come_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    come_entry = tk.Text(main_frame, height=1, width=6)
    come_entry.insert('end', f'{Output_DropMils}')
    come_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

    come_unit_var = tk.StringVar()
    come_unit_dropdown = ttk.Combobox(main_frame, textvariable=come_unit_var, values=["MILs", "MOA"], state="readonly")
    come_unit_dropdown.grid(row=1, column=2, sticky="ew", padx=10, pady=5)
    come_unit_dropdown.set('MILs')
    come_unit_dropdown.bind('<<ComboboxSelected>>', come)

    # Wind Drift
    wind_drift_label = tk.Label(main_frame, text="Come Right:")
    wind_drift_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    wind_drift_entry = tk.Text(main_frame, height=1, width=6)
    wind_drift_entry.insert('end', f'{Output_WindageMils}')
    wind_drift_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    wind_drift_unit_var = tk.StringVar()
    wind_drift_unit_dropdown = ttk.Combobox(main_frame, textvariable=wind_drift_unit_var, values=["MILs", "MOA"], state="readonly")
    wind_drift_unit_dropdown.grid(row=2, column=2, sticky="ew", padx=10, pady=5)
    wind_drift_unit_dropdown.set('MILs')
    wind_drift_unit_dropdown.bind('<<ComboboxSelected>>', wind)

    # Distance to Target
    distance_to_target_label = tk.Label(main_frame, text="Distance to Target:")
    distance_to_target_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    distance_to_target_entry = tk.Text(main_frame, height=1, width=6)
    distance_to_target_entry.insert('end', f'{round(Output_distancetoTargetft, 1)}')
    distance_to_target_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

    distance_to_target_unit_var = tk.StringVar()
    distance_to_target_unit_dropdown = ttk.Combobox(main_frame, textvariable=distance_to_target_unit_var, values=["ft", "meters"], state="readonly")
    distance_to_target_unit_dropdown.grid(row=3, column=2, sticky="ew", padx=10, pady=5)
    distance_to_target_unit_dropdown.set('ft')
    distance_to_target_unit_dropdown.bind('<<ComboboxSelected>>', target)

    # Velocity at Target
    velocity_at_target_label = tk.Label(main_frame, text="Velocity at Target:")
    velocity_at_target_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
    velocity_at_target_entry = tk.Text(main_frame, height=1, width=6)
    velocity_at_target_entry.insert('end', f'{round(Output_VelocityatTargetfts, 1)}')
    velocity_at_target_entry.grid(row=4, column=1, sticky="ew", padx=10, pady=5)

    velocity_at_target_unit_var = tk.StringVar()
    velocity_at_target_unit_dropdown = ttk.Combobox(main_frame, textvariable=velocity_at_target_unit_var, values=["fps", "m/s"], state="readonly")
    velocity_at_target_unit_dropdown.grid(row=4, column=2, sticky="ew", padx=10, pady=5)
    velocity_at_target_unit_dropdown.set('fps')
    velocity_at_target_unit_dropdown.bind('<<ComboboxSelected>>', velocity)

    # Energy on Target
    energy_on_target_label = tk.Label(main_frame, text="Energy on Target:")
    energy_on_target_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
    energy_on_target_entry = tk.Text(main_frame, height=1, width=6)
    energy_on_target_entry.insert('end', f'{round(Output_EnergyatTargetlbsft, 1)}')
    energy_on_target_entry.grid(row=5, column=1, sticky="ew", padx=10, pady=5)

    energy_on_target_unit_var = tk.StringVar()
    energy_on_target_unit_dropdown = ttk.Combobox(main_frame, textvariable=energy_on_target_unit_var, values=["ft-lbs", "Joules"], state="readonly")
    energy_on_target_unit_dropdown.grid(row=5, column=2, sticky="ew", padx=10, pady=5)
    energy_on_target_unit_dropdown.set('ft-lbs')
    energy_on_target_unit_dropdown.bind('<<ComboboxSelected>>', energy)

    # Create Export Button
    export_button = tk.Button(main_frame, text="Export", command=export)
    export_button.grid(row=6, column=0, pady=20, padx=10, sticky="w")  # Align button to the left

    # Create Restart Button
    restart_button = tk.Button(main_frame, text="Restart", command=root.destroy)
    restart_button.grid(row=6, column=2, pady=20, padx=10, sticky="e")  # Align button to the right

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    # Collect arguments from command line
    args = sys.argv[1:]  # Get all arguments after the script name

    # Print received arguments for debugging
    print(f"Arguments received: {args}")

    # Make sure you have all the necessary arguments
    if len(args) < 15:
        print("Not enough arguments provided. Exiting.")
        sys.exit(1)


    # Unpack arguments
    (
        export_file_name,
        Output_DropMils,
        Output_WindageMils,
        Output_distancetoTargetft,
        Output_VelocityatTargetfts,
        Output_EnergyatTargetlbsft,
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
    ) = args

    # Call the OutputPage function with the unpacked arguments
    OutputPage(
        export_file_name,
        float(Output_DropMils),
        float(Output_WindageMils),
        float(Output_distancetoTargetft),
        float(Output_VelocityatTargetfts),
        float(Output_EnergyatTargetlbsft),
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