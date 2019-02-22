import arcpy
import csv
arcpy.env.workspace = r'D:\Code\Ex3gdb\Exercise 3.gdb'

# Set local variables
inFeatures = 'General_Offense'
fields = ['OffenseCustom', 'locationTranslation']
cursorFields = ','.join(fields)
crimeCount = 0

filterStatements = "OffenseCustom = 'BURGLARY FORCE' and locationTranslation = 'Residence/Home'"

with open('burglarylocation.csv','w') as csvFile:
	fileWriter = csv.writer(csvFile,delimiter = ',',quotechar = '|', quoting = csv.QUOTE_MINIMAL)
	fileWriter.writerow(fields)
	with arcpy.da.SearchCursor(inFeatures,fields,filterStatements) as cursor:
		for row in cursor:
			crimeCount += 1
			fileWriter.writerow(row)

print('Created csv file')






