#CODE TO GENERATE MAPS
import geopandas 
import geoplot
import os
import pandas as pd

# Question: do we want to add hovers?
def chicago_map():
    '''
    '''
    #os.listdir("analysis_plots")
    chicago_shapes = geopandas.read_file("analysis_plots/geo_export_33ca7ae0-c469-46ed-84da-cc7587ccbfe6.dbf")
    chicago_map = chicago_shapes.plot(figsize=(25,25), 
                edgecolor='k', facecolor='b', alpha=0.25, linewidth=2) 
    
    geoplot.polyplot(chicago_map, figsize=(8, 4))
    
    #shade by attendance 

    