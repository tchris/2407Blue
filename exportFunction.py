from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

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
    
    WindageMoa = round(WindageMils / 3.4377, 1)
    DropMoa = round(DropMils / 3.4377, 1)
    
    
    
    data = {
    'output': {
        f'Up: {DropMils}': f'Up: {DropMoa}',
        f'Right: {WindageMils}': f'Right: {WindageMoa}',
    },
    'input': {
        'Ammunition': f'{ammunition}',
        'Shooting Direction': f'{shooting_direction} degrees',
        'Wind Speed': f'{wind_speed} {wind_speed_unit}',
        'Wind Direction': f'{wind_direction} degrees',
        'Humidity': f'{humidity}%',
        'Temperature': f'{temperature} {temperature_unit}',
        'Altitude': f'{altitude} {altitude_unit}',
        'Zero Range': f'{zero_range} {zero_range_unit}',
        'Distance to Target': f'{distance} {distance_unit}',
        }
    }
    downloads_folder = get_downloads_folder()
    name = f"{weapon_name}.pdf"
    # Define the output filename and path
    output_filename = os.path.join(downloads_folder, name)

    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    elements = []

    # Add styles for text
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    subtitle_style = styles['Heading2']
    normal_style = styles['Normal']

    # Title
    elements.append(Paragraph(f"{weapon_name}", title_style))
    elements.append(Spacer(1, 12))

    # # File Name
    # elements.append(Paragraph(f"File Name: {data['input']['File Name']}", normal_style))
    # elements.append(Spacer(1, 12))

    # Input Values Section
    elements.append(Paragraph("Input Values:", subtitle_style))
    elements.append(Spacer(1, 12))

    # Create a table for Input Values
    input_data = [['Variable', 'Value']]
    for key, value in data['input'].items():
        if key != "File Name":  # Skip File Name since it's shown above
            input_data.append([key, value])

    input_table = Table(input_data, colWidths=[150, 200])
    input_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(input_table)
    elements.append(Spacer(1, 24))

    # Output Values Section
    elements.append(Paragraph("Output Values:", subtitle_style))
    elements.append(Spacer(1, 12))

    # Create a table for Output Values
    output_data = [['MILs', 'MOA']]
    for key, value in data['output'].items():
        output_data.append([key, value])

    output_table = Table(output_data, colWidths=[150, 200])
    output_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(output_table)
    elements.append(Spacer(1, 24))

    # Add image if provided
    image_path = "CoolGuyLogo.png"
    if image_path and os.path.exists(image_path):
        img = Image(image_path, width=600, height=100)  # Adjust size as needed
        elements.insert(1, img)
        elements.append(Spacer(1, 24))
    # Build the PDF document
    doc.build(elements)

    
# create_pdf(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0,0)