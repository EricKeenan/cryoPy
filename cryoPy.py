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
		transform = osr.CoordinateTransformation(src, tgt)

		# Initialize tgt_Lat and tgt_Lon numpy arrays
		tgt_Lat = np.zeros(len(src_Lat))
		tgt_Lon = np.zeros(len(src_Lon))

		# For transformation, convert 2-D source lat/lon arrays to 1-D vector arrays
		is_2D = False # Flase if the array is 1-D
		if type(src_Lat) == list:
			is_List = True

		elif src_Lat.ndim == 2:
			is_2D = True
			shape_2D = src_Lat.shape
			src_Lat = src_Lat.flatten()
			src_Lon = src_Lon.flatten()
			tgt_Lat = np.zeros(src_Lat.shape)
			tgt_Lon = np.zeros(src_Lon.shape)

		# Perform coordinate transformation.
		for j in range(0, len(src_Lat)):
			tgt_coords = transform.TransformPoint(float(src_Lon[j]), float(src_Lat[j]))	
			tgt_Lon[j] = tgt_coords[0]
			tgt_Lat[j] = tgt_coords[1]

		# If source Lat/Lon were originally 2D, convert them back to 2D
		if is_2D:
			tgt_Lon = tgt_Lon.reshape(shape_2D)
			tgt_Lat = tgt_Lat.reshape(shape_2D)

		return tgt_Lat, tgt_Lon



