# Import python libraries. I need to be in my geoenv conda environment. ($ conda info --envs; $ source activate geoenv)
import gdal
import osr
import numpy as np

# Class which contains geographic manipulation functions. 
class Geo:

	# Coordinate system transformation function. 
	# src_EPSG: Source EPSG coordinate system (ex: MERRA-2 = 4326). 
	# tgt_EPSG: Target EPSG coordinate system (ex: South polar stereo = 3031).
	# src_Lat: Numpy 1-D vector array of latitude in src_EPSG to be converted to tgt_EPSG.
	# src_Lon: Numpy 1-D vector array of longitude in src_EPSG to be converted to tgt_EPSG.
	# tgt_Lat: Numpy 1-D vector array of latitude in tgt_EPSG converted from src_EPSG.
	# tgt_Lon: Numpy 1-D vector array of longitude in tgt_EPSG converted from src_EPSG.
	def coords_trans(src_EPSG, tgt_EPSG, src_Lat, src_Lon):

		# Define source (src) and target (tgt) coordinate systems. 
		src = osr.SpatialReference()
		tgt = osr.SpatialReference()
		src.ImportFromEPSG(src_EPSG)
		tgt.ImportFromEPSG(tgt_EPSG)

		# Initialize tgt_Lat and tgt_Lon numpy arrays
		tgt_Lat = np.zeros(len(src_Lat))
		tgt_Lon = np.zeros(len(src_Lon))

		# Perform coordinate transformation.
		for j in range(0, len(src_Lat)):
			tgt_coords = trasnform.TransformPoint(src_Lon[j], src_Lat[j])
			tgt_Lon[j] = tgt_coords[0]
			tgt_Lat[j] = tgt_coords[1]

		return tgt_Lat, tgt_Lon

