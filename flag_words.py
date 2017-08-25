import sys
import os

from analyse import do_analyse, do_csv_to_string

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if str(sys.argv[1]) == "--analyse":
            do_analyse()
        if "--csv_to_string" in str(sys.argv[1]):
            in_string = str(str(sys.argv[1]).split("=")[1])
            do_csv_to_string(in_string)