

#5
import arcpy
from arcpy import env

current_workspace = r'C:\Users\stillman\Desktop\Ex3\Ex3\Ex3.gdb'
geometry_type = "POLYGON"
spatialRef = arcpy.SpatialReference(26949)


featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames','Nationalities','Rivers' ]

arcpy.env.workspace = current_workspace

arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatialRef)

    print('Feature Class ' + in_fc_name + ' was sucessfully created.')

print('filteredFeatureClassNameList')

createFC = [createFeatureClass(fc) for fc in featureList]

print ('All Done')



