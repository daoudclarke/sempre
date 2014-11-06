import sys
import sexpdata

def parse_log(filename):
    logfile = open(filename)
    data = (row.split(';;;') for row in logfile)
    for row in data:
        if len(row) > 2:
            #print row
            info = sexpdata.loads(row[1])
            value = float(row[2])
            print info, value


if __name__ == "__main__":
    parse_log(sys.argv[1])
