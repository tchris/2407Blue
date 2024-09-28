from unitconversions import convert_and_run, error, error_section




# def test():



weapon_name = "5.56x45mm NATO"
ammunition = "5.56x45mm NATO"
shooting_direction = '100'
humidity = '50' 
wind_direction = '90'
wind_speed = '5'
wind_speed_unit = "mph"
altitude = '5000'
altitude_unit = "feet"
temperature = '50'
temperature_unit = "Fahrenheit"
zero_range = '100'
zero_range_unit = "yards"
distance = '500'
distance_unit = "yards"

# output = (
#     weapon_name,
#     ammunition,
#     shooting_direction,
#     humidity,
#     wind_direction,
#     wind_speed,
#     wind_speed_unit,
#     altitude,
#     altitude_unit,
#     temperature,
#     temperature_unit,
#     zero_range,
#     zero_range_unit,
#     distance,
#     distance_unit
# )
# for line in output:
#     print(line)
#     print(type(line))
try:
    DropMils, WindageMils = convert_and_run(weapon_name, ammunition, shooting_direction, humidity, wind_direction, wind_speed, wind_speed_unit, altitude, altitude_unit, temperature, temperature_unit, zero_range, zero_range_unit, distance, distance_unit)
    print("DropMils: ", DropMils)
    print("WindageMils: ", WindageMils)
except TypeError:
    errors = error()
    print(errors)
    


# DropMils, WindageMils = convert_and_run(weapon_name, ammunition, shooting_direction, humidity, wind_direction, wind_speed, wind_speed_unit, altitude, altitude_unit, temperature, temperature_unit, zero_range, zero_range_unit, distance, distance_unit)
# print("DropMils: ", DropMils)
# print("WindageMils: ", WindageMils)

# test()