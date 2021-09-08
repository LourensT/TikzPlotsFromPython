import atexit
from typing import Dict, List
import os

# import the local style dictionary from style.py
from style import style

class GenerateTikz:

    counter = 0

    def __init__(self, fp, include_colors = False, documentation=""):
        # set the style that was imported
        self.style = style

        # open .tikz file
        assert '.tikz' in fp, "should be .tikz file"
        self.f = open(fp, 'w')
        
        # make sure file is closed
        atexit.register(self.finishFile)

        # write given documentation line
        if documentation != "":
            self.f.write("%" + documentation + "\n")

        # write first introductory lines
        self.f.write(self.style["start_lines"])

        if include_colors:
            self.f.write(self.style["colors"])

    def setConfiguration(self,  xmin, xmax, 
                                ymin, ymax, 
                                xlog: bool, ylog: bool, 
                                args: List[str] = []):

        # write constant part of configuration
        self.f.write(self.style["constant_configuration"])

        # write axis rules
        self.f.write(", \n{}={}".format("xmin", xmin))
        self.f.write(", \n{}={}".format("xmax", xmax))
        self.f.write(", \n{}={}".format("ymin", ymin))
        self.f.write(", \n{}={}".format("ymax", ymax))

        if xlog:
            self.f.write(", \n{}={}".format("xmode", "log"))
        if ylog:
            self.f.write(", \n{}={}".format("ymode", "log"))

        # write additional option configs
        for item in args:
            self.f.write(", \n" + item)

        # close config
        self.f.write("]\n")

    '''
    Add a series (in dictionary form) to be plotted, by default scatter. Name is used for label. 
    '''
    def addSeries(self, series : Dict, name : str, scatter=True):

        # select scatter/line styling from the style guide
        if scatter:
            self.f.write("\n\\addplot " + self.style["scatter_styling"][self.counter])
            self.counter += 1
        else:
            self.f.write("\n\\addplot " + self.style["line_styling"][self.counter])
            self.counter += 1

        # write series data table
        self.f.write("\ntable[row sep=crcr]{\n")
        for key, value in series.items():
            self.f.write(str(key) + "\t" + str(value) + "\\\\ \n" )
        self.f.write("};\n")

        # add legend entry
        self.f.write("\\addlegendentry{" + name + "}\n")
    
    '''
    on exit, the file is finished and closed
    '''
    def finishFile(self):
        self.f.write(self.style["end_lines"])

        self.f.close()

def generate_plot(fp : str, series: List[Dict], labels : List[int], 
                            style="style.txt", 
                            log=False,
                            line=False):

    assert len(series) == len(labels), "number of labels does comply with number of series"

    if line:
        assert len(series) <= 8, "too many series (maximum 8 for lines)"
    else:
        assert len(series) <= 5, "too many series (maximum 5 for lines)"
    
    raise NotImplementedError

if __name__ == "__main__":
    cfg = GenerateTikz(os.getcwd() + "\\test\\hey.tikz")
    #args=["grid = major"]
    cfg.setConfiguration(1980, 2014, 0, 10000, False, True)
    cfg.addSeries({1980 : 900, 2014 : 9000}, "hello")