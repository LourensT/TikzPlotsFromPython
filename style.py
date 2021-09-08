style = {
    "colors" : 

'''	\\definecolor{mycolor1}{rgb}{0.00000,0.80000,0.80000}
	\\definecolor{mycolor2}{rgb}{0.00000,0.50000,0.50000}
	\\definecolor{mycolor3}{rgb}{0.00000,0.30000,0.30000}
	\\definecolor{mycolor4}{rgb}{0.00000,0.10000,0.10000}
	\\definecolor{mycolor5}{rgb}{0.00000,1,1}
''',

    "scatter_styling" :
[
    "[color=mycolor2, line width = 2pt, mark size=1.5pt, mark=*, only marks, mark options={solid, mycolor2}]",
    "[color=mycolor1, line width = 2pt, mark size=2pt, mark=diamond*, only marks, mark options={solid, mycolor1}]",
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
''',

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
legend style={legend pos=north west, legend cell align=left, align=left, draw=white!15!black}''',

    "end_lines" : 

'''
	\end{axis}
\end{tikzpicture}
'''
}