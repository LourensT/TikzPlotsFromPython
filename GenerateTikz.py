import atexit
from typing import Dict, List

from style import style


class GenerateTikz:

    counter = 0

    def __init__(self, fp, include_colors = False):
        assert '.tikz' in fp, "should be .tikz file"

        self.style = style

        self.f = open(fp, 'w')
        
        # make sure file is closed
        atexit.register(self.f.close)

        self.f.write(self.style["start_lines"])

        if include_colors:
            self.f.write(self.style["colors"])

    def setConfiguration(self,  xmin, xmax, 
                                ymin, ymax, 
                                xlog: bool, ylog: bool, 
                                args: List[str] = []):

        # write constant part 
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

    def addSeries(self, series : Dict, name : str, scatter=True):
        if scatter:
            self.f.write("\n\\addplot " + self.style["scatter_styling"][self.counter])
            self.counter += 1
        else:
            self.f.write("\n\\addplot " + self.style["line_styling"][self.counter])
            self.counter += 1

        self.f.write("\ntable[row sep=crcr]{\n")
        for key, value in series.items():
            self.f.write(str(key) + "\t" + str(value) + "\\\\ \n" )
        self.f.write("};\n")
        self.f.write("\\addlegendentry{" + name + "}\n")
    
    def finishFile(self):
        self.f.write(self.style["end_lines"])


if __name__ == "__main__":
    cfg = GenerateTikz("hey.tikz")
    #args=["grid = major"]
    cfg.setConfiguration(1980, 2014, 0, 10000, False, True)
    cfg.addSeries({1980 : 900, 2014 : 9000}, "hello")
    cfg.finishFile()