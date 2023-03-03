#CODE TO GENERATE MAPS
import geopandas 
import matplotlib.pyplot as plt
#import geoplot
import os
import pandas as pd

#Sarah 

#https://www.kaggle.com/code/threadid/geopandas-mapping-chicago-crimes 
#https://geopandas.org/en/stable/docs/user_guide/mapping.html 
#https://www.youtube.com/watch?v=xxg4Vm-Xg9g 

# We ended up not using these
def chicago_map():
    '''
    '''
    #os.listdir("analysis_plots")
    chicago_shapes = geopandas.read_file("analysis_plots/geo_export_33ca7ae0-c469-46ed-84da-cc7587ccbfe6.shp")
    
    chicago_map = chicago_shapes.plot(figsize=(25,25), 
                edgecolor='k', facecolor='b', alpha=0.25, linewidth=2) 
    
    return chicago_shapes.plot(figsize=(8, 4))
    
    #shade by attendance 

    