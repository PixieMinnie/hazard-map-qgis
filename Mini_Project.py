
import pandas as pd

#load landslide event data
landslide_df = pd.read_csv ("Global_Landslide_Catalog.csv")

#display first 5 rows
print (landslide_df.head())



import rasterio
import numpy as np

#open DEM file
dem_file = "elevation_data.tif"
with rasterio.open(dem_file) as src:
    dem_data = src.read(1) #read first band elevation values
    dem_transform = src.transform #get spatial reference

print ("DEM shape:", dem_data.shape)



# from netCDF4 import Dataset

# #load rainfall netCDF4 data
# rainfall_file = "rainfall_data.nc"
# rainfall_data = Dataset(rainfall_file)

# #extract rainfall variable
# rainfall_values = rainfall_data.variables["precipitation"][:]

# print ("Rainfall Data Shape:", rainfall_values.shape)


# from netCDF4 import Dataset

# # Open the NetCDF file
# rainfall_file = "rainfall_data.nc"
# rainfall_data = Dataset(rainfall_file)

# # Print all variable names
# print("Available variables in the dataset:")
# print(rainfall_data.variables.keys())

# # Close the file
# rainfall_data.close()


from netCDF4 import Dataset

#load rainfall netCDF4 data
rainfall_file = "rainfall_data.nc"
rainfall_data = Dataset(rainfall_file)

#extract rainfall variable
rainfall_values = rainfall_data.variables["precip"][:]

print ("Rainfall Data Shape:", rainfall_values.shape)


