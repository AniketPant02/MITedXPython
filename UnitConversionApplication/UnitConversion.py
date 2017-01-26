import math

# Km to AU, Ly, Pc, and Mpc
# Conversions through Metric Ladder: KHDeUDCM
# ArcSecond to Degrees
# Degrees to Radians

# Obtaining values
print ("What unit to begin conversion? Km, AU, Ly, Pc, Mpc, Kilo, Hecta, Deka, Unit, Deci, Centi, Milli, ArcSeconds, Degrees, and Radians are available. Use abbreviations for Metric (km, mm, etc)")
beginUnit = input("Beginning unit = ")
beginUnitValue = float(input("Beginning unit value = "))

print("What unit to convert to? Km, AU, Ly, Pc, Mpc, Kilo, Hecta, Deka, Unit, Deci, Centi, Milli, ArcSeconds, Degrees, and Radians are available. Use abbreviations for Metric (km, mm, etc)")
endUnit = input("End unit = ")
# Calculating conversion using different cases. Be able to go back and forth
# Km Functions
if beginUnit == "Km" and endUnit == "AU":
      endConversion = beginUnitValue * 6.68459 * 10**-9
      print(endConversion, endUnit)
elif beginUnit == "AU" and endUnit == "Km":
      endConversion = beginUnitValue * 1.496 * 10**8
      print(endConversion, endUnit)
elif beginUnit == "Km" and endUnit == "Ly":
      endConversion = beginUnitValue * 1.057 * 10**-13
      print(endConversion, endUnit)
elif beginUnit == "Ly" and endUnit == "Km":
      endConversion = beginUnitValue * 9.461 * 10**12
      print(endConversion, endUnit)
elif beginUnit == "Km" and endUnit == "Pc":
      endConversion = beginUnitValue * 3.24078 * 10**-14
      print(endConversion, endUnit)
elif beginUnit == "Pc" and endUnit == "Km":
      endConversion = beginUnitValue * 3.086 * 10**13
      print(endConversion, endUnit)
elif beginUnit == "Km" and endUnit == "Mpc":
      endConversion = beginUnitValue * 3.24078 * 10**-20
      print(endConversion, endUnit)
elif beginUnit == "Mpc" and endUnit == "Km":
      endConversion = beginUnitValue * 3.086 * 10**19
      print(endConversion, endUnit)
# AU Functions
elif beginUnit == "AU" and endUnit == "Ly":
      endConversion = beginUnitValue * 1.58125 * 10**-5
      print(endConversion, endUnit)
elif beginUnit == "Ly" and endUnit == "AU":
      endConversion = beginUnitValue * 63241.1
      print(endConversion, endUnit)
elif beginUnit == "AU" and endUnit == "Pc":
      endConversion = beginUnitValue * 4.84814 * 10**-6
      print(endConversion, endUnit)
elif beginUnit == "Pc" and endUnit == "AU":
      endConversion = beginUnitValue * 206265
      print(endConversion, endUnit)
elif beginUnit == "AU" and endUnit == "Mpc":
      endConversion = beginUnitValue * 4.84814 * 10**-12
      print(endConversion, endUnit)
elif beginUnit == "Mpc" and endUnit == "AU":
      endConversion = beginUnitValue * 2.063 * 10**11
      print(endConversion, endUnit)
# Ly Functions
elif beginUnit == "Ly" and endUnit == "Pc":
      endConverison = beginUnitValue * 0.306601
      print(endConversion, endUnit)
elif beginUnit == "Pc" and endUnit == "Ly":
      endConversion = beginUnitValue * 3.26156
      print(endConversion, endUnit)
elif beginUnit == "Ly" and endUnit == "Mpc":
      endConversion = beginUnitValue * 3.06601 * 10**-7
      print(endConversion, endUnit)
elif beginUnit == "Mpc" and endUnit == "Ly":
      endConversion = beginUnitValue * 3.262 * 10**6
      print(endConversion, endUnit)
# Pc Functions
elif beginUnit == "Pc" and endUnit == "Mpc":
      endConversion = beginUnitValue * 0.000001
      print(endConversion, endUnit)
elif beginUnit == "Mpc" and endUnit == "Pc":
      endConversion = beginUnitValue * 1000000
      print(endConversion, endUnit)
# All previous Mpc Functions already completed in other cases.
# Metric Ladder Functions
elif beginUnit == "Kilo" and endUnit == "Hecta":
      endConversion = beginUnitValue * 0.1
      print(endConversion, endUnit)
elif beginUnit == "Hecta" and endUnit == "Kilo":
      endConversion = beginUnitValue * 10
      print(endConversion, endUnit)
elif beginUnit == "Kilo" and endUnit == "Deka":
      endConversion = beginUnitValue * 0.01
      print(endConversion, endUnit)
elif beginUnit == "Deka" and endUnit == "Kilo":
      endConversion = beginUnitValue * 100
      print(endConversion, endUnit)
elif beginUnit == "Kilo" and endUnit == "Unit":
      endConversion = beginUnitValue * 0.001
      print(endConversion, endUnit)
elif beginUnit == "Unit" and endUnit == "Kilo":
      endConversion = beginUnitValue * 1000
      print(endConversion, endUnit)
elif beginUnit == "Kilo" and endUnit == "Deci":
      endConversion = beginUnitValue * 0.0001
      print(endConversion, endUnit)
elif beginUnit == "Deci" and endUnit == "Kilo":
      endConversion = beginUnitValue * 10000
      print(endConversion, endUnit)
