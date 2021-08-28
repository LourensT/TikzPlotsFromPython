import atexit
from typing import Dict, List


class TikzPlot:

    counter = 0

    style = {
        "scatter_styling" :
        [
            "[color=mycolor1, line width = 2pt, mark size=2pt, mark=diamond*, only marks, mark options={solid, mycolor1}]",
            "[color=mycolor2, line width = 2pt, mark size=1.5pt, mark=*, only marks, mark options={solid, mycolor2}]",
            "[color=mycolor3, line width = 2pt, mark size=1.5pt, mark=square*, only marks, mark options={solid, mycolor3}]", 
            "[color=mycolor4, line width = 2pt, mark size=1.5pt, mark=triangle*, only marks, mark options={solid, mycolor4}]"
        ],
        "line_styling":
        [
            "[color=mycolor1,line width = 2pt]",
            "[color=mycolor2,line width = 2pt]",
            "[color=mycolor3,line width = 2pt]",
            "[color=mycolor4,line width = 2pt]",
            "[color=mycolor5,line width = 2pt]",
            "[color=mycolor1,line width = 2pt]",
            "[color=mycolor2,line width = 2pt]",
            "[color=mycolor3,line width = 2pt]"
        ],

        "start_lines" : 
'''\\tikzstyle{every node}=[font=\\normalsize]

\\begin{tikzpicture}
    \\begin{axis}[%
'''
        ,

        "constant_configuration":
'''width=0.951\\fwidth,
height=\\fheight,
at={(0\\fwidth,0\\fheight)},
scale only axis,
xminorticks=true,
yminorticks=true,
axis x line*=bottom,
axis y line*=left,
x tick label style = {/pgf/number format/.cd, scaled x ticks = false, set thousands separator={}, fixed},
axis background/.style={fill=white},
legend style={legend pos=north west, legend cell align=left, align=left, draw=white!15!black}'''
        ,

        "end_lines" : 
'''
	\end{axis}
\end{tikzpicture}
'''
    }

    def __init__(self, fp):
        assert '.tikz' in fp, "should be .tikz file"

        self.f = open(fp, 'w')
        
        # make sure file is closed
        atexit.register(self.f.close)

        self.f.write(self.style["start_lines"])

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
    cfg = TikzPlot("hey.tikz")
    #args=["grid = major"]
    cfg.setConfiguration(1980, 2014, 0, 10000, False, True)
    cfg.addSeries({1980 : 900, 2014 : 9000}, "hello")
    cfg.finishFile()
