import sys
import os

from analyse import do_analyse

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if str(sys.argv[1]) == "--analyse":
            do_analyse()