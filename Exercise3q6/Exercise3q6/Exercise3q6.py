import arcpy
#Using the CallsforService feature class that you�ve been given, add a field called
#�Crime_Explanation� with the data type Text/String. Then, if the value of field �CFSType� is
#Burglary Call, write �This is a burglary� into the field that you just added.

arcpy.env.workspace = r'D:\Code\Ex3gdb\Exercise 3.gdb'

# Set local variables
inFeatures = 'CallsforService'
fieldName1 = 'Crime_Explanation'
fieldName2 = 'CFSType'
fieldLength = 20

x=r'D:\Code\Ex3gdb\Exercise 3.gdb\CallsforService'
arcpy.AddField_management(inFeatures, fieldName1, 'TEXT', field_length = fieldLength)


fields = ['CFSType', 'Crime_Explanation']

# Create update cursor for feature class 
with arcpy.da.UpdateCursor(x, fields) as cursor:
    for row in cursor:
        if row[0] == 'Burglary Call':
           row[1] = 'This is a burglary'
        

        # Update the cursor with the updated list
        cursor.updateRow(row)