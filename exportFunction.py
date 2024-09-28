import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_downloads_folder():
    # Get the user's home directory
    home_dir = os.path.expanduser("~")
    
    # Construct the Downloads folder path based on the OS
    if os.name == 'nt':  # For Windows
        downloads_folder = os.path.join(home_dir, 'Downloads')
    else:  # For macOS/Linux
        downloads_folder = os.path.join(home_dir, 'Downloads')
    
    return downloads_folder

def create_pdf(weapon_name, ammunition, shooting_direction, humidity, wind_direction, wind_speed, wind_speed_unit, altitude, altitude_unit, temperature, temperature_unit, zero_range, zero_range_unit, distance, distance_unit, DropMils, WindageMils):
    downloads_folder = get_downloads_folder()
    name = f"{weapon_name}.pdf"
    # Define the output filename and path
    output_filename = os.path.join(downloads_folder, name)

    # Create a PDF canvas
    c = canvas.Canvas(output_filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, f"{weapon_name}")

    # Line under the title
    c.line(0, height - 60, 625, height - 60)

    # Subtitle or Description
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "User Inputs:")

    # Start position for variable display
    leftcolumn = 100
    rightcolumn = 350
    c.drawString(leftcolumn, height - 120, f"Ammunition: {ammunition}")
    c.drawString(rightcolumn, height - 120, f"Shooting Direction: {shooting_direction} degrees")

    c.drawString(leftcolumn, height - 135, f"Wind Speed: {wind_speed} {wind_speed_unit}")
    c.drawString(rightcolumn, height - 135, f"Wind Direction: {wind_direction} degrees")
    
    c.drawString(leftcolumn, height - 150, f"Humidity: {humidity}%")
    c.drawString(rightcolumn, height - 150, f"Temperature: {temperature} {temperature_unit}")

    c.drawString(leftcolumn, height - 165, f"Altitude: {altitude} {altitude_unit}")
    c.drawString(rightcolumn, height - 165, f"Zero Range: {zero_range} {zero_range_unit}")

    c.drawString(leftcolumn, height - 180, f"Distance to target: {distance} {distance_unit}")

    
    # Save the PDF
    c.save()

