import atexit


class TikzPlot:

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
'''
\\tikzstyle{every node}=[font=\\normalsize]

\\begin{tikzpicture}
    \\begin{axis}[%
'''
        ,

        "constant_configuration":
'''
width=0.951\\fwidth,
height=\\fheight,
at={(0\\fwidth,0\\fheight)},
scale only axis,
xminorticks=true,
yminorticks=true,
axis x line*=bottom,
axis y line*=left,
grid = major,
x tick label style = {/pgf/number format/.cd,%
    scaled x ticks = false,
    set thousands separator={},
    fixed},
axis background/.style={fill=white},		axis background/.style={fill=white},
legend style={legend pos=north west, legend cell align=left, align=left, draw=white!15!black},

'''
        ,
        
        "custom_configuration" :
            {
                "xmin" : 1980,
                "xmax" : 2014,
                "xtick" : {1980,1985,1990,...,2015, 2014},
                "ymode" : "log",
                "ymin" : 1000,
                "ymax" : 100000,
                "ytick" :  {1000.0, 10000.0,  100000.0},
                "ylabel": "{Yearly Publications}",
            }
        ,

        "end_lines" : 
'''
    \\end{axis}
\\end{tikzpicture}%
'''
    }

    def __init__(self, fp):
        assert '.tikz' in fp, "should be .tikz file"

        self.f = open(fp, 'w')
        
        # make sure file is closed
        atexit.register(self.f.close)

        self.f.write(self.style["start_lines"])

if __name__ == "__main__":
    cfg = TikzPlot("hey.tikz")
