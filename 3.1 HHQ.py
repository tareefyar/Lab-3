from rasterio.plot import show
import rasterio
import matplotlib.pyplot as plt #For plotting our visualizations
from keras.preprocessing.image import ImageDataGenerator #Keras dataset generator class.
from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from PIL import Image

# %matplotlib inline  # Uncomment this line if running this code in Jypiter notebook

#Quetta HH
Q1 = rasterio.open(r"E:\6th Semester\Image Processing\Lab Works\IP\Lab 3\HHQ.2_UA.tif")
plt.title("HHQ")
show(Q1)