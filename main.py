import arcpy

DATABASE = r'D:\gis_projects\default\Oracle-gisdb(water_gis).sde'
arcpy.env.workspace = DATABASE
arcpy.env.overwriteOutput = True

DATASETS = arcpy.ListDatasets()
print(DATASETS)

SELECTED_LAYER = 'HAYA.OMAN'
DATASET = 'HAYA.OMAN'
TEMP_LAYER = 'memory\\wilaya_temp'
SPATIAL_REFERENCE = arcpy.Describe(DATASET).spatialReference
print(SPATIAL_REFERENCE.name)
WILAYA_FIELDS = ['WILAYATNAM', 'WNCODE', 'WILAYATID']
x_cor = 653951
y_cor = 2584641

#the test is for Al Amerat Wilaya.
point_geometry = arcpy.PointGeometry(arcpy.Point(X=x_cor, Y=y_cor), spatial_reference=SPATIAL_REFERENCE.factoryCode)

arcpy.analysis.Intersect(
    in_features=
    [point_geometry, SELECTED_LAYER],
    out_feature_class=TEMP_LAYER,
    join_attributes='ALL',
    output_type='POINT'
)

with arcpy.da.SearchCursor(in_table=TEMP_LAYER, field_names=WILAYA_FIELDS) as selected_wilaya:
    for row in selected_wilaya:
        for field in WILAYA_FIELDS:
            print(row[field])