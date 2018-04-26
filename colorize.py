import sys

# save as colorize.py, then use like so:
#
#   stern --color always <blah> | python colorize.py <KEYWORD_1> ... <KEYWORD_N>

HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

for line in sys.stdin:
    for arg in sys.argv[1:]:
        line = line.replace(arg, BOLD + RED + arg + END)
    sys.stdout.write(line)
    sys.stdout.flush()
