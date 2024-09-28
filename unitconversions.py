
from Algorithm import Bullet
from Database import Ammo

# Initialize error section
error_section = []

# Error message function
def error():
    return f"You have entered the following invalid inputs:\n{error_section}"

# Clear error section before input validation
def clear_error_section():
    global error_section 
    error_section = []

# Check if input is a number
def is_number(input_number):
    try:
        # Try to convert the input to a float
        number = float(input_number)
        return number  # Return the valid number
    except ValueError:
        # If a ValueError occurs, input was not a valid number
        error_section.append(f"{input_number}")
        return None

# Function to convert and run the main logic with input validation
def convert_and_run(weapon_name, ammunition, shooting_direction, humidity, wind_direction, wind_speed, wind_speed_unit, altitude, altitude_unit, temperature, temperature_unit, zero_range, zero_range_unit, distance, distance_unit):
    
    # Clear previous error messages
    clear_error_section()
    
    if "/" in weapon_name:
        error_section.append("/")
    elif "\\" in weapon_name:
        error_section.append("\\")
    else:
        export_file_name = weapon_name

    #ammo
    new_ammunition = f"'{ammunition}'"
    #Shooting Direction input validation
    new_shooting_direction = is_number(shooting_direction)

    # new_wind_direction = is_number(wind_direction)                        Change after GUI fix

    #windspeed
    if wind_speed_unit == "mph":
        new_wind_speed = is_number(wind_speed)
    else:
        new_wind_speed = is_number(wind_speed) / 1.609344 #kmh to mph
    
        

    #altitude
    if altitude_unit == "feet":
        new_altitude = is_number(altitude)
    else:
        new_altitude = is_number(altitude) * 3.2808399 # meters to ft
    
    new_ShooterAltitude = new_altitude
    new_TargetAltitude = new_altitude

    #humidity
    new_humidity = is_number(humidity)
    #temp
    if temperature_unit == "Fahrenheit":
        new_temperature = is_number(temperature)
    else:
        new_temperature = is_number(temperature) * (9/5) + 32 #C to F
    

    #zero range
    if zero_range_unit == "yards":
        new_zero_range = is_number(zero_range) * 3 #yds to ft
    else:
        new_zero_range = is_number(zero_range) * 3.2808399 #m to ft
    

    #distance to target
    if distance_unit == "yards":
        new_distance = is_number(distance) * 3 #yds to ft
    else:
        new_distance = is_number(distance) * 3.2808399 #m to ft
    
    
    scopeheight = 1.5

    ###                                                                             place holder till gui is fixed
    new_wind_direction = 90


#call to DB
    result = Ammo()
    info = result.cartidge(new_ammunition)

#assign vars from database
    ID,	Name, HandgunORRifle, OfficialsizeMM, MuzzleVelocityFPS, MuzzleEnergyFTLBS, MomentumLBSFTS, ChargeGR, ActualDiameterIN, BallisticCoefficient, CaseLength = info[0]

    
    true = Bullet(scopeheight,
            new_distance, 
            new_zero_range, 
            new_ShooterAltitude, 
            new_TargetAltitude, 
            new_temperature, 
            new_humidity, 
            new_wind_speed, 
            new_wind_direction, 
            new_shooting_direction, 
            new_ammunition, 
            MuzzleEnergyFTLBS,
            MuzzleVelocityFPS, 
            ActualDiameterIN,
            BallisticCoefficient)
    
    DropMils = true.DropinMILs()
    WindageMils= true.WindCorrectionMILs()

    return export_file_name, DropMils, WindageMils
    # If there are any invalid inputs, display an error message
    # if error_section != []:
    #     return error()
    
    # try:
    #     # If all inputs are valid, proceed with the conversion and calculations
    #     export_file_name = weapon_name
        
    #     # Ammo conversion (assuming this uses validated input)
    #     new_ammunition = f"'{ammunition}'"
        
    #     # Additional calculations and logic should be implemented here
    #     # For now, just return a success message
    #     return "All inputs are valid. Proceeding with calculations."
    
    # except Exception as e:
    #     # Catch any other unexpected errors
    #     return f"An error occurred: {str(e)}"
