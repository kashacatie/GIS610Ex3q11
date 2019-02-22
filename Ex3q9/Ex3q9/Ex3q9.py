
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True

current_workspace = r'D:\Code\Ex3foraddedfeaturelist\Ex3\Ex3.gdb'
geometry_type = 'POLYGON'
spatialRef = arcpy.SpatialReference(26949)


featureList = 'State_Parks'

arcpy.env.workspace = current_workspace

arcpy.CreateFeatureclass_management('D:\Code\Ex3foraddedfeaturelist\Ex3\Ex3.gdb', featureList, geometry_type, "", "DISABLED", "DISABLED", spatialRef)

print('Feature Class ' + featureList + ' was sucessfully created.')

print('filteredFeatureClassNameList')

arcpy.AddField_management('State_Parks', 'Need_Care', 'STRING', '10')


arcpy.CreateDomain_management('D:\Code\Ex3foraddedfeaturelist\Ex3\Ex3.gdb','Time_Scale', 'TimeScale', 'TEXT', 'CODED')


domDict = {'0': 'YES', '1': 'NO', '2': 'InTwoMonths', '3': 'InSixMonths', '4': 'InOneYear' }

# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
    arcpy.AddCodedValueToDomain_management('D:\Code\Ex3foraddedfeaturelist\Ex3\Ex3.gdb', 'Time_Scale', code, domDict[code])
    
# Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management('State_Parks', 'Need_Care', 'Time_Scale')

print ('All Done')








