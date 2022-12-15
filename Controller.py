HeatTemp = 90
SolarPanel = 100
TankBottomTemp = 50
diffMax = 20

AveNightlyTemp = 45
NightTempMin = 55
#NeedHeat = 11
EmergencyHeatTemp = 40
GreenhouseBottomTemp = 41
GreenhouseEyeTemp = 65
GreenhouseCielingTemp = 93
GAHTOnTemp = 85
GoundGravelTemp = 55
TankMiddleTemp  = 75


        


def EmegencyHeat():
    global SpaceHeater
    if GreenhouseBottomTemp < EmergencyHeatTemp: 
        print("Emergency Heat: Its Going to Freeze!,  Turn on the Space Heater!")  
        SpaceHeater = 1
        
    else:
        print('Emergency Heat: No Freezing, no Space heater needed')
        SpaceHeater = 0
        
    print("\n")
#End of EmegencyHeat()        
        


def NightTemp():
    global NeedHeat
    if AveNightlyTemp < NightTempMin:
        print("AveNightlyTemp: night will be Cold,  lets collect some heat!")
        
        NeedHeat = 1
        print("NeedHeat =", NeedHeat)
        
    else:
        print("AveNightlyTemp: Warm night ahead, no heat required")
        NeedHeat = 0
        print("NeedHeat =", NeedHeat)
        
    print("\n")
     # End of NightTemp()   
        


def PanelHeat():
    if SolarPanel > HeatTemp: 
        print("PanelHeat: Solar Panel is HOT")
       
    else:
        print('PanelHeat: Solar Panel is COLD') 
    
    print("\n")    
# End of PanelHeat()    
    
    
def Diff():
    global diffCalc
    diffCalc = SolarPanel - TankBottomTemp
    if diffCalc > diffMax: 
        print("Diff: Tank is Cold enough")    
    else:
        print('Diff: Tank too Hot')
    print('Differential =', diffCalc)
    print("\n") 
# End of Diff()    
  
def PumpOn():    
    if SolarPanel > HeatTemp and diffCalc > diffMax and NeedHeat == 1:
        print("PumpOn: Solar Panel Pump ON")

    else:
        print('PumpOn: Solar Panel Pump off')
    print("\n")
#End of PumpOn()  

def GAHT():
    global GAHTFan
    GAHTDiff = GoundGravelTemp + 20
    if GreenhouseCielingTemp > GAHTDiff and GreenhouseCielingTemp > GAHTOnTemp: 
        print("GAHT: Its Getting Hot!,  Turn on the GAHT fan!")  
        GAHTFan = 1
        
    else:
        print('GAHT: No GAHT Fan')
        GAHTFan = 0
    print("\n")
    
EmegencyHeat()
NightTemp()    
PanelHeat()
Diff()
PumpOn()
GAHT()


    



