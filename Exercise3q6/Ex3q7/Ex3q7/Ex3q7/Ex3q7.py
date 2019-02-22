import arcpy
from arcpy import envenv.overwriteOutput = True

arcpy.env.current_workspace = r'C:\Users\stillman\Exercise 3.gdb'
inFeatures = 'General_Offense'
outLocation = r'C:\Users\stillman\Exercise 3.gdb'
outFeature = 'Offense'
delimitedField = arcpy.AddFieldDelimiters(inFeatures, 'OffenseCustom')
expression = delimitedField + " = 'RUNAWAY '"


arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, outFeature, expression) 
 







