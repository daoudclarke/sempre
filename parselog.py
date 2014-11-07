import sys
import sexpdata
import json

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def get_source(derivation):
    return derivation[4][1][1]

def get_target(derivation):
    return derivation[4][2][1]

def get_name(symbol_or_string):
    try:
        value = symbol_or_string.value()
        if isinstance(value, list):
            assert len(value) == 1
            print value
            return get_name(value[0])
        assert isinstance(value, basestring)
        return value
    except AttributeError:
        assert (isinstance(symbol_or_string, basestring) or
                isinstance(symbol_or_string, int))
        #print symbol_or_string
        return symbol_or_string

def get_value(derivation):
    values = derivation[2][1][1:]

    #print "Values", values
    values = [tuple(get_name(v) for v in value[1:]) for value in values]
    return values

def parse_log(filename):
    logfile = open(filename)
    data = (row.split(';;;') for row in logfile)
    for row in data:
        if len(row) > 2:
            score = float(row[2])
            derivation = row[1].replace("'", "\\'")
            info = sexpdata.loads(derivation)
            # try:
            # except IndexError:
            #     logger.exception("Error parsing expression %s", row[1])
            #     continue

            value = get_value(info)

            if len(value) == 0:
                if score > 0.0:
                    raise ValueError("Positive score with no value: %r" % row)
                continue

            source = get_source(info)
            target = get_target(info)
            yield {'source': source, 'target': target, 'score': score, 'value': value}

def output_json(examples):
    header = ['source', 'target', 'value']
    with open('examples.json', 'w') as example_file:
        for example in examples:
            try:
                encoded = json.dumps(example)
            except TypeError:
                logger.exception("Invalid example: %s", example)
                raise
            example_file.write(encoded + '\n')
            

if __name__ == "__main__":
    examples = parse_log(sys.argv[1])
    output_json(examples)
