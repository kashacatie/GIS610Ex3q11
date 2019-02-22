import arcpy
from arcpy import env

arcpy.env.workspace = r'C:\Users\stillman\Exercise3.gdb'
print(arcpy.GetCount_management('CallsforService'))