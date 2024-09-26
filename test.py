from Database import Ammo
from Algorithm import Bullet
import csv



#Have user input their ammo type, Altitude, Temperature, Humidity, Windspeed and direction
scopeheight = 1.5 #in
DistanceToTarget = 1500 #ft
DistancetoZero = 300 #ft
ShooterAltitude = 5000 #ft
TargetAltitude = 5000 #ft
Temperature = 50 #F
Humidity = 50 #%
Windspeed = 5 #mph

AimDirection = 90  #degrees
WindDirection = 90 #degrees

ammotype = "'5.56x45mm NATO'"
# 5.56x45mm NATO
# .308 Winchester
# .50 BMG



result = Ammo()
info = result.cartidge(ammotype)

#assign vars from database
ID,	Name, HandgunORRifle, OfficialsizeMM, MuzzleVelocityFPS, MuzzleEnergyFTLBS, MomentumLBSFTS, ChargeGR, ActualDiameterIN, BallisticCoefficient, CaseLength = info[0]

true = Bullet( scopeheight, DistanceToTarget, DistancetoZero, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticCoefficient)
ToF = true.TimeofFlight()
DropIN = true.Drop()
DropMils = true.DropinMILs()
Dropafterzero = true.DropAfterZero()
DropAVG = true.DropAverage()
WindageMils= true.WindCorrectionMILs()
print(DropMils, WindageMils)
# data=["Range,Drop,DropAfterzero,DropAVG,MILs,WindageMILs"]
# for i in range(0, 21, 1):
#     DistanceToTarget = 150 * i + 1
    

#     true = Bullet( scopeheight, DistanceToTarget, DistancetoZero, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticCoefficient)
#     ToF = true.TimeofFlight()
#     DropIN = true.Drop()
#     DropMils = true.DropinMILs()
#     Dropafterzero = true.DropAfterZero()
#     DropAVG = true.DropAverage()
#     WindageMils= true.WindCorrectionMILs()

#     range = DistanceToTarget / 3
#     drop = DropIN
#     dropafterzero = Dropafterzero
#     MILs = DropMils
#     line = f"{range},{drop},{dropafterzero},{DropAVG},{DropMils},{WindageMils}"
#     data.append(line)

# data = [line.split(',') for line in data]

# csv_file_path = f"TestingDocs/accuracyTesting{ammotype}.csv"

# with open(csv_file_path, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# metrics = Bullet( scopeheight, DistanceToTarget, DistancetoZero, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticCoefficient) 

# print(true.WindCorrectionMILs())

# print("Ammunition Data:")
# print("Ballistics Coefficient: ", BallisticCoefficient)
# print("Muzzle Velocity: ", MuzzleVelocityFPS)
# print("Weight: ", metrics.Mass())
# print("Environmental Data")
# print("Air Pressure: ", metrics.AirPressure())

# #Test comment