import arcpy

# Static variables
DATA_STRUCTURE = {
  'HAYA.OMAN': {
    'HAYA.CensusWillayat': ['WILAYATNAM', 'WNCODE', 'WILAYATID'],
    'HAYA.Governorates': ['GOVERN_N_1', 'RNCODE'],
    'HAYA.Operational_Areas': ['Operational Area']
  },
  'WATER_GIS.Water': {
    'WATER_GIS.District_Meter_Areas_1': ['DMA_NAME'],
    'WATER_GIS.PW_Services': ['METER_ID',],
    'WATER_GIS.PW_Mains': [],
  },
  'WATER_GIS.BaseMaps': {
    'WATER_GIS.Parcels_MoHUP_Feb2026': ['PLOTNUM']
  }
}

DATABASE = r'C:\Amr\GIS_projects\default\Oracle-gisdb(water_gis).sde'

# Setting the workspace
arcpy.env.workspace = DATABASE
arcpy.env.overwriteOutput = True

# Get spatial reference
SPATIAL_REFERENCE = arcpy.Describe(r'WATER_GIS.Water\WATER_GIS.PW_Mains').spatialReference

# x, y provided by the eservice's system
x_cor = 653951
y_cor = 2584641

def select(temp, fields, x, y, reference):
    # create point geometry out of the x, y
    point_geometry = arcpy.PointGeometry(arcpy.Point(X=x, Y=y), spatial_reference=reference)
    arcpy.management.SelectLayerByLocation(in_layer=temp, overlap_type='INTERSECT', select_features=point_geometry)
    with arcpy.da.SearchCursor(in_table=temp, field_names=fields) as selected_layer:
        for row in selected_layer:
            for field in range(len(fields)):
                print(row[field])
            arcpy.management.Delete(temp)
            print('selection is Done successfuly')    

# fetch boundary code.
def fetch_code():
    # select by location
    for dataset ,layer in DATA_STRUCTURE.items():
        if dataset == 'HAYA.OMAN' and layer == 'HAYA.CensusWillayat':
            layer_path = r'HAYA.OMAN\HAYA.CensusWillayat' 
            temp_layer = arcpy.MakeFeatureLayer_management(layer_path)
            select(temp=temp_layer, fields=DATA_STRUCTURE['HAYA.OMAN']['HAYA.CensusWillayat'], x=x_cor, y=y_cor,reference=SPATIAL_REFERENCE)

        elif dataset == 'HAYA.OMAN' and layer == 'HAYA.Governorates':
            layer_path = r'HAYA.OMAN\HAYA.Governorates' 
            temp_layer = arcpy.MakeFeatureLayer_management(layer_path)
            select(temp=temp_layer, fields=DATA_STRUCTURE['HAYA.OMAN']['HAYA.Governorates'], x=x_cor, y=y_cor,reference=SPATIAL_REFERENCE)

        elif dataset == 'WATER_GIS.Water' and layer == 'WATER_GIS.District_Meter_Areas_1':
            layer_path = r'WATER_GIS.Water\WATER_GIS.District_Meter_Areas_1' 
            temp_layer = arcpy.MakeFeatureLayer_management(layer_path)
            select(temp=temp_layer, fields=DATA_STRUCTURE['WATER_GIS.Water']['WATER_GIS.District_Meter_Areas_1'], x=x_cor, y=y_cor,reference=SPATIAL_REFERENCE)
        
        elif dataset == 'WATER_GIS.BaseMaps' and layer == 'WATER_GIS.Parcels_MoHUP_Feb2026':
            layer_path = r'WATER_GIS.BaseMaps\WATER_GIS.Parcels_MoHUP_Feb2026' 
            temp_layer = arcpy.MakeFeatureLayer_management(layer_path)
            select(temp=temp_layer, fields=DATA_STRUCTURE['WATER_GIS.BaseMaps']['WATER_GIS.Parcels_MoHUP_Feb2026'], x=x_cor, y=y_cor,reference=SPATIAL_REFERENCE)

        elif dataset == 'HAYA.OMAN' and layer == 'HAYA.Operational_Areas':
            layer_path = r'HAYA.OMAN\HAYA.Operational_Areas' 
            temp_layer = arcpy.MakeFeatureLayer_management(layer_path)
            select(temp=temp_layer, fields=DATA_STRUCTURE['HAYA.OMAN']['HAYA.Operational_Areas'], x=x_cor, y=y_cor,reference=SPATIAL_REFERENCE)


fetch_code()