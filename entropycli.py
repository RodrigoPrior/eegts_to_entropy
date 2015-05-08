import optparse
import entropy


parser = optparse.OptionParser('usage %prog -f <eeg csv file>')

parser.add_option(
    '-f', dest='inputFile', type='string',
    help='specify eeg csv file')

parser.add_option(
    '-H', dest='inputHeader', type='string',
    help="""specify eeg csv file header to process.
It is possible to exclude unused fileds.
default=['time','F1','F2','F7','F3','Fz','F4','F8','T3','C3','Cz','C4','T4',
'T5','P3','Pz','P4','T6','O1','Oz','O2']""")

parser.add_option(
    '-w', dest='inputWindow', type='string',
    help='specify time window in secondes. Default 2')

parser.add_option(
    '--freq', dest='inputFreq', type='string',
    help='specify eeg frequency (Hz). Default 256')

(options, args) = parser.parse_args()
inputFile = options.inputFile
inputHeader = options.inputHeader
inputWindow = options.inputWindow
inputFreq = options.inputFreq

if (inputFile is None):
    print (parser.usage)
    exit(0)

entropy.process_csv(
    fname=inputFile, header=inputHeader)
# TODO: add the followind inputs: window=inputWindow, frequency=inputFreq)
