import arcpy

target_features = "D:\Code\Ex3gdb\Exercise 3.gdb\General_Offense"
join_features = "D:\Code\Ex3gdb\Exercise 3.gdb\Tracts"
out_feature_class = "D:\Code\Ex3gdb\Exercise 3.gdb\Offense_Tracts"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)

print('All Done')


