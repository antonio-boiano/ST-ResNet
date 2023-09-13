import os
import sys
import argparse
def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "config_file", type=str, metavar="FILE", help="path to config file"
    )
    parser.add_argument(
        "-s", "--seed", default=0, type=int, help="seed for initializing training"
    )

    return parser.parse_args()

args = make_parser()
var = args.config_file

print(var)

os.system("nohup sh -c '" +
          sys.executable + " run.py "+var+" >res1.txt" +"' &")
