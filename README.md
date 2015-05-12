Process EEG signal to entropy
=============================

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

### References

Theoto Rocha, F.; Thomaz, C.E.; Freitas da Rocha, A.; Massad, E., "Brain Mapping and Interpretation of Reading Processing in Children Using EEG and Multivariate Statistical Analysis," Graphics, Patterns and Images (SIBGRAPI), 2014 27th SIBGRAPI Conference on , vol., no., pp.251,258, 26-30 Aug. 2014, doi: 10.1109/SIBGRAPI.2014.19  
URL: http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6915315&isnumber=6915273  
http://fei.edu.br/~cet/sibgrapi14.pdf