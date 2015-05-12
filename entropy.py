import numpy as np
import pandas as pd


def eegts_to_entropy(df, window=2, frequency=256):
    """
    convert eeg timeseries to entropy by time window
    df: pandas dataframe with data for each eeg channels
    window: window time in seconds
    frequency: frequency rate in Hertz (Hz)
    """
    # start empty dataframe
    df2 = pd.DataFrame()

    # entropy method - ROCHA et all. 2014 (\cite{Rocha2014})
    def entropy(x):
        x = np.absolute(x)
        return -x * np.log2(x) - (1 - x) * np.log2(1 - x)

    for i in range(int(df.index.size))[::(frequency*window)]:
        correlation = df[i:i+(frequency*window)].corr()  # load window by freq
        correlation = correlation.replace(1., np.NAN)  # exclude diagonal - 1's
        correlation_mean = correlation.mean()  # column average
        # Rocha2014 - eq (2)
        entropy_correlation = correlation.apply(entropy)
        # Rocha2014 - eq (4)
        entropy_correlation_mean = correlation_mean.apply(entropy)
        # Rocha2014 - eq (5)
        entropy_per_channel = np.sum(
            np.absolute(
                entropy_correlation_mean - entropy_correlation))
        # create new dataframe and output
        df2[i] = entropy_per_channel

    return df2.transpose()


def process_csv(fname, window=2, frequency=256,
                header=['time', 'F1', 'F2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T3',
                        'C3', 'Cz', 'C4', 'T4', 'T5', 'P3', 'Pz', 'P4', 'T6',
                        'O1', 'Oz', 'O2']):
    """receive csv file, parse to dataframe and save output in csv"""
    df = pd.read_csv(fname, parse_dates=True, index_col='time', usecols=header)
    output = eegts_to_entropy(df=df, window=window, frequency=frequency)
    output.to_csv(fname+'.'+str(window)+'s_'+str(frequency)+'hz'+'.entropy')
    print (fname+'.'+str(window)+'s_'+str(frequency)+'hz'+'.entropy')
