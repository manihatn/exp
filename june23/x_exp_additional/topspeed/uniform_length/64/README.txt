For obtaining the out file

awk '{print $NF}' 64.log >> 64.out


Swapping the following values

18446744073709551609 = - 7
18446744073709551608 = - 8
18446744073709551602 = - 14    
18446744073709551601 = - 15


python pdf.py -i 64_1m_2m.out -o pdf.png 
python cdf.py -i 64_1m_2m.out -o cdf.png 
python histo.py -i 64_1m_2m.out -o histo.png 


run the parser.py to find the min and max 

gnuplot hist.plt

deleting the last line

sed '$d' <file>
