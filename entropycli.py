import argparse
import entropy


parser = argparse.ArgumentParser(
    prog='entropycli',
    description='Convert EEG timeseries (csv file) to entropy by time window.',
    usage='python entropycli -f <eeg csv file>'
    )

parser.add_argument('-f', dest='inputFile', help='specify eeg csv file')

parser.add_argument(
    '-H', '--header', dest='inputHeader',
    default=['time', 'F1', 'F2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T3', 'C3',
             'Cz', 'C4', 'T4', 'T5', 'P3', 'Pz', 'P4', 'T6', 'O1', 'Oz', 'O2'],
    help="""specify eeg csv file header to process.
It is possible to exclude unused fileds.
default=['time','F1','F2','F7','F3','Fz','F4','F8','T3','C3','Cz','C4','T4',
'T5','P3','Pz','P4','T6','O1','Oz','O2']""")

parser.add_argument(
    '--window', dest='inputWindow', type=int, default=2,
    help='specify time window in seconds. Default 2s')

parser.add_argument(
    '--freq', dest='inputFreq', type=int, default=256,
    help='specify eeg frequency (Hz). Default 256Hz')

args = parser.parse_args()

if not args.inputFile:
    parser.print_help()
    exit(0)

entropy.process_csv(fname=args.inputFile, header=args.inputHeader,
                    window=args.inputWindow, frequency=args.inputFreq)
