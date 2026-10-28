import arcpy

DATABASE = r'C:\Amr\GIS_projects\default\Oracle-gisdb(water_gis).sde'
arcpy.env.workspace = DATABASE
arcpy.env.overwriteOutput = True

DATASET = 'HAYA.OMAN'
SPATIAL_REFERENCE = arcpy.Describe(DATASET).spatialReference
WILAYA_FIELDS = ['WILAYATNAM', 'WNCODE', 'WILAYATID']
IN_BOUNDARY_LAYERS = [r'HAYA.OMAN\HAYA.CensusWillayat', r'HAYA.OMAN\HAYA.Governorates']
x_cor = 653951
y_cor = 2584641

#fetch boundary code.
def fetch_code(x, y, temp):
    point_geometry = arcpy.PointGeometry(arcpy.Point(X=x, Y=y), spatial_reference=SPATIAL_REFERENCE)

    arcpy.management.SelectLayerByLocation(in_layer=temp, overlap_type='INTERSECT', select_features=point_geometry)

    with arcpy.da.SearchCursor(in_table=temp, field_names=WILAYA_FIELDS) as selected_wilaya:
        for row in selected_wilaya:
            for field in range(len(WILAYA_FIELDS)):
                print(row[field])

    arcpy.management.Delete(temp)
    print('selection is Done successfuly')

for boundary in IN_BOUNDARY_LAYERS:
    temp_layer = arcpy.MakeFeatureLayer_management(boundary)
    fetch_code(x=x_cor, y=y_cor, temp=temp_layer)


