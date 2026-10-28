import arcpy

DATABASE = r'C:\Amr\GIS_projects\default\Oracle-gisdb(water_gis).sde'
arcpy.env.workspace = DATABASE
arcpy.env.overwriteOutput = True

DATASET = 'HAYA.OMAN'
SPATIAL_REFERENCE = arcpy.Describe(DATASET).spatialReference
IN_WILAYA_LAYER = r'HAYA.OMAN\HAYA.CensusWillayat'
temp_wilayat = arcpy.MakeFeatureLayer_management(IN_WILAYA_LAYER)
WILAYA_FIELDS = ['WILAYATNAM', 'WNCODE', 'WILAYATID']
x_cor = 653951
y_cor = 2584641

#the test is for Al Amerat Wilaya.
point_geometry = arcpy.PointGeometry(arcpy.Point(X=x_cor, Y=y_cor), spatial_reference=SPATIAL_REFERENCE)

arcpy.management.SelectLayerByLocation(in_layer=temp_wilayat, overlap_type='INTERSECT', select_features=point_geometry)

with arcpy.da.SearchCursor(in_table=temp_wilayat, field_names=WILAYA_FIELDS) as selected_wilaya:
    for row in selected_wilaya:
        for field in range(len(WILAYA_FIELDS)):
            print(row[field])

arcpy.management.Delete(temp_wilayat)
print('selection is Done successfuly')