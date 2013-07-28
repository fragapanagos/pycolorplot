"""Module for generating colormaps and color cycles"""

import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.pyplot as plt

class ColorGenerator:
    """Generates colors for use in colormaps or color cycles"""

    cmred = {'red':   [(0.0, 0.0, 0.0),
                       (1.0, 1.0, 1.0)],
                        
             'green': [(0.0, 0.0, 0.0),
                       (1.0, 0.0, 0.0)],
    
             'blue':  [(0.0, 0.0, 0.0),
                       (1.0, 0.0, 0.0)]}

    cmgreen = {'red':   [(0.0, 0.0, 0.0),
                         (1.0, 1.0, 1.0)],
                          
               'green': [(0.0, 0.0, 0.0),
                         (1.0, 0.0, 0.0)],
    
               'blue':  [(0.0, 0.0, 0.0),
                         (1.0, 0.0, 0.0)]}

    cmblue = {'red':   [(0.0, 0.0, 0.0),
                        (1.0, 1.0, 1.0)],
                         
              'green': [(0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)],
    
              'blue':  [(0.0, 0.0, 0.0),
                        (1.0, 0.0, 0.0)]}

    def __init__(self, cmname, cdict=None):
        if not cdict: # select colormap by name from maps defined above
            cdict = {'red':ColorGenerator.cmred, 
                     'green':ColorGenerator.cmgreen,
                     'blue':ColorGenerator.cmblue}[cmname] 
        self.cmname = cmname
        self.my_cmap = colors.LinearSegmentedColormap('my_colormap', cdict)
        self.cNorm = colors.Normalize()
        self.scalarMap = cmx.ScalarMappable(norm=self.cNorm, cmap=self.my_cmap) 

    def get_color_list(self, n=8):
        """Returns an n list of matplotlib colors.
        
        Use the list of colors to set_color_cycle of an axis object."""
        self.cNorm.autoscale((0, n-1))
        return [self.scalarMap.to_rgba(i) for i in range(n)]

    def get_color_map(self):
        """Returns the colormap of the ColorGenerator object.
        
        colormap is also registered with pyplot."""
        plt.register_cmap(self.cmname)
        return self.my_cmap
