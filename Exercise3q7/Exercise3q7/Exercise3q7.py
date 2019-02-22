import arcpy
from arcpy import envenv.overwriteOutput = True

arcpy.env.current_workspace = r'C:\Users\stillman\Exercise3.gdb'
testFC = r'C:\Users\stillman\Exercise3.gdb\General_Offense'
outLocation = r'C:\Users\stillman\Exercise3.gdb'
outFeature = 'Offense'
delimitedField = arcpy.AddFieldDelimiters(inFeatures, 'OffenseCustom')
expression = delimitedField + " = 'RUNAWAY JUVENILE'"


arcpy.FeatureClassToFeatureClass_conversion(testFC, outLocation, outFeature, expression)
print('it worked') 
 