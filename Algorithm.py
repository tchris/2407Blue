from Database import Ammo

#Have user input their ammo type, Altitude, Temperature, Humidity, Windspeed and direction
#meters
DistanceToTarget = 100
#ft
ShooterAltitude = 5000
TargetAltitude = 5000
#F
Temperature = 50
Humidity = 50
#mph
Windspeed = 5
#degrees
WindDirection = 90
AimDirection = 90
ammotype = "'.17 HM2'"

#calculate air density = p
def Pressure(Temperature, ShooterAltitude, TargetAltitude):
    h = (ShooterAltitude + TargetAltitude)/6.56167979
    P0 = 29.92
    T = ((Temperature - 32) / 1.8) + 273.15
    e = 2.7182818284590452353602
    g= 9.80655
    R = 8.31432
    M = 0.02896
    lottamath = e ** ((-g * M * h) / (R * T))
    Pressure = P0 * lottamath
    return Pressure

#calculate time of flight (ToF)
def TimeofFlight(x):
    x




#search DB for ammo
result = Ammo()
info = result.cartidge(ammotype)

#assign vars from database
ID,	Name, HandgunORRifle, OfficialsizeMM, MuzzleVelocityFPS, MuzzleEnergyFTLBS, MomentumLBSFTS, ChargeGR, ActualDiameterIN, BallisticCoefficient, CaseLength = info[0]




 


p = Pressure(Temperature, ShooterAltitude, TargetAltitude)
# ToF = TimeofFlight()


#calculate drag coefficient = C

# float(BallisticCoefficient) ** -1

#calculate bullet mass = m
# calculate area of bullet = A

bullet = float(MuzzleVelocityFPS)/float(MuzzleEnergyFTLBS)
print(MuzzleEnergyFTLBS)
print(MuzzleVelocityFPS)
print(bullet)


