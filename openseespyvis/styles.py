
class standardStyle():
    """
    A class that contains all of the dictionaries for the plot
    """
        
    def __init__(self):
    
        self.ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
        self.node_style = {'color':'black', 'marker':'o', 'facecolor':'black','linewidth':0.}
        self.node_style_animation = {'color':'black', 'marker':'o','markersize':2., 'linewidth':0.} 
        
        self.node_text_style = {'fontsize':8, 'fontweight':'regular', 'color':'green'} 
        self.ele_text_style = {'fontsize':8, 'fontweight':'bold', 'color':'darkred'} 
        self.ele_text_style = {'fontsize':6, 'fontweight':'bold', 'color':'darkred'}             
        
        self.WireEle_style = {'color':'black', 'linewidth':1, 'linestyle':':'} # elements
        self.Eig_style = {'color':'red', 'linewidth':1, 'linestyle':'-'} # elements
        
        ele_lim_a_style = {'color':'blue', 'linewidth':1.5, 'linestyle':'-'} # elements
        ele_lim_b_style = {'color':'green', 'linewidth':1.5, 'linestyle':'-'} # elements
        ele_lim_c_style = {'color':'orange', 'linewidth':1.5, 'linestyle':'-'} # elements
        ele_lim_d_style = {'color':'red', 'linewidth':1.5, 'linestyle':'-'} # elements
        
        # 'color':eleStyle, 'linewidth':1.0, 'linestyle':'-', 'marker':'o', 'mfc':eleStyle, 'markersize':2
        zle_lim_a_style = {'color':'blue','mfc':'blue', 'linewidth':5, 'linestyle':'-', 'marker':''} # elements
        zle_lim_b_style = {'color':'green','mfc':'green', 'linewidth':5, 'linestyle':'-', 'marker':''} # elements
        zle_lim_c_style = {'color':'orange','mfc':'orange', 'linewidth':5, 'linestyle':'-', 'marker':''} # elements
        zle_lim_d_style = {'color':'red','mfc':'red', 'linewidth':5, 'linestyle':'-', 'marker':''} # elements
        
        
        
        
        self.limStateColors = ["blue","green","orange","red"]
        self.ele_lim_styles = {self.limStateColors[0]:ele_lim_a_style,
                               self.limStateColors[1]:ele_lim_b_style,
                               self.limStateColors[2]:ele_lim_c_style,
                               self.limStateColors[3]:ele_lim_d_style,
                              }
        self.zle_lim_styles = {self.limStateColors[0]:zle_lim_a_style,
                               self.limStateColors[1]:zle_lim_b_style,
                               self.limStateColors[2]:zle_lim_c_style,
                               self.limStateColors[3]:zle_lim_d_style,
                              }        
        
        self.fillSurface = True
        self.facecolor = '#ffffff'
        self.backgroundcolor = '#ffffff'
        self.axisOff = False


class wireStyle(standardStyle):
    """
    Replaces any specified arguements in the basic style object.
    """
        
    
    def __init__(self):
        super().__init__()
        self.ele_style = {'color':'black', 'linewidth':1, 'linestyle':':'}
        self.fillSurface = False
        
class customStyle(standardStyle):
    """
    Replaces any specified arguements in the basic style object.
    """
    
    def __init__(self, **args):
        super().__init__()
        
        for key in args.keys():
            self.__dict__[key] = args[key]
            
