reset
n=20 #number of intervals
max=20 #max value, sort this TODO
min=0 #min value
width=(max-min)/n #interval width 
#function used to map a value to the intervals
hist(x,width)=width*floor(x/width)+width/2.0
set term postscript #output terminal and file
set output "conf1.ps"
set xrange [min:max]
set yrange [0:]
set title "Latency in the test configuration for reference switch"
#to put an empty boundary around the
#data inside an autoscaled graph.
set offset graph 0.05,0.05,0.05,0.0
set xtics min,(max-min)/n,max
set boxwidth width
set style fill solid 0.5 #fillstyle
set tics out nomirror
set xlabel "Latency (in ns)"
set ylabel "Frequency"
#count and plot
plot "conf1_analyse.out" u (hist($1,width)):(1.0) smooth freq w boxes lc rgb"blue" title 'Min'
#     "copper_arista.data" u (hist($2,width)):(1.0) smooth freq w boxes lc rgb"green" title 'Median',\
#     "copper_arista.data" u (hist($3,width)):(1.0) smooth freq w boxes lc rgb"blue" title 'Max'


reset
n=20 #number of intervals
max=20 #max value, sort this TODO
min=0 #min value
width=(max-min)/n #interval width 
#function used to map a value to the intervals
hist(x,width)=width*floor(x/width)+width/2.0
set term postscript #output terminal and file
set output "conf2.ps"
set xrange [min:max]
set yrange [0:]
set title "Latency of the DAG"
#to put an empty boundary around the
#data inside an autoscaled graph.
set offset graph 0.05,0.05,0.05,0.0
set xtics min,(max-min)/n,max
set boxwidth width
set style fill solid 0.5 #fillstyle
set tics out nomirror
set xlabel "Latency (in ns)"
set ylabel "Frequency"
#count and plot
plot "conf2_analyse.out" u (hist($1,width)):(1.0) smooth freq w boxes lc rgb"blue" title 'Min'
#     "copper_arista.data" u (hist($2,width)):(1.0) smooth freq w boxes lc rgb"green" title 'Median',\
#     "copper_arista.data" u (hist($3,width)):(1.0) smooth freq w boxes lc rgb"blue" title 'Max'




#plot "data.dat" u (hist($1,width)):(1.0):2 w yerrorbars 


#plot "result.dat" u (hist($1,width)):(1.0) smooth freq w boxes lc rgb"green" notitle
