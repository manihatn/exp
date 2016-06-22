reset
n=50 #number of intervals
max=50. #max value, sort this TODO
min=0. #min value
width=(max-min)/n #interval width 
#function used to map a value to the intervals
hist(x,width)=width*floor(x/width)+width/2.0
set term png #output terminal and file
set output "64B.png"
set xrange [min:max]
set yrange [0:]
set title "Latency of DAG (Tap to port 0 (1m), Tap to port 1 (5m))"
#to put an empty boundary around the
#data inside an autoscaled graph.
set offset graph 0.05,0.05,0.05,0.0
set xtics min,(max-min)/10,max
set boxwidth width
set style fill solid 0.5 #fillstyle
set tics out nomirror
set xlabel "Latency (in ns)"
set ylabel "Frequency"
#count and plot
plot "64.out" u (hist($1,width)):(1.0) smooth freq w boxes lc rgb"red" title '64 B'