elif beginUnit == "Kilo" and endUnit == "Centi":
      endConversion = beginUnitValue * 0.00001
      print(endConversion, endUnit)
elif beginUnit == "Centi" and endUnit == "Kilo":
      endConversion = beginUnitValue * 100000
      print(endConversion, endUnit)
elif beginUnit == "Kilo" and endUnit == "Milli":
      endConversion = beginUnitValue * 0.000001
      print(endConversion, endUnit)
elif beginUnit == "Milli" and endUnit == "Kilo":
      endConversion = beginUnitValue * 1000000
      print(endConversion, endUnit)
elif beginUnit == "Hecta" and endUnit == "Deka":
      endConversion = beginUnitValue * 0.1
      print(endConversion, endUnit)
elif beginUnit == "Deka" and endUnit == "Hecta":
      endConversion = beginUnitValue * 10
      print(endConversion, endUnit)
elif beginUnit == "Hecta" and endUnit == "Unit":
      endConversion = beginUnitValue * 0.01
      print(endConversion, endUnit)
elif beginUnit == "Unit" and endUnit == "Hecta":
      endConversion = beginUnitValue * 100
      print(endConversion, endUnit)
elif beginUnit == "Hecta" and endUnit == "Deci":
      endConversion = beginUnitValue * 0.001
      print(endConversion, endUnit)
elif beginUnit == "Deci" and endUnit == "Hecta":
      endConversion = beginUnitValue * 1000
      print(endConversion, endUnit)
elif beginUnit == "Hecta" and endUnit == "Centi":
      endConversion = beginUnitValue * 0.0001
      print(endConversion, endUnit)
elif beginUnit == "Centi" and endUnit == "Hecta":
      endConversion = beginUnitValue * 10000
      print(endConversion, endUnit)
elif beginUnit == "Hecta" and endUnit == "Milli":
      endConversion = beginUnitValue * 0.00001
      print(endConversion, endUnit)
elif beginUnit == "Milli" and endUnit == "Hecta":
      endConversion = beginUnitValue * 100000
      print(endConversion, endUnit)
elif beginUnit == "Deka" and endUnit == "Unit":
      endConversion = beginUnitValue * 10
      print(endConversion, endUnit)
elif beginUnit == "Unit" and endUnit == "Deka":
      endConversion = beginUnitValue * 0.1
      print(endConversion, endUnit)
elif beginUnit == "Deka" and endUnit == "Deci":
      endConversion = beginUnitValue * 100
      print(endConversion, endUnit)
elif beginUnit == "Centi" and endUnit == "Deka":
      endConversion = beginUnitValue * 0.01
      print(endConversion, endUnit)
elif beginUnit == "Deka" and endUnit == "Milli":
      endConversion = beginUnitValue * 1000
      print(endConversion, endUnit)
elif beginUnit == "Milli" and endUnit == "Deka":
      endConversion = beginUnitValue * 0.001
      print(endConversion, endUnit)
elif beginUnit == "Unit" and endUnit == "Deci":
      endConversion = beginUnitValue * 10
      print(endConversion, endUnit)
elif beginUnit == "Deci" and endUnit == "Unit":
      endConversion = beginUnitValue * 0.1
      print(endConversion, endUnit)
elif beginUnit == "Unit" and endUnit == "Centi":
      endConversion = beginUnitValue * 100
      print(endConversion, endUnit)
elif beginUnit == "Centi" and endUnit == "Unit":
      endConversion = beginUnitValue * 0.01
      print(endConversion, endUnit)
elif beginUnit == "Unit" and endUnit == "Milli":
      endConversion = beginUnitValue * 1000
      print(endConversion, endUnit)
elif beginUnit == "Milli" and endUnit == "Unit":
      endConversion = beginUnitValue * 0.001
      print(endConversion, endUnit)
elif beginUnit == "Deci" and endUnit == "Centi":
      endConversion = beginUnitValue * 10
      print(endConversion, endUnit)
elif beginUnit == "Centi" and endUnit == "Deci":
      endConversion = beginUnitValue * 0.1
      print(endConversion, endUnit)
elif beginUnit == "Deci" and endUnit == "Milli":
      endConversion = beginUnitValue * 100
      print(endConversion, endUnit)
elif beginUnit == "Milli" and endUnit == "Deci":
      endConversion = beginUnitValue * 0.01
      print(endConversion, endUnit)
elif beginUnit == "Centi" and endUnit == "Milli":
      endConversion = beginUnitValue * 10
      print(endConversion, endUnit)
elif beginUnit == "Milli" and endUnit == "Centi":
      endConversion = beginUnitValue * 0.1
      print(endConversion, endUnit)
# End of Metric Ladder
# Arc Seconds to Degrees
elif beginUnit == "Arcseconds" and endUnit == "Degrees":
      endConversion = beginUnitValue * 0.000277778
      print(endConversion, endUnit)
elif beginUnit == "Degrees" and endUnit == "Arcseconds":
      endConversion = beginUnitValue * 3600
      print(endConversion, endUnit)
#End of Arcseconds to Degrees
#Degrees to Radians
elif beginUnit == "Degrees" and endUnit == "Radians":
      endConversion = beginUnitValue * (math.pi/180)
      print(endConversion, endUnit)
elif beginUnit == "Radians" and endUnit == "Degrees":
      endConversation = beginUnitValue * (180/math.pi)
      print(endConversation, endUnit)
