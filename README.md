Process EEG singnal to entropy
==============================

Convert EEG timeseries (csv file) to entropy by time window. (wip)

### Requirements

- Python +2.7.x
 - Numpy  
 - Pandas  

### Fast Track

    $ git clone <this project>
    $ cd <this project>
    $ pip install -r requirements.txt
    $ python entropycli.py -f example/example.dat.csv
    $ <text editor> example/example.dat.csv.2s_256hz.entropy
