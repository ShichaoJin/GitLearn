import os,numpy as np
if 1: #arcpy2
    import arcpy,os
    from arcpy.sa import *
    arcpy.CheckOutExtension("Spatial")
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("GeoStats")
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = cd
else:#python3
    try:
        from osgeo import gdal
        from osgeo import ogr
        from osgeo import osr
    except:
        import ogr,osr,gdal
    from IPython import embed


if __name__ == '__main__':
    root = os.path.dirname(os.path.abspath(__file__))
    outdir = ""
    if not os.path.exists(outdir): os.makedirs(outdir)

    embed()
