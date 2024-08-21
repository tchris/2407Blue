from Database import Ammo
import math


class Bullet:
    def __init__(self, DistanceToTarget, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticsCoefficient):
        self.DistanceToTarget = float(DistanceToTarget)
        self.ShooterAltitude = float(ShooterAltitude)
        self.TargetAltitude = float(TargetAltitude)
        self.Temperature = float(Temperature)
        self.Humidity = float(Humidity)
        self.Windspeed = float(Windspeed)
        self.WindDirection = float(WindDirection)
        self.AimDirection = float(AimDirection)
        self.ammotype = ammotype
        self.MuzzleEnergyFTLBS = float(MuzzleEnergyFTLBS)
        self.MuzzleVelocityFPS = float(MuzzleVelocityFPS)
        self.ActualDiameterIN = float(ActualDiameterIN)
        self.BallisticsCoefficient = float(BallisticsCoefficient)
    
    #calculate air density = p in kg/m^3
    def AirDensity(self):
        h = (self.ShooterAltitude + self.TargetAltitude)/6.56167979
        P0 = 29.92
        T = ((self.Temperature - 32) / 1.8) + 273.15
        Cels = ((self.Temperature - 32) / 1.8)
        e = 2.7182818284590452353602
        g = 9.80655
        R = 8.31432
        M = 0.02896


        lottamath = e ** ((-g * M * h) / (R * T))
        TotalPressure = P0 * lottamath
        
        p1 = 6.1078 * (10 ** ((7.5 * Cels) / (Cels + 237.3)))
        pv = p1 * Humidity
        pd = TotalPressure * 3386.389 - pv

        density = ((pd / (287.058 * T)) + (pv / (461.495 * T)))

        return density
        #caclulate bullet mass in gr
    def Mass(self):
        Mass = 450436.686 * float(self.MuzzleEnergyFTLBS)/((float(self.MuzzleVelocityFPS)) ** 2)
        return Mass
    #Calculate Cross Section Area in in^2
    def CrossSection(self):
        CrossSection = 3.1415 * (.5 * float(self.ActualDiameterIN)) ** 2
        return CrossSection
    #Calculate Drag Coefficient (Cd)
    def DragCoefficient(self):
        M = self.Mass()
        CrossSectionA =self.CrossSection()
        DragCoefficient = M * 0.0000648 / (float(self.BallisticsCoefficient) * CrossSectionA)
        return DragCoefficient
    #Calculate Drag in Newtons = Fd
    def Drag(self):
        Density = self.AirDensity()
        C = self.DragCoefficient()
        A = self.CrossSection()
        Drag = .5 * Density * ((float(self.MuzzleVelocityFPS) * 0.3048)** 2) * C * A * 0.00064516
        return Drag
    #calculate Deceleration lbft/s/s 
    def Deceleration(self):
        Drag = self.Drag()
        FPSLostPerSecond = -Drag * 2.2046 * 3.2808399
        #KG to lbs: * 2.2046
        #mps to fps:  * 3.2808399  
        return FPSLostPerSecond
    #calculate time of flight (ToF)
    def TimeofFlight(self):
        deceleration = self.Deceleration()

        #use quardradic equation
        a = .5 * deceleration
        b = float(self.MuzzleVelocityFPS)
        c = -float(self.DistanceToTarget)
        ToF = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        return ToF
    #Calculate Drop in mm
    def Drop(self):
        ToF = self.TimeofFlight()
        g = 9.81 #mps^2
        drop = (.5 * g * ToF ** 2) * 1000
        return drop
    #Calculate DropinMILs
    def DropinMILs(self):
        DropMM = self.Drop()
        DropM = DropMM / 1000
        DistanceToTargetM = self.DistanceToTarget * .3048
        DropinMILs = DropM / DistanceToTargetM * 1000
        return DropinMILs
    #find angle  of shot
    def Angle(self):
        dropMM = self.Drop()
        Distance = self.DistanceToTarget
        angle = math.atan(dropMM/Distance)
        return angle





        #search DB for ammo

#Have user input their ammo type, Altitude, Temperature, Humidity, Windspeed and direction
#meters
DistanceToTarget = 350
DistancetoZero = 100
#ft
ShooterAltitude = 5000
TargetAltitude = 5000
#F
Temperature = 69
Humidity = 50
#mph
Windspeed = 5
#degrees
WindDirection = 90
AimDirection = 90
ammotype = "'.50 BMG'"
result = Ammo()
info = result.cartidge(ammotype)

#assign vars from database
ID,	Name, HandgunORRifle, OfficialsizeMM, MuzzleVelocityFPS, MuzzleEnergyFTLBS, MomentumLBSFTS, ChargeGR, ActualDiameterIN, BallisticCoefficient, CaseLength = info[0]



true = Bullet( DistanceToTarget, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticCoefficient)
Zero = Bullet( DistancetoZero, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticCoefficient)



theta2 = true.Angle()

theta1 = Zero.Angle()


print(theta1)
print(theta2)



