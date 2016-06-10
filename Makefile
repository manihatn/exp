all:
	make clean
	mkdir single
	cp parser.py single
	for i in *.log; do awk '{print $$NF}' $$i >> single/$${i%.*}.out; done
	cd single && for i in *.out; do python parser.py -i $$i >> finalresults.txt; done

clean:
	rm -rf single
