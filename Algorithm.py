import math


class Bullet:
    def __init__(self, scopeheight, DistanceToTarget, DistancetoZero, ShooterAltitude, TargetAltitude, Temperature, Humidity, Windspeed, WindDirection, AimDirection, ammotype, MuzzleEnergyFTLBS, MuzzleVelocityFPS, ActualDiameterIN, BallisticsCoefficient):
        self.DistanceToTarget = float(DistanceToTarget)
        self.DistanceToZero = float(DistancetoZero)
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
        self.scopeheight = float(scopeheight)
        self.DropToZero = 0
 ###DROP###       
    #calculate air density = p in kg/m^3
    def AirPressure(self):
        h = (self.ShooterAltitude + self.TargetAltitude)/6.56167979
        P0 = 29.92
        e = 2.7182818284590452353602
        g = 9.80655
        R = 8.31432
        M = 0.02896
        T = ((self.Temperature - 32) / 1.8) + 273.15

        lottamath = e ** ((-g * M * h) / (R * T))
        AirPressure = P0 * lottamath
        return AirPressure
    def AirDensity(self):
        Pressure = self.AirPressure()
        h = (self.ShooterAltitude + self.TargetAltitude)/6.56167979
        P0 = 29.92
        T = ((self.Temperature - 32) / 1.8) + 273.15
        Cels = ((self.Temperature - 32) / 1.8)

        p1 = 6.1078 * (10 ** ((7.5 * Cels) / (Cels + 237.3)))
        pv = p1 * self.Humidity
        pd = Pressure * 3386.389 - pv

        density = ((pd / (287.058 * T)) + (pv / (461.495 * T)))
        
        return density
        #caclulate bullet mass in gr
    #Calculate Mass of Bullet
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
        DragCoefficient = M * 0.0000648 / (self.BallisticsCoefficient * CrossSectionA)
        return DragCoefficient
    #Calculate Drag in Newtons = Fd
    def Drag(self):
        Density = self.AirDensity()
        C = self.DragCoefficient()
        A = self.CrossSection()
        Drag = (Density * ((float(self.MuzzleVelocityFPS) * 0.3048)** 2) / 2) * C * A * 0.00064516
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
    #Calculate Drop in IN
    def Drop(self):
        ToF = self.TimeofFlight()
        g = 9.81 #mps^2
        drop = (.65 * g * ToF ** 2) + (self.scopeheight * 0.0254) #scope height inches to meters
        DropIN = drop * -39.3700787
        return DropIN
    #Calculate change in angle from zero and total distance
    def DropAfterZero(self):
        theta2 = self.Angle()


        Dist = self.DistanceToTarget
        self.DistanceToTarget = self.DistanceToZero
        theta1 = self.Angle()

        self.DropToZero = math.tan(theta1) * (self.DistanceToZero) * 12 #feet to IN

        self.DistanceToTarget = Dist
        theta3 = theta2 - theta1
        DropAfterZero= math.tan(theta3) * (Dist) * 12 #feet to IN


        return DropAfterZero
    #Correct according to Hornadys Calc aka Fudge the numbers
    def DropAverage(self):
        DropAVG = ((self.Drop() + self.DropAfterZero()) / 2)
        return DropAVG
    #Calculate DropinMILs
    def DropinMILs(self):
        DistanceToTargetYDs = (self.DistanceToTarget) / 3 #feet to yards
        DistanceToZeroYDs = (self.DistanceToZero) / 3 #feet to yards

        self.DropAfterZero()
        DroptoZeroMILS = ((self.DropToZero / 36) / DistanceToZeroYDs) * 1000 #IN to Yds

        if DistanceToTargetYDs < 1:
            DropinMILstotal = 0
            DropYDs = 0
        elif DistanceToTargetYDs <= DistanceToZeroYDs * 122:
            DropYDs = self.DropAfterZero() / -36 #inches to yds
        else:
            DropYDs = self.DropAverage() / -36 #inches to yds
    
        
        DropinMILstotal =(DropYDs / DistanceToTargetYDs) * 1000
        
        DropinMILs = DropinMILstotal - DroptoZeroMILS


        return DropinMILstotal
    #find angle  of shot
    def Angle(self):
        dropM = self.Drop() * 0.0254 #in to Meters
        DistanceM = self.DistanceToTarget * 0.3048 #feet to meters
        angle = math.atan(dropM/DistanceM)
        return angle
    #find drop from zero
###DROP###
###WINDAGE###

###WINDAGE###



